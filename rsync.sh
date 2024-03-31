#!/bin/sh

hugo && rsync -av -e 'ssh -p 65002' --progress ./public/ u472268278@212.1.208.71:./public_html/

