import os
import shutil as s
import random as rn

FOLDER = 'Crops'
SAMPLES = 50
DESTINATION = 'VIT_Data'
os.makedirs(DESTINATION, exist_ok=True)

for c in sorted(os.listdir(FOLDER)):
    os.makedirs(os.path.join(DESTINATION, c))
    images = [os.path.join(FOLDER, c, i) for i in os.listdir(os.path.join(FOLDER, c))]
    # images = rn.choices(images, k=SAMPLES)
    images = images[:SAMPLES]
    for i in images:
        s.copyfile(i, os.path.join(DESTINATION, c, os.path.basename(i)))
