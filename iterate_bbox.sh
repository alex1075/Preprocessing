#! /bin/sh

./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_1000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_1000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_2000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_2000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_3000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_3000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_4000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_4000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_5000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_5000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_6000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_6000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_7000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_7000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_8000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_8000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_9000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_9000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_10000.weights -dont_show -ext_output < Mini/test.txt > Balanced/result_10000.txt

python -c "from import_results import *; import_and_filder_results('Balanced/result_1000.txt', 'Balanced/results_1000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_2000.txt', 'Balanced/results_2000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_3000.txt', 'Balanced/results_3000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_4000.txt', 'Balanced/results_4000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_5000.txt', 'Balanced/results_5000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_6000.txt', 'Balanced/results_6000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_7000.txt', 'Balanced/results_7000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_8000.txt', 'Balanced/results_8000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_9000.txt', 'Balanced/results_9000.txt')"
python -c "from import_results import *; import_and_filder_results('Balanced/result_10000.txt', 'Balanced/results_10000.txt')"

rm Balanced/result_10000.txt
rm Balanced/result_9000.txt
rm Balanced/result_8000.txt
rm Balanced/result_7000.txt
rm Balanced/result_6000.txt
rm Balanced/result_5000.txt
rm Balanced/result_4000.txt
rm Balanced/result_3000.txt
rm Balanced/result_2000.txt
rm Balanced/result_1000.txt

python -c "from import_results import *; make_groud_truth('Balanced/gt.txt', '/home/as-hunt/Mini/')"
python -c "from import_results import *; cleanup('Balanced/results_1000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_2000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_3000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_4000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_5000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_6000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_7000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_8000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_9000.txt')"
python -c "from import_results import *; cleanup('Balanced/results_10000.txt')"
python -c "from import_results import *; cleanup('Balanced/gt.txt')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_1000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/1000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_1000.txt', '/home/as-hunt/Balanced/1000/', '/home/as-hunt/Balanced/1000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_2000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/2000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_2000.txt', '/home/as-hunt/Balanced/2000/', '/home/as-hunt/Balanced/2000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_3000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/3000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_3000.txt', '/home/as-hunt/Balanced/3000/', '/home/as-hunt/Balanced/3000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_4000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/4000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_4000.txt', '/home/as-hunt/Balanced/4000/', '/home/as-hunt/Balanced/4000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_5000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/5000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_5000.txt', '/home/as-hunt/Balanced/5000/', '/home/as-hunt/Balanced/5000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_6000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/6000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_6000.txt', '/home/as-hunt/Balanced/6000/', '/home/as-hunt/Balanced/6000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_7000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/7000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_7000.txt', '/home/as-hunt/Balanced/7000/', '/home/as-hunt/Balanced/7000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_8000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/8000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_8000.txt', '/home/as-hunt/Balanced/8000/', '/home/as-hunt/Balanced/8000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_9000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/9000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_9000.txt', '/home/as-hunt/Balanced/9000/', '/home/as-hunt/Balanced/9000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_10000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/10000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/results_10000.txt', '/home/as-hunt/Balanced/10000/', '/home/as-hunt/Balanced/10000/')"

python -c "from confusion import *; get_the_csv('Balanced/gt.txt', 'Balanced/results_1000.txt')"
python -c "from confusion import *; get_the_csv('Balanced/results_2000.txt', 'Balanced/results_3000.txt')"
python -c "from confusion import *; get_the_csv('Balanced/results_4000.txt', 'Balanced/results_5000.txt')"
python -c "from confusion import *; get_the_csv('Balanced/results_6000.txt', 'Balanced/results_6000.txt')"
python -c "from confusion import *; get_the_csv('Balanced/results_7000.txt', 'Balanced/results_8000.txt')"
python -c "from confusion import *; get_the_csv('Balanced/results_9000.txt', 'Balanced/results_10000.txt')"

python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_1000.csv', title='Confusion_matrix_1000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_2000.csv', title='Confusion_matrix_2000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_3000.csv', title='Confusion_matrix_3000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_4000.csv', title='Confusion_matrix_4000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_5000.csv', title='Confusion_matrix_5000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_6000.csv', title='Confusion_matrix_6000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_7000.csv', title='Confusion_matrix_7000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_8000.csv', title='Confusion_matrix_8000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_9000.csv', title='Confusion_matrix_9000')"
python -c "from confusion import *; plot_confusion_matrix('Balanced/gt.csv', 'Balanced/results_10000.csv', title='Confusion_matrix_10000')"

python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_1000.csv', title='Normalised_Confusion_matrix_1000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_2000.csv', title='Normalised_Confusion_matrix_2000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_3000.csv', title='Normalised_Confusion_matrix_3000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_4000.csv', title='Normalised_Confusion_matrix_4000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_5000.csv', title='Normalised_Confusion_matrix_5000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_6000.csv', title='Normalised_Confusion_matrix_6000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_7000.csv', title='Normalised_Confusion_matrix_7000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_8000.csv', title='Normalised_Confusion_matrix_8000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_9000.csv', title='Normalised_Confusion_matrix_9000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('Balanced/gt.csv', 'Balanced/results_10000.csv', title='Normalised_Confusion_matrix_10000')"

mv Confusion_matrix* Balanced/
mv Normalised_Confusion_matrix* Balanced/
rm Balanced/*.csv

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/1000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/1000/', '/home/as-hunt/Balanced/1000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/2000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/2000/', '/home/as-hunt/Balanced/2000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/3000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/3000/', '/home/as-hunt/Balanced/3000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/4000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/4000/', '/home/as-hunt/Balanced/4000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/5000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/5000/', '/home/as-hunt/Balanced/5000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/6000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/6000/', '/home/as-hunt/Balanced/6000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/7000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/7000/', '/home/as-hunt/Balanced/7000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/8000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/8000/', '/home/as-hunt/Balanced/8000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/9000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/9000/', '/home/as-hunt/Balanced/9000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/10000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/gt.txt', '/home/as-hunt/Balanced/10000/', '/home/as-hunt/Balanced/10000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_1000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/1000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_1000.txt', '/home/as-hunt/Balanced/1000/', '/home/as-hunt/Balanced/1000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_2000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/2000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_2000.txt', '/home/as-hunt/Balanced/2000/', '/home/as-hunt/Balanced/2000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_3000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/3000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_3000.txt', '/home/as-hunt/Balanced/3000/', '/home/as-hunt/Balanced/3000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_4000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/4000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_4000.txt', '/home/as-hunt/Balanced/4000/', '/home/as-hunt/Balanced/4000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_5000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/5000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_5000.txt', '/home/as-hunt/Balanced/5000/', '/home/as-hunt/Balanced/5000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_6000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/6000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_6000.txt', '/home/as-hunt/Balanced/6000/', '/home/as-hunt/Balanced/6000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_7000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/7000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_7000.txt', '/home/as-hunt/Balanced/7000/', '/home/as-hunt/Balanced/7000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_8000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/8000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_8000.txt', '/home/as-hunt/Balanced/8000/', '/home/as-hunt/Balanced/8000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_9000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/9000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_9000.txt', '/home/as-hunt/Balanced/9000/', '/home/as-hunt/Balanced/9000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/Balanced/results_10000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Balanced/10000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/Balanced/results_10000.txt', '/home/as-hunt/Balanced/10000/', '/home/as-hunt/Balanced/10000/', 'pd')"

python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_1000.txt')" > Balanced/details_1000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_2000.txt')" > Balanced/details_2000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_3000.txt')" > Balanced/details_3000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_4000.txt')" > Balanced/details_4000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_5000.txt')" > Balanced/details_5000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_6000.txt')" > Balanced/details_6000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_7000.txt')" > Balanced/details_7000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_8000.txt')" > Balanced/details_8000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_9000.txt')" > Balanced/details_9000.txt
python -c "from confusion import *; do_math('Balanced/gt.txt', 'Balanced/results_10000.txt')" > Balanced/details_10000.txt