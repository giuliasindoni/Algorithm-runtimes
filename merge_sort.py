def merge_sort_2(myarray):
	if len(myarray) > 1:
		#Diving the array elements in two halfs
		S1 = myarray[:len(myarray)//2]
		S2 = myarray[len(myarray)//2:]

		#sorting the two halves

		merge_sort_2(S1)
		merge_sort_2(S2)

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


x = [3, 45, 1, -9, 10, 8]
print(merge_sort_2(x))

y = [3, 5, -1, 90, -89, 30, 59, 2, 4, 3]

print(merge_sort_2(y))
		


