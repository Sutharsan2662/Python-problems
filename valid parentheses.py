#
#valid parantheses



def valid_paren(char):
    
    initial = []
    
    brac = {"(":")","[":"]","{":"}"}
    
    for paren in char:
        if paren in brac.values():
            initial.append(paren)
        elif initial and brac[paren] == initial[-1]:
            initial.pop()
            
        else:
            return False
    return True   
    
            
char = str(input("enter the expressions = "))

valid_paren(char)
