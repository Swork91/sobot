'''
Created on May 8, 2018

@author: Sam

Tries to auto generate a message for each person based on the holiday or other significant event.
Other pieces later may add in auto sending or alerts prompting confirmation.  
'''
import datetime
now = datetime.datetime.now()
importantDates = ["4.1", "4.20", "5.1"]
sobotOutput = open("SobotSays.txt","w+")

# creates the last "from, me" line
def greeting(addresseName):
    sobotOutput.write("Hello,\n{}\n\n".format(addresseName))
# creates first "hello, you" line
def goodbyeMessage(yourName):
        sobotOutput.write("\n\nThanks,\n {}".format(yourName))
    
'''
uses some stereotypes to determine keywords used by the person.
 and uses the date to determine what the occasion is. 
 then we jumble that into something human-ish.
'''
class SobotBody():
    def thankYouBody(self, yourPersonality):
        sobotOutput.write("I wanted to express my sincerest thank you.")
    
    def celebrationBody(self, yourPersonality):
        sobotOutput.write("Good work on that thing you did.")
        
        
greeting("EXAMPLE_NAME")
# Checks all important dates against today
for date in importantDates:
    # if real important send longer detail message
    if (str(now.month) + "." + str(now.day) == date):
        longMessage = SobotBody()
        longMessage.celebrationBody("relaxed")
    # less important get a "thinking of you" message
    else:
        quickMessage = SobotBody()
        quickMessage.celebrationBody("relaxed")
goodbyeMessage("Sam")