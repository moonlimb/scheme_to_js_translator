
# parse a lisp program
# generate lisp ABT 
# convert to JS ABT

# open a lisp file
# read as a long string
# interpret


# f = open(lisp.txt)
# program = f.readlines()
# should I replaces '\n' with ""?


"""
def to_string(exp):
	"Convert a Python objet back into a Lisp-readable string."
	return '(' +' '.join(map(to_string, exp))+')' if isa(exp, list) else str(exp)
"""

def tokenize(s):
	"Convert a string into a list of tokens."
	return s.replace('(', ' ( ').replace(')',' ) ').split()

# evaluate the list of tokens
# def evaluate(tokens):
# 	for token in tokens:
#	
# is eval a pre-defined function?

def parse(prompt):
	return str(prompt)

def repl(prompt='scheme >> '):
	"A prompt-read-eval-print loop." 
	
	while True:		# while user types sth
		user_input = raw_input(prompt)
		val = parse(user_input)
		if val == '(exit)':
			return
		print val

#		val = eval(parse(user_prompt))
#		if val is not None: print to_string(val)
