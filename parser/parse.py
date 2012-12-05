from sys import argv
from js_ast import RecursiveFnCall, JsAST, Stmt, ReturnStmt, PrintStmt, IfStmt, ElseIfStmt, ElseStmt, Expr, ValueExpr, VarExpr, MathExpr, Function, Operator, IfElseStmt
import re
#use regular expression to distinguish float /int and strings
ops = ['+','*','-','=','<','>','>=','<=','eq?', 'equal?']

logic = ['and', 'or', 'not'] # are there more in Scheme?
FN_NAME='' # *******vim Note: CTRL + O takes to previous position ********* 
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

def make_expr(token):
	expr=''
	if isinstance(token, list):
		return write_js_from(token)
	try: return ValueExpr(token)
	except ValueError: # Variable is a Symbol 
		return VarExpr(str(token))	
"""
# (if <pred> <consq> <alt>)
def construct_else(stmt):
	if isinstance(stmt, list):
		return ElseStmt(write_js_from(stmt))
	else:
		return make_expr(stmt)
"""

def negate_var(operator, operand):
	return str(operator) + str(operand)

# op is an operator
# currently, only supports 1~2 operands
def construct_math(op, operands):
	if len(operands) == 1:
		assert op == '-'
		return VarExpr(negate_var(op, operands[0]))
	else:
		op, l_op, r_op =  [make_expr(op_part) for op_part in [op, operands[0], operands[1]]]
		return MathExpr(Operator(op), l_op, r_op)
# y if x else z
# (if x y z)
# predicate is any expr that evaluates top #f or #t
# special forms are keywords defined in Scheme
"""
if --> token in the nested_ls is a special form
elseif --> token in the nested_ls is a list
else --> token in the nested_ls is a VarExpr or ValueExpr
	# elt is an atom (int or Symbol)
	# determine whether valueExpr, VarExpr or String?
"""
def make_recursive_fn(elt,nested_ls):
	return RecursiveFnCall(elt, make_expr(write_js_from(nested_ls)))
def write_js_from(nested_ls):
	#print nested_ls	
	if not nested_ls:
		assert nested_ls == []
		return ""	
	if isinstance(nested_ls, str):
		return make_expr(nested_ls)
	if isinstance(nested_ls, list):
		elt = nested_ls.pop(0)
		if elt == FN_NAME:
			return make_recursive_fn(elt, nested_ls)
		if elt in ops:
			operands = nested_ls
			if elt == '=':
				return construct_math('==', operands)
			return construct_math(elt, operands)
		try:
			if special_form.get(elt): 
				return special_form[elt](nested_ls)
		except TypeError:
			pass				
		return make_expr(elt)
	return nested_ls

# (if (<pred>) (<body>) else_stmt))
def construct_if_else(nested_ls):
	pred, body, else_stmt= [write_js_from(elt) for elt in nested_ls]
	#else_stmt may be an expression 
	return construct_if_obj(pred, body, Expr(write_js_from(else_stmt)))

def construct_if_obj(pred, body, else_stmt):
	#assert isinstance(pred, MathExpr)
	return IfElseStmt(pred, Expr(ReturnStmt(body)), ElseStmt(ReturnStmt(else_stmt)))
	# predicate could also be a nested list
	# in such case predicate is write_js_from(elt.pop())

def write_fn_body(nested_ls, js_code, fn_def):
	pass

# works fine
def write_fn_def(nested_ls):
	fn_attrib = nested_ls.pop(0)
	name = fn_attrib[0]	
	params = fn_attrib[1:]
	body = [write_js_from(ls) for ls in nested_ls]	
	return Function(name, params,body) 
		
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
	try:	return int(token)
	except ValueError:
		try: return float(token)
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
	elif ')' == token: raise SyntaxError('unexpected ) while reading') 
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
special_form = {'define': write_fn_def, 'cond': construct_cond, 'if': construct_if_else} 

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
