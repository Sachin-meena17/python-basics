#Creating a Function
def my_function():
  print("Hello from a function")
my_function()
print("Outside the function")


#Information can be passed into functions as arguments.
def my_function(fname):
  print(fname)
my_function("Emil")
my_function("Tobias")
my_function("Linus")


#passing two value as arguments
def my_divsion(a,b):
  print(a/b)
my_divsion(2,10)


# assigning value so order of argument does not disturb variables
def my_function(child3, child2, child1):
  print("The youngest child is " + child1)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Default Parameter Value
def my_function(country="Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#return value
def my_function(x):
    return 5 * x
b=my_function(5)
print(b)


#local and global variable
def bugs():
    numbugs = int(input('How many bugs?' ))
    print (numbugs)
bugs()


def bugs():
    numbugs = int(input('How many bugs? '))
    print (numbugs)
bugs()
print (numbugs) # error! Variable numbugs


#different local variable with same name for different function
def newjersey():
    numbugs = 1000
    print ("NJ has", numbugs, "bugs")

def newyork():
    numbugs = 2000
    print ("NY has", numbugs, "bugs")

newjersey()
newyork()
newjersey()


#usage of global variable inside and outside function

name = 'Obama'
def showname():
    print("Function:", name)

showname()
print("Main program:", name)

# usage of global variable inside and outside function and changing inside function

name = "Obama"
def showname():
    global name
    print ("Function 1:", name)
    name = "John"
    print ("Function 2:", name)
    print ("Main program 1:", name)

showname()
print ("Main program 2:", name)

#lambda

#Python Lambda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#lambda arguments : expression

x = lambda a : a + 10
print(x(10))

x = lambda a, b : a * b
print(x(5, 6))
