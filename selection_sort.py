def selection_sort(array):
	for i in range(len(array) - 1):
		mini = i
		for j in range(i+1, len(array)):
			if array[j] < array[mini]:
				mini = j
		tmp = array[i]
		array[i] = array[mini]
		array[mini] = tmp
	return(array)



# x = [5, 9, 2, 50, -34]


# example = [-14, 7, 8, 6, -2, -1, -100]

# example2 = [67, 0, -1, 90, 89, 5, 9, 7, 7]


# example3 = [0, 0, 90, 8, -2, 56, 0]

# example4 = [8, -3, 3]


# print(selection_sort(example))

