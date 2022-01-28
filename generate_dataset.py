from shutil import copyfile
import os
from datetime import datetime
import yaml
import time
import sys

import erdbeermet.simulation as sim

def log(msg):
    with open(target_folder+"\\"+logfile, "a") as f:
        f.write(msg+"\n")
    time.sleep(0.1)

def isDirectory(dir):
    return os.path.isdir(dir)

def createDir(dir):
    if not isDirectory(dir):
        os.makedirs(dir)

def getTime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def buildFilename(file_config, index):
    global target_folder, default_n, default_branching_prob, default_circular, default_clockwise

    N=file_config["n"] if "n" in file_config.keys() else default_n
    branching_prob=file_config["branching_prob"] if "branching_prob" in file_config.keys() else default_branching_prob
    circular=file_config["circular"] if "circular" in file_config.keys() else default_circular
    clockwise=file_config["clockwise"] if "clockwise" in file_config.keys() else default_clockwise

    return file_config["set_name"]+"/"+f'N={N}_circular={circular}_clockwise={clockwise}_branchingProperty={branching_prob}_file{index}.txt'

def generateHistoryFile(file_config, index):
    global target_folder, default_n, default_branching_prob, default_circular, default_clockwise

    N=file_config["n"] if "n" in file_config.keys() else default_n
    branching_prob=file_config["branching_prob"] if "branching_prob" in file_config.keys() else default_branching_prob
    circular=file_config["circular"] if "circular" in file_config.keys() else default_circular
    clockwise=file_config["clockwise"] if "clockwise" in file_config.keys() else default_clockwise

    scenario = sim.simulate(N, branching_prob, circular, clockwise)
    scenario.write_history(os.path.join(target_folder, buildFilename(file_config, index)))

datasetname=sys.argv[1] if len(sys.argv)>1 else "generate_dataset_config.yaml"
print(f'Datsetname: {datasetname}')

with open(datasetname, "r") as stream:
    dict={}
    try:
        dict = yaml.safe_load(stream)
        print(dict)
        target_folder = dict["dataset_name"]
        config_sets = dict["config_sets"]
        default_branching_prob = dict["default_branching_prob"]
        default_n=dict["default_n"]
        default_circular=dict["default_circular"]
        default_clockwise=dict["default_clockwise"]
        default_size=dict["default_size"]
        logfile=dict["logfile"]

    except yaml.YAMLError as exc:
        print(exc)

createDir(target_folder)
for s in config_sets:
    size=s["size"] if "size" in s.keys() else default_size
    createDir(target_folder+"/"+s["set_name"])
    for i in range(size):
        generateHistoryFile(s, i)

log(f'=================\n')
log(f'Dataset creation finished successfully at {getTime()}\n')
