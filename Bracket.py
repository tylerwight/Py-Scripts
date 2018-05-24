#A script that parses a set a of brackets and determines if they are opened/closed in the correct order or not.
def checkio(expression):
    openbrackets = [ "(",  "[",  "{" ]
    closebrackets = [ ")", "]", "}"]
    brackets = list()
    left = list()
    right = list()
    
    #populate list brackets with all brackets that exist in order
    #populate list left with open brackets and right with close brackets
    for i in expression:
        if (i in openbrackets):
            brackets.append(i)
            left.append(i)
        if (i in closebrackets):
            brackets.append(i)
            right.append(i)
    
    print(brackets)
    print(left)
    print(right)
    
    #check if there are a different number of open/close brackets, if there are return false
    if (len(left) != len(right)):
        return False
        
        
    #looking = the type of bracket we want to find next
    #backup = a list to put brackets in if we find another open bracket instead of the close bracket we want
    
    looking = '';
    backup = list()
    
    for i in range(len(brackets)):
        if (brackets[i] in openbrackets):
            if (looking != ''):
                #if I hit an open bracket, and we are already looking for something, add it to the backup list
                backup.append(looking)
            
            #bracket we are looking for currently is the opposite of the kind we just found
            looking=opposite(brackets[i]);
            
        if (brackets[i] in closebrackets):
            #if it's not the bracket we were looking for, return false
            if (brackets[i] != looking):
                return False
            #if it was the bracket we were looking for, update looking to the next bracket in the backup list and remove it from the list then continue seraching
            if (backup):
                looking = backup[-1]
                backup.pop()

    return True



def opposite(brack):
    if brack == ')':
        return '('
        
    if brack == '(':
        return ')'
        
    if brack == '[':
        return ']'
        
    if brack == ']':
        return '['
        
    if brack == '{':
        return '}'
        
    if brack == '}':
        return '{'
    print("NO BRACKET GIVEN")



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True, "cmon mayn"
    assert checkio("((5+3)*2+1)") == True, "Simple"
    print("SIMPLE DONE")
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    print("Diff")
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    print("Done with ALONE")
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    print("ALL DONE BABY")
    assert checkio("[(3)+(-1)]*{3}") == True, "wtf man"
    print("wtf DONE")
    assert checkio("[1+202]*3*({4+3)}") == False, "dudebro"
    print("DUDEBRO DONE")
    assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True, "cmon mayn"
