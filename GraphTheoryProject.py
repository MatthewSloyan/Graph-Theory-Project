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