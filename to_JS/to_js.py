import xml.etree.ElementTree as ET
from sys import argv
import re

script, xml_file = argv
#python to_JS.py filename.xml

#xml_file = raw_input('xml_filename >> ')

filename = re.search('([^.]+)\.xml', xml_file).group(1)
# extracts the name of the xml file

js_file = filename + ".js"	# same name, js version
tree = ET.parse(xml_file)	# tree is ElementTree

root = tree.getroot()		# root ie Element

# ElementTree as et
# list(et) lists all of et's child Element objs

def get_children(el):
	return list(el)

def get_text(el):
	for i in el.iter():
	

"""
Element as el
<tag name="value" name2="value2">text</tag>
el.tag - tag 
el.text - gets the text content in/bw the tags
el.items() - el's attributes as a seq of (name, value) pairs; 
	not in order
"""


