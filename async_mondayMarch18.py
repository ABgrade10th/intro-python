# Async work Monday March 18th, 2024.

#1. Create a function that will count the number of characters in a string
# that is passed in by a user. The string value can be passed in either as 
# a paramter or by using the input function.
 
# keyword
# parameter
# input
# string
# function
# haracters
# len()
# user

def wordCount(word): # create a wordcount()
#function and pass parameter for the data we
# will pass in.
    
    print(len(word) ) # we are using the len() function
# to count the number of characters in the data.
# we are then using the print() function
# to display/ output our result.
    

wordCount('Abdul')
    


# You must be write down and explain how your program 
# works in complete sentences in order to get full credit. 

# 2. Use your notes, W3schools, and what we have learned in class to develop
# a simple rock, paper, scissors game. Your game should allow the user to enter a letter
# that will represent the values rock, paper, and scissors (ex. r = rock, p = paper, s= scissors).

# EXTREMELY IMPORTANT NOTE
# at the top of you page write import random
# use the random.randrange(1,3) function to develop your random value logic 
# for your rock, paper, scissor game. 

# Please describe the steps you took, or if you weren't able to complete this activity,
# the steps you would've taken to solve this problem in complete sentences. 
# This must be completed in order to get full credit. 

# Clues and keywords

# Values = r,p,s
# ranodom.randrange(1,3) = this will help us to
# create the random values.

# what are we trying to accomplish:
# Create a rock, paper, scissors.
# We'll need to create random values.

# We'll need to print out the result of the match.

def rspGame():











def game(player1, player2):
    r='rock'
    p='paper'
    s='scissor'
    if player1 ==r and player2==p:
        print('player 2 wins.')
    elif player1 ==s and player2==r:
        print('player 1 wins')
    else:
        print('there is an error. ')

game('rock','scissor')






