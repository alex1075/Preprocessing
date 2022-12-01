#! /bin/sh

darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_1000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_1000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_2000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_2000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_3000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_3000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_4000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_4000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_5000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_5000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_6000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_6000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_7000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_7000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_8000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_8000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_9000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_9000.txt
darknet detector test /home/as-hunt/Etra-Space/3-class-sideless/obj.data /home/as-hunt/Etra-Space/3-class-sideless/yolov4.cfg Etra-Space/3-class-sideless/backup/yolov4_10000.weights -dont_show -ext_output < /home/as-hunt/Etra-Space/3-class-sideless/test/test.txt > 3-class-out_sideless/result_10000.txt

python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_1000.txt', '3-class-out_sideless/results_1000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_2000.txt', '3-class-out_sideless/results_2000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_3000.txt', '3-class-out_sideless/results_3000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_4000.txt', '3-class-out_sideless/results_4000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_5000.txt', '3-class-out_sideless/results_5000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_6000.txt', '3-class-out_sideless/results_6000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_7000.txt', '3-class-out_sideless/results_7000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_8000.txt', '3-class-out_sideless/results_8000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_9000.txt', '3-class-out_sideless/results_9000.txt')"
python -c "from import_results import *; import_and_filder_results('3-class-out_sideless/result_10000.txt', '3-class-out_sideless/results_10000.txt')"

# rm 3-class-out_sideless/result_10000.txt
# rm 3-class-out_sideless/result_9000.txt
# rm 3-class-out_sideless/result_8000.txt
# rm 3-class-out_sideless/result_7000.txt
# rm 3-class-out_sideless/result_6000.txt
# rm 3-class-out_sideless/result_5000.txt
# rm 3-class-out_sideless/result_4000.txt
# rm 3-class-out_sideless/result_3000.txt
# rm 3-class-out_sideless/result_2000.txt
# rm 3-class-out_sideless/result_1000.txt

python -c "from import_results import *; make_groud_truth('3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_1000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_2000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_3000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_4000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_5000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_6000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_7000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_8000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_9000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/results_10000.txt')"
python -c "from import_results import *; cleanup('3-class-out_sideless/gt.txt')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_1000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/1000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_1000.txt', '/home/as-hunt/3-class-out_sideless/1000/', '/home/as-hunt/3-class-out_sideless/1000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_2000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/2000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_2000.txt', '/home/as-hunt/3-class-out_sideless/2000/', '/home/as-hunt/3-class-out_sideless/2000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_3000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/3000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_3000.txt', '/home/as-hunt/3-class-out_sideless/3000/', '/home/as-hunt/3-class-out_sideless/3000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_4000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/4000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_4000.txt', '/home/as-hunt/3-class-out_sideless/4000/', '/home/as-hunt/3-class-out_sideless/4000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_5000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/5000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_5000.txt', '/home/as-hunt/3-class-out_sideless/5000/', '/home/as-hunt/3-class-out_sideless/5000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_6000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/6000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_6000.txt', '/home/as-hunt/3-class-out_sideless/6000/', '/home/as-hunt/3-class-out_sideless/6000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_7000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/7000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_7000.txt', '/home/as-hunt/3-class-out_sideless/7000/', '/home/as-hunt/3-class-out_sideless/7000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_8000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/8000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_8000.txt', '/home/as-hunt/3-class-out_sideless/8000/', '/home/as-hunt/3-class-out_sideless/8000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_9000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/9000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_9000.txt', '/home/as-hunt/3-class-out_sideless/9000/', '/home/as-hunt/3-class-out_sideless/9000/')"

python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_10000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/10000/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/results_10000.txt', '/home/as-hunt/3-class-out_sideless/10000/', '/home/as-hunt/3-class-out_sideless/10000/')"

python -c "from confusion import *; get_the_csv('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_1000.txt')"
python -c "from confusion import *; get_the_csv('3-class-out_sideless/results_2000.txt', '3-class-out_sideless/results_3000.txt')"
python -c "from confusion import *; get_the_csv('3-class-out_sideless/results_4000.txt', '3-class-out_sideless/results_5000.txt')"
python -c "from confusion import *; get_the_csv('3-class-out_sideless/results_6000.txt', '3-class-out_sideless/results_6000.txt')"
python -c "from confusion import *; get_the_csv('3-class-out_sideless/results_7000.txt', '3-class-out_sideless/results_8000.txt')"
python -c "from confusion import *; get_the_csv('3-class-out_sideless/results_9000.txt', '3-class-out_sideless/results_10000.txt')"

python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_1000.csv', title='Confusion_matrix_1000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_2000.csv', title='Confusion_matrix_2000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_3000.csv', title='Confusion_matrix_3000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_4000.csv', title='Confusion_matrix_4000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_5000.csv', title='Confusion_matrix_5000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_6000.csv', title='Confusion_matrix_6000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_7000.csv', title='Confusion_matrix_7000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_8000.csv', title='Confusion_matrix_8000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_9000.csv', title='Confusion_matrix_9000')"
python -c "from confusion import *; plot_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_10000.csv', title='Confusion_matrix_10000')"

python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_1000.csv', title='Normalised_Confusion_matrix_1000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_2000.csv', title='Normalised_Confusion_matrix_2000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_3000.csv', title='Normalised_Confusion_matrix_3000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_4000.csv', title='Normalised_Confusion_matrix_4000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_5000.csv', title='Normalised_Confusion_matrix_5000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_6000.csv', title='Normalised_Confusion_matrix_6000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_7000.csv', title='Normalised_Confusion_matrix_7000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_8000.csv', title='Normalised_Confusion_matrix_8000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_9000.csv', title='Normalised_Confusion_matrix_9000')"
python -c "from confusion import *; plot_normalised_confusion_matrix('3-class-out_sideless/gt.csv', '3-class-out_sideless/results_10000.csv', title='Normalised_Confusion_matrix_10000')"

mv Confusion_matrix* 3-class-out_sideless/
mv Normalised_Confusion_matrix* 3-class-out_sideless/
rm 3-class-out_sideless/*.csv

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/1000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/1000/', '/home/as-hunt/3-class-out_sideless/1000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/2000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/2000/', '/home/as-hunt/3-class-out_sideless/2000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/3000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/3000/', '/home/as-hunt/3-class-out_sideless/3000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/4000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/4000/', '/home/as-hunt/3-class-out_sideless/4000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/5000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/5000/', '/home/as-hunt/3-class-out_sideless/5000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/6000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/6000/', '/home/as-hunt/3-class-out_sideless/6000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/7000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/7000/', '/home/as-hunt/3-class-out_sideless/7000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/8000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/8000/', '/home/as-hunt/3-class-out_sideless/8000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/9000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/9000/', '/home/as-hunt/3-class-out_sideless/9000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/10000/', 'gt')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/gt.txt', '/home/as-hunt/3-class-out_sideless/10000/', '/home/as-hunt/3-class-out_sideless/10000/', 'gt')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_1000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/1000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_1000.txt', '/home/as-hunt/3-class-out_sideless/1000/', '/home/as-hunt/3-class-out_sideless/1000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_2000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/2000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_2000.txt', '/home/as-hunt/3-class-out_sideless/2000/', '/home/as-hunt/3-class-out_sideless/2000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_3000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/3000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_3000.txt', '/home/as-hunt/3-class-out_sideless/3000/', '/home/as-hunt/3-class-out_sideless/3000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_4000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/4000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_4000.txt', '/home/as-hunt/3-class-out_sideless/4000/', '/home/as-hunt/3-class-out_sideless/4000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_5000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/5000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_5000.txt', '/home/as-hunt/3-class-out_sideless/5000/', '/home/as-hunt/3-class-out_sideless/5000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_6000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/6000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_6000.txt', '/home/as-hunt/3-class-out_sideless/6000/', '/home/as-hunt/3-class-out_sideless/6000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_7000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/7000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_7000.txt', '/home/as-hunt/3-class-out_sideless/7000/', '/home/as-hunt/3-class-out_sideless/7000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_8000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/8000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_8000.txt', '/home/as-hunt/3-class-out_sideless/8000/', '/home/as-hunt/3-class-out_sideless/8000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_9000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/9000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_9000.txt', '/home/as-hunt/3-class-out_sideless/9000/', '/home/as-hunt/3-class-out_sideless/9000/', 'pd')"

python -c "from add_bbox import *; iterate_over_images('/home/as-hunt/3-class-out_sideless/results_10000.txt', '/home/as-hunt/Etra-Space/3-class/test/', '/home/as-hunt/3-class-out_sideless/10000/', 'pd')"
python -c "from add_bbox import *; reiterate_over_images('/home/as-hunt/3-class-out_sideless/results_10000.txt', '/home/as-hunt/3-class-out_sideless/10000/', '/home/as-hunt/3-class-out_sideless/10000/', 'pd')"

python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_1000.txt')" > 3-class-out_sideless/details_1000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_2000.txt')" > 3-class-out_sideless/details_2000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_3000.txt')" > 3-class-out_sideless/details_3000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_4000.txt')" > 3-class-out_sideless/details_4000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_5000.txt')" > 3-class-out_sideless/details_5000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_6000.txt')" > 3-class-out_sideless/details_6000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_7000.txt')" > 3-class-out_sideless/details_7000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_8000.txt')" > 3-class-out_sideless/details_8000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_9000.txt')" > 3-class-out_sideless/details_9000.txt
python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_10000.txt')" > 3-class-out_sideless/details_10000.txt

python -c "from confusion import *; do_math('3-class-out_sideless/gt.txt', '3-class-out_sideless/results_10000.txt')" > 3-class-out_sideless/report.txt