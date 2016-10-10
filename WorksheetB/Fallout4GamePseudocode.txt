```
secretWord = generate a 5 letter word
secretWord1 = get first letter			<break down secretWord into parts>
secretWord2 = get second letter
secretWord3 = get third letter
secretWord4 = get fourth letter
secretWord5 = get fifth letter

attempts = 0

message: "Try and guess my 5 letter word, you have 4 attempts"

loop 4 times[
	attempts = attempts + 1

	guess = get string input from user
	guess1 = get first letter			<break down guess into parts>
	guess2 = get second letter
	guess3 = get third letter
	guess4 = get fourth letter
	guess5 = get fifth letter
	
	numberCorrect = 0			<resets numberCorrect after each run through the loop>
	
	if guess1 matches secretWord1:
		+1 to numberCorrect
	end if
		
	if guess2 matches secretWord2:
		+1 to numberCorrect
	end if
		
	if guess3 matches secretWord3:
		+1 to numberCorrect
	end if
		
	if guess4 matches secretWord4:
		+1 to numberCorrect
	end if
		
	if guess5 matches secretWord5:
		+1 to numberCorrect
	end if
	
	if numberCorrect = 5:
		message: "you win!"
		end loop
	elif attempts = 4:
		message: "Sorry, you only got " numberCorrect ", and you're out of tries. You lose"
	else:
		message: "You got" numberCorrect "letters correct. Try again.
	end if
]

end of code
```
