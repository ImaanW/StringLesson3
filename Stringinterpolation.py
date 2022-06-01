#Literal string interpolation
names = ['Tom', 'Harry', 'Jane','Mary']
suffix = ['st', 'nd',' rd','th']
n = 1
s = f"{str(n+1) + suffix[n]} of {len(names)} is {names[n]}"
print(s)

#Slicing a string
sentence = "this is my thursday code"
print(sentence[0:7])
#slice form the start to from end +1
#if you don't put a value of either positions then it will go to defult

#Splitting and joining
line = 'root::0:0:superuser:/root:/bin/sh'
#how unix user information
elems = line.split(' : ')
#splits the sting(line) at the colons : using split method, turned this
elems[0] = 'avatar'
elems[4] = 'the super-user (zero)'
line = ':'.join(elems)
print(line)
#strings are immunutable, lists are mutiable, there for you reform it into a string