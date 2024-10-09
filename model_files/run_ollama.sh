#!/bin/bash

cd /model_files

echo "Starting Ollama server..."
ollama serve &  # Start Ollama in the background

echo "Ollama is ready, creating the model..."

sleep 2

ollama create maapu -f ./Modelfile
ollama run maapu
