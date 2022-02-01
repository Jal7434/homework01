for num in range(3,100):
	if all(num%i !=0 for i in range(2,num)):
		print (num)

