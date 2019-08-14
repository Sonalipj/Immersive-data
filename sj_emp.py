#Python program to calculate employee salary
#Declaring employee dictionary in dictionary

emp = {
		'001': {'name': 'mary', 'rate' : 15.00,'hours': 40},
		'002': {'name': 'john', 'rate' : 22.00,'hours': 25},
		'003': {'name': 'bob', 'rate' : 35.00, 'hours': 4},
		'004': {'name': 'mel', 'rate' : 43.00, 'hours': 62},
		'005': {'name': 'jen', 'rate' : 17.00, 'hours': 33},
		'006': {'name': 'sue', 'rate' : 29.00, 'hours': 45},
		'007': {'name': 'ken', 'rate' : 40.00, 'hours': 36},
		'008': {'name': 'dave','rate' : 20.00, 'hours': 17},
		'009': {'name': 'beth','rate' : 37.00, 'hours': 37},
		'010': {'name': 'ray', 'rate' : 16.50, 'hours': 80}
		

	} 

"""Accessing dictionary in dictionary to calculate pay for each employee
id is key and emp info is value.
individual elements are accessed by using indices of inside dictionary"""

for  id, emp_info in emp.items():
	if emp_info['hours'] >40:
	 totalpay = (((emp_info['hours']-40)*1.5* emp_info['rate']) +(40*emp_info['rate']))
	  
	 
	else:
	 totalpay = emp_info['hours']*emp_info['rate']
	 
	print(f"Total salary of {emp_info['name'].title()} is,    {totalpay}") 
	 
  
 