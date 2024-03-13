





# Intro to Python Async Work
# Monday March 11th, 2024.

# INSTRUCTIONS
# Create a new python file called async_3_11.py
# Answer the following questions. Once you've completed the questions, commit
# and sync your work.
# This activity must be completed by the end of class in order to recieve
# a grade.

# REMEMBER - TAKE YOUR TIME AND DO YOUR BEST! DO NOT GIVE UP! 

# 1. Which Python datacasting function would
# you use if you wanted to convert a string data type
# into an integer data type? Please write your response
# in a complete sentence.



'I would use the int() data casting function. This fucntion converts'
'Anything passed inside of it into a integer number. '


#Keywords
#fucntions- there is some function we use to convert datatypes
# integer- non-decimal numbers
# string- anything wrapped inside of qoutations ""
# we know we need to change a string into an integer
# datacasting- the process of converting data types
# data types- fundamental building blocks of a program language.

# 2. Create a list called numbCol that contains three (3 ) colors and three (3) numbers.
numbercol= ['red,' 'blue ,'green ,' 1,2,3]
{} # turly- These brackets are used for objects.
[] # Square- These brackets are used for lists.
() # Round- These brackets are used for fucntions


# 3. You have been hired by a University to create
# a scholarship function. The client would like to provide 
# students a scholarship to their school based on the following
# conditions; 
# - If the user has never gotten a loan before and,
#-  if the user has never been to college before.
# The client would like you to use the logical NOT operator that will
# compare the condtions and return false. If the result is false, the client
# would also like the program to print the message "congrats! you've gotten the scholarship."
# the client has given you the choice on how to enter data for your function.
# you may enter data using input or pass in data into your function as parameters. 


# Keywords
# Conditionals Statements (if / elif/ else)
#- we can output specific outcomes for specific condtions

# input- allow us to PUT IN data.

# print- sends data out.
# we need to print the message
# "congrats! you've gotten the scholarship."

#  Function - set of instructions that willrun when called.

# Compare --> Logical operator- the question is telling
# us to use the NOT keyword.

# Parameter- placeholder for data in a function definiton.
def Scholarship(userLoan, BeenToCollege):
     if userLoan == 'True' and beenToCollege == True:
        print('Congrats youve gotten the scholarship')
    elif userLoan== True and beenToCollege == False:
         print('Sorry, unfortunately you dont qualify for the scholarship')      
    elif userLoan== False and beenToCollege == True:
         print('Sorry, unfortunately you dont qualify for the scholarship')            
    else:
         print('Sorry, unfortunately you dont qualify for the scholarship')
         
         Scholarship(False, False)
                     
