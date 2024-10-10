 # Base image with dependencies
FROM python:3.12-slim AS base

# Update system packages
RUN apt-get update --fix-missing
RUN apt-get install -y --no-install-recommends git gcc libc6-dev
RUN apt-get clean

# Installing Python requirements
RUN pip install --upgrade pip poetry

# set work directory
WORKDIR /app
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

# Installing Poetry and python requirements
RUN poetry config virtualenvs.create true
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root --only main


FROM python:3.12-slim AS production-image

WORKDIR /app
# copy application from base image
COPY --from=base /app .
COPY app/ .

ARG VERSION
ARG BITBUCKET_BUILD_NUMBER
ARG BITBUCKET_COMMIT
ARG BITBUCKET_PR_ID

ENV VERSION=$VERSION
ENV SENTRY_RELEASE=$VERSION
ENV BITBUCKET_BUILD_NUMBER=$BITBUCKET_BUILD_NUMBER
ENV BITBUCKET_COMMIT=$BITBUCKET_COMMIT
ENV BITBUCKET_PR_ID=$BITBUCKET_PR_ID
ENV PATH="/app/.venv/bin:$PATH"

# Establish the runtime user (with no password and no sudo)
RUN touch /tmp/healthy
RUN useradd -m worker
USER worker

# Healthcheck Instruction
HEALTHCHECK CMD cat /tmp/healthy || exit 1
