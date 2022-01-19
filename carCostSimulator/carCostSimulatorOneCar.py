# -*- coding: utf-8 -*-
"""
#just 1 car, cost simulator

Created on Wed Oct 27 02:00:06 2021
@author: mikko

car cost simulator1
This is an edit
This is another edit
this is a third edit
This is a 4th edit
"""


dayLifeCount = 0 #how many days the car has been alive
milesLifeCount = 0 #how many miles left on the car
milesWhenJunked = 250000 #projected miles the car will last
daysWhenJunked = 20*365 #how many days the car might last not totally dependant on miles driven

averageMilesPerDay = 30000/365

yearCounter = 0
monthOfYearCounter = 0
dayOfMonthCounter = 0#this will increase to 30 in the loop and then reset
dayOfWeekCounter = 0 #this will go to 12 then flip to 0



#car costs
bankAccountC1 = 0

#monthly payments for, loan, insurance, average maintaince bill, etc. This could definately be itemized out
monthlyPaymentC1 = 0

#what is the car's average MPG. This could be expanded out
mpgC1 = 20

#this loop is designed to loop once per day and you need to ma
while dayLifeCount < daysWhenJunked  and milesLifeCount < milesWhenJunked :

    #print calendar###########################################################
    print(f"day of life:   {dayLifeCount}")
    print(f"day of month:  {dayOfMonthCounter}")
    print(f"month of year: {monthOfYearCounter}")

    if dayOfMonthCounter == 15:
        bankAccountC1 = bankAccountC1 - monthlyPaymentC1

    if dayOfWeekCounter == 6 :
        bankAccountC1 += 700


    #milage updater#############################################################
    milesLifeCount += averageMilesPerDay#this will go to milesWhenJunked(250,000) if nothing else stops it

    #cost updaters##############################################################


    #calendar updaters##########################################################
    dayLifeCount += 1 #this will go to 7300 if nothing stops it
    dayOfWeekCounter += 1
    if dayOfWeekCounter > 7:
        dayOfWeekCounter = 1

    #update day of month counter
    dayOfMonthCounter += 1
    if dayOfMonthCounter > 30:
        dayOfMonthCounter = 1
    
    #update month of year
    monthOfYearCounter += 1
    if monthOfYearCounter > 12:
      monthOfYearCounter = 1



#final results
print(bankAccountC1)
