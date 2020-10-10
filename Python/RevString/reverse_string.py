# Reversing a string using slicing

my_string = "ABCDE"
reversed_string = my_string[::-1]

print(reversed_string)

# Output
# EDCBA

# Reversing a string without slicing

string="abcde"
str_rev=""
for i in string:
  str_rev=i+str_rev
print(str_rev)



# output: edcba
