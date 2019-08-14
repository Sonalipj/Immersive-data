#program to check prime number
x= int(input("Upper limit of the range:"))
print(x)
i=1
#j=1
print("These are the prime number for the range 1 though " + str(x) + " are")
print(i)
while i<= x:
    j=2
    while j<=i:
        if i%j==0:
            break
        else:
            j += 1
            continue

    if i==j:
        print(i)
	i+=1
		
		









