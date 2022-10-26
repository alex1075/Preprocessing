#! /bin/sh
export CUDA_VISIBLE_DEVICES=0
echo "Let's go!"

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Initiating training:"


# Bare metal training:
# ./darknet/darknet detector train /home/as-hunt/Etra-Space/obj.data /home/as-hunt/Etra-Space/cfg/yolov4.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 
./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_1000.weights
mv chart.png Etra-Space/backup/Step_3/chart_1000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "1000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_1000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_2000.weights
mv chart.png Etra-Space/backup/Step_3/chart_2000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "2000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_2000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_3000.weights
mv chart.png Etra-Space/backup/Step_3/chart_3000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "3000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_3000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_4000.weights
mv chart.png Etra-Space/backup/Step_3/chart_4000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "4000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_4000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_5000.weights
mv chart.png Etra-Space/backup/Step_3/chart_5000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "5000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_5000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_6000.weights
mv chart.png Etra-Space/backup/Step_3/chart_6000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "6000 epochs complete, moving on."


./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_6000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_7000.weights
mv chart.png Etra-Space/backup/Step_3/chart_7000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "7000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_7000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_8000.weights
mv chart.png Etra-Space/backup/Step_3/chart_8000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "8000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_8000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_9000.weights
mv chart.png Etra-Space/backup/Step_3/chart_9000.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "9000 epochs complete, moving on."

./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/obj.data /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg /home/as-hunt/Etra-Space/backup/Step_3/yolov4_9000.weights -mjpeg_port 8090 -clear -dont_show
mv Etra-Space/backup/yolov4_1000.weights Etra-Space/backup/Step_3/yolov4_10000.weights
mv chart.png Etra-Space/backup/Step_3/chart_10000.png


./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Training complete!"
