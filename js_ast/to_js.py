import xml.etree.ElementTree as ET
from sys import argv
import re
import operators as op
#op.basic is a dictionary of basic operators
from decorate import add_curly_braces

script, xml_file = argv
#python to_JS.py filename.xml:
#xml_file = raw_input('xml_filename >> ')

filename = re.search('([^.]+)\.xml', xml_file).group(1)
# extracts the name of the xml file

js_file = filename + ".js"	# same name, js version
#js_file.write('hello')
tree = ET.parse(xml_file)	# tree is ElementTree

#def get_root():
#	return root
# ElementTree as et

# procedures_defreturn --> fcn with a return statement
# procedures_defnoreturn --> fcn w/ no return statement
# Q: Use decorators/wrapper function to add curly braces?
	# curly braces when:
	#	- block.attrib['type'] ==procedures_defreturn
	#	- if	/ 	for

# all blocks have types: ex. procedures_defreturn, math_arithmetic, variables_get 
# first_block.attrib['type'] --> "procedures_defreturn"

def get_type(block):
	return block.attrib['type']
	
def get_children(el):
	return [e for e in root.iter()]

def print_children(el):
	#iter() = creates tree iterator with the current element as the root
	# iterator iterates over el and all elements below it (depth first order)
	for el in root.iter():	 
		print el

def get_keys(el):
	return [i.keys() for i in el.iter()]

def get_items(el):
	return [i.items() for i in el.iter()]
	
# not useful
"""def get_key_item_pair(el):
	return zip(get_keys(el), get_items(el)) 
"""

def get_attributes(el):
	return el.attrib

def get_name_text_pairs(el):
	for el_object in el:
		print el_object		
	#return [get_name_text_pair(el_object) for el_object in el] 

# given a single element, return its name and text pair
def get_name_text_pair(el):
	return (el.tag, el.text, el.items())

def get_text(el):
	return [i.text for i in el.iter()]

"""Element as el
<tag name="value" name2="value2">text</tag>
el.tag - tag 
el.text - gets the text content in/bw the tags
el.items() - el's attributes as a seq of (name, value) pairs; 
	not in order
"""

#can you use a decorator within a function?
def make_fcn_content(content):
	return content
	# adds { content;}
 
"""
def make_function(name, args):
	return "function %s%s" %(name, args)

def get_args(el):
	for arg in list(el):
"""
		
# element's children are argument nodes 
# ex. <arg name = "x"/>
def make_params(parent_of_args):
	args = [arg.attrib['name'] for arg in list(parent_of_args)]
	return '('+ ", ".join(args) + ')'

#this is an awesome function
#given a block element --> returns [add, ADD, x, y]
def get_function_details():
	fn_details = []
	for child in get_children(el):
		if child.tag == 'title':
			fn_details.append(child.text)	
	return fn_details


"""
get block tags

"""

"""	
fnc = "function %s" %fn_details[0] 
	body = get_function_body(fn_details[1],fn_details[2:])	
	return fnc	
"""
@add_curly_braces		
def get_function_body(op_token, args):
	operator = op.basic[op_token]	
	body = operator.join(args)
	return body	
	
def get_title_tag(block):
	pass	

block_types ={'procedures_defreturn': get_function, 
'math_arithmetic': get_title_tag, 
'variables_get': get_title_tag}

# all blocks have types: ex. procedures_defreturn, math_arithmetic, variables_get
# first_block.attrib['type'] --> "procedures_defreturn"
def get_type(block): 
	return block_types[block.attrib['type']]

def return_empty_str(el):
	return ""
		
# write a function to get the tree depth
# explore loggin module in Python!! 

# first_block = list(root)[0]     #the first_block object is ADD function
# bl_type = get_type(first_block)	#bl_type is 'procedures_defreturn'		
tag_category ={'block': get_type, 'mutation': make_params, 'title': return_empty_str, 'value': return_empty_str, 'arg': return_empty_str, 'xml': return_empty_str }

#explore python loggin module
def parse_tree(root):
	js_code=""
	for el in root.iter():
		print el		
		#change to get method
		temp = tag_category[el.tag](el)
		#which is more efficient? isinstance() or type()
		if isinstance(temp,str):
			js_code += temp
		#print js_code
	return js_code

def main():	
	root = tree.getroot()		# root ie Element
	js_code = parse_tree(root)
	print js_code

if __name__ == "__main__":
	main()
