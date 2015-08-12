#!/usr/bin/python

import sys, pprint, datetime;
from math import sqrt;
from sys import argv;

#Function returns distance between two cities, rounded to float, cast to int

file_name = argv[1]

def get_distance(c1, c2):
	return int(round(sqrt((c1[1]-c2[1])*(c1[1]-c2[1]) + (c1[2]-c2[2])*(c1[2]-c2[2]))))

i = 0
#list to hold all cities
cities = []
with open(file_name, "r") as text_file:
	#for each line in file
	for line in text_file:
		#add another list to the cities list (i.e. add another city)
		cities.append([])
		#add the information from the line ([0] is id, [1] is x, [2] is y)
		cities[i].append(int(line.strip().split()[0]))
		cities[i].append(int(line.strip().split()[1]))
		cities[i].append(int(line.strip().split()[2]))
		i = i + 1

#get distances between all cities
def distance(cities):
	if len(cities) == 0:
		return 0
	distance = 0
	for i in range(len(cities) - 1):
		distance += get_distance(cities[i], cities[i+1]);
	distance += get_distance(cities[len(cities) - 1], cities[0])
	return distance

def two_opt(cities):
  for i in range(len(cities) - 1):
    for j in range(i + 2, len(cities) - 1):
      if get_distance(cities[i], cities[i+1]) + get_distance(cities[j], cities[j+1]) > get_distance(cities[i], cities[j]) + get_distance(cities[i+1], cities[j+1]):          cities[i+1:j+1] = reversed(cities[i+1:j+1])



#As two_opt loops through the circuit, breakig two conections at a time and improving them, and each call of two_opt makes a loop of all nodes, each call will most likely be an incremental improvement.  Therefore, if we have a time period of 5min, it would be best to make as many calls of two-opt as possible in that time period that still improve the overall circuit.  Essentially LP.
single_run_time = datetime.timedelta(microseconds=0);
total_diff = datetime.timedelta(microseconds=0);
old_length = distance(cities) + 1
new_length = distance(cities)
#check to see if an additional run will cause run time to go past ~5min
while (old_length > new_length):
	#first get time
	t1 = datetime.datetime.now()

	#core algorithm that minimizes 2-opt distance in min time
	old_length = new_length	
	two_opt(cities)	
	new_length = distance(cities)


	#second get time
	t2 = datetime.datetime.now()
	single_run_time = t2 - t1
	total_diff = total_diff + single_run_time
	#clear screen
	sys.stderr.write("\x1b[2J\x1b[H")
	print 'Execution time: ', total_diff.seconds, 's', int(total_diff.microseconds/1000), 'ms'
	

print 'Final Execution time: ', total_diff.seconds, 's', int(total_diff.microseconds/1000), 'ms'

cities_order = tuple(x[0] for x in cities)


#build the array as a string for printing to file

output = file_name + '.tour_no_limit'
file = open(output, "w")

file.write("%i\n" % distance(cities))
for i in range(len(cities)):
	file.write("%i\n" % cities_order[i])
file.close()
