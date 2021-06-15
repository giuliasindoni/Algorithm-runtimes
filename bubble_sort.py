import numpy
import time

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

def create_n_random_arrays(n, mysize):
	list_of_arrays = []
	for i in range(n):
		created_array = numpy.random.randint(-200, 200, size=mysize, dtype=int)
		list_of_arrays.append(created_array)
	return list_of_arrays
#print(create_n_random_arrays(5, 2))


# run my_bubble sort on n = 10 arrays of size 5 
# for each of the 10 arrays measure the time taken
# then avarage the time 

list_of_avarages = []

for i in [5,10, 50, 100, 500, 1000]:
	lenght_i = create_n_random_arrays(10, i)
	attempt = []
	for array in lenght_i:
		start_time = time.time()
		my_bubble_sort(array)
		end_time = time.time()
		time_taken = end_time - start_time
		attempt.append(time_taken)
	attempt_avarage_i = sum(attempt) / len(attempt)
	list_of_avarages.append(attempt_avarage_i)

print(list_of_avarages)

#simple check

	
if all(list_of_avarages[i] < list_of_avarages[i+1] for i in range(len(list_of_avarages)-1)):
	print("TRUE")




# run my_bubble sort on n = 10 arrays of size 10
#for each of the 10 arrays measure the time taken
# then avarage the time 


#lenght_10 = create_n_random_arrays(10, 10)
#attempt = []
#for array in lenght_10:
#	start_time = time.time()
#	my_bubble_sort(array)
#	end_time = time.time()
#	time_taken = end_time - start_time
#	attempt.append(time_taken)
#attempt_avarage_10 = sum(attempt) / len(attempt)
#print(attempt_avarage_10)
#list_of_avarages.append(attempt_avarage_10)

# run my_bubble sort on n = 10  arrays of size 50 
#for each of the 10 arrays measure the time taken
# then avarage the time 


#lenght_50 = create_n_random_arrays(10, 50)
#attempt = []
#for array in lenght_50:
#	start_time = time.time()
#	my_bubble_sort(array)
#	end_time = time.time()
#	time_taken = end_time - start_time
#	attempt.append(time_taken)
#attempt_avarage_50 = sum(attempt) / len(attempt)
#print(attempt_avarage_50)
#list_of_avarages.append(attempt_avarage_50)

# run my_bubble sort on n = 10 arrays of size 100
#for each of the 10 arrays measure the time taken
# then avarage the time 


#lenght_100 = create_n_random_arrays(10, 100)
#attempt = []
#for array in lenght_100:
#	start_time = time.time()
#	my_bubble_sort(array)
#	end_time = time.time()
#	time_taken = end_time - start_time
#	attempt.append(time_taken)
#attempt_avarage_100 = sum(attempt) / len(attempt)
#print(attempt_avarage_100)
#list_of_avarages.append(attempt_avarage_100)

# run my_bubble sort on n = 10 arrays of size 500
#for each of the 10 arrays measure the time taken
# then avarage the time 


#lenght_500 = create_n_random_arrays(10, 500)
#attempt = []
#for array in lenght_500:
#	start_time = time.time()
#	my_bubble_sort(array)
#	end_time = time.time()
#	time_taken = end_time - start_time
#	attempt.append(time_taken)
#attempt_avarage_500 = sum(attempt) / len(attempt)
#print(attempt_avarage_500)
#list_of_avarages.append(attempt_avarage_500)

#lenght_1000 = create_n_random_arrays(10, 1000)
#attempt = []
#for array in lenght_1000:
#	start_time = time.time()
#	my_bubble_sort(array)
#	end_time = time.time()
#	time_taken = end_time - start_time
#	attempt.append(time_taken)
#attempt_avarage_1000 = sum(attempt) / len(attempt)
#print(attempt_avarage_1000)
#list_of_avarages.append(attempt_avarage_1000)


# simple check

#if attempt_avarage_5 < attempt_avarage_10 and attempt_avarage_50 < attempt_avarage_100 and attempt_avarage_100 < attempt_avarage_500 and attempt_avarage_500 < attempt_avarage_1000:
#	print("TRUE")





#test = numpy.random.randint(-1000, 1000, size=5, dtype=int)

