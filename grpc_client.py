import sys
import os
import io
import grpc
import argparse
import skimage
import base64
import warnings

from services.snet import snet_setup
from services import registry

import services.service_spec.segmentation_pb2_grpc as grpc_bt_grpc
import services.service_spec.segmentation_pb2 as grpc_bt_pb2

SERVER_NAME = 'mask_rcnn_server'


def save_img(fn, pb_img):
    #binary_image = base64.b64decode(pb_img.content)
    img_data = io.BytesIO(pb_img.content)
    img = skimage.io.imread(img_data)
    skimage.io.imsave(fn, img)


def main():
    script_name = sys.argv[0]
    parser = argparse.ArgumentParser(prog=script_name)

    default_endpoint = "127.0.0.1:{}".format(registry[SERVER_NAME]['grpc'])
    parser.add_argument("--endpoint", help="grpc server to connect to", default=default_endpoint,
                        type=str, required=False)
    parser.add_argument("--snet", help="call services on SingularityNet - requires configured snet CLI",
                        action='store_true')
    parser.add_argum