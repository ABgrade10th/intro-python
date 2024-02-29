'Conditonal statements evaluate specific conditions,'
'and will output specific outcomes'
'based on that condition.'

foodSubscription= True
if foodSubscription == True:
    print("order the next meal for subscriber")
else:
    print("you are not a subscriber, would you like to join?")





# Clues / Keyword
# 1. We need to write Fucntion --> we need a function def,
# and call
# 2. We need to use the input fucntion to take in data
# score of user
# 3. We need to use IF/Else --> need to determine if 
# user has gotten the high score
# if score > 3000; user has achieved the high score
# else score < 3000; user needs to restart, you did not get the
# the high score

def wasHighscoreReached():
    userscore = int(input('what is your score? '))
    if userscore > 3000:
        print('Congrats! You have the high score!')
    else:
        print('You did not reach the high score. Try again.')

wasHighscoreReached()


def myfucntion(notknownData):
    print('here are the instrusctions...')

if 13-10 > 10+10:
# 0 greater 20 ...what, no. this is false.
        print("Good job.")
else:
     print("not right...")

         












