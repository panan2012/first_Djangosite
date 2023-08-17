# My Blog

## Build container

Build command with podman 

```bash
podman build -t panan2012/blog .
```

looking inside Container
```bash
podman run -p 9000:8000 -it panan2012/blog /bin/bash
```
coninside Container
```bash
podman  exec -it fc /bin/bash
```

```bash
podman run -it -p 9000:8000 panan2012/blog
```

## DB
```bash
podman run --name blog-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:15 
```
