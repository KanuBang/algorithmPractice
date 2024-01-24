x = 3.14
if x == int(x):
    print("integer")
else:
    print("float") #herer

y = 3
if isinstance(y, int):
    print("integer")
else:
    print("float") #here

string = "hello!"
if isinstance(string, (int,str,list)):
    print("match") # here
else:
    print("no-match")