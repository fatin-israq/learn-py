"""Some string methods in python"""

name = "talha"

print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase()) # makes upper characters lower, and lowers to upper

txt = "I like strawberries"
# replace("what we replace", "what we replace with")
x = txt.replace("strawberries", "apples")

print(x)

# counts how many occurrence of the parameter. this case it counts "r" in txt
print(txt.count('r'))