#! /bin/sh

# train the model

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Initiating training:"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Yolov4 default cfg"

# Bare metal training:
darknet detector train /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/default.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Training complete!"

mv chart.png /home/as-hunt/Etra-Space/xmas_tests/results/charts/default.png
mv /home/as-hunt/Etra-Space/xmas_tests/backup/yolov4_final.weights /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights

# test

darknet detector test /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/default.cfg /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/xmas_tests/test/test.txt > /home/as-hunt/Etra-Space/xmas_tests/result.txt

# python -c "from import_results import *; import_and_filder_results('/home/as-hunt/Etra-Space/xmas_tests/result.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

# rm /home/as-hunt/1_in_100/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/test/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Etra-Space/xmas_tests/gt.csv', '/home/as-hunt/Etra-Space/xmas_tests/results.csv', title='Confusion_matrix_default')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/1_in_100/gt.csv', '/home/as-hunt/1_in_100/results.csv', title='Normalised_Confusion_matrix_default')"

# mv Confusion_matrix_test_dataset /home/as-hunt/1_in_100/
mv *Confusion_matrix* /home/as-hunt/Etra-Space/xmas_tests/results

python -c "from confusion import *; do_math('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-space/xmas-tests/results.txt')" > /home/as-hunt/Etra-Space/xmas_tests/results/default_report.txt

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Tests complete!"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Moving on..."

# train the model

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Initiating training:"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Yolov4 low learning rate cfg"

# Bare metal training:
darknet detector train /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/low_LR.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Training complete!"

mv chart.png /home/as-hunt/Etra-Space/xmas_tests/results/charts/default.png
mv /home/as-hunt/Etra-Space/xmas_tests/backup/yolov4_final.weights /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights

# test

darknet detector test /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/low_LR.cfg /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/xmas_tests/test/test.txt > /home/as-hunt/Etra-Space/xmas_tests/result.txt

# python -c "from import_results import *; import_and_filder_results('/home/as-hunt/Etra-Space/xmas_tests/result.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

# rm /home/as-hunt/1_in_100/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/test/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Etra-Space/xmas_tests/gt.csv', '/home/as-hunt/Etra-Space/xmas_tests/results.csv', title='Confusion_matrix_default')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/1_in_100/gt.csv', '/home/as-hunt/1_in_100/results.csv', title='Normalised_Confusion_matrix_default')"

# mv Confusion_matrix_test_dataset /home/as-hunt/1_in_100/
mv *Confusion_matrix* /home/as-hunt/Etra-Space/xmas_tests/results

python -c "from confusion import *; do_math('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/1_in_100/results.txt')" > /home/as-hunt/Etra-Space/xmas_tests/results/default_report.txt

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Tests complete!"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Moving on..."

# train the model

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Initiating training:"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Yolov4 very low learning rate cfg"

# Bare metal training:
darknet detector train /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/vlow_LR.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Training complete!"

mv chart.png /home/as-hunt/Etra-Space/xmas_tests/results/charts/default.png
mv /home/as-hunt/Etra-Space/xmas_tests/backup/yolov4_final.weights /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights

# test

darknet detector test /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/vlow_LR.cfg /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/xmas_tests/test/test.txt > /home/as-hunt/Etra-Space/xmas_tests/result.txt

# python -c "from import_results import *; import_and_filder_results('/home/as-hunt/Etra-Space/xmas_tests/result.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

# rm /home/as-hunt/1_in_100/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/test/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Etra-Space/xmas_tests/gt.csv', '/home/as-hunt/Etra-Space/xmas_tests/results.csv', title='Confusion_matrix_default')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/1_in_100/gt.csv', '/home/as-hunt/1_in_100/results.csv', title='Normalised_Confusion_matrix_default')"

# mv Confusion_matrix_test_dataset /home/as-hunt/1_in_100/
mv *Confusion_matrix* /home/as-hunt/Etra-Space/xmas_tests/results

python -c "from confusion import *; do_math('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/1_in_100/results.txt')" > /home/as-hunt/Etra-Space/xmas_tests/results/default_report.txt

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Tests complete!"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Moving on..."

# train the model

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Initiating training:"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Yolov4 high learning rate rate cfg"

# Bare metal training:
darknet detector train /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/high_LR.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Training complete!"

mv chart.png /home/as-hunt/Etra-Space/xmas_tests/results/charts/default.png
mv /home/as-hunt/Etra-Space/xmas_tests/backup/yolov4_final.weights /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights

# test

darknet detector test /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/high_LR.cfg /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/xmas_tests/test/test.txt > /home/as-hunt/Etra-Space/xmas_tests/result.txt

# python -c "from import_results import *; import_and_filder_results('/home/as-hunt/Etra-Space/xmas_tests/result.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

# rm /home/as-hunt/1_in_100/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/test/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Etra-Space/xmas_tests/gt.csv', '/home/as-hunt/Etra-Space/xmas_tests/results.csv', title='Confusion_matrix_default')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/1_in_100/gt.csv', '/home/as-hunt/1_in_100/results.csv', title='Normalised_Confusion_matrix_default')"

# mv Confusion_matrix_test_dataset /home/as-hunt/1_in_100/
mv *Confusion_matrix* /home/as-hunt/Etra-Space/xmas_tests/results

python -c "from confusion import *; do_math('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/1_in_100/results.txt')" > /home/as-hunt/Etra-Space/xmas_tests/results/default_report.txt

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Tests complete!"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Moving on..."

# train the model

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Initiating training:"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Yolov4 very high learning rate cfg"

# Bare metal training:
darknet detector train /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/vhigh_LR.cfg /home/as-hunt/Etra-Space/cfg/yolov4.conv.137 -mjpeg_port 8090 -clear -dont_show -map | tee -a train.txt 

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Training complete!"

mv chart.png /home/as-hunt/Etra-Space/xmas_tests/results/charts/default.png
mv /home/as-hunt/Etra-Space/xmas_tests/backup/yolov4_final.weights /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights

# test

darknet detector test /home/as-hunt/Etra-Space/xmas_tests/obj.data /home/as-hunt/Etra-Space/xmas_tests/cfgs/vhigh_LR.cfg /home/as-hunt/Etra-Space/xmas_tests/results/weights/default.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/xmas_tests/test/test.txt > /home/as-hunt/Etra-Space/xmas_tests/result.txt

# python -c "from import_results import *; import_and_filder_results('/home/as-hunt/Etra-Space/xmas_tests/result.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

# rm /home/as-hunt/1_in_100/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/test/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/Etra-Space/xmas_tests/results.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Etra-Space/xmas_tests/gt.csv', '/home/as-hunt/Etra-Space/xmas_tests/results.csv', title='Confusion_matrix_default')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/1_in_100/gt.csv', '/home/as-hunt/1_in_100/results.csv', title='Normalised_Confusion_matrix_default')"

# mv Confusion_matrix_test_dataset /home/as-hunt/1_in_100/
mv *Confusion_matrix* /home/as-hunt/Etra-Space/xmas_tests/results

python -c "from confusion import *; do_math('/home/as-hunt/Etra-Space/xmas_tests/gt.txt', '/home/as-hunt/1_in_100/results.txt')" > /home/as-hunt/Etra-Space/xmas_tests/results/default_report.txt

./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Tests complete!"
./matrix.sh  --homeserver=https://matrix.as-hunt.co.uk --token=syt_ZGFya25ldA_jdToBfGEejNeGMICXYlZ_15gFyp --room=\!FORqRFTVymsOxOpMDk:matrix.as-hunt.co.uk "Moving on..."

