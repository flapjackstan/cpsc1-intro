import random

# First iteration
# print(random.randint(1, 10))

# Second 
# random_variable = random.randint(1, 10)
# print("Random Variable:", random_variable)

# Third
# input_number = input("Please type a number:")
# print("Input number is:", input_number)

# Fouth
# input_number = input("Please type a number: ")
# print("Input number is:", input_number)

# Fifth
# if 2 == 5:
# 	print('Hello True!')
# else:
# 	print("Hello False!")

# Sixth
# input_number = input("Please type a number: ")

# if input_number == 5:
# 	print('Hello True!')
# else:
# 	print("Hello False!")

# Seventh
# input_number = input("Please type a number: ")
# input_number = int(input_number)

# if input_number == 5:
# 	print('Hello True!')
# else:
# 	print("Hello False!")

# Eigth - same same but different
# input_number = int(input("Please type a number: "))

# if input_number == 5:
# 	print('Hello True!')
# else:
# 	print("Hello False!")

# Ninth
# random_variable = random.randint(1, 10)
# input_number = int(input("Please type a number: "))

# if input_number == random_variable:
# 	print('You guessed the right number!')
# else:
# 	print("You guessed wrong!")

# Tenth
# random_variable = random.randint(1, 10)
# input_number = int(input("Please type a number: "))

# if input_number == random_variable:
# 	print('You guessed the right number!')
# elif input_number < random_variable:
# 	print("Too Low!")
# else:
# 	print("Too High!")

# Eleventh
# random_variable = random.randint(1, 10)
# print("Random variable is:", random_variable)
# input_number = int(input("Please type a number: "))

# if input_number == random_variable:
# 	print('You guessed the right number!')
# elif input_number < random_variable:
# 	print("Too Low!")
# else:
# 	print("Too High!")

# Twelfth
# count = 0
# while (count < 3):   
#     count = count + 1
#     print("Hello Geek")

# Fourteenth
# while (2 < 3):   
#     print("Hello Geek")

# # Fifteenth
# while (True):   
#     print("Hello Geek")

# # Sixteenth
# while (False):   
#     print("Hello Geek")

# Seventeenth
# flag = False
# while (flag):   
#     print("Hello Geek")

# Eighteenth
# flag = True
# while (flag):   
#     print("Hello Geek")
#     flag = False

# Nineteenth
# random_variable = random.randint(1, 10)
# input_number = int(input("Please type a number: "))
# flag = True

# while(flag):

# 	if input_number == random_variable:
# 		print('You guessed the right number!')
# 		flag = False
# 	elif input_number < random_variable:
# 		print("Too Low!")
# 	else:
# 		print("Too High!")

# Twentieth
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