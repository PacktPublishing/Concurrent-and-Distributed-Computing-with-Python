import time
import os
from PIL import Image  # pip install pillow if not found
from glob import glob

__author__ = "Mithun"


def create_thumbnail(image_file):
    size = 128, 128

    file_name, ext = os.path.splitext(image_file)
    image = Image.open(image_file)
    image.thumbnail(size)

    image.save(file_name + ".t.jpeg", "jpeg")

    print("Thumbnail created for {} as {}".format(image_file, file_name + ".t.jpeg"))


if __name__ == "__main__":
    image_files = glob("/Users/mithun.lakshmanswamy/Downloads/happy-face/*.jpeg")

    start = time.time()

    for image_file in image_files:
        create_thumbnail(image_file)

    end = time.time()

    print("Total time taken is for thumbnail generation is {} seconds".format(end - start))
