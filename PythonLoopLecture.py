# For Loops- iterates over a collection of data.
# While Loops- iterates and runs a condition so long as its true.

# Best way to use for loop =
# Alarms - set s specific time that loops at specific intervals.
# 5 am - M-F
def alarmClock():
     dayOfWeek= input('what day is it ? ')
     milltaryTime = [1-24]
     # when the hour is >22 --> change the day.

    
     while dayOfWeek != 'sat' and 'sun':
        for hour in milltaryTime:
            if hour == 5:
                 print('sound the alarm')
            print(hour)
        dayOfWeek= input('what day is it ? ')
        if dayOfWeek != 'saturday' or 'sunday':
            print('No alarm today. Have a good weekend. ')

alarmClock()



# Best way to use a While loop =





# In your own words, descibe the difference between a for loop and a while loop
# Provide a scenario where you would use each of these constructs in a unique way.
# What is best/ ideal scenario for using a for loop and what is the best ideal way of using a while loop?
# Create a loop that will count through 20 numbers. When your loop lands on an even number it should print a message saying this number is even.


































