# -*- coding: utf-8 -*-
"""
#I need a version of this with only 1 car instead of 2

Created on Wed Oct 27 02:00:06 2021
@author: mikko

car cost simulator1
This is an edit
This is another edit
this is a third edit
This is a 4th edit
this is a 5th edit
6th edit
"""

#this is edit 2
#this is edit 3

dayLifeCount = 0 #how many days the car has been alive
milesLifeCount = 0 #how many miles left on the car
milesWhenJunked = 250000 #projected miles the car will last
daysWhenJunked = 20*365 #how many days the car might last not totally dependant on miles driven

averageMilesPerDay = 30000/365

yearCounter = 0
monthOfYearCounter = 0
dayOfMonthCounter = 0#this will increase to 30 in the loop and then reset

dayOfWeekCounter = 0






#car costs
bankAccountC1 = 0
bankAccountC2 = 0

monthlyPaymentC1 = 0
monthlyPaymentC2 = 300

mpgC1 = 20
mpgC2 = 30



#this loop is designed to loop once per day and you need to ma
while dayLifeCount < daysWhenJunked  and milesLifeCount < milesWhenJunked :


    print(dayLifeCount)
    print(dayOfMonthCounter)

    if dayOfMonthCounter == 15:
        bankAccountC2 = bankAccountC2 - monthlyPaymentC2

    if dayOfWeekCounter == 6 :
        bankAccountC1 += 700
        bankAccountC2 += 700


    ############################################################################
    #milage updater
    milesLifeCount += averageMilesPerDay#this will go to milesWhenJunked(250,000) if nothing else stops it

    #calendar updaters
    dayLifeCount += 1 #this will go to 7300 if nothing stops it
    dayOfWeekCounter += 1
    if dayOfWeekCounter > 7:
        dayOfWeekCounter = 1

    #update day of month counter
    dayOfMonthCounter += 1
    if dayOfMonthCounter > 30:
        dayOfMonthCounter = 1


#final results
print(bankAccountC1)
print(bankAccountC2)
