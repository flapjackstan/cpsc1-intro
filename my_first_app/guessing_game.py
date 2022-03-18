import random

random_variable = random.randint(1, 10)
input_number = int(input("Please type a number: "))
flag = True

while(flag):

	if input_number == random_variable:
		print('You guessed the right number!')
		flag = False
	elif input_number < random_variable:
		print("Too Low!")
		input_number = int(input("Please type a number: "))
	else:
		print("Too High!")
		input_number = int(input("Please type a number: "))