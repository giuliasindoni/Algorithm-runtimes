def sequential_search(array, key):
	i = 0
	while i <= (len(array)-1) and array[i] != key:
		i = i+1 
	if i < len(array):
		return i 
	else:
		return -1

A = [9, 0, 2, 8, 10]

K = 3

print(sequential_search(A, K))