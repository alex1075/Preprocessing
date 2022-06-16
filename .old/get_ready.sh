#! /bin/sh

echo "Getting read for the training"
echo "Downloading yolov4 weights"
sh /sh/get_weights.sh
echo "Downloading yolov4 weights done"
echo "Creating yolov4.cfg"
sh /sh/makecfg.sh
echo "Creating yolov4.cfg done"
echo "Copying over train.sh over to data folder"
cp /sh/train.sh /data/train.sh
echo "Copying over train.sh over to data folder done"
echo "Ready to start trainning! Good luck!"
