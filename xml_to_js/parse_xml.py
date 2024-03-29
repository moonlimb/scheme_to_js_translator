#from __future__ import print_function 
import xml.etree.ElementTree as ET
from sys import argv
import re
from js_ast import JsAST, FunctionDef, Expr, Stmt, PrintStmt, ReturnStmt, MathExpr, IfStmt, ElseStmt, ElseIfStmt
import logging
#from decorate import add_curly_braces

block_type={}

def get_children(node):
	return list(node)

#for nodes with single child
def get_only_child(node):
	return list(node)[0]

def get_descendants(node):
	return [e for e in node.iter()]

# all blocks have types: ex. procedures_defreturn, math_arithmetic, variables_get
def get_type(block): 
	return block.attrib['type']

def get_text(node):
	return node.text

def get_name(node):
	return node.attrib['name']

# get_var and get_num calls get_value
def get_value(block):
	title = list(block)[0]
	return title.text

#get_block_from_parent
def get_block(node):
	return get_only_child(node)

def construct_math_expr(operator, l_operand, r_operand):
	return MathExpr(operator, l_operand, r_operand)

def write_math(block):
	level_1 = get_children(block)
	operator = level_1[0].text	#ex. ADD
	level_2 = [get_block(node) for node in level_1[1:]]	#level_2 consists of block childs of value nodes
	result= [process_block(block) for block in level_2]	
	return construct_math_expr(operator, result[0], result[1])

# <mutation><arg name="x"></arg>
def get_args(mutation_node):
	args = [get_name(arg) for arg in get_children(mutation_node)]
	# args is a list of arguments (in string)
	return args

# <value name="RETURN"> <block..type="math_arithmetic"><title><value><value>
def get_return_stmt(node):
	if get_name(node)=='RETURN':
		math_expr = process_block(get_only_child(node))
		return ReturnStmt(math_expr)

def get_fn_name(title_node):
	return get_text(title_node) 

def process_stmt(node):
	return process_block(get_only_child(node))

# will need to reassign 'value': get_return_stmt for functions with no return statements

tags = {'mutation':get_args, 'title': get_fn_name, 'value': get_return_stmt, 'statement': process_stmt }
# create a helper fn for write_fn and write_no_return_fn
def write_fn(block):
	# how to write an elegant code for this part?
	nodes = get_children(block)
	args, fn_name, return_stmt = [tags[n.tag](n) for n in nodes] 	
	fn = FunctionDef(fn_name, args, return_stmt)
	return fn

def write_no_return_fn(block):
	nodes = get_children(block)
	args, fn_name, stmt = [tags[n.tag](n) for n in nodes]
	fn = FunctionDef(fn_name, args, stmt)
	return fn

def process_block_internal(node):
	return block_type[get_type(node)](node)

def make_print_stmt(block):
	children= get_only_child(block) 
	if children.tag == 'value':
		expr = process_block_internal(get_only_child(children))
		return PrintStmt(expr)

def process_stmt(stmt_block):
	block = stmt_block.get_only_child()	
	pass

def build_if(if_node, do_node):
	if if_node.attrib['name'] == 'IF0':
		return (process_controls(if_node), process_controls(do_node))
	else:
		return ElseIfStmt(process_controls(if_node), process_controls(do_node))

def build_else(control_node):
	return ElseStmt(process_controls(control_node))

def process_block(node):
	return block_type[get_type(node)](node)

def process_controls(parent_block):
	return process_block(get_only_child(parent_block))

def loop_for_each():
	pass

def loop_for():
	pass

def loop_while():
	pass


def build_control(stmts):
	condition = stmts[0][0]
	body = stmts[0][1]	
	elses = stmts[1:] if len(stmts)>1 else [""]
	return IfStmt(condition, body, elses)

# reverse() is O(n)
def write_controls(block):
	nodes = get_children(block)
	nodes.reverse() 
	stmts=[]
	while len(nodes) > 0:
		node = nodes.pop()
		if node.tag == 'value':
			stmts.append(build_if(node, nodes.pop()))
		elif node.tag == 'statement':
			stmts.append(build_else(node))
	return build_control(stmts)

def parse_xml(root):
	blocks = get_children(root)
	processed_blocks = [process_block(b) for b in blocks]	#map(process_block, blocks)
	return JsAST(processed_blocks)

def make_js_file():
	pass	
	# xml_file = raw_input('xml_filename >> ')
	# filename = re.search('([^.]+)\.xml', xml_file).group(1)                             # extracts the name of the xml file
	# js_file = filename + ".js"  # same name, js version                            
	# need to make a file with js_file
	#	process_xml()

def main():	
	script, xml_file = argv
	tree = ET.parse(xml_file)   # tree is ElementTree
	root = tree.getroot()		# root is Element
	js_code = parse_xml(root)	
	print(js_code)	

block_type = {"procedures_defreturn": write_fn, "procedures_defnoreturn": write_no_return_fn, "controls_if": write_controls, "text_print": make_print_stmt, "math_arithmetic": write_math, "logic_compare": write_math, "math_number": get_value, "variables_get": get_value, 'text': get_value, "controls_forEach": loop_for_each, "controls_for": loop_for, "controls_whileUntil": loop_while}

if __name__ == "__main__":
	main()
