

# what is a literal
# what is a token
# what is an atom

#where is exp defined?

def eval(x, env=global_env):
	if isa(x, Symbol):			# variable reference
		return env.find(x)[x]
	elif not isa(x, list):		# constant literal
		return x
	elif x[0] == 'quote':		# (quote exp)
		(_, exp) = x
		return exp
#****resume here
	elif x[0] == 'if': 			# (if test conseq alt)
		(_, test, conseq, alt) = x
		return eval((conseq if eval(test,env) else alt), env)
		# deconstruct the above statement

	elif x[0] == 'set!'			# (set! var exp)
		(_, var, exp) =x
		env[var] = eval(exp, env)
	elif x[0] == 'lambda':		# (lambda (var*) exp)
		(_, vars, exp) = x)
		return lambda *args: eval(exp, Env(vars, args, env))
	elif x[0] == 'begin':		# (begin exp*)
		for exp in x[1:]:
			val = eval(exp, env)
		return val
	else:						# ([rpc exp*)
		exps = [eval(exp, env) for exp in x]
		proc = exps.pop(0)
		return proc(*exps)

isa = isinstance 	# isinstance(object, class)	returns True/False
Symbol = str		#symbol is a string of chars, may include '-'	

