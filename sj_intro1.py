print("Hello and welcome to Immersive Datacamp")
print("My favorite color is purple")

#Python program to calculate employee salary
#Declaring employee array

emp = [[1, "Mary", 15.00, 40], [ 2, "John", 22.00, 25], [3, "Bob", 35.00, 4], [4, "Mel", 43.00, 62], [5, "Jen", 7.00, 33], [6, "Sue", 29.00, 45],
[7, "Ken", 40.00, 36], [8, "Dave", 20.00, 17], [9, "Beth", 37.00, 37],[10, "Ray", 16.50, 80] ] 

print(emp)

for id, name, rate, hours in emp:
	if hours>40:
	 totalpay = (((hours-40)*1.5) +(40*rate))
	 
	 
	else:
	 totalpay = hours*rate
	 
	 print(name, totalpay)
	 
  
 
  

