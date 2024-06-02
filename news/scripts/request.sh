#!/bin/sh
curl --header "Content-Type:application/json" --request POST --data '{"input":"news"}' http://localhost:8087/input
