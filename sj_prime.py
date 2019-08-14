# Program to calculate prime number

x= int(input("Please enter the number to check if prime:"))


i=2
while i<x:
	if x%i ==0:
		print(f"{x} is Not Prime")
		break
			
	else:
		i = i+1
		continue
		
		
	
if i==x:
	print(f"{x} is Prime")	

	

