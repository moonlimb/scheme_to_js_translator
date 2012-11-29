class Env(dict):
	"An environment: a dict of {'var': val} pairs, with an outer Env"

	def __init__(self, params = (), args=(), outer=None):
		self.update(zip(params, args))
		self.outer = outer
	def find(self, var):
		"Find the innermost Env where var appears."
		return self if var in self else self.outer.find(var)
	

