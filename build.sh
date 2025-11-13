#!/bin/bash
set -e

echo "Installing Go..."
curl -L https://go.dev/dl/go1.21.5.linux-amd64.tar.gz | tar -C /tmp -xzf -
export PATH="/tmp/go/bin:$PATH"
export GOPATH="/tmp/go"

echo "Installing Hugo..."
curl -L https://github.com/gohugoio/hugo/releases/download/v0.152.2/hugo_extended_0.152.2_linux-amd64.tar.gz | tar -xzf - -C /tmp

echo "Verifying installations..."
/tmp/go/bin/go version
/tmp/hugo version

echo "Building Hugo site..."
/tmp/hugo --gc --minify

echo "Build complete!"
