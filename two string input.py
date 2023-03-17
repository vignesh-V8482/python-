input_string="3haaris"
n=int(input_string[0])
name=input_string[1:]
output=" "
for i ,char in enumerate(name):
    if (i+1) % n==0:
        output += "z"
    else:
        output += char
print(output)
