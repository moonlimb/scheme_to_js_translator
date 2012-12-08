tab, tab2 = "    ", "        "

"""
    @add_curly_braces
    def get_function_body(op_token, args):
        operator = op.basic[op_token]
        body = operator.join(args)
        return body 
           
    # element's children are argument nodes 
    # ex. <arg name = "x"/>
    def make_params(parent_of_args):
        args = [arg.attrib['name'] for arg in list(parent_of_args)]
        return '('+ ", ".join(args) + ')'
    """


class JsAST(object):
    # code is a list of different parts of the code
    def __init__(self, code):
        self.code = code
    def __str__(self):
        if len(self.code)==1:
            return str(self.code)   
        else:
            str_code = [str(chunk) for chunk in self.code]
            return '\n'.join(str_code)

# Expression is a combination of values, variables, operators, and function calls
class Expr(object):
    def __init__(self, expr):
        self.expr = expr 
    def __str__(self):
        return '%s' %str(self.expr)

# ex. if (stmt)
# Statement is an instruction Python interpreter can execute
class Stmt(object):
    def __init__(self, stmt):
        self.stmt = stmt
    def __str__(self):
        if isinstance(self.stmt, list):
            stmt = ' '.join(self.stmt).replace('( ', '(').replace(' )',')')
            return '%s' %stmt
        else:   # isinstance(self.stmt, str)
            return "%s" %str(self.stmt)

class Operator(Expr):
    def __init__(self, symbol):
        self.symbol = symbol
    def __str__(self):
        return "%s" %str(self.symbol)

class ValueExpr(Expr):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return '%s' %str(self.value)

class VarExpr(Expr):
    def __init__(self, name):
        self.name = name    
    def __str__(self):
        return '%s' %str(self.name)

class DeclarationStmt(Stmt):
    def __init__(self, var_expr): 
        self.var_expr = var_expr
    def __str__(self):
        return 'var %s;' %str(self.var_expr)

class AssignmentStmt(Stmt):
    def __init__(self, var_expr, value, is_declaration):
        self.var_expr = var_expr
        self.value = value
        self.is_declar = is_declar
    def __str__(self):
        assignment = '%s = %value' %(self.var_expr, self.value) 
        if self.is_declaration:
            return 'var %s' %assignment 
        else:
            return assignment

# should ElseIfStmt inherit from object or Statement?
class ElseIfStmt(object):
    def __init__(self, cond, stmt):
        self.cond = cond
        self.stmt = stmt
    def __str__(self):
        return "else if (%s) {\n%s%s \n};" %(str(self.cond), tab2, str(self.stmt))

class ElseStmt(Stmt):
    def __str__(self):
        return "else {\n    %s \n};" %(str(self.stmt))

class IfElseStmt(object):
    def __init__(self, pred, body, else_stmt):
        self.pred = pred    # pred is predicate (evaluates to a boolean literal)
        self.body = body    # body is consequential expression corresponding to a predicate 
        self.else_stmt = else_stmt
    def __str__(self):
        return "if (%s) {\n%s%s\n}; %s" %(str(self.pred), tab, str(self.body), str(self.else_stmt))

class IfStmt(object):
    def __init__(self, cond, body, elses):
        self.cond = cond    # cond is expression
        self.body = body    # body is if statement's body 
        self.elses = elses  # list of elseif and else stmts 
    def __str__(self):
        if self.elses:
            return "if (%s) {\n%s%s\n}; %s" %(str(self.cond), tab, str(self.body),' '.join([str(else_if) for else_if in self.elses]))

class BreakStmt(Stmt):
    def __init__(self):
        self.stmt = "break;"

class ContinueStmt(Stmt):
    def __init__(self):
        self.stmt = "continue;"

class FunctionCall(name, args):
    def __init__(self, name, args):
        self.name = name
        self.args = args
    def __str__(self):
        return " %s(%s)" %(str(self.name), str(self.args))

# loop constructions
class ForLoop(object):
    def __init__(self, init, cond, incr, body): 
        self.init= init
        self.cond = cond
        self.incr = incr    # may be an increment or decrement  
        self.body = body
    def __str__(self):
        return "for (%s; %s; %s) {\n%s%s;\n}" %(str(self.init), str(self.cond), str(self.incr), tab, str(self.body))

class ForEachLoop(object):
    def __init__(self, index, iterable, body):
        self.index = index
        self.iterable = iterable    
        self.body = body
    def __str__(self):
        return "for (var %s in %s) {\n%s%s\n}" %(str(self.index), str(self.iterable), tab, str(self.body))
        
class WhileLoop(object):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body    #body is stmt
    def __str__(self):
        return "while (%s) {\n%s%s\n}" %(str(self.cond), tab, str(self.body))

class Function(object):
    def __init__(self, name, args, body):
        self.name = name
        self.args = args    #args is a list
        self.body = body    #body is a liAt
        
    def __str__(self):
        param = ', '.join(self.args)
        #body_exprs = ''.join(str(self.body))   # better var name?
        body_str  = "\n".join([str(item) for item in self.body])
        return "function %s(%s) {\n%s \n}" %(str(self.name), param, body_str)

class MathExpr(object):
    # operand could be variables or expressions
    def __init__(self, operator, left_operand, right_operand):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
    def __str__(self):  
        return "%s %s %s" %(str(self.left_operand), str(self.operator), str(self.right_operand))

# use decorators to add wrapper to expr? 
class PrintStmt(Stmt):
    def __str__(self):
        return "console.log('" + str(self.stmt) + "');"
    
class ReturnStmt(Stmt):
    def __str__(self):
        return "return " + str(self.stmt) + ";"
