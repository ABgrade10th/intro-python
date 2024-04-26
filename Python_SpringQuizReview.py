# what is a computer program? - 
# digital instruction for computers  to execute - Instructions

# what is Syntax?
# the rules of a programing language.
# ex, Spanish is lauguage that has 
# certain wocab rules that aren't in other lauguaes
# an example of syntax (how to write) a function using python.
def myFunction():
    print(type(10))
myFunction()

# An example of syntax ( how to write) a function in JavaScipt.
# function myFunction(){
# console.log('here are my instutions')

#}

# what is a data type in python? - 
# A data is piece information that the computer understands to
# fundamental; datas are our alphabet for a programing language.

# what is data casting?-
# data casting is the process of changing a data type.

# ex. We use the int() function to change the string value into an integer
def multiplyNumber():
    number = input('please enter a number and this program will multiply it by 4.')
    result = int(number) * 4
    print(f'here is the result: {result}')
    multiplyNumber()

# what are operators in Python-
# operators allow us to perform actions on data. Actions can be things such
# as doing math, comparing infromtion (data), or assigning informtion (data).

action_1 = 2 + 2
# the answer is 4, and we are doing addition on these two data types
# this is an aritimatic oprators (addition)

action_2 = 'abdul'
action_3 = 'baaqee'
# this is going to have the value of 'abdul' . We are assinging
# this string data to a variable.
# This is the assignment oprator
# anytime there is 1 (ONE) equal sign, means we are assinging a value.

action_4 = 2 == 2
# This is going to be true, because the number 2 is the SAME as the other
# other number 2.
# This is the comparison oprators=.
# whenever there are 2(TWO) equal signs, it means we are comparing if
# the data/ information is the SAVE

# what is a list? -
# A list its a collection of data. 
# A list can store different data types.
# when we want to create a list we use square brackets []

randomList = ['cheese' ,10, 10.292, True, ['abdul','baaqee'], my Function,']
print(randomList)

# why do we use list? -
# To save/ store, and retrieve information
# List can also keep data in order.

# what is a function?-
# instructions (program) that we can SAVE
# for later and CALL when we need it.

# what are functions arguments and parameters?
# what is the difference between them?

# a fucntion parameter is a placeholder for data.
# We pass this data inside the function definition.
# (The part where we write def)
# remember P- for parameter, P- for placeholder.

# A fucntion argument is the ACTUAl data we pass into the function can
# remember  A for agrument, A for Actual/ Real Data.

def addition(number):
result = number + 100
print(result)
      
addition(100)