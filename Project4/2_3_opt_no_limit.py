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

def three_opt(cities):
	#variable to hold length of potential paths
	length = [0 for k in range(6)]
	for i in range(len(cities)):
		#get indexes for each city in 
		city1 = i
		city2 = city1 + 1
		if (city2 >= len(cities)):
			city2 = 0
		city3 = city2 + 1
		if (city3 >= len(cities)):
			city3 = 0

		#get distance for each potential path
		length[0] = get_distance(cities[city1], cities[city2]) + get_distance(cities[city2], cities[city3])
		length[1] = get_distance(cities[city1], cities[city3]) + get_distance(cities[city3], cities[city2])
		length[2] = get_distance(cities[city2], cities[city1]) + get_distance(cities[city1], cities[city3])
		length[3] = get_distance(cities[city2], cities[city3]) + get_distance(cities[city3], cities[city1])
		length[4] = get_distance(cities[city3], cities[city1]) + get_distance(cities[city3], cities[city2])
		length[5] = get_distance(cities[city3], cities[city2]) + get_distance(cities[city2], cities[city1])

		#pprint.pprint(length)
		minimum_path = 0
		for j in range(len(length)):
			if (length[j] < length[minimum_path]):
				minimum_path = j

		#print minimum_path
		#if i == 0, path is already optimal
		if(minimum_path == 1):
			city_swap(cities, city2, city3)
		if(minimum_path == 2):
			city_swap(cities, city1, city2)
		if(minimum_path == 3):
			city_swap(cities, city1, city3)
			city_swap(cities, city3, city2)
		if(minimum_path == 4):
			city_swap(cities, city1, city3)
			city_swap(cities, city2, city1)
		if(minimum_path == 5):
			city_swap(cities, city1, city3)


def city_swap(cities, c1, c2):
	temp_city = []
	temp_city.append(cities[c1][0])
	temp_city.append(cities[c1][1])
	temp_city.append(cities[c1][2])
	cities[c1][0] = cities[c2][0]
	cities[c1][1] = cities[c2][1]
	cities[c1][2] = cities[c2][2]
	cities[c2][0] = temp_city[0]
	cities[c2][1] = temp_city[1]
	cities[c2][2] = temp_city[2]

#As two_opt loops through the circuit, breakig two conections at a time and improving them, and each call of two_opt makes a loop of all nodes, each call will most likely be an incremental improvement.  Therefore, if we have a time period of 5min, it would be best to make as many calls of two-opt as possible in that time period that still improve the overall circuit.  Essentially LP.  #including three_opt() makes this optimization even more powerful.
single_run_time = datetime.timedelta(microseconds=0);
total_diff = datetime.timedelta(microseconds=0);
old_length = distance(cities) + 1
new_length = distance(cities)
#check to see if an additional run will cause run time to go past ~5min
while (old_length > new_length):
	#first get time
	t1 = datetime.datetime.now()
	

	#core algorithm that minimizes 2-opt distance in min time
	#through trial and error it was found that this combination of 2/3 opt produced optimal results
	old_length = new_length
	if (len(cities) < 999):
		two_opt(cities)
		three_opt(cities)
		two_opt(cities)
		three_opt(cities)
		two_opt(cities)	
		three_opt(cities)
		two_opt(cities)
	if (len(cities) >= 999 and len(cities) < 2999):
		two_opt(cities)
		three_opt(cities)
		two_opt(cities)
	if (len(cities) >= 2999):
		two_opt(cities)

	new_length = distance(cities)
	#print 'old_length = ', old_length
	print 'new_length = ', new_length

	#second get time
	t2 = datetime.datetime.now()
	single_run_time = t2 - t1
	total_diff = total_diff + single_run_time
	#clear screen
	#sys.stderr.write("\x1b[2J\x1b[H")
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
