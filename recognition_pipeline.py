from itertools import permutations
from os import read
from stringprep import b1_set
import sys
from typing import Sequence
import yaml
import glob
import erdbeermet.simulation as sim
import erdbeermet.recognition as rec
import modified_recognition as modrec
import WP4_modified_recognition as wp4rec
import os
import numpy as np
import matplotlib.pyplot as plt
import time
import copy
import random
from enum import Enum
import shutil


def readConfigFile(configfile):
    with open(configfile, "r") as stream:
        dict = {}
        try:
            dict = yaml.safe_load(stream)
            return dict
        except yaml.YAMLError as exc:
            print(exc)


def getFilesToAnalyse(foldername, dataset_location):
    files = glob.glob(os.path.join(dataset_location, foldername) + '/*.txt')

    return files


def getSimulationParams(foldername):
    sim_n = "unknown"
    sim_circular = "unknown"
    sim_clockwise = "unknown"

    for s in foldername.split("_"):
        if s == "small":
            sim_n = 6
        if s == "medium":
            sim_n = 7
        if s == "big":
            sim_n = 8
        if s == "circular":
            sim_circular = True
        if s == "noncircular":
            sim_circular = False
        if s == "clockwise":
            sim_clockwise = True
        if s == "nonclockwise":
            sim_clockwise = False

    return sim_n, sim_circular, sim_clockwise


def readScenario(h_file):
    return sim.load(h_file)


def isDirectory(dir):
    return os.path.isdir(dir)


def createDir(dir):
    if not isDirectory(dir):
        os.makedirs(dir)


def recognitionSuccessful(r_tree):
    for v in r_tree.preorder():
        if v.valid_ways > 0:
            return True
    return False


def succesfulRecognitions(r_tree):
    return len(getValidRStepSequences(r_tree))


def traverseTree(node, sequence, paths):
    if node.valid_ways == 0:
        return

    cloned_sequence = copy.deepcopy(sequence)

    cloned_sequence.append(node)

    if not node.children:

        paths.append(cloned_sequence)
        return

    for child in node.children:
        traverseTree(child, cloned_sequence, paths)


def traversalToRstepSequences(forwardPath):

    forwardPath.reverse()

    sequence = []

    counter = 4  
    for step in forwardPath:
        assert len(step.V) == counter

        counter += 1
        sequence.append({"V": step.V, "r-step": step.R_step, "D": step.D})

    return sequence


def getValidRStepSequences(recognition_tree):

    paths = []

    traverseTree(recognition_tree.root, [], paths)

    for path in paths:
        assert len(path) == recognition_tree.root.n - 3

    r_step_sequences = []
    for path in paths:
        r_step_sequences.append(traversalToRstepSequences(path))

    return r_step_sequences


def xLeafMapMatchesSimulation(reconstructed_r_step_sequences, x=4):

    leaf_node_of_path = reconstructed_r_step_sequences[0]
    recognition_leafs = leaf_node_of_path["V"]

    for i in range(x):
        if not i in recognition_leafs:
            return False

    return True


def allXLeafMapMatchSimulation(reconstructed_r_step_sequences, x, simulation_r_step_sequences):
    for seq in reconstructed_r_step_sequences:
        if not xLeafMapMatchesSimulation(seq, x, simulation_r_step_sequences):
            return False

    return True


def buildSimulationSequence(original_scenario):
    r_step_sequence = []
    for x, y, z, alpha, delta in original_scenario.history:

        if x <= y:
            r_step_dict = {
                "x": x,
                "y": y,
                "z": z
            }
        else:
            r_step_dict = {
                "x": y,
                "y": x,
                "z": z
            }
        r_step_sequence.append(r_step_dict)

    return r_step_sequence


def number_cooptimal_sol(all_green_paths):
    paths_out_of_order_count = 0
    for path in all_green_paths:
        normal_seq = [[0, 1, 2, 3]]
        for index in range(1, len(path)):
            save = copy.deepcopy(normal_seq[index - 1])
            save.append(index + 3)
            normal_seq.append(save)
        node_order = []
        for step in path:
            node_order.append(step["V"])
        if not normal_seq == node_order:
            paths_out_of_order_count += 1
    return paths_out_of_order_count


def commonTriples(reconstruction_sequence, simulation_sequence):

    recognition_r_steps = set()
    for r in reconstruction_sequence:
        if r["r-step"]:
            r_step = r["r-step"]
            recognition_r_steps.add(
                f'({r_step[0]}, {r_step[1]}: {r_step[2]})')

            if r_step[0] <= r_step[1]:
                recognition_r_steps.add(
                    f'({r_step[0]}, {r_step[1]}: {r_step[2]})')
            else:
                recognition_r_steps.add(
                    f'({r_step[1]}, {r_step[0]}: {r_step[2]})')
    simulation_r_steps = set() 
    for s in simulation_sequence:
        simulation_r_steps.add(f'({s["x"]}, {s["y"]}: {s["z"]})')

    return simulation_r_steps.intersection(recognition_r_steps)


def choosePathRandomly(paths):

    if len(paths) < 1:
        return False

    index = random.randrange(len(paths))

    return paths[index]


def realistic_recognition(D, B_set_size):

    B_sets = list(permutations(range(len(D)), B_set_size))

    random.shuffle(B_sets)

    for B_set in B_sets:
        tree = modrec.modified_recognize(D, B_set, first_candidate_only=True)

        if recognitionSuccessful(tree):
            return tree

    return False


def reserved(D, reserved_size):
    B_set = list(range(reserved_size))
    return modrec.modified_recognize(D, B_set, first_candidate_only=True)


def base_alg(D):
    return rec.recognize(D, first_candidate_only=True)


def base_spike(D):
    return wp4rec.spike_recognize(D, first_candidate_only=True)


def get_recognition_tree(case_type, d_matrix):
    recognition_tree = None
    if case_type.value is 'base':
        recognition_tree = base_alg(d_matrix)
    elif case_type.value is 'reserve-3':
        recognition_tree = reserved(d_matrix, 3)
    elif case_type.value is 'reserve-4':
        recognition_tree = reserved(d_matrix, 4)
    elif case_type.value is 'realistic-3':
        recognition_tree = realistic_recognition(d_matrix, B_set_size=3)
    elif case_type.value is 'realistic-4':
        recognition_tree = realistic_recognition(d_matrix, B_set_size=4)
    elif case_type.value is 'spike':
        recognition_tree = base_spike(d_matrix)

    return recognition_tree


def backupFailedHistory(h_file, config, case_type):

    createDir(os.path.join(config["result_folder"],
              "failed_recognitions", case_type.value))

    cleaned_filename = h_file.replace('\\', '/')
    cleaned_filename = cleaned_filename.split("/")[-1]

    shutil.copy(h_file, os.path.join(
        config["result_folder"], "failed_recognitions", case_type.value, cleaned_filename))


def recognizeFile(h_file, config, folder, case_type=None):

    print(f'\n\n\n')
    print(f'======================================')
    print(f'Start analysis of {h_file}')

    result_object = {}
    original_scenario = readScenario(h_file)

    simulation_sequence = buildSimulationSequence(original_scenario)

    d_matrix = original_scenario.D

    ts_before = time.time()
    recognition_tree = get_recognition_tree(case_type, d_matrix)
    ts_after = time.time()
    duration = ts_after - ts_before
    result_object["duration"] = duration

    cleaned_filename = h_file[len(config["dataset_folder"]) + 1:]
    recognition_tree.write_to_file(
        f'{config["result_folder"]}/{cleaned_filename}')

    print(f'ts_before {ts_before}')
    print(f'ts_after {ts_after}')
    print(f'Duration {duration}')

    print(f'Recognition successful {recognitionSuccessful(recognition_tree)}')
    print(
        f'Recognition successful total {succesfulRecognitions(recognition_tree)}')

    all_green_paths = getValidRStepSequences(recognition_tree)

    path = choosePathRandomly(all_green_paths)

    anzahl_matched_leaves = 0
    for i in all_green_paths:
        if xLeafMapMatchesSimulation(i):
            anzahl_matched_leaves += 1

    if len(all_green_paths) > 0:
        result_object["Percentage of 4 Leaves map matches simulation"] = (
            anzahl_matched_leaves/len(all_green_paths))*100
    else:
        result_object["Percentage of 4 Leaves map matches simulation"] = 0

    if recognitionSuccessful(recognition_tree):
        print(f'randomly determined Path {path}')

        random_path_matched = 0
        if xLeafMapMatchesSimulation(path):
            random_path_matched = 1
        result_object["4_Leaves_matches_simulation_count"] = random_path_matched

        result_object["Recognition successful total"] = succesfulRecognitions(
            recognition_tree)
        print(f'4 leaf matches {xLeafMapMatchesSimulation(path, 4)}')
        result_object["final_three_matches_simulation"] = xLeafMapMatchesSimulation(
            path, 3)
        result_object["final_four_matches_simulation"] = xLeafMapMatchesSimulation(
            path, 4)

        print(f'common triples {commonTriples(path, simulation_sequence)}')
        result_object["common_triples"] = commonTriples(
            path, simulation_sequence)
        result_object["number_of_common_triples"] = len(
            commonTriples(path, simulation_sequence))
        try:
            result_object["percent_of_common_triples"] = len(commonTriples(path, simulation_sequence)) / (
                len(path) - 1) * 100
            print(
                f'percentage_of_common_triples {result_object["percent_of_common_triples"]}')
        except ZeroDivisionError:
            result_object["percent_of_common_triples"] = 0
    else:

        result_object["final_three_matches_simulation"] = False
        result_object["final_four_matches_simulation"] = False
        result_object["common_triples"] = "no common triples"
        result_object["number_of_common_triples"] = 0
        result_object["percent_of_common_triples"] = 0
        result_object["Recognition successful total"] = 0

        result_object["4_Leaves_matches_simulation_count"] = 0

        backupFailedHistory(h_file, config, case_type)

    result_object["co_optimal_solutions"] = number_cooptimal_sol(
        all_green_paths)
    print(f'co_optimal_solutions {result_object["co_optimal_solutions"]}')

    result_object["recognition_success"] = recognitionSuccessful(
        recognition_tree)
    result_object["recognition_success_total"] = succesfulRecognitions(
        recognition_tree)
    return result_object


def getDirectoriesToAnalyse(datasets_directory):
    folders = [name for name in os.listdir(datasets_directory) if os.path.isdir(
        os.path.join(datasets_directory, name))]
    return folders


def setupDirectoryForFailedRecognitions(result_folder):
    createDir(os.path.join(result_folder, "failed_recognitions"))

    for a in Algorithm:
        createDir(os.path.join(result_folder, "failed_recognitions", a.value))


def analyse(configfile):
    config = readConfigFile(configfile)
    createDir(config["result_folder"])

    setupDirectoryForFailedRecognitions(config["result_folder"])

    folders = getDirectoriesToAnalyse(config["dataset_folder"])

    for f in folders:
        for algorithm in Algorithm:
            analyseFolder(f, config, algorithm)


def countFailures(results):
    failure_count = 0

    for r in results:
        if r["recognition_success"] == False:
            failure_count += 1

    percentage = failure_count/len(results) * 100
    return failure_count, percentage


def analyseFolder(folder, config, case_type):
    global four_leaf_matches_simulation_test
    history_files = getFilesToAnalyse(folder, config["dataset_folder"])
    sim_n, sim_circular, sim_clockwise = getSimulationParams(folder)

    count_path =  {}

    createDir(config["result_folder"])
    createDir(os.path.join(config["result_folder"], folder))
    createDir(os.path.join(config["result_folder"], "plots", folder))
    paths_per_h_file_in_percent = []

    results = []

    common_triples_count = 0
    common_triples_percentage = 0
    total_duration = 0
    four_leaf_matches_simulation_test = 0
    correctly_classified_r_maps = 0
    correctly_classified_r_map = 0
    number_of_co_optimal_solutions = 0
    percentage_four_leaf_matches_simulation = 0
    for h in history_files:
        result_object = recognizeFile(h, config, folder, case_type)
        h_rmap = 1 if result_object["recognition_success"] is True else 0
        correctly_classified_r_map = correctly_classified_r_map + h_rmap
        common_triples_count = common_triples_count + \
            result_object["number_of_common_triples"]
        common_triples_percentage = (
            common_triples_percentage + result_object["percent_of_common_triples"])
        if result_object["Recognition successful total"] in count_path.keys():
            count_path[result_object["Recognition successful total"]]  = count_path[result_object["Recognition successful total"]] +  1
        else:
            count_path[result_object["Recognition successful total"]] = 1
        four_leaf_matches_simulation_test = four_leaf_matches_simulation_test + \
            result_object["4_Leaves_matches_simulation_count"]
        percentage_four_leaf_matches_simulation = percentage_four_leaf_matches_simulation + \
            result_object["Percentage of 4 Leaves map matches simulation"]
        correctly_classified_r_maps = correctly_classified_r_maps + \
            result_object["recognition_success_total"]
        number_of_co_optimal_solutions = number_of_co_optimal_solutions + \
            result_object["co_optimal_solutions"]
        total_duration = total_duration + result_object['duration']

        results.append(result_object)

    common_triples_count = common_triples_count / len(history_files)
    common_triples_percentage = common_triples_percentage / len(history_files)
    print(f'average number of common triples: {common_triples_count}')
    print(
        f'average percentage of common triples: {common_triples_percentage} %')

    avarage_duration = total_duration / len(results)
    print(f'1 result object {results[0]}')
    print(f'avarage duration {avarage_duration}s')


    if config["interrupt_matplotlib"]:
        plt.show()

    failuresCount, failuresPercentage = countFailures(results)

    d = {
        "Algorithm": case_type.value,
        "Percentage of failed recognitions": str(failuresPercentage) + "%",
        "Percentage of classified R-Maps": str(
            (correctly_classified_r_map / len(history_files)) * 100) + " %",
        
        "Percentage of common triples": str(common_triples_percentage) + "%",
        "Amount of path distribution": count_path,
        "Percentage 4 leaf matching": str(percentage_four_leaf_matches_simulation/len(history_files)) + " %",
        "Average random green path 4 leaf matching": four_leaf_matches_simulation_test/len(history_files),
        "Dataset size": sim_n,
        "Generate circular": sim_circular,
        "Generate clockwise": sim_clockwise,
        "Co-optimal solutions average": number_of_co_optimal_solutions / len(history_files),
        "Absolute processing time": total_duration,
        "Average recognition time": avarage_duration
    }

    createDir(os.path.join('results', 'benchmark'))
    yaml_name = os.path.join('results', 'benchmark',
                             f'{folder}_{case_type.value}_result.yml')

    with open(yaml_name, 'w') as yaml_file:
        yaml.dump(d, yaml_file, default_flow_style=False)


class Algorithm(Enum):
    BASE = 'base'
    RESERVE_3 = 'reserve-3'
    RESERVE_4 = 'reserve-4'
    REALISTIC_3 = 'realistic-3'
    REALISTIC_4 = 'realistic-4'
    BASE_SPIKE = 'spike'


if __name__ == '__main__':
    recognition_config = "recognition_config.yaml" if len(
        sys.argv) == 1 else sys.argv[1]
    print(f'Analysis Files: {recognition_config}')

    analyse(recognition_config)
