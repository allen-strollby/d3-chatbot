# Building and Running 

Create docker image for server using 
```bash
docker build -t maapu-server .
```

Create model with ollama create

```bash
ollama create maapu -f ./Modelfile
```

When running server also run the ollama server with 

```bash
ollama run
```


