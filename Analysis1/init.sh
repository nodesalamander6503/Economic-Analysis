#!/usr/bin/env zsh
rm *.db
rm figures/*.sh
python3.12 scrape.py
python3.12 analysis.py
