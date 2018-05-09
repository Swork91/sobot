'''
Created on May 8, 2018

@author: Sam

Tries to auto generate a message for each person based on the holiday or other significant event.
Other pieces later may add in auto sending or alerts prompting confirmation.  
'''
import datetime
now = datetime.datetime.now()
importantDates = ["4.1", "4.20", "5.1",]
sobotOutput = open("SobotSays.txt","w+")

# creates the last "from, me" line
def greeting(addresseName):
    sobotOutput.write("Hello,\n{}\n\n".format(addresseName))
# creates first "hello, you" line
def goodbyeMessage(yourName):
        sobotOutput.write("\n\nThanks,\n{}".format(yourName))
'''
uses some stereotypes to determine keywords used by the person.
 and uses the date to determine what the occasion is. 
 then we jumble that into something human-ish.
'''
def celebrationBody(yourPersonality):
    FoundIt = False
    for date in importantDates:
        if(str(now.month) + "." + str(now.day) == date):
            sobotOutput.write("Good work on that thing you did. I'm glad that think happened. Hope you are doing well.")
            FoundIt =  True
            break
    if (FoundIt == False):
        sobotOutput.write("I don't know why I'm writing you, but GOOD TO KNOW YA!")

greeting("EXAMPLE_NAME") 
celebrationBody("relaxed")
goodbyeMessage("Sam")