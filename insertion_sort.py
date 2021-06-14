def insertion_sort(array):
	for i in range(len(array)):
		tmp = array[i]
		j = i - 1
		while j >= 0 and tmp < array[j]:
			array[j + 1] = array[j]
			j = j -1
			array[j + 1] = tmp
	return(array)

x = [0, 89, -2, 9, 10]


example = [-14, 7, 8, 6, -2, -1, -100]

example2 = [67, 0, -1, 90, 89, 5, 9, 7, 7]


print(insertion_sort(example))

