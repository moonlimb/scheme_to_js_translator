from operators import basic

"""
	@add_curly_braces
	def get_function_body(op_token, args):
		operator = op.basic[op_token]
		body = operator.join(args)
		return body	
	       
	# element's children are argument nodes 
	# ex. <arg name = "x"/>
	def make_params(parent_of_args):
    	args = [arg.attrib['name'] for arg in list(parent_of_args)]
    	return '('+ ", ".join(args) + ')'
	
"""
class JsAST(object):
	# code is a list of different parts of the code
	def __init__(self, code):
		self.code = code
	def __str__(self):
		str_code = [str(chunk) for chunk in self.code]
		return '\n\n'.join(str_code)

class Assignment(object):
	def __init__(self, var_name, value, is_declar):
		self.var_name = var_name
		self.value = value
		self.is_declar = is_declar
	def __str__(self):
		assignment = '%s = %value' %(self.var_name, self.value) 
		if self.is_declar:
			return 'var %s' %assignment 
		else:
			return assignment

class Declaration(object):
	def __init__(self, var_name): 
		self.var_name = var_name
	def __str__(self):
		return 'var %s;' %self.var_name

class Stmt(object):
	def __init__(self, expr):
		self.expr = expr
	
class IfStmt(object):
	def __init__(self, if_type, condition, stmt):
		self.if_type= if_type
		self.condition = condition
		self.stmt = stmt
	def __str__(self):
		return "%s (%s) {\n%s\n}" %(self.if_type, self.condition, self.stmt)

class ElseIf(object):
	def __init__(self, ls_else_if):
		self.ls_else_if = ls_else_if
	def __str__(self):
		return ' '.join[ls_else_if]

class ElseStmt(Stmt):
	def __str__(self):
		return "else {\n%s\n}" %s(self.expr)
	
# write a decorator for condition: '(' cond ')'
# write a decorator for stmt: '{' and '}'
class Conditional(object):
	def __init__(self, if_stmt, else_stmt):
		self.if_stmt= if_stmt
		self.else_if_ls = else_if_ls
		self.else_stmt = else_stmt
	def __str__(self):
		return "%s%s %s" %(str(if_stmt), str(ls_else_if), str(else_stmt))

class FunctionDef(object):
	def __init__(self, name, args, stmt):
		self.name = name
		self.args = args	#args is a list
		self.stmt = stmt
	def __str__(self):
		param = ', '.join(self.args)
		return "function " + self.name + '(' + param + ')' + ' {\n    ' + str(self.stmt) +'\n}'	

class MathExpr(object):
	# operand could be variables or expressions
	def __init__(self, operator, left_operand, right_operand):
		self.operator= operator
		self.left_operand=left_operand
		self.right_operand=right_operand
	def __str__(self):	
		return str(self.left_operand) + basic[self.operator] + str(self.right_operand)

# use decorators to add wrapper to expr? 
class PrintStmt(Stmt):
	def __str__(self):
		return "    console.log('" + str(self.expr) + "');"
	
class ReturnStmt(Stmt):
	def __str__(self):
		return "return " + str(self.expr) + ";"
