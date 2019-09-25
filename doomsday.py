# Implementing Conway's famous 'DOOMSDAY' algorithm:D

import random
import math
import sys
import time

def date_indicator(date):
    #returns (day,month,year) if the date is valid (in the dd/mm/yyyy format) and 0 otherwise
    if type(date) is str == False:
        return 1
    elif len(date) != 10:
        return 1
    elif date[2] != '/':
        return 1
    elif date[5] != '/':
        return 1
    
    #STILL NEED LOGIC FOR MONTH AND DAY NUMBER SINCE THESE ARE RESTRICTED!
    try:
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    except ValueError:
        return 1
    
    if month not in range(1,13):
        return 1
    
    month_days = {1: 30, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9:30, 10:31, 11:30, 12:31 }
    
    if  0 <= day<= month_days[month]:
        return (day, month, year) 
    elif month == 2 and day ==29 and year%4 == 0:
        return (day, month, year)
    else:
        return 1
        
    
def prepare(date):
    date = str(date)
    
    while date_indicator(date) == 1:
        date = input('Invalid date.\n\nPlease enter a date in the form dd/mm/yyyy: ')
        date = str(date)
        
    return(date)

def dd(date):
    #Returns the DOOMSDAY for a given year
    #We want to make sure the date is given in the form 'dd/mm/yyyy'
    
    date = prepare(date)
        
    (day, month, year) = date_indicator(date)
    
    #(Gregorian) calendars repeat themselves every 400 years. Below we have anchor days.
    anchor_days = {2: 5,
               3: 3,
               0: 2,
               1: 0}
    
    #Keys are (centuary-1)mod4. so 2015 is 21st centuary has key 0.
    #Items are days of week (0 is Sunday, 6 is Friday.)
    
    #Now we run the doomsday algorithm
    #First let a be the number of times 12 fits into the last two digits of the year.
    a = math.floor((year%100)/12)
    #Next let b be the value of the last two digits of the year mod 12
    b = (year%100)%12
    #Next let c be the floor of b/4
    c = math.floor(b/4)
    #Let d be the sum of a,b and c
    d = a+b+c
    #Count forward by d days (or d mod 7 das, if you like) from the anchor day
    #for the date's centuary to calculate that year's DOOMSDAY.
    anchor_day = anchor_days[math.floor(year/100)%4]
    dday = (anchor_day + d%7)%7
    #print("The DOOMSDAY for the date " + date + " is a" , days[dday])
    return dday

def Day(date):
    date = prepare(date)
    doomsday = dd(date)
    (day, month, year) = date_indicator(date)
    doomsdays = {1: 3, 2: 28, 3: 7, 4: 4, 5: 9, 6: 6, 7: 4, 8: 8, 9: 5, 10: 10, 11: 7, 12:12}
    if year%4==0 and (month == 1 or month ==2):
        doomsdays[1] = 4
        doomsdays[2] = 29
    return (doomsday + day - doomsdays[month])%7

def test():
    month_days = {1: 30, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9:30, 10:31, 11:30, 12:31 }
    days = {'Sunday': 0, 'sunday': 0, 'Monday': 1, 'monday': 1,
            'Tuesday': 2, 'tuesday': 2, 'Wednesday': 3, 'wednesday': 3,
            'Thursday': 4, 'thursday': 4, 'Friday': 5, 'friday': 5,
            'Saturday': 6, 'saturday': 6}
    points = 0
    questions = 5
    start = time.time()
    for i in range(questions):
        month = random.randint(1,12)
        day = random.randint(1,month_days[month])
        year = random.randint(1900,2099)
        
        if day<10:
            day_str = '0' + str(day)
        else:
            day_str = str(day)
            
        if month<10:
            month_str = '0' + str(month)
        else:
            month_str = str(month)
            
        year_str = str(year)
        
        date = day_str + '/' + month_str + '/' + year_str
        
        print('(' + str(i) + '/' + str(questions) + '). What day was the ' + date + '?')
        answer = input('Your answer: ')
        answer = str(answer)
        if answer == 'quit':
            sys.exit()
        while answer not in days.keys():
            print('That is not a valid day.')
            answer = input('Your answer: ')
            answer = str(answer)  
            if answer == 'quit':
                sys.exit()
        point =1        
        while days[answer] != Day(date):
            point = 0
            answer = input('Incorrect, try again. Your answer: ')
            answer = str(answer)
            while answer not in days.keys():
                print('That is not a valid day.')
                answer = input('Your answer: ')
                answer = str(answer)
                if answer == 'quit':
                    sys.exit()
        
        points = points + point
        print('Correct!\n')
    end = time.time()
    print('You scored ' + str(points) + '/' + str(questions) + '.')
    print('Time elapsed was ' + "{0:.2f}".format(end-start) + ' seconds.')
        
        