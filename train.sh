#! /bin/sh

./build_release/darknet detector map train data/train/_darknet.labels cfg/yolov4.cfg weights.file -json_port 8070 -mjpeg_port 8090 