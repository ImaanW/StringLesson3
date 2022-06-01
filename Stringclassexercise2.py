names = ['imaan', 'gabby', 'salima']
names_string =""
#for loops get hold of a interator and goes through the things in the list (introduces itslef"
for item in names:
    names_string = names_string + item + " "

print(names_string)
name = "imaan"
message = "teddy's favourite thing is .."
#Quotes - if you want to embedd and ' you have to use double outer-quotes - these can be interchangeable

#triple quotes to add in html code """ """

#string quotess!

name_lenght = len(name)
print(name)
#len is a FUNCTION, we pass the string as parameter (len does the work)

name_as_upppercase = name.upper()
print(name_as_upppercase)
#upper is a METHOD, object.method()

x = 2
y = 3
z = x + 7
#addition operation as the operands are both numeric
print(z)

z = str(x) + str(4)
print(z)
# concationation when its strings- gluing them together

z = x * y
print(z)
#operands are both numeric so its MULTIPLYING IT

z = str(x) * 4
print(z)
# Repeat operator, one string, one number

seperator = "-"
print(seperator * 50)

if 'im' in name:
    print("im is in imaan ")

text = "hello world"
print(text.count('o'))

text = " \t\r\n"
if text.isspace():
    print('string is whitespace')
    #here \t\r\n is whitespace  .isspace is a method

#STRING FORMATTING

#literal string interpolation
# #f strings - can evaluate the code inside the braces and glue it into


