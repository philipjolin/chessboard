"""
Chessboard Evaluation with the Relative Value System
"""

print()
print("*************************************************************************")
print("Empty Space (-), (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn.")
print("Lowercase letters are white pieces and uppercase letters are black pieces.")
print("*************************************************************************")
print()

# Create two dictionaries, scoreMapBlack and scoreMapWhite, to map the chess piece abbreviations into numberical values.
scoreMapBlack = {'Q':10,'R':5,'N':3,'B':3,'P':1, 'K':0, '-':0, ' ':0}

scoreMapWhite = {'q':10,'r':5,'n':3,'b':3,'p':1, 'k':0, '-':0, ' ':0}

# Create the function getChessboard to obtain 8 characters for each row of the chessboard
def getChessboard():

	# Create 8 lists
	chessboard = [0] * 8

	# Create a variable to hold index
	index = 0

	# Create a variable to hold a string
	characters = ''

	# Get the 8 characters for each row starting from the 8th row
	for r in range(8,0,-1):
		
		# From Row 8 to Row 4
		if r > 3:

			# Prompt user for 8 characters
			print('Please type 8 characters for the ', \
				r, "th row of the chessboard: ", sep='', end='')
			characters = str(input())	

			# Verify if there are 8 characters present in the string. If not then keep prompting user.
			while (len(characters) != 8):
				print('Please type exactly 8 characters for the ', \
				r, "th row of the chessboard: ", sep='', end='')
				characters = str(input())
			
			# Call the validateKeys function to validate whether the characters received from the user contains only the characters in the dictionaries. If not then infrom the user and keep prompting them until the validation returns True.
			while ((validateKeys(scoreMapBlack, characters)) == False) and ((validateKeys(scoreMapWhite, characters)) == False): 
				print()
				print("The allowed characters are as follows: Empty Space (-), (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn.")
				print()
				print('Please type 8 characters for the ', \
				r, "th row of the chessboard: ", sep='', end='')
				characters = str(input())
			
			# Assign characters to the list at index
			chessboard[index] = characters

			# Add 1 to the counter
			index += 1

		# Row 3
		elif r == 3:
			
			# Prompt user for 8 characters
			print('Please type 8 characters for the ', \
				r, 'rd row of the chessboard: ', sep='', end='')
			characters = str(input())
			
			# Verify if there are 8 characters present in the string. If not then keep prompting user.
			while len(characters) != 8:
				print('Please type exactly 8 characters for the ', \
				r, "rd row of the chessboard: ", sep='', end='')
				characters = str(input())

			# Call the validateKeys function to validate whether the characters received from the user contains only the characters in the dictionaries. If not then infrom the user and keep prompting them until the validation returns True.
			while ((validateKeys(scoreMapBlack, characters)) == False) and ((validateKeys(scoreMapWhite, characters)) == False): 
				print()
				print("The allowed characters are as follows: Empty Space (-), (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn.")
				print()
				print('Please type 8 characters for the ', \
				r, "th row of the chessboard: ", sep='', end='')
				characters = str(input())
			
			# Assign characters to the list at index
			chessboard[index] = characters

			# Add 1 to the counter
			index += 1
		
		# Row 2
		elif r == 2:
			
			# Prompt user for 8 characters
			print('Please type 8 characters for the ', \
				r, 'nd row of the chessboard: ', sep='', end='')
			characters = str(input())

			# Verify if there are 8 characters present in the string. If not then keep prompting user.
			while len(characters) != 8:
				print('Please type exactly 8 characters for the ', \
				r, "nd row of the chessboard: ", sep='', end='')
				characters = str(input())
			
			# Call the validateKeys function to validate whether the characters received from the user contains only the characters in the dictionaries. If not then infrom the user and keep prompting them until the validation returns True.
			while ((validateKeys(scoreMapBlack, characters)) == False) and ((validateKeys(scoreMapWhite, characters)) == False): 
				print()
				print("The allowed characters are as follows: Empty Space (-), (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn.")
				print()
				print('Please type 8 characters for the ', \
				r, "th row of the chessboard: ", sep='', end='')
				characters = str(input())
			
			# Assign characters to the list at index
			chessboard[index] = characters

			# Add 1 to the counter
			index += 1
		
		# Row 1
		else:

			# Prompt user for 8 characters
			print('Please type 8 characters for the ', \
				r, 'st row of the chessboard: ', sep='', end='')
			characters = str(input())

			# Verify if there are 8 characters present in the string. If not then keep prompting user.
			while len(characters) != 8:
				print('Please type exactly 8 characters for the ', \
				r, "st row of the chessboard: ", sep='', end='')
				characters = str(input())

			# Call the validateKeys function to validate whether the characters received from the user contains only the characters in the dictionaries. If not then infrom the user and keep prompting them until the validation returns True.
			while ((validateKeys(scoreMapBlack, characters)) == False) and ((validateKeys(scoreMapWhite, characters)) == False): 
				print()
				print("The allowed characters are as follows: Empty Space (-), (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn.")
				print()
				print('Please type 8 characters for the ', \
				r, "th row of the chessboard: ", sep='', end='')
				characters = str(input())

			# Assign characters to the list at index
			chessboard[index] = characters

			# Add 1 to the counter
			index += 1

	# Return the list
	return chessboard

"""
Code modified and obtained from http://stackoverflow.com/a/12771730
  // s='abcd'
	 d={'a':1, 'b':2, 'c':3}
	 all(c in d for c in s)
"""
# Create validateKeys function to accept a dictionary and string as arguments and validate whether a string received from the user contains only the characters in the dictionaries.
def validateKeys(dictionary, string):
	# Returns True if all characters in string are present in dictionary, otherwise returns False. 
	return all(c in dictionary for c in string)

# Create rowCompare function to accept a string as an argument and compare a string with keys in the dictionaries.
def rowCompare(string):
    
    # Create two variables to hold the total score value of black and white
    totalW = 0
    totalB = 0
    
    # Iterate through the string 
    for letter in string:

    	# If a character is lowercase then get its numerical value in the dictionary and add it to totalW
    	if ((string.islower()) == True):
    		totalW += scoreMapWhite.get(letter, 0)
    	# Else if character is uppercase then get its numerical value in the dictionary and add it to totalB
    	elif((string.isupper()) == True):
    		totalB += scoreMapBlack.get(letter, 0)
    
    # Return both totalW and totalB
    return totalW, totalB

# Create getScore function acquire to accept a list as an argument and calculate the final score of black and white
def getScore(chessboard):

	# Create variables to hold the sum and titak
	blackTotal = 0
	whiteTotal = 0
	blackSum = 0
	whiteSum = 0

	# Loop through every index value in the chessboard list
	for i in range(len(chessboard)):

		# Assign the value in chessboard[i] to 'string'
		string = chessboard[i]

		# Call the rowCompare function with 'string' as an argument and assign the return values to whiteTotal and blackTotal
		whiteTotal, blackTotal = rowCompare(string)

		# Keep the final sum of both
		blackSum += blackTotal
		whiteSum += whiteTotal

	# Return the final sum
	return whiteSum, blackSum

# Create main function to print results
def main():

	# Call function getScore() with getChessboard as an argument and set whiteScore and blackSore variables to equal the return values.
	whiteScore, blackScore = getScore(getChessboard())
	
	# Print 3 different sentences depending on who wins or if the game is a tie.
	if whiteScore == blackScore:
		print()
		print("White has a score of", whiteScore, "and Black has a score of", blackScore,", so this game is a tie.")
	elif whiteScore > blackScore:
		print()
		print("White has a score of", whiteScore, "and Black has a score of", blackScore,", so white is winning.")
	else:
		print()
		print("White has a score of", whiteScore, "and Black has a score of",blackScore,", so black is winning.")

# Call main function
main()