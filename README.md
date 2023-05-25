
# JG's Semantic Image Segmentation\n\nWelcome to the JujitsuGang's service for comprehensive semantic segmentation on images. It currently supports only the Mask_RCNN approach leveraging Matterport's Mask_RCNN.\n\n## Setup\n\nOur service requires Python 3.6 or above and NodeJS/npm. Follow the below steps to setup:\n\n```
pip install -r requirements.txt
git clone https://github.com/JujitsuGang/JG-semantic-image-segmentation.git
cd JG-semantic-image-segmentation
./scripts/blockchain install
pip install -e .
```
\n## Calling the published service\n\n```
snet channel open-init snet JG-semantic-image-segmentation  0.001 +10days
snet --print-traceback client call snet JG-semantic-image-segmentation segment '{"img": {"file@content":"test.jpg", "mimetype": "image/jpeg"}, "visualise":true}'
```
\nExtracting the contents of the response currently can't easily be done with the CLI.\n\n## Issues\n\nIn case of an ImportError ending with `cytoolz/functoolz.cpython-36m-x86_64-linux-gnu.so: undefined symbol: PyFPE_jbuf`, this can be solved as per [this Stack Overflow post](https://github.com/pytoolz/cytoolz/issues/120) with:\n\n`pip install --no-cache-dir cytoolz`