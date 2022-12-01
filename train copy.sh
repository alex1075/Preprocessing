#! /bin/sh
export CUDA_VISIBLE_DEVICES=0
echo What is the name of the run?
read runname
echo 'Where is it saved? (do not add the / at the end)'
read runpath

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Initiating training:"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk $runname

# Bare metal training:
# ./darknet/darknet detector train /home/as-hunt/Etra-Space/obj.data /home/as-hunt/Etra-Space/cfg/yolov4.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 
./darknet/darknet detector train /home/as-hunt/Etra-Space/new_data_sidless/obj.data /home/as-hunt/Etra-Space/new_data_sidless/yolov4.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Training complete!"

echo Training complete
cat train.txt | grep map | tee $runname.csv
echo Exported the mAP to $runname.csv
mv $runpath/yolov4_final.weights Saved_weights/$runname.weights
echo Saved the weights to Saved_weights/$runname.weights
mv chart.png Saved_charts/$runname.png

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk --file=Saved_charts/$runname.png
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk --file=$runname.csv
