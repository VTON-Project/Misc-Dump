import os
import json
import glob

import cv2
from label_studio_converter.brush import decode_rle

DATAPATH = "/home/chaitanya/personal/C-VTON/dataset/LS/"
tasks = glob.glob(os.path.join(DATAPATH, "tasks", "*"))

if not tasks:
    raise FileNotFoundError("No files found in tasks path.")

for path in tasks:
    with open(path, 'r') as f:
        task = json.load(f)
    name = task['task']['data']['image']
    name = os.path.basename(name[name.index("?")+3:].replace('.jpg', '.png'))

    try:
        rle = task['result'][0]['value']['rle']
    except IndexError:
        print("Mask not available in task to create", name)
        continue
    mask = decode_rle(rle)
    mask = mask.reshape(task['result'][0]['original_height'], task['result'][0]['original_width'], 4)[:,:,:3]
    cv2.imwrite(os.path.join(DATAPATH, 'masks', name), mask)
