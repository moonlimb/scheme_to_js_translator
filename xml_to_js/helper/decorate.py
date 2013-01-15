# file containing decorator / helper functions
# Q: Use decorators/wrapper function to add curly braces?


def make_fcn(fn):
	def wrapper():
		return fn() + "()"
	return wrapper

def add_parens(fn):
	def wrapper():
		return "(" + fn() + ")"
	return wrapper

def add_curly_braces(content):
	def wrapper():
		return "{" + content + "; }"
	return wrapper

#keywords=['function', 'if', 'for']
"""
content_test= "function content"
@add_curly_braces
def decorator_test():
	return content_test

loop_cond_test = "i=0; i<=10; i++"
@add_parens
def paren_test():
	return loop_cond_test

fcn_name='square'
@make_fcn
def call_function():
	return fcn_name
print decorator_test()
print paren_test()
print call_function()
"""
