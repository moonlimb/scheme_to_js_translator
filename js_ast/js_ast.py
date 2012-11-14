from operators import basic

"""
class JavascriptAST:
	def __init__(self)

"""
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
class JsAST:
	def __init__(self, code):
		self.code = code 
	def __str__(self):
		return '\n'.join(self.code)

class FunctionDef(object):
	def __init__(self, name, args, return_stmt):
		self.name = name
		self.args = args	#args is a list
		self.return_stmt = return_stmt
	def __str__(self):
		param = ', '.join(self.args)
		return "function " + self.name + '(' + param + ')' + ' {\n    ' + str(self.return_stmt) +'\n}'	

class Expr(object):
	# operand could be variables or expressions
	def __init__(self, operator, left_operand, right_operand):
		self.operator= operator
		self.left_operand=left_operand
		self.right_operand=right_operand
	def __str__(self):	
		return str(self.left_operand) + basic[self.operator] + str(self.right_operand)

class ReturnStmt(object):
	def __init__(self, expr):
		self.expr = expr
	def __str__(self):
		return "return " + str(self.expr) + ";"
