#! /bin/sh

./darknet/darknet detector test Etra-Space/new_data_sidless_no_rcc_1/obj.data Etra-Space/new_data_sidless_no_rcc_1/yolov4.cfg Etra-Space/backup/Step_3/yolov4_10000.weights -dont_show -ext_output < Fake/fake.txt > Fake/result.txt

python -c "from import_results import *; import_and_filder_results('Fake/result.txt', 'Fake/results.txt')"

rm /home/as-hunt/Fake/result.txt

python -c "from import_results import *; make_groud_truth('/home/as-hunt/Fake/gt.txt', '/home/as-hunt/Fake/in/')"
python -c "from confusion import *; get_the_csv('Etra-Space/Diffy-10k/1/gt.txt', 'Etra-Space/Diffy-10k/1/results.txt')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Fake/gt.txt', '/home/as-hunt/Fake/results.txt', '/home/as-hunt/Fake/in/', '/home/as-hunt/Fake/out/')"
python -c "from add_bbox import *; get_prediction_mistakes_iterative('/home/as-hunt/Fake/gt.txt', '/home/as-hunt/Fake/results.txt', '/home/as-hunt/Fake/out/', '/home/as-hunt/Fake/out/')"
python -c "from confusion import *; get_the_csv('/home/as-hunt/Fake/gt.txt', '/home/as-hunt/Fake/results.txt')"
python -c "from confusion import *; plot_confusion_matrix('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.csv', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.csv', title='Confusion_matrix_Diffy10k-1')"
python -c "from confusion import *; plot_normalised_confusion_matrix('/home/as-hunt/Etra-Space/Diffy-10k/1/gt.csv', '/home/as-hunt/Etra-Space/Diffy-10k/1/results.csv', title='Normalised_Confusion_matrix_Diffy10k-1')"

mv Confusion_matrix* /home/as-hunt/Fake/
mv Normalised_Confusion_matrix* /home/as-hunt/Fake/
rm /home/as-hunt/Fake/*.csv


python -c "from confusion import *; do_math('Fake/gt.txt', 'Fake/results.txt')" > Fake/details.txt