#!/bin/bash

pip --version

LOG_FILE="pip_install.log"
PYTHON_PATH="/usr/bin/python3"
INSTALL_DIR="./install_dir"
MY_PROGRAM="my_program.py"

mkdir -p "$INSTALL_DIR"
pip install git+https://github.com/jaraco/path.git --target="$INSTALL_DIR" --log="$LOG_FILE"

if [ $? -eq 0 ]; then
    echo "Installation réussie de path.py"
    python3 $MY_PROGRAM
else
    echo "Échec de l'installation de path.py"
fi