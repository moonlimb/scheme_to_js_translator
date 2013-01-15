from operators import basic
tab, tab2 = "    ", "        "

class JsAST(object):
	# code is a list of different parts of the code
	def __init__(self, code):
		self.code = code
	def __str__(self):
		str_code = [str(chunk) for chunk in self.code]
		return '\n'.join(str_code)

# Expression is a combination of values, variables, operators, and function calls
class Expr(object):
	def __init__(self, expr):
		self.expr = expr 
	def __str__(self):
		return '%s' %self.expr

# ex. if (stmt)
# Statement is an instruction Python interpreter can execute
class Stmt(object):
	def __init__(self, stmt):
		self.stmt = stmt
	def __str__(self):
		return "%s" %str(self.stmt)

class ValueExpr(Expr):
	def __init__(self, value):
		self.value = value

class VarExpr(Expr):
	def __init__(self, name):
		self.name = name	
	def __str__(self):
		return '%s' %str(self.name)
"""
class DeclarationStmt(Stmt):
	def __init__(self, var_expr): 
		self.var_expr = var_expr
	def __str__(self):
		return 'var %s;' %str(self.var_expr)

class AssignmentStmt(Stmt)
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

# should ElseIfStmt inherit from object or Statement?
class ElseIfStmt(object):
	def __init__(self, cond, stmt):
		self.cond = cond
		self.stmt = stmt
	def __str__(self):
		return "else if (%s) {\n%s%s \n};" %(str(self.cond), tab2, str(self.stmt))

class ElseStmt(Stmt):
	def __str__(self):
		return "else {\n    %s \n};" %(str(self.stmt))

class IfStmt(object):
	def __init__(self, cond, body, elses):
		self.cond = cond	# cond is expression
		self.body = body	# body is if statement's body 
		self.elses = elses 	#list of elseif and else stmts	
	def __str__(self):
		if self.elses:
			return "if (%s) {\n%s%s\n}; %s" %(str(self.cond), tab, str(self.body),' '.join([str(else_if) for else_if in self.elses]))

class BreakStmt(Stmt):
	def __init__(self):
		self.stmt = "break;"

class ContinueStmt(Stmt):
	def __init__(self):
		self.stmt = "continue;"

# loop constructions
class ForLoop(object):
	def __init__(self, init, cond, incr, body): 
		self.init= init
		self.cond = cond
		self.incr = incr	# may be an increment or decrement	
		self.body = body
	def __str__(self):
		return "for (%s; %s; %s) {\n%s%s;\n}" %(str(self.init), str(self.cond), str(self.incr), tab, str(self.body))

class ForEachLoop(object):
	def __init__(self, index, iterable, body):
		self.index = index
		self.iterable = iterable	
		self.body = body
	def __str__(self):
		return "for (var %s in %s) {\n%s%s\n}" %(str(self.index), str(self.iterable), tab, str(self.body))
		
class WhileLoop(object):
	def __init__(self, cond, body):
		self.cond = cond
		self.body = body	#body is stmt
	def __str__(self):
		return "while (%s) {\n%s%s\n}" %(str(self.cond), tab, str(self.body))

class FunctionDef(object):
	def __init__(self, name, args, stmt):
		self.name = name
		self.args = args	#args is a list
		self.stmt = stmt
	def __str__(self):
		param = ', '.join(self.args)
		return "function %s(%s) {\n%s%s \n}" %(str(self.name), param, tab, str(self.stmt))

class MathExpr(object):
	# operand could be variables or expressions
	def __init__(self, operator, left_operand, right_operand):
		self.operator = operator
		self.left_operand = left_operand
		self.right_operand = right_operand
	def __str__(self):	
		return str(self.left_operand) + basic[self.operator] + str(self.right_operand)

# use decorators to add wrapper to expr? 
class PrintStmt(Stmt):
	def __str__(self):
		return "console.log('" + str(self.stmt) + "');"
	
class ReturnStmt(Stmt):
	def __str__(self):
		return "return " + str(self.stmt) + ";"
