#! /bin/sh

conda activate Preprocessing

python -c "from code.convert import *; iterateBlurMove('/mnt/e22684ab-96ea-4683-8d3d-e0fed05e3c86/25032022/PHD/', 0, 100, 5)"