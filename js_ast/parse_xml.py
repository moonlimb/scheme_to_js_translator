import xml.etree.ElementTree as ET
from sys import argv
import re
from js_ast import JsAST, FunctionDef, ReturnStmt, AddExpr
import operator as op
#from __future__ import 

#op.basic is a dictionary of basic operators
#from decorate import add_curly_braces

script, xml_file = argv
#python parse_xml.py filename.xml:
#xml_file = raw_input('xml_filename >> ')

filename = re.search('([^.]+)\.xml', xml_file).group(1)	
# extracts the name of the xml file

js_file = filename + ".js"	# same name, js version
# js_file.write('hello')
# need to make a file with js_file

tree = ET.parse(xml_file)	# tree is ElementTree

def get_children(node):
	return list(node)

def get_descendants(node):
	return [e for e in node.iter()]

# all blocks have types: ex. procedures_defreturn, math_arithmetic, variables_get
def get_type(block): 
	return block.attrib['type']

def get_text(node):
	return node.text

def get_name_att(node):
	return node.attrib['name']
	
# given a single element, return its name and text pair
def get_name_text_pair(el):
	return (el.tag, el.text, el.items())

"""Element
<tag name="value" name2="value2">text</tag>
el.tag - tag 
el.text - gets the text content in/bw the tags
el.items() - el's attributes as a seq of (name, value) pairs; 
	not in order
"""

def return_empty_str(el):
	return ""

def get_var(block):
	# <block type="variables_get">
	#  <title name="VAR">x</title>
	# </block>
	title = list(block)[0]	# may not be true all the time
	return title.text	
	
# prefix calculator format
def write_math(block):
	#	<block type="math_arithmetic" inline="true">
	#	  <title name="OP">ADD</title>
	#	  <value name = "A">
	#	    <block type="variables_get">
	#	  <value name = "B">
	#		...
	bl_level_1 = get_children(block)
	operator = op.basic[bl_level_1[0].text]
	
	# may need to check for the title name of the operator

	# bl_level_2 is block types of value blocks
	bl_level_2 = [list(child)[0] for child in bl_level_1[1:]]
	result = [map(process_block, bl_level_2)]	
	#return operator, result
	return "operator %s, result %s" %s(operator, " ".join(result))

# <mutation><arg name="x"></arg>
def get_args(mutation_node):
	args = [get_name_att(arg) for arg in get_children(mutation_node)]
	# args is a list of arguments (in string)
	return args

def get_return_stmt(node):
	pass
	
def get_fn_name(title_node):
	return get_text(title_node) 

tags = {'mutation':get_args, 'title': get_fn_name, 'value': get_return_stmt}
def write_fn(block):
	# how to write an elegant code for this part?
	nodes = get_children(block)
	args, fn_name, return_stmt = [tags[n.tag](n) for n in nodes] 	
	print args, fn_name, return_stmt

# receives a fnc block as input
	# makes js_ast class objects
	# return a js_representation 

#	blocks = get_children(root)
#def write_block(block):
#	pass
# expression
# argument
# function name
# left operand
# right operand

# write a function to combine blocks together

block_type = {"procedures_defreturn": write_fn, "math_arithmetic": write_math, 
"variables_get": get_var} 

def process_block(node):
	print node
	print get_type(node)
	print block_type[get_type(node)]
	return block_type[get_type(node)](node)

def parse_xml(root):
	blocks = get_children(root)
	processed_blocks = [process_block(b) for b in blocks]
	# alt: processed_blocks = map(process_block, blocks)
	# return JsAST(processed_blocks)
	return "parsed xml"

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
	print js_code
	return js_code

if __name__ == "__main__":
	main()
