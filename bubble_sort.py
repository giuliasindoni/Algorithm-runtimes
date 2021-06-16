import numpy
import time
import matplotlib.pyplot as plt

# definitiom of bubble sort algorithm

def my_bubble_sort(mylist):
	for i in range(len(mylist) - 1):
		for j in range(0, ( (len(mylist) -1) - i)):
			if mylist[j] > mylist[j+1]:
				tmp = mylist[j]
				mylist[j] = mylist[j+1]
				mylist[j+1] = tmp
	return(mylist)
	



example = [-14, 7, 8, 6, -2, -1, -100]

example2 = [67, 0, -1, 90, 89, 5, 9, 7, 7]

example3 = [0, 0, 90, 8, -2, 56]

#print(my_bubble_sort(example3))


# function to create n random arrays of size mysize

# def create_n_random_arrays(n, mysize):
# 	list_of_arrays = []
# 	for i in range(n):
# 		created_array = numpy.random.randint(-200, 200, size=mysize, dtype=int)
# 		list_of_arrays.append(created_array)
# 	return list_of_arrays
# #print(create_n_random_arrays(5, 2))


# # run my_bubble sort on n = 10 arrays of size 5 
# # for each of the 10 arrays measure the time taken
# # then avarage the time 

# list_of_avarages = []

# for i in [5,10, 50, 100, 500, 1000]:
# 	lenght_i = create_n_random_arrays(10, i)
# 	attempt = []
# 	for array in lenght_i:
# 		start_time = time.time()
# 		my_bubble_sort(array)
# 		end_time = time.time()
# 		time_taken = end_time - start_time
# 		attempt.append(time_taken)
# 	attempt_avarage_i = sum(attempt) / len(attempt)
# 	list_of_avarages.append(attempt_avarage_i)

# #print(list_of_avarages)

# #simple check

	
# #if all(list_of_avarages[i] < list_of_avarages[i+1] for i in range(len(list_of_avarages)-1)):
# #	print("TRUE")


# size = [5,10, 50, 100, 500, 1000]

# avarage = list_of_avarages

# plt.plot(size, avarage)
# plt.xlabel('Size')
# plt.ylabel('Avarage')
# plt.show()



