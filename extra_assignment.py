def format_roster(names):
    result=[]
    for c in names:
        without_whitespace=c.strip()
        cap_letters=without_whitespace.upper()
        if cap_letters=="":
            continue
        else:
            result.append(cap_letters)
    
    return result













student_list = [
    "  john doe ",
    "JANE SMITH",
    "   ",
    "alice wonderland",
    "bOb rOsS  "
]
cleaned_roster = format_roster(student_list)
print(cleaned_roster)