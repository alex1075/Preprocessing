#! /bin/sh

./darknet/darknet detector map data/obj.data cfg/yolov4.cfg data/backup/yolov4_final.weights | tee -a test.txt
