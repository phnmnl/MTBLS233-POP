#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e
  
echo "Pulling docker images" 
sudo docker pull farmbio/luigid
sudo docker pull farmbio/mtbls233-jupyter
