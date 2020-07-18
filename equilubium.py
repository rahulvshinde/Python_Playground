def equi():
	my_array = [3,1,2,4,3]
	finaldiff = sum(my_array)
	length=len(my_array)
	for p in range(1,length):
		first=my_array[:p]
		second=my_array[p:]
		diff=abs(sum(first)-sum(second))
		if diff < finaldiff:
			finaldiff = diff
		p+=1
	print(finaldiff)

equi()
