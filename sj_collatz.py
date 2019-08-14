
x= int(input("Please enter number to create sequence"))
#print("You entered" +" " + str(i))
print(x, end = " ")
#while input(x):
	
while x != 1:
		if x % 2 ==0:
			x = x//2
			print(x, end = " ")
		
		else:
			x = x * 3 + 1
			print(x, end = " ")
			x = x//2
			print(x, end = " ")
			
	








