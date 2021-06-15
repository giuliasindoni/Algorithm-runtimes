def quick_sort(array):
	if len(array) <= 1:
		return array
	smaller = []
	equal = []
	greater = []
		
	pivot = array[0]
	for a in array:
		if a < pivot:
			smaller.append(a)
		elif a == pivot:
			equal.append(a)
		else:
			greater.append(a)
	return quick_sort(smaller) + equal + quick_sort(greater)

ex1 = [4, 9, 3, -2, 9, 10, -5, 8, 4]



# def quick_sort_2(array):
# 	if len(array) <= 1:
# 		return array
# 	smaller = []
# 	equal = []
# 	greater = []
		
# 	pivot = array[0]
# 	for a in array:
# 		if a < pivot:
# 			smaller.append(a)
# 		elif a == pivot:
# 			equal.append(a)
# 		else:
# 			greater.append(a)
# 		quick_sort_2(smaller)
# 		quick_sort_2(greater)
# 	return smaller + equal + greater



print(quick_sort(ex1))








