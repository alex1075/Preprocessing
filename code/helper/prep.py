import os
import glob

# file = open("/darknet/data/train/train.txt", "w")
# dirs = os.listdir("/darknet/data/train/")


def train_prep(file="./data/train/train.txt", dir="./data/train/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("./data/train/" + image + "\n")
    filoo.close()

def test_prep(file="./data/test/test.txt", dir="./data/test/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("./data/test/" + image + "\n")
    filoo.close()

def val_prep(file="./data/valid/valid.txt", dir="./data/valid/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("./data/valid/" + image + "\n")
    filoo.close()

def allDaPrep():
    train_prep()
    test_prep()
    val_prep()

