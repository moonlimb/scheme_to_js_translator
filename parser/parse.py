from sys import argv
from js_ast import JsAST, Stmt, ReturnStmt, PrintStmt, IfStmt, ElseIfStmt, ElseStmt, Expr, ValueExpr, VarExpr, ArithExpr

op = ['+','-','<','>','>=','<=','eq?', 'equal?']
logic = ['and', 'or', 'not'] # are there more in Scheme?

# what is the difference b/w op.is_ and op.eq?
	# eq? : op.is_
	# equal?: op.eq

# keywords: cond, define, abs

#(if <predicate> <consequent> <alternative>)
# <p> is a predicate
# <e> consequent expr

"""
<note>		'() empty list --> don't split these

boolean literal: #t, #f
integer literal: 3/ -3
string literal: "hello()"
"""

# use decorator
# use regex? 
# boolean variables to keep in track: is_string is_list	
# redefine a split function 		

special_form = {}

# converts any function in Scheme to equivalent string expr in JS

# (else <Stmt>) --> else { return <Stmt>; } 
# (if (<pred>) (<do_stmt>) alt_stmt)) 
		# --> if (<pred>){return <do_stmt>;} 
		#	  else { return alt_stmt ;}
		#return atom(tokens[pos]), pos+1

# send predicate to read_from 
# send expr to read_from
def construct_cond(tokens, pos):
	pass

# (if <pred> <consq> <alt>)
def construct_if(tokens, pos):
	pass	

def construct_else():
	pass

# (if (<pred>) (<body>) else_stmt))

# y if x else z
# (if x y z)
# predicate is any expr that evaluates top #f or #t
def predicate(op, l_op, r_op):
	return ArithExpr(op, l_op, r_op)

def construct_if_else(tokens, pos):
	pass
	"""l_op, pos = read_from(tokens, pos+1)
	r_op, pos = read_from(tokens, pos)
	op = tokens[0]
	l_op = Stmt(l_op) if isinstance(l_op, list) else atom(l_op)
	r_op = Stmt(r_op) if isinstance(r_op, list) else atom(r_op)
	return MathExpr(op, l_op, r_op)
"""

# updates pos by 1 and returns the new corresponding token
def get_next_token(tokens, pos):
	return tokens[pos+1], pos+1	# pos+1 is the new_pos
	
# cond ((predicate) expr)
#	predicate) expr
"""
def get_expr(tokens, pos):
	expr = []
	while token != ')':		# 	append predicate to pred 
		expr.append(token)
		token, pos = get_next_token(tokens, pos)
	return expr
"""
# all () after cond is if_do pair
def write_cond(tokens):
	pass
"""
	token = tokens[pos+2]	# token --> predicate 
	pred = get_expr(tokens)
	do_stmt = read_from(get_expr(tokens))
	while token != ')':
		do_stmt.append(token)
		token = get_next_token(tokens)
	return construct_if(pred, do_stmt) 
"""
#iterative: build_cond(tokens, pos)

def write_fn(tokens):
	pass
	# call get_expr function	
	# name, args (list), stmt
	# (define (<name> <params>)
		# <stmt>)	

def write_js_from(AST):
	node = AST.pop()
	pass

	# define --> function{}
		# name, args, stmts
		# name = abs
		# args x
		# stmts
		# if ( x < 0):
		# 	return -x
		# else:
		# 	return x
	# abs --> ValueExpr
	#  x--> VarExpr
	# if --> IfStmt / ElseStmt
	# CondStmts

""" 
	node = AST[0] 
	if len(AST) == 0:
		print "unexpected end of code while reading"
    elif '(' == node:
        L = [] 
        while tokens[0] != ')': 
            L.append(read_from(tokens)) 
        tokens.pop(0)   # pop off ')' 
        return L 
    elif ')' == token: 
        raise SyntaxError('unexpected ) while reading') 
    else: 
        return atom(token) 
"""	

def write_js(AST):
	#js_code = write_js_from(AST)	
	js_code = "Scheme to JS translation success!"
	return js_code

# atom integer / letters/ combination of both and special char / ()
def atom(token):
	# Norvig Style: "Numbers become numbers. Every other token is a symbol." 
	Symbol = str
	try:	return float(token)
	except ValueError:
		return Symbol(token)	#token is a Symbol

# return tokens with ( replaced by [ and ) by ]		
# base case: reached ) --> close the list and return to outer list
def read_from(tokens):
	pass
"""
	if len(tokens) == 0: 
		raise SyntaxError('unexpected EOF while reading') # EOF = end of file
token = tokens.pop() 
if '(' == token: 
L = [] 
while tokens[-1] != ')': 
	L.append(read_from(tokens)) 
tokens.pop()   # pop off ')' 
return L 
elif ')' == token: 
raise SyntaxError('unexpected ) while reading') 
else: 
return atom(token) 
"""		 
def read(tokens):
	# create a nested list structure from a list of tokens
	return read_from(tokens)

def tokenize(s):
	# convert a string into a list of tokens
	return s.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(s):
	tokens = tokenize(s)
	tokens.reverse()
	# reverse tokens to pop from the end 
	return read(tokens)
	
# reverse a list O(n)
# pop()	O(1) vs. pop(n) O(n)

# dictionary that maps from special_forms in Scheme to functions that will construct JS equivalents
special_form = {'define': write_fn, 'cond': write_cond, 'else': construct_else, 'if': construct_if_else}

def read_file(file):
	f = open(file)
	f_str = f.read()
	f.close()
	return f_str

def main():
	script, file_name = argv
	f = read_file(file_name)
	AST = parse(f)
	print write_js(AST)

if __name__ == '__main__':
	main()	
