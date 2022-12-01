#! /bin/sh

darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_10000.weights -dont_show -ext_output < /home/as-hunt/1in10/test/test.txt > /home/as-hunt/1in10/result.txt

python -c "from import_results import *; import_and_filder_results('/home/as-hunt/1in10/result.txt', '/home/as-hunt/1in10/results.txt')"

# rm /home/as-hunt/1in10/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/1in10/gt.txt', '/home/as-hunt/1in10/test/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/1in10/gt.txt', '/home/as-hunt/1in10/results.txt', '/home/as-hunt/1in10/test/', '/home/as-hunt/1in10/mistakes/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/1in10/gt.txt', '/home/as-hunt/1in10/results.txt', '/home/as-hunt/1in10/mistakes/', '/home/as-hunt/1in10/mistakes/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/1in10/gt.txt', '/home/as-hunt/1in10/results.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/1in10/gt.csv', '/home/as-hunt/1in10/results.csv', title='Confusion_matrix_test_dataset')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/1in10/gt.csv', '/home/as-hunt/1in10/results.csv', title='Normalised_Confusion_matrix_test_dataset')"

# mv Confusion_matrix_test_dataset /home/as-hunt/1in10/
mv Normalised_Confusion_matrix_test_dataset /home/as-hunt/1in10/
rm /home/as-hunt/1in10/*.csv

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/1in10/gt.txt', '/home/as-hunt/1in10/test/', '/home/as-hunt/1in10/gt/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/1in10/gt.txt', '/home/as-hunt/1in10/gt/', '/home/as-hunt/1in10/gt/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/1in10/results.txt', '/home/as-hunt/1in10/test/', '/home/as-hunt/1in10/pd/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/1in10/results.txt', '/home/as-hunt/1in10/pd/', '/home/as-hunt/1in10/pd/', 'pd')"

python -c "from confusion import *; do_math('/home/as-hunt/1in10/gt.txt', '/home/as-hunt/1in10/results.txt')" > /home/as-hunt/1in10/report.txt
