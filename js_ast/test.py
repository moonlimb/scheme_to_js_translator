"""

if block type == 'procedures_defreturn':
	<mutation>
	arg name --> ('x','y')
	</mutation>
	title name 'add' ==> add()
		if block type == 'math_arithmetic'
			if title name == OP
				title.value (ADD) : '+' / 'operator.add'	
					value child # --> # arguments
						block type = 'variables_get' 
							title name:x

function add(x,y) {
	return x+y;
}	

 <block type="procedures_defreturn" inline="false" x="255" y="-18">
    <mutation>
      <arg name="x"></arg>
      <arg name="y"></arg>
    </mutation>
    <title name="NAME">add</title>
    <value name="RETURN">
      <block type="math_arithmetic" inline="true">
        <title name="OP">ADD</title>
        <value name="A">
          <block type="variables_get">
            <title name="VAR">x</title>
          </block>
        </value>
        <value name="B">
          <block type="variables_get">
            <title name="VAR">y</title>
          </block>
        </value>
      </block>
    </value>
  </block>


(block type procedures_defreturn)

"""

#block is tag name
(	'block', 
	'\n    ',	#text 
 	[	('y', '96'), 	#items()
  		('inline', 'false'), 
  		('type', 'procedures_defreturn'),
  		('x', '270')
	]
)

