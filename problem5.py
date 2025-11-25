def parse_markdown(text):
    result=[]
    for i in range(len(text)):
        if not text[i] in ['*', "_"]:
            result.append(text[i])
        elif text[i]=='*' and text[i+1]=='*' and 'a'<= text[i+2].lower()<= 'z':
            result.append('<b>')
        elif text[i]=='*' and text[i+1]=='*' and text[i+2]==' ':
            result.append('</b>')
        elif text[i]=='_' and 'a'<= text[i+1].lower()<= 'z':
            result.append('<i>')
        elif text[i]=='_' and text[i+1]==' ':
            result.append('</i>')
        elif text[i]=='_' and text[i+1]=='.':
            result.append('</i>')
        result_str="".join(result)
    return result_str












print(parse_markdown("This is **bold** text."))
print(parse_markdown("Hello _world_."))
print(parse_markdown("Make **this** bold and _this_ italic."))
print(parse_markdown("No formatting here."))
print(parse_markdown("**Bold** at start."))
