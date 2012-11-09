import xml.etree.ElementTree as ET

root = ET.parse('calculator.xml')
# root is an Element object

def get_root():
	return root

"""
ElementTree as et
et.getroot() - Element object that is root
list(et) - list its child Element

Element as el
<tag name="value" name2="value2">text</tag>
el.tag - tag 
el.text - gets the text content in/bw the tags
el.items() - el's attributes as a seq of (name, value) pairs; 
	not in order
"""


