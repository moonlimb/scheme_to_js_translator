import xml.etree.ElementTree as ET
from sys import argv
import re

script, xml_file = argv
#python to_JS.py filename.xml:
#xml_file = raw_input('xml_filename >> ')

filename = re.search('([^.]+)\.xml', xml_file).group(1)
# extracts the name of the xml file

js_file = filename + ".js"	# same name, js version
js_file.write('hello')

tree = ET.parse(xml_file)	# tree is ElementTree

root = tree.getroot()		# root ie Element
def get_root():
	return root
# ElementTree as et
# list(et) lists all of et's child Element objs

fcn = "function"
fcn_return = fcn
fcn_no_return = fcn

# procedures_defreturn --> fcn with a return statement
# procedures_defnoreturn --> fcn w/ no return statement
# Q: Use decorators/wrapper function to add curly braces?
	# curly braces when:
	#	- block.attrib['type'] ==procedures_defreturn
	#	- if	/ 	for

#types = {"procedures_defreturn": fcn_return,
#"math_arithmetic":'OP',
#"variables_get":'VAR'
#}

title_names = {"OP": {'MULTIPLY':'*', 'DIVIDE': '/', 'ADD': '+', 'MINUS': '-'}}
# block type ="procedures_def return maps to keyword function
	#title name="NAME"> square </title> 

# used to get fcn name, etc.
# all blocks have types: ex. procedures_defreturn, math_arithmetic, variables_get 
def get_type(block):
	return block.attrib['type']
	
def get_elements(el):
	return [e for e in root.iter()]

def print_elements(el):
	#iter() = creates tree iterator with the current element as the root
	# iterator iterates over this element and all elements below it (depth first order)
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

def get_children(el):
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
