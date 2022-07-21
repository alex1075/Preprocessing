from turtle import st
import cv2
import glob, os, datetime
from PIL import Image
from imutils import paths
from code.helper.utils import *
from code.helper.imageTools import *
import shutil

def convert(path_to_folder='/Volumes/PhD/PhD/Data/'):
    for infile in os.listdir(path_to_folder):
        print ("file : " + infile)
        if infile[-3:] == "bmp":
            print ("is bmp")
            outfile = infile[:-3] + "jpg"
            im = Image.open(path_to_folder + infile)
            print ("new filename : " + outfile)
            out = im.convert("RGB")
            out.save(path_to_folder + outfile, "jpeg", quality=100)
            os.remove(path_to_folder + infile)
        elif infile[-4:] == "tiff":
            print ("is tiff")
            outfile = infile[:-4] + "jpg"
            im = Image.open(path_to_folder + infile)
            out = im.convert("RGB")
            out.save(path_to_folder + outfile, "jpeg", quality=100)
            os.remove(path_to_folder + infile)
        elif infile[-3:] == "png":
            print ("is png")
            outfile = infile[:-3] + "jpg"
            img = cv2.imread(path_to_folder + infile)
            cv2.imwrite(path_to_folder + outfile, img)
            os.remove(path_to_folder + infile)
        elif infile[-3:] == "jpg" or infile[-3:] == "jpeg":
            print ("is jpg, no change")
        else:
            print ("Not an image")

#Cycles through iamges in path_to_folder and resize them the desired size
def resizeAllJpg(path_to_folder='/Volumes/PhD/PhD/Data/', newhight=1080, newwid=1080):
  jpgs = glob.glob(path_to_folder + '*.jpg')
  for image in jpgs:
      print ("resizing image" + image)
      name_without_extension = os.path.splitext(image)[0]
      img = cv2.imread(image)
      resized, newheight, newwidth = resizeTo(img, newhight, newwid)
      cv2.imwrite(name_without_extension + ".jpg", resized)

#Cycles through videos in path_to_folder and outputs jpg to out_folder
def convertVideoToImage(path_to_folder='/Volumes/PhD/PhD/Video/', out_folder='/Volumes/PhD/PhD/Data/'):
    for fi in os.listdir(path_to_folder):
        nam, ext = os.path.splitext(fi)
        if ext == '.mp4':
            cam = cv2.VideoCapture(path_to_folder + fi)
            try:
                # creating a folder named data
                if not os.path.exists(out_folder):
                    os.makedirs(out_folder)
            # if not created then raise error
            except OSError:
                print ('Error: Creating directory of' + out_folder)
            # frame
            currentframe = 0
            while(True):
                # reading from frame
                ret,frame = cam.read()
                if ret:
                    # if video is still left continue creating images
                    name = out_folder + nam + '_frame_' + str(currentframe) + '.jpg'
                    print ('Creating...' + name)
                    # writing the extracted images
                    cv2.imwrite(name, frame)
                    # increasing counter so that it will
                    # show how many frames are created
                    currentframe += 1
                else:
                    break
            # Release all space and windows once done
            cam.release()
            cv2.destroyAllWindows()

def normalise(path_to_folder=r'/Volumes/PhD/PhD/Data/'):
    jpgs = glob.glob(path_to_folder + '*.jpg')
    for infile in jpgs:
        print ("file : " + infile)
        flute = cv2.imread(infile)
        print ("Normalising " + infile)
        im = normaliseImg(flute)
        cv2.imwrite(path_to_folder + infile, im)

def randomCrop(path_to_folder='/Volumes/PhD/PhD/Data/', outfolder='/Volumes/PhD/PhD/Dataset/', crop_height=256, crop_width=256):
    jpgs = glob.glob(path_to_folder + '*.jpg')
    for jpg in jpgs:
        print("randomly cropping: " + jpg)
        flute = cv2.imread(jpg, 0)
        jpg_name = jpg.split('/')[-1]
        infile = jpg_name[:-4] + "_cropped_" + str(datetime.datetime.now()) + ".jpg"
        print(infile)
        im = getRandomCrop(flute, crop_height, crop_width)
        cv2.imwrite(outfolder + infile, im)

def convert2Gray(path_to_folder='/Volumes/PhD/PhD/Dataset/'):
    jpgs = glob.glob(path_to_folder  + '*.jpg')
    for jpg in jpgs:
        print('Converting to grayscale: ' + jpg)
        flute = cv2.imread(jpg, 0)
        print(flute.shape)
        cv2.imwrite(jpg, flute)

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

def detectBlurr(path_to_folder='/Volumes/PHD/', threshold=100.0):
    file = open(path_to_folder + 'recap.txt', "w")
    file.write('Threshold: ' + str(threshold) + '\n')
    print('Detecting blurr')
   # loop over the input images
    for imagePath in paths.list_images(path_to_folder):
        # load the image, convert it to grayscale, and compute the
        # focus measure of the image using the Variance of Laplacian
        # method
        print("Checking image: " + imagePath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        text = 'Not Blurry'
 
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        if fm < threshold:
            text = 'Blurry'
            print(imagePath)
            # file.write(fm + "<" + threshold + '\n')
            file.write('Below threshold' + imagePath + '\n')
        # print(image)
    
    file.close()

def iterateBlur(path_to_folder='/Volumes/PHD/', start=0, end=100, step=5):
    for i in range(start, end, step):
        print('Threshold: ' + str(i))
        detectBlurr(path_to_folder, threshold=i)

def detectAndMoveBlurr(path_to_folder='/Volumes/PHD/', threshold=100.0, currentstep=110, outfolder='/Volumes/PHD/sorted/'):
    file = open(outfolder + 'recap.txt', "w")
    file.write('Threshold: ' + str(threshold) + '\n')
    print('Detecting blurr')
    os.makedirs(outfolder + 'threshold_' + str(threshold), exist_ok=True)
   # loop over the input images
    for imagePath in paths.list_images(path_to_folder):
        # load the image, convert it to grayscale, and compute the
        # focus measure of the image using the Variance of Laplacian
        # method
        print("Checking image: " + imagePath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        if fm < threshold & threshold < currentstep:
            print(imagePath)
            # file.write(fm + "<" + threshold + '\n')
            file.write('Below threshold' + imagePath + '\n')
            shutil.copy(imagePath, outfolder + 'threshold_' + str(threshold))
            os.remove(imagePath)
            print("Moved " + imagePath)
            file.write('Moved ' + imagePath + ' to folder' + '\n')

    file.close()

def iterateBlurMove(path_to_folder='/Volumes/PHD/', outfolder='/Volumes/PHD/sorted/', start=0, end=100, step=5):
    for i in range(start, end, step):
        print('Threshold: ' + str(i))
        currentstep = str(range) + str(step)
        detectAndMoveBlurr(path_to_folder, threshold=i, currentstep=currentstep, outfolder=outfolder)

def selectIMG(path_to_folder='/Volumes/PHD/sorted/', outfolder='/Volumes/PHD/sorted/', number=200):
    randomSelect(path_to_folder, outfolder, number)

def chopUpDataset(path_to_folder='/Users/alexanderhunt/Preprocessing/test_dataset_no_OTH/', outfolder='/Users/alexanderhunt/Preprocessing/output/', x=416, y=416, annotations=True):
    crop_images(x, y, path_to_folder, outfolder, annotations)
    if annotations == True:
        remove_non_annotated(outfolder)
    else:
        pass
    checkAllImg(outfolder, x, y)

def batchBackgroundRemove(path_to_folder='output/', background_folder='background/', outfolder='/Volumes/PHD/removed/'):
    return print('Not implemented yet')

def batchBackgroundRemove(path_to_folder='output/', background_folder='backgrounds/', outfolder='data_2/', alpha=2):
    list_img=[img for img in os.listdir(path_to_folder) if img.endswith('.jpg')==True]
    list_background=[img for img in os.listdir(background_folder) if img.endswith('.jpg')==True]
    list_txt=[img for img in os.listdir(path_to_folder) if img.endswith('.txt')==True]
    for img in list_img:
        index = img.split('_')
        name = index[0] + '_' + index[1]
        first_chop = index[2]
        second_chop = index[3]
        condition = 'background''_' + str(first_chop) + '_' + str(second_chop)
        img_path = outfolder + img
        background_element = [x for x in list_background if x==condition]
        background = str(background_element[0])
        img = background_removal_with_alpha(path_to_folder+img, background_folder+background, alpha)
        cv2.imwrite(img_path, img)
        print('Matched ' + img_path + ' with ' + background)
        annotation_condition  = name + '_' + str(first_chop) + '_' + str(second_chop)[:-4] + '.txt'
        annotation_file = [x for x in list_txt if x==annotation_condition]
        annotation = str(annotation_file[0])
        print('Matched ' + annotation + ' with ' + annotation_condition)
        os.system('cp ' + path_to_folder + annotation + ' ' + outfolder + annotation)
    classes_file = [x for x in list_txt if x=='classes.txt']
    classes = str(classes_file[0])
    os.system('cp ' + path_to_folder + classes + ' ' + outfolder + classes)