"""
This is a helper class to aid in debugging
"""

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

class Node(Element):
	def __init__(self):
		pass

	def __str__(self):
		pass

# all blocks have types (ex. procedures_defreturn)
# first_block.attrib['type'] --> "procedures_defreturn"
	def get_block_type(self):
		return self.attrib['type']

	def get_attribs(self):
		return self.attrib

	def get_text(el):
		return [i.text for i in el.iter()]

# iter() = created tree iterator with the current el
# as the root; iterates over el and all its children	
# depth first order	
	def get_children(self):
		return [child for child in self.iter()]	
	
	def print_children(self):
		for child in get_children(self):
			print child 

# some of these fncs may not be useful
	def get_keys(self):
		return [i.keys() for i in self.iter()]

	def get_items(self):
		return [i.items() for i in self.iter()]	

"""
	#return texts of all tags named title among the node's children
	#given a block element --> returns [add, ADD, x, y]
	def get_function_details(self):
		fn_details = []
		for child in get_children(self):
        	if child.tag == 'title':
				fn_details.append(child.text)
		return fn_details
	
"""
