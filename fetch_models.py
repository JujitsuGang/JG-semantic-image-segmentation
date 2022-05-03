
import requests
import os
import sys
import json
import math
import pathlib

from tqdm import tqdm

model_urls = []
with open("models.json", "r") as f:
    model_urls = json.load(f)["model_urls"]

# TODO maybe make models.json a parameter and use it's location as the root/my_path
my_path = os.getcwd()

if __name__ == "__main__":
    pathlib.Path(os.path.join(my_path, "models")).mkdir(parents=True, exist_ok=True)
    download_dir = os.path.join(my_path, "downloads")
    if len(sys.argv) > 1:
        download_dir = sys.argv[1]
    pathlib.Path(download_dir).mkdir(parents=True, exist_ok=True)

    for url, file_filter in model_urls:
        model_dir = os.path.join(my_path, "models")

        local_name = os.path.join(download_dir, url.split('/')[-1])
        print("Downloading %s => %s" % (url, local_name))

        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))