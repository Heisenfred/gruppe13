import yaml
import os

class Algorithm:
	def __init__(self, name):
		self.name = name
		self.list_percentage_of_common_triples = []
		self.list_percentage_of_failed_recognitions = []
		self.list_percentage_of_classified_R_Maps = []
		self.list_amount_of_path_distribution = []
		self.list_percentage_four_leaf_matching = []
		self.list_average_random_green_path_four_leaf_matching = []
		self.list_dataset_size = []
		self.list_generate_circular = []
		self.list_generate_clockwise = []
		self.list_cooptimal_solutions = []
		self.list_absolute_processing_time = []
		self.list_average_recognition_time = []
		
	def add_percentage_of_common_triples(self, percetage_of_common_triples):
		self.list_percentage_of_common_triples.append(percetage_of_common_triples)
	
	def add_percentage_of_failed_recognitions_(self, list_percentage_of_common_triples):
		self.list_percentage_of_common_triples.append(list_percentage_of_common_triples)
	
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
	
	def add_generate_circular(self, generate_circular):
		self.list_generate_circular.append(generate_circular)
		
	def add_generate_clockwise(self, generate_clockwise):
		self.list_generate_clockwise.append(generate_clockwise)
		
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
		
		
	

algorithm_list = []

directory = os.path.join('results', 'benchmark')
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
			generate_circular = data["Generate circular"]
			generate_clockwise = data["Generate clockwise"]
			cooptimal_solutions = data["Co-optimal solutions average"]
			absolute_processing_time = data["Absolute processing time"]
			average_recognition_time = data["Average recognition time"]
			
			name = data['Algorithm']
			
			already_in_list = False
			for algorithm in algorithm_list:
				if algorithm.compare_name(name) == True:
					algorithm.add_percentage_of_failed_recognitions_(percentage_of_failed_recognitions)
					algorithm.add_percentage_of_classified_R_Maps(percentage_of_classified_R_Maps)
					algorithm.add_percentage_of_common_triples(percentage_of_common_triples)
					algorithm.add_amount_of_path_distribution(amount_of_path_distribution)
					algorithm.add_percentage_four_leaf_matching(percentage_four_leaf_matching)
					algorithm.add_average_random_green_path_four_leaf_matching(average_random_green_path_four_leaf_matching)
					algorithm.add_dataset_size(dataset_size)
					algorithm.add_generate_circular(generate_circular)
					algorithm.add_generate_clockwise(generate_clockwise)
					algorithm.add_cooptimal_solutions(cooptimal_solutions)
					algorithm.add_absolute_processing_time(absolute_processing_time)
					algorithm.add_average_recognition_time(average_recognition_time)
					
					already_in_list = True
				
			if already_in_list == False:
				algorithm = Algorithm(name)
				algorithm_list.append(algorithm)
				algorithm.add_percentage_of_failed_recognitions_(percentage_of_failed_recognitions)
				algorithm.add_percentage_of_classified_R_Maps(percentage_of_classified_R_Maps)
				algorithm.add_percentage_of_common_triples(percentage_of_common_triples)
				algorithm.add_amount_of_path_distribution(amount_of_path_distribution)
				algorithm.add_percentage_four_leaf_matching(percentage_four_leaf_matching)
				algorithm.add_average_random_green_path_four_leaf_matching(average_random_green_path_four_leaf_matching)
				algorithm.add_dataset_size(dataset_size)
				algorithm.add_generate_circular(generate_circular)
				algorithm.add_generate_clockwise(generate_clockwise)
				algorithm.add_cooptimal_solutions(cooptimal_solutions)
				algorithm.add_absolute_processing_time(absolute_processing_time)
				algorithm.add_average_recognition_time(average_recognition_time)
		
		except yaml.YAMLError as exc:
			print(exc)
			
print(algorithm_list)



#for x in range(len(count_path)):
#	percentage = (count_path[x] / len(history_files)) * 100
#	print("Percentage of trees found with {} path: {}%".format(x, percentage))
#	paths_per_h_file_in_percent.append(percentage)
#
#ypos = np.arange(len(paths_per_h_file_in_percent))
#plt.xlabel('Paths found')
#plt.ylabel('Proportion of paths found in %')
#plt.title('Paths found per dataset')

#ax = plt.gca()
#ax.set_xlim([0, 10])
#ax.set_ylim([0, 100])
#plt.bar(ypos, paths_per_h_file_in_percent)
#plt.savefig(os.path.join(
#	config["result_folder"], "plots", folder, f'{folder}_{case_type.value}_plot.png'))
#plt.clf()