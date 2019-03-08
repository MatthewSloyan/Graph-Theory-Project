# Matthew Sloyan G00348036
# https://github.com/MatthewSloyan/Graph-Theory-Project
# Shunting Algorithm Test, will build upon for project

def infixConversion(infix):
    # declare the special operands and their priority. This will be updated down the line to add +- etc.
    specials = {'*': 50, '.': 40, '|': 30}

    pofix, stack = "", ""

    # interate through each character in the infix string
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            # if the end of round brackets, add what's on the stack till '(' is encountered
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            # remove '(' from stack
            stack = stack[:-1]
        elif c in specials:
            # get(c, 0) = value in dictionary or return 0
            # if priority is <= 
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    # remove rest of elements from stack and print to postfix
    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
        
    return pofix

print(infixConversion("(a.b)|(c*.d)"))

# Thompson's contruction start
# ===========================

# Represents a state with two arrows, labelled by label.
# Use None for a label representing 'e' arrows 
class state: 
    # None = no value as of now but will assign
    label = None
    edge1 = None
    edge2 = None

# An NFA is represented by it's initial and accept states
class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = initial

def compile(pofix):
    nfaStack = []

    for c in pofix:
        if c == '.':

        elif c == '|':

        elif c == '*':

        else:
            # Create new initial and accept states.
            accept = state()
            initial = state()
            # Joing the initial state, the accept state using an arrow labelled c.
            initial.label = c 
            initial.edge1 = accept 
            # Push new NFA to the stack.
            nfaStack.append(nfa(initial, accept)) # combine states
    
    return nfaStack.pop()