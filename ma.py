#
# Math Attack 1.0
#
# A simple math game that helps people practice basic 
# addition, subtraction, multiplication and division.
#
# Developed on September 24th, 2017 by Matt Frey

import random

def compare(int1,int2,operator,ans_type): #Tests which int is larger and what type of information to return.
	if ans_type == "str": #Return Equation in String Form.
		if operator == " / ":
			if int1 < int2:
				return str(int2*int1) + operator + str(int1)
			else:
				return str(int1*int2) + operator + str(int2)
		else:
			if int1 < int2:
				return str(int2) + operator + str(int1)
			else:
				return str(int1) + operator + str(int2)
	else:	#Return the Answer to the Equation
		if int1 < int2:
			if operator == " + ":
				ans = int2+int1
			elif operator == " - ":
				ans = int2-int1
			elif operator == " * ":
				ans = int2*int1
			else:
				ans = int2
			return ans
		else:
			if operator == " + ": 
				ans = int1+int2
			elif operator == " - ":
				ans = int1-int2
			elif operator == " * ":
				ans = int1*int2
			else:
				ans = int1
			return ans

def get_questions(amount, diff, range1, range2):
	i = 1
	amount+= 1
	questions = []
	while i < amount:
		if diff == "easy" or diff == "ez":
			int1 = random.randint(1,10)
			int2 = random.randint(1,10)
		elif diff == "medium" or diff == "med":
			int1 = random.randint(1,10)
			int2 = random.randint(1,20)
		else: 
			int1 = random.randint(1,10)
			int2 = random.randint(1,30)
		get_op = random.randint(range1,range2) #determine the type of arithmetic to be performed.
		if get_op == 0: #Determine Operator
			operator = " + "
		elif get_op == 1:
			operator = " - "
		elif get_op == 2:
			operator = " * "
		else:
			operator = " / "
		q = compare(int1, int2, operator,"str")
		ans = compare(int1, int2, operator,"int")
		questions.append(["Question "+str(i)+": "+q,str(ans)])
		i+= 1
	return questions

def game_settings(typeQ, diff, amount):
	if typeQ == "a":
		questions = get_questions(amount, diff, 0, 1) # Addition/Subtraction
	elif typeQ == "m":
		questions = get_questions(amount, diff, 2, 3) # Multiplication/Division
	else:
		questions = get_questions(amount, diff, 0, 3) # All Operators Included
	return questions

def ask(questions):
	stats = {"right":0,"wrong":0,"total":0}
	i = 0 
	while i < len(questions):
		answer = input("\n"+str(questions[i][0]+" "))
		if answer == questions[i][1]:
			stats["right"] += 1
		else:
			stats["wrong"] += 1
		stats["total"] +=1
		i+= 1
	print("\nGood Job! You Finished up with "+ str(stats["right"]) +" correct, out of a total of "+ str(stats["total"]) +" problems.\n Giving you "+ str((stats["right"]/stats["total"])*100) +"%.")
	replay = input("\nWant to play again? Y/N ").upper()
	if replay.startswith("Y"):
		play()
	else:
		print("Thanks for playing!")
			
def play():
	print("Welcome to Math Attack 1.0 . The Game is simple, get as many correct as possible. \nTry to do every question only using mental arithmetic. Why?! Because it will help your brain! Good Luck!") 
	while True:
		amount = input("\nHow many questions do want to complete? It can be any number. ")
		if amount.isnumeric(): #[num for num in range(0,10)]
			break
	while True:
		diff = input("\nChoose a difficulty: Easy ('e'), Medium ('m'), or Hard ('h'). ").lower()
		if diff.startswith("e") or diff.startswith("m") or diff.startswith("h"):
			break
	while True:
		typeQ = input("\nChoose between Addition/Subtraction (a), Multiplication/Division (b), or All (c): ").lower()
		if typeQ.startswith("a") or typeQ.startswith("b") or typeQ.startswith("c"):
			break
	questions = game_settings(typeQ, diff, int(amount))
	ask(questions)

print("\n\n\n")	
print("----------------------------------------------------------------------------------------")
print("|     MM  MM     AAA   TTTTTT HH  HH      AAA  TTTTTT  TTTTTT  AAA    CCCC  KK KK      |")
print("|    MMMMMMMM   AA AA    TT   HHHHHH     AA AA   TT      TT   AA AA  CC     KKK        |")
print("|   MM   M  MM  AA AA    TT   HH  HH     AA AA   TT      TT   AA AA   CCCC  KK KK      |")
print("----------------------------------------------------------------------------------------")
print("\n\n\n")

play() #Start game
