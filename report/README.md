# ADM report

## Build with `pandocker` image

```bash
docker build -t pandocker:latest . # Run this only once
make docker-pdf
```

## Build locally

```bash
# Install dependencies
sudo apt install pandoc texlive-full wget xz-utils
wget https://github.com/lierdakil/pandoc-crossref/releases/download/latest/pandoc-crossref-Linux-X64.tar.xz
tar -xf pandoc-crossref-Linux-X64.tar.xz
mv pandoc-crossref /usr/local/bin

# Create pdf
make pdf
```
