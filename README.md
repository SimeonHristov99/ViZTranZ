# ViZTranZ

Upload an image and get translation of the objects in the image.

## Quick Start

```bash
# Creating a new virtual environment
python3 -m venv venv
source ./venv/bin/activate

# Installing application dependencies
pip3 install -r requirements.txt

mkdir tf_model
cd tf_model

wget https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1?tf-hub-format=compressed
mv 1\?tf-hub-format\=compressed model.gz
gzip -d model.gz
tar -xf model

# Starting application
streamlit run app.py
```

> **Note:** The **first run will take some time** as `Tensorflow` will have to download the models it will use for object detection.

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
- [X] Add sidemenu with `AWS` and `Tensorflow` modes.
- [ ] Add `Tensorflow` mode.
- [ ] Finishing touches.
- [ ] Upload paper.

## About

Created as part of a university course: `Application programming interfaces for Cloud Architectures with AWS`.

### References

- AWS API Gateway to Lambda Tutorial in Python | Build a REST API: <https://www.youtube.com/watch?v=uFsaiEhr1zs>
- AWS Tutorial : Image recognition and notification with AWS Lambda, Rekognition, SNS, S3, Python: <https://www.youtube.com/watch?v=wnTvVB1ojPk>
- Secure your API Gateway with Lambda Authorizer: <https://www.youtube.com/watch?v=al5I9v5Y-kA>
- Tensorflow Hub: <https://tfhub.dev/google/efficientnet/b1/classification/1>
