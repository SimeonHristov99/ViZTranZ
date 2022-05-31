#!/bin/bash

echo 'Starting application'
shellcheck source=./venv/bin/activate

streamlit run app.py
