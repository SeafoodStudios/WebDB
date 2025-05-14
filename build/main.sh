#!/bin/bash
cd Documents
git clone https://github.com/SeafoodStudios/WebDB
pip3 install flask
pip3 install tinydb
pip3 install bcrypt
python3 WebDB/src/server/main.py
python3 -m flask --app WebDB/src/server/main.py run
