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
		return '\n'.join(str_code)

# Expression is a combination of values, variables, operators, and function calls
class Expression(object):
	def __init__(self, expr):
		self.expr = expr 
	def __str__(self):
		return '%s' %self.expr

# ex. if (stmt)
# Statement is an instruction Python interpreter can execute
class Statement(object):
	def __init__(self, stmt):
		self.stmt = stmt
	def __str__(self):
		return "%s" %self.stmt

class ValueExpr(Expression):
	def __init__(self, value):
		self.value = value

class VariableExpr(Expression):
	def __init__(self, name):
		self.name = name	

"""
class DeclarationStmt(Statement):
	def __init__(self, var_expr): 
		self.var_expr = var_expr
	def __str__(self):
		return 'var %s;' %str(self.var_expr)

class AssignmentStmt(Statement)
	def __init__(self, var_expr, value, is_declaration):
		self.var_expr = var_expr
		self.value = value
		self.is_declar = is_declar
	def __str__(self):
		assignment = '%s = %value' %(self.var_expr, self.value) 
		if self.is_declaration:
			return 'var %s' %assignment 
		else:
			return assignment
"""

class ElseIfStmt(Statement):
	def __init__(self, cond, stmt):
		self.cond = cond
		self.stmt = stmt
	def __str__(self):
		return """else if (%s) {
       %s
   };""" %(str(self.cond), str(self.stmt))

class ElseStmt(Statement):
	def __str__(self):
		return """else {
       %s
   }; %(str(self.expr))
"""

class IfStmt(object):
	def __init__(self, cond, body, elses):
		self.cond = cond	# cond is expression
		self.body = body	# body is if statement's body 
		self.elses = elses 	#list of elseif and else stmts	
	def __str__(self):
		return """if (%s) {
       %s
   } %s %s 
""" %(self.cond, ' '.join([str(else_if) for else_if in self.elses]), str(self.body))

class FunctionDef(object):
	def __init__(self, name, args, stmt):
		self.name = name
		self.args = args	#args is a list
		self.stmt = stmt
	def __str__(self):
		param = ', '.join(self.args)
		return "function " + str(self.name) + '(' + param + ')' + ' {\n    ' + str(self.stmt) +'\n}'	

class MathExpr(object):
	# operand could be variables or expressions
	def __init__(self, operator, left_operand, right_operand):
		self.operator = operator
		self.left_operand = left_operand
		self.right_operand = right_operand
	def __str__(self):	
		return str(self.left_operand) + basic[self.operator] + str(self.right_operand)

# use decorators to add wrapper to expr? 
class PrintStmt(Statement):
	def __str__(self):
		return "console.log('" + str(self.stmt) + "');"
	
class ReturnStmt(Statement):
	def __str__(self):
		return "return " + str(super(Statement,expr)) + ";"
