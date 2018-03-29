

def kmph_to_mph(raw_input):
    mph= int(0.6214* raw_input)
    return mph

raw_input = 200 #variable by user

output = "the speed in miles/hr is" , kmph_to_mph(raw_input)
print(output)
