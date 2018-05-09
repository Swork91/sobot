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
        sobotOutput.write("\n\nThanks,\n{}".format(yourName))
'''
uses some stereotypes to determine keywords used by the person.
 and uses the date to determine what the occasion is. 
 then we jumble that into something human-ish.
'''
def celebrationBody():
    if(str(now.month) + "." + str(now.day) == "1.30"): # Jacob Birthday
        sobotOutput.write("Happy birthday. I hope its a good one.")
    if(str(now.month) + "." + str(now.day) == "5.1"): # Sam Birthday
        sobotOutput.write("Happy birthday. I hope its a good one.")
    if(str(now.month) + "." + str(now.day) == "10.31"): # Halloween
        sobotOutput.write("Happy Halloween. I hope you are well. ")
    if(str(now.month) + "." + str(now.day) == "12.25"): # Christmas
        sobotOutput.write("Merry Christmas. I hope you are well. ")
    else:
        sobotOutput.write("I don't know why I'm writing you, but GOOD TO KNOW YA!")

greeting("EXAMPLE_NAME") 
celebrationBody()
goodbyeMessage("Sam")