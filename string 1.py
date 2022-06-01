x = 42
hungry = False
name = "teddy"
#stdout - standard output stream
print(x)

#stdin startdard input stream
entered_pin =  input("enter your pin")
print(type(entered_pin))

#Errors - exceptions
#stderr standard error stream
#standard output stream and standard error stream both go to the same output which is why sometimes they stand on each other

print(x , hungry,name)
print(hungry, x,name, sep="*")
#sep="" is a seprator
print(hungry, x,name, end="!\t")
#\n how to get a new linw \nt how to tab

print(name,'hello')
fullname = name + ' ' + 'williams'
print(fullname)
