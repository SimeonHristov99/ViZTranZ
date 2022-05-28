# ViZTranZ

Upload an image and get translation of the objects in the image.

## Quick Start

```bash
# Creating a new virtual environment
python3 -m venv venv2
source ./venv/bin/activate

# Installing application dependencies
pip3 install -r requirements.txt

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
- [ ] Set up `AWS Translate`.
- [ ] Finishing touches.
- [ ] Upload paper.

## About

Created as part of a university course: `Application programming interfaces for Cloud Architectures with AWS`.

### References

- AWS API Gateway to Lambda Tutorial in Python | Build a REST API: <https://www.youtube.com/watch?v=uFsaiEhr1zs>
- AWS Tutorial : Image recognition and notification with AWS Lambda, Rekognition, SNS, S3, Python: <https://www.youtube.com/watch?v=wnTvVB1ojPk>
- Secure your API Gateway with Lambda Authorizer: <https://www.youtube.com/watch?v=al5I9v5Y-kA>
