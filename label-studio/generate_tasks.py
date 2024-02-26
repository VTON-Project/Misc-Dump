import json
import glob

from label_studio_converter import brush

DATAPATH = "/home/chaitanya/personal/C-VTON/dataset/LS/"
images = sorted(glob.glob(DATAPATH + "images/*"))
tasks = []

for image in images:
    try:
        annotation = [brush.image2annotation(image.replace('images', 'masks').replace('.jpg', '.png'), "upper_body", 'tag', 'image')]
    except FileNotFoundError:
        annotation = []

    tasks.append({
        "data": {
            "image": f"data/local-files/?d={image[image.find('images'):]}"
            },
        "annotations" : annotation,
        })



with open(DATAPATH + "tasks_to_import.json", 'w') as f:
    json.dump(tasks, f)
