# You have been hired as an engineer to develop a 
# gradebook system.
# The client would like to create 
# a fucntion that uses conditional statements 
# that will allow teachers to enter a numerical grade
# and then automatically generates a letter grade for that number (for example a teacher 
# enters a 70, the program should output a C).
# The numerical grade should be entered as an argument. 
# The client has provided you with the following grade rubric.

# A = 90 and up
# B = 80 and up 
# C = 70 and up
# D = 60 and up
# F = 59 and below


# clues and keywords
# conditional statements IF/ELSE/ ELIF
# need to use a arguement to a pass in a number grade - Integer
# need to print() a letter for the grade - String.
# need to use comparison operators (Less than, greater than)
# we need to make a function.



def gradeBook(studentGrade):
    if studentGrade >= 60 and studentGrade <= 69:
        print('This student has a D.')
    elif studentGrade >=70 and studentGrade <= 79:
        print('This student has a C.')
    elif studentGrade >=80 and studentGrade <= 89:
        print('This Student has a B.')
    elif  studentGrade >= 90 and studentGrade <=100:      
        print('This student has an A')
    else:
        print('This student has an F.')
# gradeBook(102)


# if gymMember():

satisfacntion_Score = input()
if survey():






















