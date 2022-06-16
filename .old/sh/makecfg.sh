#! /bin/sh 

echo "Be sure to have modified yolov4-custom.cfg to reflect your own dataset"
wait
cp /preprocessing/yolov4-custom.cfg /preprocessing/cfg/yolov4.cfg
ehco "yolov4.cfg created in cfg folder"
