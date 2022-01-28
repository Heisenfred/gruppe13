GROUP 13 - RECOGNITION MANUEL

#1 install Erdbeermet and clone this repo to a new directory

#2 cd /gruppe13

#3 python generate_dataset.py
this creates the datasets directory and stores all configurations there  

#4 python recognition_pipeline.py
this will start the recognition process and will create .yaml results files in the results/benchmark directory

#5 python yaml_evaluation.py 
will take the yaml result files and plot them into evaluation graphs


FOLDERS:

/datasets 
stores generated datasets from generate_datasets.py

/archiv_failed_recognitions
stores annotated and failed recognitions from our previous iterations

/results/benchmark
stores the result.yaml files that will be evaluated

/results/example_recognition
stores trees and failed recognitions
