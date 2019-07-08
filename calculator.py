#Fetch two numbers to operate on
print ("Choose two numbers?")
a = int(input("First Number: "))
b = int(input("Second Number: "))

#Ask User what they would want to do with the numbers
print ("Want do you want to do with these numbers?")
print ("a = add : s = substract : d = divide: m = multiply")
c = input ("You want to?:")

#execute the arithmetic based on choice
if c == 'a':
    print (a+b)
elif c == 's':
    print (a-b)
elif c == 'd':
    if b == 0:
        print ("You can't divide by zero")
    else: print (a/b)
elif c == 'm':
    print (a*b)
