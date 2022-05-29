"""Code to run object detection with Tensorflow."""

import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub

from constants import MODULE_HANDLE
from PIL import Image

detector = hub.load(MODULE_HANDLE).signatures['default']


def run_detector(im_bytes):
    """Perform object detection using the specified model."""
    img = Image.open(im_bytes)

    converted_img = tf.image.convert_image_dtype(
        img,
        tf.float32
    )[tf.newaxis, ...]

    result = detector(converted_img)

    result = {key: value.numpy() for key, value in result.items()}
    
    return result
