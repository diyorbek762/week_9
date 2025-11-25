def reformat_number(phone_number):
    phone_number=phone_number.replace(" ", "").replace("-", "").strip()
#     First, remove all spaces and dashes from the input string, leaving only the digits.
    new_list=[]
    for i in range(0, len(phone_number), 3):
        new_list.append(phone_number[i: i+3])
    if len(new_list[-1])==1:
        new_list[-1]=new_list[-2][-1]+new_list[-1]
        new_list[-2]=new_list[-2][0:2]
    return "-".join(new_list)
    

    



# Next, group the digits into blocks of three, separated by dashes.
# The final block of digits is an exception. It can have a length of two, three, or four.
# If the number of remaining digits at the end is 4, they should be grouped into two blocks of two digits each (e.g., XX-XX).
# If the number of remaining digits is 2 or 3, they form a single final block.
print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3
print(reformat_number("123-456-7890"))    # 10 digits -> 3-3-2-2 (4 remaining -> 2-2)
print(reformat_number("123 45 678"))      # 8 digits -> 3-3-2
print(reformat_number("12"))              # 2 digits -> 2
print(reformat_number("12345"))           # 5 digits -> 3-2
print(reformat_number("--1 23 4-5 6-7--")) # 7 digits -> 3-2-2 (4 remaining -> 2-2)