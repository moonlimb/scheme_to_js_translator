from sys import argv
from js_ast import JsAST, Stmt, ReturnStmt, PrintStmt, IfStmt, ElseIfStmt, ElseStmt, Expr, ValueExpr, VarExpr, ArithExpr, Function

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
def construct_cond(tokens):
	pass

# (if <pred> <consq> <alt>)
def construct_else(stmt):
	if isinstance(stmt, list):
		return ElseStmt(write_js_from(stmt))
	else:
		try: return ValueExpr(float(token))
		except ValueError: # Variable is a Symbol 
			return VariableExpr(str(token))	

def negate_var(op, r_op):
	assert op == '-'
	return str(op) + str(r_op)
	
def construct_math(op, l_op, r_op):
	if not l_op:
		return VarExpr(negate_var(op, r_op)) 
	return ArithExpr(op, l_op, r_op)

# y if x else z
# (if x y z)
# predicate is any expr that evaluates top #f or #t
# special forms are keywords defined in Scheme
"""
if --> token in the nested_ls is a special form
elseif --> token in the nested_ls is a list
else --> token in the nested_ls is a VarExpr or ValueExpr
"""

def write_js_from(nested_ls):
	if not nested_ls:
		assert nested_ls == []
		return ""	
	elt = nested_ls.pop(0)
	# print elt
	#if isinstance(elt, list):
	#	js_code.append(write_js_from(nested_ls))
	try:
		if special_form.get(elt): 
			return special_form[elt](nested_ls)
	except TypeError:
		# elt is an atom (int or Symbol)
		# determine whether valueExpr, VarExpr or String?
		return Expr(elt) 
	return nested_ls

# (if (<pred>) (<body>) else_stmt))
def construct_if_else(nested_ls):
	print [write_js_from(elt) for elt in nested_ls]
def construct_if_obj():
	# predicate could also be a nested list
	# in such case predicate is write_js_from(elt.pop())
	predicate = construct_math(pred_ls)
	body = write_js_from(body_ls)
	else_stmt = construct_else(else_ls)
#	print  IfStmt(predicate, body, [else_stmt])
	return IfStmt(predicate, body, [else_stmt])

def write_fn_body(nested_ls, js_code, fn_def):
	pass

# works fine
def write_fn_def(nested_ls):
	fn_attrib = nested_ls.pop(0)
	name = fn_attrib[0]	
	params = fn_attrib[1:]
	stmt = [write_js_from(elt) for elt in nested_ls]
	print stmt
	return Function(name, params, stmt)
		
	# call get_expr function	
	# name, args (list), stmt
	# (define (<name> <params>)
		# <stmt>	

def write_js(nested_lists):
	js_code=[]
	return write_js_from(nested_lists)

# atom integer / letters/ combination of both and special char / ()
# modify atom so that atom becomes VarExpr, ValueExpr, String
def atom(token):
	# Norvig Style: "Numbers become numbers. Every other token is a symbol." 
	Symbol = str
	try:	return float(token)
	except ValueError:
		return Symbol(token)	#token is a Symbol

# return tokens with ( replaced by [ and ) by ]		
# base case: reached ) --> close the list and return to outer list
def read_from(tokens):
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

# create a nested list structure from a list of tokens
def read(tokens):
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
special_form = {'define': write_fn_def, 'cond': construct_cond, 'else': construct_else, 'if': construct_if_else}

def read_file(file):
	f = open(file)
	f_str = f.read()
	f.close()
	return f_str

def main():
	script, file_name = argv
	f = read_file(file_name)
	nested_lists = parse(f)  # nested_lists is Scheme AST
	print write_js(nested_lists)

if __name__ == '__main__':
	main()	
