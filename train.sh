#! /bin/sh
echo What is the name of the run?
read runname
echo 'Where is it saved? (do not add the / at the end)'
read runpath

# ./darknet/darknet detector train data_2/obj.data cfg/yolov4.cfg cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -map -dont_show | tee -a train.txt
# ./darknet/darknet detector train data/obj.data cfg/yolov4-tiny.cfg cfg/yolov4-tiny.weights -mjpeg_port 8090 -clear -map | tee -a train.txt
./darknet/darknet detector train data_NoSidesNoBG/obj.data cfg/yolov4.cfg cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -map  -dont_show | tee -a train.txt
# ./darknet/darknet detector train data/obj.data cfg/yolov4-p6.cfg cfg/yolov4-p6.weights -mjpeg_port 8090 -clear -map | tee -a train.txt

echo Training complete
cat train.txt | grep map | tee $runname.csv
echo Exported the mAP to $runname.csv
mv $runpath/yolov4_final.weights Saved_weights/$runname.weights
echo Saved the weights to Saved_weights/$runname.weights