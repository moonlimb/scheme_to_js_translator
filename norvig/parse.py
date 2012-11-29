

# Parsing: 1) lexical analysis 2) syntactic analysis

# lexical analysis:	input char str --> break up into a sequence of tokens
# syntactic analysis: tokens assembled into an internal representation


# lispy tokens: 	parentehses, symbols, and numbers
		# symbols include any string (ex. function name, variable, str)

# returns a list of 
def read(s):
	"Read a Scheme expression from a string."
	return read_from(tokenize(s))

def tokenize(s):
	"Convert a string into a list of tokens."
	return s.replace('(,' ' ( ').replace(')'. ' ) ').split()
	# replace all parens with parens decorated by empty space on both sides
	# --> so we can split s by empty spaces to get the tokens

def read_from(tokens):
	"Read an expression from a sequence of tokens."
	if len(tokens) == 0:
		raise SyntaxError('unexpected EOF while reading')
	token = tokens.pop(0)
	if '(' == token:		# called only once for '('
		L = []
		while tokens[0] != ')':
			L.append(read_from(tokens))
		tokens.pop(0) #pop off ')'
		return L
	elif ')' == token:
		raise syntaxError('unexpected )')
	else:
		return atom(token)
		#this part traverses through all the atoms in tokens

def to_string(exp):
	"Convert a Python object back into a Lisp-readable string."
	return '('+' '.join(map(to_string, exp))+')' if isa(exp, list) else str(exp)

# map(fcn, seq) calls fcn(item) for item in sequence
#	seq must be an iterable (either list, tuple, or dictionary--will apply to keys)
#	returns a list
#	returns [] if seq empty

# reduce(fcn, seq) or reduce(fcn, seq, start) 
#	calls fcn on the first two items of seq, then on the result and next item, so on
#	fcn must be a binary fcn (takes in 2 args)
#	returns a single value
#		if seq has 1 item returns it. 
#		elif seq is empty, raises an exception or returns starting_val if specified

# define a func read that reads any exp (number, symbol, or nested list)

# read calls read_from on tokens obtained by tokenize

# 1. raise an error if the first token is ')'
# 2. non-parenthetical parens => interpret as int / float / symbol



