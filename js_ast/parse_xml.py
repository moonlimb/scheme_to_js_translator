#from __future__ import print_function 
import xml.etree.ElementTree as ET
from sys import argv
import re
from js_ast import JsAST, FunctionDef, Stmt, PrintStmt, ReturnStmt, MathExpr, IfStmt, ElseStmt, ElseIf, Conditional
import logging
#from decorate import add_curly_braces

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

def get_block_from_value(node):
	return get_children(node)[0]

def write_math(block):
	level_1 = get_children(block)
	operator = level_1[0].text	#ex. ADD
	# may need to check for the title name of the operator
	
	#level_2 consists of block childs of value nodes
	level_2 = [get_block_from_value(node) for node in level_1[1:]]
	result= [process_block(block) for block in level_2]	
	return operator, result[0], result[1]

# <mutation><arg name="x"></arg>
def get_args(mutation_node):
	args = [get_name(arg) for arg in get_children(mutation_node)]
	# args is a list of arguments (in string)
	return args

# <value name="RETURN"> <block..type="math_arithmetic"><title><value><value>
def get_return_stmt(node):
	if get_name(node)=='RETURN':
		operator, left_operand, right_operand = process_block(get_only_child(node))
		math_expr = MathExpr(operator, left_operand, right_operand)
		return ReturnStmt(math_expr)

def get_print_stmt(node):
	if get_name(node) == ' ':
		pass		

def get_fn_name(title_node):
	return get_text(title_node) 

#fix this statement!!
def process_stmt(node):
	process_block(get_only_child(node))
	print "processing stmt"

#return process_block(get_only_child(node))
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

def text_print(block):
	block.get_children()	
	print_stmt = PrintStmt()	
# write a function to combine blocks together
	
block_type = {"procedures_defreturn": write_fn, "procedures_defnoreturn": write_no_return_fn, "controls_if": write_controls, "text_print": get_print_stmt, "math_arithmetic": write_math, "logic_compare": write_math, "math_number": get_value, "variables_get": get_value, 'text': get_value} 

def process_block(node):
	return block_type[get_type(node)](node)

def construct_if(condi):
	pass
	
def write_controls(block):
	children = get_children(block)    
	first_node = children[0]
	elseif_count, else_count = 0,0
	if first_node.tag == 'mutation':
		else_count = first_node.attrib.get('else',0)
		elseif_count = first_node.attrib.get('elseif',0)	
		print "else_count is %s" %else_count
	print "elseif_count is $s" %elseif_count		
		
"""
	if first_node.tag == 'mutation':
		else_count = first_node.attrib.get('else',0)
		elseif_count = first_node.attrib.get('elseif',0)	
	cond=[]
for n in xrange(0,2*(elseif_count+1)),2):
		if_stmt = get_only_child(children[n])
		stmt = get_only_child(children[n+1])		
	"""	
	
#Conditional(if_stmt, else_stmt)	
#	print "need to process if statement"

def process_block(node):
	return block_type[get_type(node)](node)

def parse_xml(root):
	blocks = get_children(root)
	print blocks
	processed_blocks = [process_block(b) for b in blocks]
	print processed_blocks	
# alt: processed_blocks = map(process_block, blocks)
	#print "parsed xml. yay!"
	return JsAST(processed_blocks)

# return tag_to_function.get(root.tag)(child)
# tag_to_function = {'xml': parse_xml, 'block': process_block}

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

if __name__ == "__main__":
	main()
