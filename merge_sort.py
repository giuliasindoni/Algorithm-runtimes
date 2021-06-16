import numpy
import time
import matplotlib.pyplot as plt

def merge_sort(myarray):
	if len(myarray) > 1:
		#Diving the array elements in two halfs
		S1 = myarray[:len(myarray)//2]
		S2 = myarray[len(myarray)//2:]

		#sorting the two halves

		merge_sort(S1)
		merge_sort(S2)

	#array = ['x' for m in range( (len(S1) + len(S2)) )]
		i = j = k = 0
		p = len(S1)
		q = len(S2)
		while i < p and j < q:
			if S1[i] <= S2[j]:
				myarray[k] = S1[i]
			#print(array)
				i = i +1
			else:
				myarray[k] = S2[j]
				j = j+1
			#print(array)
			k = k+1
		#print(S1)
		#print(S2)
	
		if i == p:
			myarray[k:(p+q)] = S2[j:(q)] 
		else:
			myarray[k:(p+q)] = S1[i:(p)] 
		return(myarray)


# def create_n_random_arrays(n, mysize):
# 	list_of_arrays = []
# 	for i in range(n):
# 		created_array = numpy.random.randint(-200, 200, size=mysize, dtype=int)
# 		list_of_arrays.append(created_array)
# 	return list_of_arrays

# list_of_avarages = []

# for i in [5,10, 50, 100, 500, 1000]:
# 	lenght_i = create_n_random_arrays(10, i)
# 	attempt = []
# 	for array in lenght_i:
# 		start_time = time.time()
# 		merge_sort_2(array)
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



# #size = [5,10, 50, 100, 500, 1000, 5000]


# #plt.plot(size, list_of_avarages_bubble , 'b-', label='bubble sort')
# #plt.plot(size, list_of_avarages_merge, 'r-', label='merge sort')

# #plt.xlabel('Size')
# #plt.ylabel('Avarage')
# #plt.show()


