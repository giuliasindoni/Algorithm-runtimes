import math


def binary_search(sortedarray, key):
	left = 0
	right = len(sortedarray) - 1
	while left <= right:
		mid = math.floor((left + right) / 2)
		if key == sortedarray[mid]:
			return mid
		else:
			if key < sortedarray[mid]:
				right = mid -1
			else:
				left = mid + 1
	return -1 



#x = [49, 50, 50, 50, 900]

#mykey = 50

#print(binary_search(x, mykey))