"""Program to find multiples of 3, 5, or 15 in the range of 1 through 100)"""

i=1

for i in range(101):
	if i%3 == 0 and i%5 == 0:
		print("Fizz Buzz")
		continue
		
	elif i%3 ==0:
		print("fizz")
		continue
	elif i%5 == 0:
				
		print('buzz')
		continue
	
	else:
		print(i)
				
				
		
	
			

		
	
	
