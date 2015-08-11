#!/usr/bin/python

import sys, pprint;
from math import sqrt;

#Function returns distance between two cities, rounded to float, cast to int

points = []
size = 550
def get_distance(c1, c2):
	return int(round(sqrt((c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)))

i = 0
#list to hold all cities
cities = []
with open("tsp_example_1.txt", "r") as text_file:
	#for each line in file
	for line in text_file:
		#add another list to the cities list (i.e. add another city)
		cities.append([])
		#add the information from the line ([0] is id, [1] is x, [2] is y)
		cities[i].append(int(line.strip().split()[0]))
		cities[i].append(int(line.strip().split()[1]))
		cities[i].append(int(line.strip().split()[2]))
		i = i + 1

#2D list to hold disatances between cities, accessed by city id:
#e.g. distances[0][1] is the distance between city the first city in list and the second
distances = [0 for i in range(len(cities))]

#get distances between all cities
def distance(cities):
	if len(cities) == 0:
		return 0
	distance = 0
	for i in range(len(cities) -1 ):
			distance += get_distance(cities[i], cities[i+1]);			
	return distance

def two_opt(cities):
  for i in range(len(cities) - 1):
    for j in range(i + 2, len(cities) - 1):
      if get_distance(cities[i], cities[i+1]) + get_distance(cities[j], cities[j+1]) > get_distance(cities[i], cities[j]) + get_distance(cities[i+1], cities[j+1]):          cities[i+1:j+1] = reversed(cities[i+1:j+1])
  return cities

	
two_opt(cities)	
	

#two_opt(distances)

for i in range(len(cities)):
		print  cities[i]
print distance(cities)

#for i in range(len(distance)):
