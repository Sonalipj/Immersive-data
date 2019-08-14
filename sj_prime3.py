x= int(input("Please enter number for upper range"))
print("You entered" +" " + str(x))
i=1
print(f"{i} is a prime number!")

while i<=x:
	j=2
	while j<i:
		if i%j ==0:
			break
			
		else:
			j += 1
			continue
	if i==j:
		print(str(i) + " is a prime number!")
		
	i += 1
	
