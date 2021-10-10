#!/bin/bash

# Open browser
open http://localhost:8000

# Run Docker container
docker run -v $(pwd):/soskids -p 8000:8000 --name soskids soskids.azurecr.io/soskids
# -v tag allows sync upon save between folder in local machine to a folder in docker container
# $(pwd) Mac/Linux, %cd% Windows command shell, ${pwd} Windows PowerShell