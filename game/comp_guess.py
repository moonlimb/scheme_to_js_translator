import random

# Human will make random number 
# Computer will make an initial constant guess: 50 constant. And print this number. 
# The human will give feedback to computer if number guess is too hi or too low 
# THe computer will then make a new guess, which is a middle number in the new range. 
# the computer will repeat the process until it reaches the final number

# count the number of guesses 
def human_feedback(): 
	return raw_input("\nIs my guess 'too high', 'too low', or 'perfect'? ")

def smart_CS_guess(): 
	CS_guess = 50
	count = 1
#	human_answer = a certain number

	too_high = "too high" 
	too_low = "too low"
	perfect = "perfect"

	print "Hi. My name is Max the computer. I made my first guess: %d." %CS_guess

	human_input = human_feedback()

	#The computer does thinking below: 
	low_bound = 1
	high_bound = 100 

	while (human_input != perfect):
		if (human_input != too_high) and (human_input != too_low):
			print "EPIC FAIL! Type in a sensible reply, you're not a clever human."
			break
		elif human_input == too_high:
			high_bound = CS_guess - 1
			print low_bound, high_bound
		else: #human_input == too_low: 
			low_bound= CS_guess+1
			print low_bound, high_bound 
		CS_guess = (low_bound + high_bound)/2
		count+=1
		print count
		print "This is my new guess: %d." %CS_guess

		human_input = human_feedback()

	print "Congratulations Max! %d is the correct number. You got it in %d trials." %(CS_guess, count)

smart_CS_guess()




