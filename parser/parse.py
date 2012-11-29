op = [] # may not be necssary
# WED, 28 NOV
# Objective: Parse 'cond' and 'if' expressions in Scheme to JS

# keywords: cond, define, abs

#(if <predicate> <consequent> <alternative>)
# <p> is a predicate
# <e> consequent expr

#and or not

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

""" condition = stmts[0][0] 
    body = stmts[0][1]   
    elses = stmts[1:] if len(stmts)>1 else [""] 
    return IfStmt(condition, body, elses) 

def write_controls(block): 
   nodes = get_children(block) 
    nodes.reverse()  
    stmts=[] 
    while len(nodes) > 0: 
        node = nodes.pop() 
        if node.tag == 'value': 
            stmts.append(build_if(node, nodes.pop())) 
        elif node.tag == 'statement': 
            stmts.append(build_else(node)) 
    return build_control(stmts) 

"""

special_form = {}

def tokenize(s):
	return s.replace('(', ' ( ').replace(')', ' ) ').split()
# converts any function in Scheme to equivalent string expr in JS

# (else <Stmt>) --> else { return <Stmt>; } 
# (if (<pred>) (<do_stmt>) alt_stmt)) 
		# --> if (<pred>){return <do_stmt>;} 
		#	  else { return alt_stmt ;}

def read_from(tokens, pos):
	token = tokens[pos]		# token is a current token
	if len(tokens) == 0:
		return "EOF"	# norvig raises an EOF error here 
	if token == '(':
		L=[]	
		while tokens[pos] != ')':
			pos += 1
			L.append(read_from(tokens, pos))
		pos += 1	# move past )
		return L	
	elif token == ')':
		pass # raise error
	elif special_form.get(token):	# token is a special form
		return special_form[token](tokens, pos)
	else:	# token is an atom
		return atom(token[pos])

def write_math():
	pass

# predicate is any expr that evaluates top #f or #t
def predicate(expr):
	op = expr[0]
	if len(expr) == 3:
		return MathExpr(op, expr[1], expr[2])
	else:
		read_from(expr, 1)	
	return MathExpr(expr[0], 

# send predicate to read_from 
# send expr to read_from
def construct_cond(tokens, pos):
	pass
	# must construct

# (if <pred> <consq> <alt>)
def construct_if(tokens, pos):
	pass	

def construct_else():
	pass

# (if (<pred>) (<body>) else_stmt))

def construct_if_else():
	pass
# updates pos by 1 and returns the new corresponding token
def get_next_token(tokens, pos):
	new_pos = pos + 1
	return tokens[new_pos], new_pos
	
# cond ((predicate) expr)
#	predicate) expr
def get_expr(tokens, pos):
	expr = []
	while token != ')':		# 	append predicate to pred 
		expr.append(token)
		token, pos = get_next_token(tokens, pos)
	return expr, pos+1

# all () after cond is if_do pair
def write_cond(tokens, pos):
	token = tokens[pos+2]	# token --> predicate 
	pred, pos = get_expr(tokens, pos)
	do_stmt = read_from(get_expr(tokens))
	while token != ')':
		do_stmt.append(token)
		token, pos = get_next_token(tokens, pos)
	construct_if(pred, do_stmt)		
	
return construct_if(pred, do_expr) 

#iterative: build_cond(tokens, pos)

def write_fn(tokens, pos):
	pass
	# call get_expr function	
	# name, args (list), stmt
	# (define (<name> <params>)
		# <stmt>)	
		
# int or string
def atom(token):
	token = tokens[pos]
	if isinstance(token, int) or isinstance(token, float):
		return float(token):
	if isinstance(token, str): 	#str is a Symbol
		return token
"""
Norvig Style:"Numbers become numbers. Every other token is a symbol." 
    try: return int(token) 
    except ValueError: 
        try: return float(token) 
        except ValueError: 
            return Symbol(token)
"""
	
def read(s):
	return read_from(tokenize(s), 0)

def parse(s):
	print read(tokenize(s))

special_form = {'define': write_fn, 'cond': write_cond, 'else': construct_else, 'if': construct_if_else}
