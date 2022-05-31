# ViZTranZ

Upload an image and get translation of the objects in the image.

## Quick Start

```bash
# Creating a new virtual environment
python3 -m venv venv
source ./venv/bin/activate

# Installing application dependencies
pip3 install -r requirements.txt

# Setup Tensorflow for performing object detection
mkdir tf_model
cd tf_model
wget https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1?tf-hub-format=compressed
mv 1\?tf-hub-format\=compressed model.gz
gzip -d model.gz
tar -xf model

# Setup Pytorch and Hugging Face Transformers for neural machine translation
sudo apt-get install git-lfs
git lfs install

# Downloading model for de-bg translations
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Helsinki-NLP/opus-mt-en-bg
cd opus-mt-en-bg
git lfs pull
cd ..

# Downloading model for en-ru translations
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Helsinki-NLP/opus-mt-en-ru
cd opus-mt-en-ru
git lfs pull
cd ..

# Downloading model for en-de translations
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/Helsinki-NLP/opus-mt-en-de
cd opus-mt-en-de
git lfs pull
cd ..

# Starting application
streamlit run app.py
```

## Tasks

- [X] Create local project.
- [X] Basic UI.
- [X] Create github project.
- [X] Create AWS account.
- [X] Set up S3 bucket that would act as a trigger to the lambda.
- [X] Create the `AWS Lambda` function.
- [X] Set up `AWS Rekognition`.
- [X] Connect lambda to another S3 to publish results.
- [X] Prettify code.
- [X] Set up `AWS Translate`.
- [X] Add sidemenu with `AWS` and `Local` modes.
- [X] Link `Hugging Face` to UI.
- [X] Finish `Local` mode.
- [X] Package code.
- [ ] Add bash script `setup.sh` instead of commands in `quick start` section.
- [ ] Add bash script `run.sh`.
- [ ] Upload paper.

## About

Created as part of a university course: `Application programming interfaces for Cloud Architectures with AWS`.

### References

- AWS Tutorial : Image recognition and notification with AWS Lambda, Rekognition, SNS, S3, Python: <https://www.youtube.com/watch?v=wnTvVB1ojPk>
- AWS: Image analysis using Rekognition via Lambda function: <https://www.youtube.com/watch?v=3r_ue7TQkCE>
- Using AWS Rekognition and Python to Identify Objects / Text in Images: <https://www.youtube.com/watch?v=gjUwPEqnEeI>
- AWS Architecture: Serverless Photo Recognition: <https://www.youtube.com/watch?v=GIdJz7VnP58>
- Translating documents with Amazon Translate, AWS Lambda: <https://www.youtube.com/watch?v=-_2wCN5heXw&t=448s>
- Tensorflow Hub model for object detection: <https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1>
- Hugging Face model for translating en-de: <https://huggingface.co/Helsinki-NLP/opus-mt-en-de>
- Hugging Face model for translating en-bg: <https://huggingface.co/Helsinki-NLP/opus-mt-en-bg>
- Hugging Face model for translating en-ru: <https://huggingface.co/Helsinki-NLP/opus-mt-en-ru>
