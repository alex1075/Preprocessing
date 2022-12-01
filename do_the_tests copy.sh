#! /bin/sh

# darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_1000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/test/test.txt > /home/as-hunt/out/result.txt

python -c "from import_results import *; import_and_filder_results('/home/as-hunt/out/result.txt', '/home/as-hunt/out/results.txt')"

# rm /home/as-hunt/out/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/out/gt.txt', '/home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/test/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/out/gt.txt', '/home/as-hunt/out/results.txt', '/home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/test/', '/home/as-hunt/out/mistakes/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/out/gt.txt', '/home/as-hunt/out/results.txt', '/home/as-hunt/out/mistakes/', '/home/as-hunt/out/mistakes/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/out/gt.txt', '/home/as-hunt/out/results.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/out/gt.csv', '/home/as-hunt/out/results.csv', title='Confusion_matrix_test_dataset')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/out/gt.csv', '/home/as-hunt/out/results.csv', title='Normalised_Confusion_matrix_test_dataset')"

# mv Confusion_matrix_test_dataset /home/as-hunt/out/
mv Normalised_Confusion_matrix_test_dataset /home/as-hunt/out/
rm /home/as-hunt/out/*.csv

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/out/gt.txt', '/home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/test/', '/home/as-hunt/out/gt/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/out/gt.txt', '/home/as-hunt/out/gt/', '/home/as-hunt/out/gt/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/out/results.txt', '/home/as-hunt/Etra-Space/new_data_sidless_no_rcc_1/test/', '/home/as-hunt/out/pd/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/out/results.txt', '/home/as-hunt/out/pd/', '/home/as-hunt/out/pd/', 'pd')"

python -c "from confusion import *; do_math('out/gt.txt', 'out/results.txt')" > out/report.txt
