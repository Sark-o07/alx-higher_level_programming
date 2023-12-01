#!/bin/bash

# A script that takes in a URL, Adds custom headers to the HTTP GET request.

curl -sH "X-School-User-Id: 98" "$1"
