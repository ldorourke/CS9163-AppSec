#!/bin/sh
docker rm appsec 2> /dev/null || true 
docker run -it -p 8000:8000 -v $PWD:/home/djangoappsec appsec bash
