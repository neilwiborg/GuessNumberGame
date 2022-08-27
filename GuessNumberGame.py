import random

def parseRangeInput(rangeInput: str) -> list[int]:
	type = ""
	if rangeInput[0] == '(' and rangeInput[-1] == ')':
		type = "exclusive"
	elif rangeInput[0] == '[' and rangeInput[-1] == ']':
		type = "inclusive"
	else:
		return []
	
	rangeInput = rangeInput[1:-1].replace(" ", "")
	# TODO check to make sure all characters are 0-9 or , (no letters/symbols)
	numbers = [int(x) for x in rangeInput.split(",")]
	if len(numbers) != 2:
		return []

	if type == "exclusive":
		numbers[0] += 1
		numbers[1] -= 1

	if numbers[0] >= numbers[1]:
		return []
	
	return numbers

def main():
	print("==============================================================")
	print("Welcome to the Guess a Number Game!")
	numbers = []
	while (len(numbers) == 0):
		range = input("Enter range: ")
		numbers = parseRangeInput(range)
		if len(numbers) == 0:
			print("Invalid input! Please try again.")
	secretNumber = random.randint(numbers[0], numbers[1])
	# TODO check if input is number
	attempts = int(input("Enter number of attempts to allow: "))
	while (attempts > 0):
		# TODO check if input is number
		guess = int(input("Enter your guess: "))
		if (guess == secretNumber):
			print("CORRECT!!!")
			break
		print("WRONG!")
		attempts -= 1
	if (attempts > 0):
		print("Good guess! Hope your luck continues next time!")
	else:
		print("Too bad, the correct answer was " + str(secretNumber) + ". Try again next time!")

if __name__ == "__main__" :
	main()