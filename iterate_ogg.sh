#! /bin/sh

./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_1000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_1000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_2000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_2000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_3000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_3000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_4000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_4000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_5000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_5000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_6000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_6000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_7000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_7000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_8000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_8000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_9000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_9000.txt
./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_2/yolov4_10000.weights -dont_show -ext_output < Mini/test.txt > Original_sidless/result_10000.txt

python -c "from import_results import *; import_and_filder_results('Original_sidless/result_1000.txt', 'Original_sidless/results_1000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_2000.txt', 'Original_sidless/results_2000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_3000.txt', 'Original_sidless/results_3000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_4000.txt', 'Original_sidless/results_4000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_5000.txt', 'Original_sidless/results_5000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_6000.txt', 'Original_sidless/results_6000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_7000.txt', 'Original_sidless/results_7000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_8000.txt', 'Original_sidless/results_8000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_9000.txt', 'Original_sidless/results_9000.txt')"
python -c "from import_results import *; import_and_filder_results('Original_sidless/result_10000.txt', 'Original_sidless/results_10000.txt')"

rm Original_sidless/result_10000.txt
rm Original_sidless/result_9000.txt
rm Original_sidless/result_8000.txt
rm Original_sidless/result_7000.txt
rm Original_sidless/result_6000.txt
rm Original_sidless/result_5000.txt
rm Original_sidless/result_4000.txt
rm Original_sidless/result_3000.txt
rm Original_sidless/result_2000.txt
rm Original_sidless/result_1000.txt

python -c "from import_results import *; make_groud_truth('Original_sidless/gt.txt', '/home/as-hunt/Mini/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_1000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/1000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_1000.txt', '/home/as-hunt/Original_sidless/1000/', '/home/as-hunt/Original_sidless/1000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_2000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/2000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_2000.txt', '/home/as-hunt/Original_sidless/2000/', '/home/as-hunt/Original_sidless/2000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_3000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/3000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_3000.txt', '/home/as-hunt/Original_sidless/3000/', '/home/as-hunt/Original_sidless/3000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_4000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/4000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_4000.txt', '/home/as-hunt/Original_sidless/4000/', '/home/as-hunt/Original_sidless/4000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_5000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/5000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_5000.txt', '/home/as-hunt/Original_sidless/5000/', '/home/as-hunt/Original_sidless/5000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_6000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/6000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_6000.txt', '/home/as-hunt/Original_sidless/6000/', '/home/as-hunt/Original_sidless/6000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_7000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/7000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_7000.txt', '/home/as-hunt/Original_sidless/7000/', '/home/as-hunt/Original_sidless/7000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_8000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/8000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_8000.txt', '/home/as-hunt/Original_sidless/8000/', '/home/as-hunt/Original_sidless/8000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_9000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/9000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_9000.txt', '/home/as-hunt/Original_sidless/9000/', '/home/as-hunt/Original_sidless/9000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_10000.txt', '/home/as-hunt/Mini/', '/home/as-hunt/Original_sidless/10000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_10000.txt', '/home/as-hunt/Original_sidless/10000/', '/home/as-hunt/Original_sidless/10000/')"

python -c "from confusion import *; get_the_csv('/home/as-hunt/Original_sidless/gt.txt', '/home/as-hunt/Original_sidless/results_1000.txt')"
python -c "from confusion import *; get_the_csv('/home/as-hunt/Original_sidless/results_2000.txt', '/home/as-hunt/Original_sidless/results_3000.txt')"
python -c "from confusion import *; get_the_csv('/home/as-hunt/Original_sidless/results_4000.txt', '/home/as-hunt/Original_sidless/results_5000.txt')"
python -c "from confusion import *; get_the_csv('/home/as-hunt/Original_sidless/results_6000.txt', '/home/as-hunt/Original_sidless/results_6000.txt')"
python -c "from confusion import *; get_the_csv('/home/as-hunt/Original_sidless/results_7000.txt', '/home/as-hunt/Original_sidless/results_8000.txt')"
python -c "from confusion import *; get_the_csv('/home/as-hunt/Original_sidless/results_9000.txt', '/home/as-hunt/Original_sidless/results_10000.txt')"

python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_1000.csv', title='Confusion_matrix_1000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_2000.csv', title='Confusion_matrix_2000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_3000.csv', title='Confusion_matrix_3000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_4000.csv', title='Confusion_matrix_4000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_5000.csv', title='Confusion_matrix_5000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_6000.csv', title='Confusion_matrix_6000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_7000.csv', title='Confusion_matrix_7000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_8000.csv', title='Confusion_matrix_8000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_9000.csv', title='Confusion_matrix_9000')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_10000.csv', title='Confusion_matrix_10000')"

python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_1000.csv', title='Normalised_Confusion_matrix_1000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_2000.csv', title='Normalised_Confusion_matrix_2000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_3000.csv', title='Normalised_Confusion_matrix_3000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_4000.csv', title='Normalised_Confusion_matrix_4000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_5000.csv', title='Normalised_Confusion_matrix_5000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_6000.csv', title='Normalised_Confusion_matrix_6000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_7000.csv', title='Normalised_Confusion_matrix_7000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_8000.csv', title='Normalised_Confusion_matrix_8000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_9000.csv', title='Normalised_Confusion_matrix_9000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Original_sidless/gt.csv', '/home/as-hunt/Original_sidless/results_10000.csv', title='Normalised_Confusion_matrix_10000')"

mv Confusion_matrix* /home/as-hunt/Original_sidless/
mv Normalised_Confusion_matrix* /home/as-hunt/Original_sidless/
rm /home/as-hunt/Original_sidless/*.csv

python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_1000.txt')" > Original_sidless/details_1000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_2000.txt')" > Original_sidless/details_2000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_3000.txt')" > Original_sidless/details_3000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_4000.txt')" > Original_sidless/details_4000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_5000.txt')" > Original_sidless/details_5000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_6000.txt')" > Original_sidless/details_6000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_7000.txt')" > Original_sidless/details_7000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_8000.txt')" > Original_sidless/details_8000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_9000.txt')" > Original_sidless/details_9000.txt
python -c "from confusion import *; do_math('Original_sidless/gt.txt', 'Original_sidless/results_10000.txt')" > Original_sidless/details_10000.txt