#!/bin/bash
cd Documents
git clone https://github.com/SeafoodStudios/WebDB
pip3 install flask
pip3 install requests
python3 -m flask --app WebDB/src/scratchwrapper/main.py run
