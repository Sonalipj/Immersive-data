#Program for Eliza chatbot
welcome = input("Hello!. What is your name? ")
print(f"Welcome, {welcome.title()}!")
message = input("Enter your response here or Q to quit:")
print("Hello {}". format(message))
msg = " "
prompt = "\n Tell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
#temp = "i am fine"
while True:
	msg= input(prompt)
	#print(msg)
	if msg.lower() == 'quit':
		break
		
	'''if	msg.find(temp):
		break'''
		
	print(msg.title())
	
print("END")
		
'''

while message != 'quit':
    message = input(prompt)
    print(message)'''