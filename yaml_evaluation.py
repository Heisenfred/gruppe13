import yaml
import os

class Algorithm:
	def __init__(self, name, adt, poc):
		self.name = name
		self.avarage_duration_time = adt
		self.percent_of_common_triples = poc

algorithm_list = []

directory = os.path.join('results', 'benchmark')
for file in os.listdir(directory):
	with open(os.path.join(directory, file)) as yaml_file:
		try:
			# TODO one object for one Algorithm,
			#  get data in a list, methods to evaluate the list
			data = yaml.safe_load(yaml_file)
			name = data['Algorithm']
			adt = data['Avarage duration time']
			poc = data['Average percent number of common triples']
			algorithm_list.append(Algorithm(data, adt, poc))
		
		except yaml.YAMLError as exc:
			print(exc)
			
for element in algorithm_list:
	print(element.avarage_duration_time)



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