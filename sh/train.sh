#! /bin/sh

./darknet/darknet detector train data/obj.data cfg/yolov4.cfg cfg/yolov4.conv.137 -json_port 8070 -mjpeg_port 8090 -clear -map | tee -a train.txt
