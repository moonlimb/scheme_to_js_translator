import random

# Evaluate user input + print output statements 

# compare_user_guess will compare user_num and rand_num 
def compare_nums(user_num, rand_num):
	if user_num > rand_num:
		print "your guess is too high, try again."
	else: 
		print "your guess is too low, try again."

#returns user input converted from string to int
def get_user_guess(count):
	# increment user guess count by 1
	return int(raw_input("Type your guess: ")), count+1

def generate_rand_num():
	"produce random # betwen 1-100"
	return random.randint(1,100)

def make_guesses(rand_num):
	user_num, count = get_user_guess(0)
	while (user_num != rand_num):
		compare_nums(user_num, rand_num)
		user_num, count = get_user_guess(count)
	return count

def main():
	user_name = raw_input("what is your name? ")
	rand_num = generate_rand_num()	
	print "%s, i'm thinking of a number between 1 and 100. Try to guess my number." %user_name

	# count is number of user guesses
	count = make_guesses(rand_num)	

	# congratulatory message
	print "well done, %s! you found my number in %d tries!" %(user_name, count)

main()
