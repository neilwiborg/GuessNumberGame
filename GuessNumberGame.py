import random
import re

def printWelcome() -> None:
	print("==============================================================")
	print("Welcome to the Guess a Number Game!")

def parseRangeInput(rangeInput: str) -> list[int]:
	type = ""
	# TODO allow no brackets around
	# TODO allow negative numbers
	if rangeInput[0] == '(' and rangeInput[-1] == ')':
		type = "exclusive"
	elif rangeInput[0] == '[' and rangeInput[-1] == ']':
		type = "inclusive"
	else:
		return []
	
	rangeInput = rangeInput[1:-1].replace(" ", "")
	invalid_characters = re.compile(r"[^0-9,]")
	if invalid_characters.search(rangeInput):
		return []
	numbers = [int(x) for x in rangeInput.split(",")]
	if len(numbers) != 2:
		return []

	if type == "exclusive":
		numbers[0] += 1
		numbers[1] -= 1

	if numbers[0] >= numbers[1]:
		return []
	
	return numbers

def getRange() -> list[int]:
	numbers = []
	while (len(numbers) == 0):
		range = input("Enter range: ")
		numbers = parseRangeInput(range)
		if len(numbers) == 0:
			print("Invalid input! Please try again.")
	return numbers

def getAttempts() -> int:
	attempts = 0
	while attempts < 1:
		attempts = input("Enter number of attempts to allow: ")
		# TODO check if negative number{20,30}
		if attempts.isdigit():
			attempts = int(attempts)
			if (attempts  < 1):
				print("Invalid number of attempts!")
		else:
			attempts = 0
			print("Invalid input!")
	return attempts

def printEnding(remainingAttempts: int, secretNumber: int) -> None:
	if (remainingAttempts > 0):
		print("Good guess! Hope your luck continues next time!")
	else:
		print("Too bad, the correct answer was " + str(secretNumber) + ". Try again next time!")

def runGame(numbers: list[int], attempts: int) -> None:
	secretNumber = random.randint(numbers[0], numbers[1])

	while (attempts > 0):
		# TODO check if input is number
		guess = int(input("Enter your guess: "))
		if (guess == secretNumber):
			print("CORRECT!!!")
			break
		print("WRONG!")
		attempts -= 1
		if (guess < secretNumber and attempts > 0):
			print("Try higher....")
		elif (guess > secretNumber and attempts > 0):
			print("Try lower...")

	printEnding(attempts, secretNumber)	

def main():
	printWelcome()
	runGame(getRange(), getAttempts())
		
if __name__ == "__main__" :
	main()
