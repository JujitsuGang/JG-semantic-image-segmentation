import sys
import os
import io
import grpc
import argparse
import skimage
import base64
import warnings

from services.snet import snet_setup
from