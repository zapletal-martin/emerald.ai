#!/bin/sh

uvicorn --app-dir=.. server:app --host 0.0.0.0 --port 8083