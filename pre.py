import os
import glob

# file = open("/darknet/data/train/train.txt", "w")
# dirs = os.listdir("/darknet/data/train/")


def train_prep(file="/mnt/c/Users/Alexander Hunt/data/train/train.txt", dir="/mnt/c/Users/Alexander Hunt/data/train/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("/mnt/c/Users/Alexander Hunt/data/train/" + image + "\n")
    filoo.close()

def test_prep(file="/mnt/c/Users/Alexander Hunt/data/test/test.txt", dir="/mnt/c/Users/Alexander Hunt/data/test/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("/mnt/c/Users/Alexander Hunt/data/test/" + image + "\n")
    filoo.close()

def val_prep(file="/mnt/c/Users/Alexander Hunt/data/valid/valid.txt", dir="/mnt/c/Users/Alexander Hunt/data/valid/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("/mnt/c/Users/Alexander Hunt/data/valid/" + image + "\n")
    filoo.close()

def more_prep(file="mini_valdi/valid.txt", dir="mini_valdi/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("mini_valdi/" + image + "\n")
    filoo.close()


def allDaPrep():
    train_prep()
    test_prep()
    val_prep()

if __name__ == "__main__":
    # allDaPrep()
    more_prep()
