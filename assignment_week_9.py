def parse_config(config_string, required_settings):
    if config_string[-1]!='>':
        return "Error: Incomplete configuration."
    else:
        my_list=list(config_string)
        my_list.pop(-1)
        my_str=''.join(my_list)
        my_str=my_str.split("--")
        new_list=[]
        for c in my_str:
            parsed_values=c.split("::")
            new_list.append(parsed_values)
        result=[]
        missing_list=[]
        for char in required_settings:
            is_found=False
            for config_char in new_list:
                if config_char[0]==char:
                    result.append(config_char[1])
                    is_found=True
                    break
            if not is_found:
                missing_list.append(char)
                # return f"Error: Missing setting ['{char}']"
        if len(missing_list)!=0:
            return f"Error: Missing settings: {missing_list}"


        return result
                    
    



#output
# ['GuestNet', 'Secret123', 'DHCP']
# Error: Missing settings: ['PASS']
# Error: Incomplete configuration.
# ['Localhost', '8080', '30']



# conf1 = "SSID::GuestNet--PASS::Secret123--IP::DHCP>"
# req1 = ["SSID", "PASS", "IP"]
# print(parse_config(conf1, req1))

# # Test Case 2: Valid config but missing a setting
# conf2 = "SSID::HomeWifi--CHANNEL::6>"
# req2 = ["SSID", "PASS"]
# print(parse_config(conf2, req2))

# # Test Case 3: Invalid format (missing end bracket)
# conf3 = "SSID::Office--PASS::Admin"
# req3 = ["SSID"]
# print(parse_config(conf3, req3))

# # Test Case 4: Different order
# conf4 = "TIMEOUT::30--PORT::8080--HOST::Localhost>"
# req4 = ["HOST", "PORT", "TIMEOUT"]
# print(parse_config(conf4, req4))
config = "COLOR::blue--SIZE::large--PRICE::25>"
required = ["COLOR", "SIZE", "PRICE"]
print(parse_config(config, required))
# Expected: ['blue', 'large', '25']

config = "COLOR::red--SHAPE::circle>"
required = ["COLOR", "SIZE", "PRICE", "SHAPE"]
print(parse_config(config, required))
# Expected: Error: Missing settings: ['SIZE', 'PRICE']

config = "PORT::8080--SECRET::abc123!@#--TIMEOUT::300>"
required = ["PORT", "SECRET"]
print(parse_config(config, required))
# Expected: ['8080', 'abc123!@#']

config = "Zebra::last--Alpha::first--Beta::middle>"
required = ["Beta", "Alpha", "Zebra"]
print(parse_config(config, required))
# Expected: ['middle', 'first', 'last']

config = "SOME::value>"
required = []
print(parse_config(config, required))
# Expected: []