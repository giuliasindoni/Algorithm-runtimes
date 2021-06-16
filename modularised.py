import numpy
import time
import matplotlib.pyplot as plt
import math 


from bubble_sort import my_bubble_sort

from insertion_sort import insertion_sort

from selection_sort import selection_sort

from merge_sort import merge_sort

from quick_sort import quick_sort





#------- Function to create a certain number n of arrays of size my size. 
#------- For example create_n_random_arrays(2, 3) creates 2 arrays of size 3.
#-------- Returns an array of n arrays of size mysize.

def create_n_random_arrays(n, mysize):
  	list_of_arrays = []
  	for i in range(n):
  		created_array = numpy.random.randint(-200, 200, size=mysize, dtype=int)
  		list_of_arrays.append(created_array)
  	return list_of_arrays




#-------- Function to collect average running times of algorithms on arrays of sizes 5, 10, 50, 100... 
#-------- Argument "algorithm" specify which algorithm we want to collect the data for
#-------- Argument array_of_sizes is an array collecting the sizes we want the arrays argument of the algorithm to be
#-------- We always create n = 10 arrays of each size, but this parameter could be changed.

def collect_data(algorithm, array_of_sizes):
	list_of_averages_algorithm = []
	for size in array_of_sizes:
		lenght_size = create_n_random_arrays(10, size)
		attempt = []
		for array in lenght_size:
			start_time = time.time()
			algorithm(array)
			end_time = time.time()
			time_taken = end_time - start_time
			attempt.append(time_taken)
		attempt_average_size = sum(attempt) / len(attempt)
		list_of_averages_algorithm.append(attempt_average_size)
	return list_of_averages_algorithm

#-------- Some tests to collect on merge_sort, quick_sort ... with arrays of sizes 5, 10, 50, 100, ..., 5000

sizes = [5,10, 50, 100, 500, 1000, 5000]


list_of_averages_merge = collect_data(merge_sort, sizes)

#print(list_of_average_merge)


list_of_averages_quick = collect_data(quick_sort, sizes)

#print(list_of_average_quick)


#list_of_average_bubble = collect_data(my_bubble_sort, sizes)

#print(list_of_average_bubble)


#list_of_average_insertion = collect_data(insertion_sort, sizes)

#print(list_of_average_insertion)


#list_of_average_selection = collect_data(selection_sort, sizes)

#print(list_of_average_selection)


#---------- Plotting the data and save img as png file



plt.xscale('log')
plt.yscale('log')
#plt.plot(size, list_of_avarages_bubble , 'b-', label='bubble sort')
plt.plot(sizes, list_of_averages_merge, 'r-', label='merge sort')
plt.plot(sizes, list_of_averages_quick, 'y-', label='quick sort')


#--------__Plotting some functions to appreciate the bounds of the algorithms curves


x = range(5,5000)
y = [(1/10**6)*i*math.log(i,2) for i in x]
t = [(1/10**6)*i**2 for i in x]
k =  [ (1/10**6)* i for i in x]



plt.plot(x, y, '-g')
#plt.plot(x, k)

#plt.plot(x, t)


plt.xlabel('Size')
plt.ylabel('Average')
#plt.savefig('merge-quick')

plt.savefig('merge-quick-nlogn')













