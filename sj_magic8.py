#Program for Magic 8 ball
'''welcome = input("Hello!. What is your name? ")
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
		
	''if	msg.find(temp):
		break
		
	print(msg.title())
	
print("END")
		


while message != 'quit':
    message = input(prompt)
    print(message)'''
	
answers = {'1':'It is certain', '2': 'It is decidedly so', '3' : ' Without a doubt', '4' : 'yes definitely', '5' : 'You may rely on it', '6' : 'As I see it, yes',
			'7' : 'Most likely', '8' : 'Outlook good', '9' : 'Yes', '10' : 'Signs point to yes', '11' : 'Reply hazy try again', '12' : 'Ask again later',
			'13' : 'Better not tell you now', '14' : 'Cannot predict now', '15' : 'Concentrate and ask again', '16' : 'Don\'t count on it', '17' : 'My reply is no',
			'18' : 'My sources say no', '19' : 'Outlook not so good', '20' : 'Very doubtful'
 }
 
ch = random.randint(1,18)
print(ch)
"""for choice, answer in answers:
	ch = random(1,18)
	print(ch.answer)"""