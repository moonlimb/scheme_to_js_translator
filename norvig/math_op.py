def add_globals(env):
	"Add some Scheme standard procedures to an environment"
	import math
	import operator as op
	isa= isinstance
	# ininstance(object, classinfo) return bool		
	Symbol = str
	#str is object
#	env.update(vars(math)) #sin, sqrt, ...
#	env.update(	

	{'+':op.add, '-':op.sub, '*':op.mul, '/':op.div, 'not':op.not_,
	'>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 'equal?':op.eq, 
	'eq?':op.is_, 'length':len, 'cons':lambda x,y:[x]+y, 'car': lambda x:x[0], 
	'cdr':lambda x:x[1:], 'append':op.add, 'list':lambda *x:list(x), 
	'list?': lambda x:isa(x,list), 'null?':lambda x:x==[], 
	'symbol?':lambda x: isa(x, Symbol) }
#)
#global_env = add_globals(Env())

""" (cons exp1 exp2)	returns the combined list of exp1 and exp2
					converts exp1 to list; exp2 must be a list
	(car exp)	returns the first element of a list
	   	   		exp must be a list
	(cdr exp)	returns the rest of the list excluding the first element
				if the list has only 1 element, returns empty list
				if the list empty, raises an error
				exp must be a list
	(append exp1 exp2)	takes 2+ lists and constructs a new list
						arguments must be a list
	(list *exp)	constructs a list of all *exp
	(list? exp)	returns #f or #t; evaluates wheter exp is a list
				must have only 1 arg
	(null? exp)	returns #t if exp is an empty list, #f otherwise
				exp must be a list
"""


