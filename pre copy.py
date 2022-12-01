import os
import glob

# file = open("/darknet/data/train/train.txt", "w")
# dirs = os.listdir("/darknet/data/train/")


def train_prep(file="train.txt", path="/mnt/c/Users/Alexander Hunt/data/train/"):
    filoo = open(path + file, 'w')
    for image in os.listdir(path):
        if image.endswith(".jpg"):
            print(image)
            filoo.write(path + image + "\n")
    filoo.close()

def test_prep(file="test.txt", path="1_in_100/train"):
    filoo = open(path + file, 'w')
    for image in os.listdir(path):
        if image.endswith(".jpg"):
            print(image)
            filoo.write(path + image + "\n")
    filoo.close()

def val_prep(file="valid.txt", path="/mnt/c/Users/Alexander Hunt/data/valid/"):
    filoo = open(path + file, 'w')
    for image in os.listdir(path):
        if image.endswith(".jpg"):
            print(image)
            filoo.write(paht + image + "\n")
    filoo.close()

# def more_prep(file="mini_valdi/valid.txt", dir="mini_valdi/"):
#     filoo = open(file, 'w')
#     for image in os.listdir(dir):
#         if image.endswith(".jpg"):
#             print(image)
#             filoo.write("mini_valdi/" + image + "\n")
#     filoo.close()


def allDaPrep():
    # train_prep('train.txt', '/mnt/c/Users/Alexander Hunt/Preprocessing/data_2/train/')
    test_prep('test.txt', '/home/as-hunt/1in10/test/')
    # val_prep()

if __name__ == "__main__":
    allDaPrep()
