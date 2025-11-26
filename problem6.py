def is_balanced(expression):
    expression_list=list(expression)
    new_list=[]
    for i in range(0,int(len(expression_list))):
        if expression_list[i] in "(){}[]":
            new_list.append(expression_list[i])
        else:
            continue
    # print(new_list)
        # if 'a' <= expression[i].lower() <= 'z':
        #     expression=expression.replace(expression[i], "")
        # elif expression[i] in "1234567890":
        #     expression=expression.replace(expression[i], "")

    my_list=new_list
    length_of_list=len(my_list)
    if length_of_list%2!=0:
        return False
      

    for i in range(0, length_of_list//2):
        if my_list[0]=="[" and my_list[-1]=="]":
            my_list=my_list[1: -1]
            return True
        elif my_list[0]=="(" and my_list[-1]==")":
            my_list=my_list[1: -1]
            return True
        elif my_list[0]=="{" and my_list[-1]=="}":
            my_list=my_list[1: -1]
            return True
        else: 
            return False

        



# True
# False
# False
# True
# True
# False
# False









print(is_balanced("{[()]}"))       # Nested correctly
print(is_balanced("{[}]"))         # Incorrect nesting order
print(is_balanced("(]"))           # Mismatched types
print(is_balanced("((()))"))       # Simple nesting
print(is_balanced("print(list[0])")) # Code with text (valid)
print(is_balanced("((("))          # Unclosed
print(is_balanced("]"))            # Closing without opening