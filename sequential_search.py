import random 
import numpy
import time
import matplotlib.pyplot as plt
import math 

def sequential_search(array, key):
	i = 0
	while i <= (len(array)-1) and array[i] != key:
		i = i+1 
	if i < len(array):
		return i 
	else:
		return -1

A = [9, 0, 2, 8, 10, 10]

K = 10



#print(sequential_search(A, K))



def create_n_random_arrays(n, mysize):
  	list_of_arrays = []
  	for i in range(n):
  		created_array = numpy.random.randint(-500000, 500000, size=mysize, dtype=int)
  		list_of_arrays.append(created_array)
  	return list_of_arrays



def collect_search_data(algorithm, array_of_sizes):
	list_of_averages_algorithm = []
	for size in array_of_sizes:
		lenght_size = create_n_random_arrays(10, size)
		attempt = []
		for array in lenght_size:
			randomkey = random.choice(array)
			start_time = time.time()
			algorithm(array, randomkey)
			end_time = time.time()
			time_taken = end_time - start_time
			attempt.append(time_taken)
		attempt_average_size = sum(attempt) / len(attempt)
		list_of_averages_algorithm.append(attempt_average_size)
	return list_of_averages_algorithm

my_sizes = [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

print(collect_search_data(sequential_search, my_sizes))




