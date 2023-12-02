#!/bin/bash
# A script that Sends data in the request body (for POST requests)
curl -s -X  POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
