import yaml
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter
import numpy as np


class Algorithm:
	def __init__(self, name, alg_name, cc_name):
		self.alg_name = alg_name
		self.cc_name = cc_name
		self.name = name
		self.list_percentage_of_common_triples = []
		self.list_percentage_of_failed_recognitions = []
		self.list_percentage_of_classified_R_Maps = []
		self.list_amount_of_path_distribution = []
		self.list_percentage_four_leaf_matching = []
		self.list_average_random_green_path_four_leaf_matching = []
		self.list_dataset_size = []
		self.list_cc = []
		self.list_cooptimal_solutions = []
		self.list_absolute_processing_time = []
		self.list_average_recognition_time = []
	
	def average_absolut_processing_time(self):
		return sum(self.list_absolute_processing_time)
	
	def average_percentage_of_four_leaf_matching(self):
		c = []
		for x in self.list_percentage_four_leaf_matching:
			print(x)
			fl = x[:-2]
			float_fl = float(fl)
			c.append(float_fl)
		
		return sum(c) / len(c)
	
	def average_cooptimal_solutions(self):
		return sum(self.list_cooptimal_solutions) / len(self.list_cooptimal_solutions)
	
	def average_percentage_of_failed_recognition(self):
		c = []
		for x in self.list_percentage_of_failed_recognitions:
			print(x)
			fl = x[:-2]
			float_fl = float(fl)
			c.append(float_fl)
		
		return sum(c) / len(c)
	
	def percentage_of_common_triples(self):
		c = []
		for x in self.list_percentage_of_common_triples:
			print(x)
			fl = x[:-2]
			float_fl = float(fl)
			c.append(float_fl)
		
		return sum(c) / len(c)
	
	def add_percentage_of_common_triples(self, percetage_of_common_triples):
		self.list_percentage_of_common_triples.append(percetage_of_common_triples)
	
	def add_percentage_of_failed_recognitions_(self, list_percentage_of_failed_recognition):
		self.list_percentage_of_failed_recognitions.append(list_percentage_of_failed_recognition)
	
	def add_percentage_of_classified_R_Maps(self, percentage_of_classified_R_Maps):
		self.list_percentage_of_classified_R_Maps.append(percentage_of_classified_R_Maps)
	
	def add_amount_of_path_distribution(self, amount_of_path_distribution):
		self.list_amount_of_path_distribution.append(amount_of_path_distribution)
	
	def add_percentage_four_leaf_matching(self, percentage_four_leaf_matching):
		self.list_percentage_four_leaf_matching.append(percentage_four_leaf_matching)
	
	def add_average_random_green_path_four_leaf_matching(self, average_random_green_path_four_leaf_matching):
		self.list_average_random_green_path_four_leaf_matching.append(average_random_green_path_four_leaf_matching)
	
	def add_dataset_size(self, dataset_size):
		self.list_dataset_size.append(dataset_size)
	
	def add_cc(self, cc):
		self.list_cc.append(cc)
	
	def add_cooptimal_solutions(self, cooptimal_solutions):
		self.list_cooptimal_solutions.append(cooptimal_solutions)
	
	def add_absolute_processing_time(self, absolute_processing_time):
		self.list_absolute_processing_time.append(absolute_processing_time)
	
	def add_average_recognition_time(self, average_recognition_time):
		self.list_average_recognition_time.append(average_recognition_time)
	
	def compare_name(self, name):
		if self.name == name:
			return True
		else:
			return False


def clockwise_circular(cc):
	if cc[0] == False and cc[1] == False:
		return 'non-circular/non-clockwise'
	elif cc[0] == True and cc[1] == False:
		return 'circular/non-clockwise'
	elif cc[0] == False and cc[1] == True:
		return 'non-circular/clockwise'
	elif cc[0] == True and cc[1] == True:
		return 'circular/clockwise'


algorithm_list = []

directory = os.path.join('benchmark')
for file in os.listdir(directory):
	with open(os.path.join(directory, file)) as yaml_file:
		try:
			# TODO one object for one Algorithm,
			#  get data in a list, methods to evaluate the list
			data = yaml.safe_load(yaml_file)
			
			avarage_duration_time = data['Absolute processing time']
			percentage_of_common_triples = data['Percentage of common triples']
			
			percentage_of_failed_recognitions = data["Percentage of failed recognitions"]
			percentage_of_classified_R_Maps = data["Percentage of common triples"]
			amount_of_path_distribution = data["Amount of path distribution"]
			percentage_four_leaf_matching = data["Percentage 4 leaf matching"]
			average_random_green_path_four_leaf_matching = data["Average random green path 4 leaf matching"]
			dataset_size = data["Dataset size"]
			cc = (data["Generate clockwise"], data["Generate circular"])
			cooptimal_solutions = data["Co-optimal solutions average"]
			absolute_processing_time = data["Absolute processing time"]
			average_recognition_time = data["Average recognition time"]
			
			name = data['Algorithm'] + str(clockwise_circular(cc))
			alg_name = data['Algorithm']
			cc_name = clockwise_circular(cc)
			
			algorithm = Algorithm(name, alg_name, cc_name)
			algorithm.add_percentage_of_failed_recognitions_(percentage_of_failed_recognitions)
			algorithm.add_percentage_of_classified_R_Maps(percentage_of_classified_R_Maps)
			algorithm.add_percentage_of_common_triples(percentage_of_common_triples)
			algorithm.add_amount_of_path_distribution(amount_of_path_distribution)
			algorithm.add_percentage_four_leaf_matching(percentage_four_leaf_matching)
			algorithm.add_average_random_green_path_four_leaf_matching(
				average_random_green_path_four_leaf_matching)
			algorithm.add_dataset_size(dataset_size)
			algorithm.add_cc(cc)
			algorithm.add_cooptimal_solutions(cooptimal_solutions)
			algorithm.add_absolute_processing_time(absolute_processing_time)
			algorithm.add_average_recognition_time(average_recognition_time)
			
			algorithm_list.append(algorithm)
			
		
		except yaml.YAMLError as exc:
			print(exc)




plt.style.use('ggplot')


# Algorithm List
a = ('base', 'realistic-3', 'realistic-4', 'reserve-3', 'reserve-4', 'spike')
b = ('c cl', 'nc cl', 'c cl', 'nc ncl')

ccl = []
nccl = []
cncl = []
ncncl = []

asdasd = ['non-circular/non-clockwise',  'circular/non-clockwise',  'non-circular/clockwise', 'circular/clockwise']

base_liste = []
realistic_3_liste = []
realistic_4_liste = []
reserve_3_liste = []
reserve_4_liste = []
spike_liste = []

#base
for algorithm in algorithm_list:
	if algorithm.alg_name == 'base':
		base_liste.append(algorithm)
		
for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_average_recognition_time[0])
		
	if algorithm.cc_name ==  'non-circular/clockwise':
		nccl.append(algorithm.list_average_recognition_time[0])
		
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_average_recognition_time[0])
		
	if algorithm.cc_name ==  'non-circular/non-clockwise':
		ncncl.append(algorithm.list_average_recognition_time[0])

# realistic-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-3':
		realistic_3_liste.append(algorithm)

for algorithm in realistic_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_average_recognition_time[0])

#realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-4':
		realistic_4_liste.append(algorithm)

for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_average_recognition_time[0])

# reserve-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-3':
		reserve_3_liste.append(algorithm)

for algorithm in reserve_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_average_recognition_time[0])

# realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-4':
		reserve_4_liste.append(algorithm)

for algorithm in reserve_4_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_average_recognition_time[0])

# spike
for algorithm in algorithm_list:
	if algorithm.alg_name == 'spike':
		spike_liste.append(algorithm)

for algorithm in spike_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_average_recognition_time[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_average_recognition_time[0])

fig, ax = plt.subplots()
index = np.arange(6)
bar_width = 0.2
opacity = 1
ax.bar(index, ccl, bar_width, alpha=opacity, color='darkblue',
                label='ccl')
ax.bar(index+bar_width, nccl, bar_width, alpha=opacity, color='red',
                label='nccl')
ax.bar(index + 2*bar_width, cncl, bar_width, alpha=opacity, color='seagreen',
                label='cncl')
ax.bar(index+3*bar_width, ncncl, bar_width, alpha=opacity, color='orange',
                label='ncncl')

ax.set_xlabel('')
ax.set_ylabel('recognition time [s]')
ax.set_title('Recognition time')
ax.set_xticks(index + bar_width / 4)
ax.set_xticklabels(a)
ax.legend(ncol=4)
plt.show()

#############################################################
# COOPTIMAL  SOLUTIONS

base_liste = []
realistic_3_liste = []
realistic_4_liste = []
reserve_3_liste = []
reserve_4_liste = []
spike_liste = []
ccl = []
nccl = []
cncl = []
ncncl = []

asdasd = ['non-circular/non-clockwise', 'circular/non-clockwise', 'non-circular/clockwise', 'circular/clockwise']

# base
for algorithm in algorithm_list:
	if algorithm.alg_name == 'base':
		base_liste.append(algorithm)

for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_cooptimal_solutions[0])

# realistic-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-3':
		base_liste.append(algorithm)

for algorithm in realistic_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_cooptimal_solutions[0])

# realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-4':
		realistic_4_liste.append(algorithm)

for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_cooptimal_solutions[0])

# reserve-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-3':
		reserve_3_liste.append(algorithm)

for algorithm in reserve_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_cooptimal_solutions[0])

# realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-4':
		reserve_4_liste.append(algorithm)

for algorithm in reserve_4_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_cooptimal_solutions[0])

# spike
for algorithm in algorithm_list:
	if algorithm.alg_name == 'spike':
		spike_liste.append(algorithm)

for algorithm in spike_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_cooptimal_solutions[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_cooptimal_solutions[0])

fig, ax = plt.subplots()
index = np.arange(6)
bar_width = 0.2
opacity = 1
ax.bar(index, ccl, bar_width, alpha=opacity, color='darkblue',
       label='ccl')
ax.bar(index + bar_width, nccl, bar_width, alpha=opacity, color='red',
       label='nccl')
ax.bar(index + 2 * bar_width, cncl, bar_width, alpha=opacity, color='seagreen',
       label='cncl')
ax.bar(index + 3 * bar_width, ncncl, bar_width, alpha=opacity, color='orange',
       label='ncncl')


ax.set_xlabel('')
ax.set_ylabel('Average co-optimal solutions')
ax.set_title('Co-optimal solutions')
ax.set_xticks(index + bar_width / 4)
ax.set_xticklabels(a)
ax.legend(ncol=4)
plt.show()


################################################

#############################################################
# PERCENTAGE FOUR LEAVES MATCHING

base_liste = []
realistic_3_liste = []
realistic_4_liste = []
reserve_3_liste = []
reserve_4_liste = []
spike_liste = []
ccl = []
nccl = []
cncl = []
ncncl = []

asdasd = ['non-circular/non-clockwise', 'circular/non-clockwise', 'non-circular/clockwise', 'circular/clockwise']

# base
for algorithm in algorithm_list:
	if algorithm.alg_name == 'base':
		base_liste.append(algorithm)

for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_four_leaf_matching[0])

# realistic-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-3':
		base_liste.append(algorithm)

for algorithm in realistic_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_four_leaf_matching[0])

# realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-4':
		realistic_4_liste.append(algorithm)

for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_four_leaf_matching[0])

# reserve-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-3':
		reserve_3_liste.append(algorithm)

for algorithm in reserve_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_four_leaf_matching[0])

# realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-4':
		reserve_4_liste.append(algorithm)

for algorithm in reserve_4_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_four_leaf_matching[0])

# spike
for algorithm in algorithm_list:
	if algorithm.alg_name == 'spike':
		spike_liste.append(algorithm)

for algorithm in spike_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_four_leaf_matching[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_four_leaf_matching[0])

fig, ax = plt.subplots()
index = np.arange(6)
bar_width = 0.2
opacity = 1
ax.bar(index, ccl, bar_width, alpha=opacity, color='darkblue',
       label='ccl')
ax.bar(index + bar_width, nccl, bar_width, alpha=opacity, color='red',
       label='nccl')
ax.bar(index + 2 * bar_width, cncl, bar_width, alpha=opacity, color='seagreen',
       label='cncl')
ax.bar(index + 3 * bar_width, ncncl, bar_width, alpha=opacity, color='orange',
       label='ncncl')

ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
ax.set_xlabel('')
ax.set_ylabel('Percentage of 4 leafs matching')
ax.set_title('4 leafs matching')
ax.set_xticks(index + bar_width / 4)
ax.set_xticklabels(a)
ax.legend(ncol=4)
plt.show()

#############################################################
# PERCENTAGE OF COMMON TRIPLES

base_liste = []
realistic_3_liste = []
realistic_4_liste = []
reserve_3_liste = []
reserve_4_liste = []
spike_liste = []
ccl = []
nccl = []
cncl = []
ncncl = []

asdasd = ['non-circular/non-clockwise', 'circular/non-clockwise', 'non-circular/clockwise', 'circular/clockwise']

# base
for algorithm in algorithm_list:
	if algorithm.alg_name == 'base':
		base_liste.append(algorithm)

for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_of_common_triples[0])

# realistic-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-3':
		base_liste.append(algorithm)

for algorithm in realistic_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_of_common_triples[0])

# realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'realistic-4':
		realistic_4_liste.append(algorithm)

for algorithm in base_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_of_common_triples[0])

# reserve-3
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-3':
		reserve_3_liste.append(algorithm)

for algorithm in reserve_3_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_of_common_triples[0])

# realistic-4
for algorithm in algorithm_list:
	if algorithm.alg_name == 'reserve-4':
		reserve_4_liste.append(algorithm)

for algorithm in reserve_4_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_of_common_triples[0])

# spike
for algorithm in algorithm_list:
	if algorithm.alg_name == 'spike':
		spike_liste.append(algorithm)

for algorithm in spike_liste:
	if algorithm.cc_name == 'circular/clockwise':
		ccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/clockwise':
		nccl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'circular/non-clockwise':
		cncl.append(algorithm.list_percentage_of_common_triples[0])
	
	if algorithm.cc_name == 'non-circular/non-clockwise':
		ncncl.append(algorithm.list_percentage_of_common_triples[0])

fig, ax = plt.subplots()
index = np.arange(6)
bar_width = 0.2
opacity = 1
ax.bar(index, ccl, bar_width, alpha=opacity, color='darkblue',
       label='ccl')
ax.bar(index + bar_width, nccl, bar_width, alpha=opacity, color='red',
       label='nccl')
ax.bar(index + 2 * bar_width, cncl, bar_width, alpha=opacity, color='seagreen',
       label='cncl')
ax.bar(index + 3 * bar_width, ncncl, bar_width, alpha=opacity, color='orange',
       label='ncncl')

ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
ax.set_xlabel('')
ax.set_ylabel('Percentage of common triples')
ax.set_title('Common triples')
ax.set_xticks(index + bar_width / 4)
ax.set_xticklabels(a)
ax.legend(ncol=4)
plt.show()

"""
# plot processing time
y_pos = np.arange(len(a))
value = []
for algorithm in algorithm_list:
	value.append(algorithm.average_absolut_processing_time())
error = np.random.rand(len(a))
plt.bar(a, value)
plt.ylabel("Absolute processing time in s")
plt.show()

# plot cooptimal solutions
y_pos = np.arange(len(a))
value = []
for algorithm in algorithm_list:
	value.append(algorithm.average_cooptimal_solutions())
error = np.random.rand(len(a))
plt.bar(a, value)
plt.ylabel("Avarage of cooptimal solutions")
plt.show()

# plot cooptimal solutions
y_pos = np.arange(len(a))
value = []
for algorithm in algorithm_list:
	value.append(algorithm.average_percentage_of_four_leaf_matching())
error = np.random.rand(len(a))
plt.bar(a, value)
plt.ylabel("Percentage of four leaf matching [%]")
plt.show()

# failed recognition
y_pos = np.arange(len(a))
value = []
for algorithm in algorithm_list:
	value.append(algorithm.average_percentage_of_failed_recognition())
error = np.random.rand(len(a))
plt.bar(a, value)
plt.ylabel("failed recognition [%]")
plt.show()

# common triples
y_pos = np.arange(len(a))
value = []
for algorithm in algorithm_list:
	value.append(algorithm.percentage_of_common_triples())
error = np.random.rand(len(a))
plt.bar(a, value)
plt.ylabel("Common triples [%]")
plt.show()

# for x in range(len(count_path)):
#	percentage = (count_path[x] / len(history_files)) * 100
#	print("Percentage of trees found with {} path: {}%".format(x, percentage))
#	paths_per_h_file_in_percent.append(percentage)
#
# ypos = np.arange(len(paths_per_h_file_in_percent))
# plt.xlabel('Paths found')
# plt.ylabel('Proportion of paths found in %')
# plt.title('Paths found per dataset')

# ax = plt.gca()
# ax.set_xlim([0, 10])
# ax.set_ylim([0, 100])
# plt.bar(ypos, paths_per_h_file_in_percent)
# plt.savefig(os.path.join(
#	config["result_folder"], "plots", folder, f'{folder}_{case_type.value}_plot.png'))
# plt.clf()
"""
