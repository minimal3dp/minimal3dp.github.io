#!/bin/bash
set -e

echo "Installing Go..."
curl -L https://go.dev/dl/go1.21.5.linux-amd64.tar.gz -o go.tar.gz
tar -C /tmp -xzf go.tar.gz
export PATH="/tmp/go/bin:$PATH"
export GOPATH="/tmp/go"

echo "Go version:"
go version

echo "Building Hugo site..."
hugo --gc --minify

echo "Build complete!"
