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
	print tokens, pos
	token = tokens[pos]		# token is a current token
	if len(tokens) == 0:
		raise "unexpected EOF while reading"	# copied from Norvig	
		# EOF = end of file
	if token == '(':
		L=[]
		print "printing L:%r and token:%r" %(L, token)
		while tokens[pos] != ')':
			print "hello"
			(ls, pos)= read_from(tokens, pos+1)
			L.append(ls)
			return L
		print L, pos+1		# pos skips that of )
	elif token == ')':
		raise SyntaxError("unexpected \) while reading")	# copied from Norvig
	elif special_form.get(token):	# token is a special form
		return special_form[token](tokens, pos), pos
	elif token in op:
		print "current_token: %s" %token
		l_op, current_pos = read_from(tokens, pos+1)
		predicate()	
		print "current_token: %s" %l_op
		#r_op, pos = atom(tokens[pos], current_pos+1)	
	# l_op and r_op may be a list or a str
	else:	# token is an atom
		print "i am an atom: %r" %(token)
		return atom(token), pos+1
"""
		#return atom(tokens[pos]), pos+1
l_op, pos= read_from(tokens, pos+1)
		r_op, pos= read_from(tokens, pos)
		print l_op, r_op
		print predicate(token, l_op, r_op), pos"""
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

# y if x else z
# (if x y z)
# predicate is any expr that evaluates top #f or #t
def predicate(op, l_op, r_op):
	pass	

def construct_if_else(tokens, pos):
#	l_op, pos = read_from(tokens, pos+1)
#	r_op, pos = read_from(tokens, pos)
	op = tokens[0]
	l_op = Stmt(l_op) if isinstance(l_op, list) else atom(l_op)
	r_op = Stmt(r_op) if isinstance(r_op, list) else atom(r_op)
	return MathExpr(op, l_op, r_op)


# updates pos by 1 and returns the new corresponding token
def get_next_token(tokens, pos):
	return tokens[pos+1], pos+1	# pos+1 is the new_pos
	
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
	return construct_if(pred, do_stmt) 

#iterative: build_cond(tokens, pos)

def write_fn(tokens, pos):
	pass
	# call get_expr function	
	# name, args (list), stmt
	# (define (<name> <params>)
		# <stmt>)	
		
# int or string
def atom(token):
	if isinstance(token, int) or isinstance(token, float):
		return float(token)
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
	
def read(tokens):
	return read_from(tokens, 0)

def parse(s):
	tokens = tokenize(s)
	print tokens, len(tokens)
	js_code, final_pos = read(tokens)
	assert final_pos == len(tokens)-1		 
	print final_pos

special_form = {'define': write_fn, 'cond': write_cond, 'else': construct_else, 'if': construct_if_else}
