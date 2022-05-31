#!/bin/bash

echo 'Creating a new virtual environment ...'
python3 -m venv venv
source ./venv/bin/activate

echo 'Installing application dependencies ...'
pip3 install streamlit tensorflow torch matplotlib plotly boto3 python-dotenv transformers git-lfs sentencepiece tensorflow_hub sacremoses

echo 'Setting up Tensorflow for performing object detection ...'
mkdir tf_model
cd tf_model || exit
wget https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1?tf-hub-format=compressed
mv 1\?tf-hub-format\=compressed model.gz
gzip -d model.gz
tar -xf model
cd ..

echo 'Downloading model for en-bg translations ...'
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Helsinki-NLP/opus-mt-en-bg
cd opus-mt-en-bg || exit
git lfs install
git lfs pull
cd ..

echo 'Downloading model for en-ru translations ...'
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Helsinki-NLP/opus-mt-en-ru
cd opus-mt-en-ru || exit
git lfs install
git lfs pull
cd ..

echo 'Downloading model for en-de translations ...'
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Helsinki-NLP/opus-mt-en-de
cd opus-mt-en-de || exit
git lfs install
git lfs pull
cd ..

echo 'Installation successful! :)'
