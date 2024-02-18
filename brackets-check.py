#WAP to check the proper order of brackets. Brackets are of types '{}','()','[]'.
#Level = EASY

def bracket(inp):
    stack=[]
    for i in inp:
        if i in('{','[','('):
            stack.append(i)
        elif i=='}' and stack.pop()!='{':
            return False
        elif i==']' and stack.pop()!='[':
            return False
        elif i==')' and stack.pop()!='(':
            return False
    return True
input_=input()
print(bracket(input_))
