#!/bin/bash

if [ $# -ge 1 ]; then
  env="$1"
else
  env="python3"
fi

# Create data_clean directory if it doesn't exist
if [ ! -d "./data_clean" ]; then
  mkdir data_clean
fi

# Run all Python scripts in scripts/
for script in ./scripts/*.py; do
  echo "Running $script"
  $env "$script"
done