#!/bin/bash
curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
