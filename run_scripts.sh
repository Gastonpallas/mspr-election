#!/bin/bash

# Create data_clean directory if it doesn't exist
if [ ! -d "./data_clean" ]; then
  mkdir data_clean
fi

# Run age.py
echo "Running age script"
python3 ./scripts/age.py

# Run chomage.py
echo "Running chomage script"
python3 ./scripts/chomage.py

# Run culture.py
echo "Running culture script"
python3 ./scripts/culture.py

# Run election2017.py
echo "Running election2017 script"
python3 ./scripts/election2017.py

# Run election2022.py
echo "Running election2022 script"
python3 ./scripts/election2022.py

# Run entreprise.py
echo "Running entreprise script"
python3 ./scripts/entreprise.py

# Run security.py
echo "Running security script"
python3 ./scripts/security.py

# Run table_de_faits.py
echo "Running table_de_faits script"
python3 ./scripts/table_de_faits.py