"""
class JavascriptAST:
	def __init__(self)
"""

class FunctionDef(object):
	def __init__(self, name, args, return_stmt):
		self.name = name
		self.args = args	#args is a list
		self.return_stmt = return_stmt
	def __str__(self):
		param = ', '.join(self.args)
		return "function " + self.name + '(' + param + ')' + ' {\n    ' + str(self.return_stmt) +'\n}'	

class AddExpr(object):
	# operand could be variables or expressions
	def __init__(self, left_operand, right_operand):
		self.left_operand=left_operand
		self.right_operand=right_operand
	def __str__(self):
		return str(self.left_operand) + ' + ' + str(self.right_operand)

class ReturnStmt(object):
	def __init__(self, expr):
		self.expr = expr
	def __str__(self):
		return "return " + str(self.expr) + ";"
