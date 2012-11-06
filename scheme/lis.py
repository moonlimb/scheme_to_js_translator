

# what is a literal
# what is a token
# what is an atom
# what is 

def eval(x, env=global_env):
	if isa(x, Symbol):			# variable reference
		return env.find(x)[x]
	elif not isa(x, list):		# constant literal
		return x
	elif x[0] == 'quote':		# (quote exp)
		(_, exp) = x
		return exp
