"""
Assignment 1

Author: Woosung Kim
Date: Oct. 13, 2021

PROBLEM: You have too many important dates written down on your notebook, but
    don't have enough time to organize them. 
TASK: Build a program that'll help you organize your schedule.
"""

#This varible is made to hold onto the list of dates
#Right now it only holds the word "blank" so that the index value doesn't
#come out as error in the while loop
list_of_dates = ["blank"]

#This prints out "List the important dates"
print("\nList the important dates as follows: Month/Day/Year(i.e. 01/01/2003) and Task. \
Press enter after one date. Type \"done\" when done.")

#This loop asks the user to input an important date with it's task and prints out their 
#list, until they type "done"
while list_of_dates[-1] != "done":
    print("")
    dates = str(input("Date + Task: "))
    if list_of_dates[-1] == "blank":
        list_of_dates.remove("blank")
    list_of_dates.append(dates)
    print(list_of_dates)

#This function organizes the dates so that it prioritizes the year, month, then day
def date_order(date):
    return date[6:10], date[:2], date[3:5]

#This sorts the list of dates to match the function "date_order"
list_of_dates.sort(key = date_order)

#Removes the "done" in the list
list_of_dates.remove("done")

#This print "[List of Important Dates]", this will be a header to keep things organized
print("\n    [List of Important Dates]")

#This for loop prints each dates in order going from the earliest due date to the latest
for i in range(len(list_of_dates)):
    x=i+1
    print(f"{x}. {list_of_dates[i]}")

#Asks the user if they would like to edit anything
edit = input("\nWould you like to edit the list above?\n(Yes/No): ")

#This while loop keeps going until the user responds the "edit" input 
#anything other than yes
#This loop has 3 purpose: to edit a date, add more to list, and/or see in reverse order
while edit == "Yes" or edit == "yes":

    #Asks user what they would like to do today
    what = input("\nWhat would you like to do?\n(add more to list/edit a date/\
see in reverse order): ")

    #This if statement checks if the user typed in "add more to list"
    if what == "add more to list":

        #These codes are the same as the few bunch from the beginning to add to list
        #and to organize them
        while list_of_dates[-1] != "done":
            print("")
            dates = str(input("Date + Task: "))
            list_of_dates.append(dates)
            print(list_of_dates)
        list_of_dates.remove("done")
        list_of_dates.sort(key = date_order)
        print("\n    [List of Important Dates]")
        for i in range(len(list_of_dates)):
            x=i+1
            print(f"{x}. {list_of_dates[i]}")

    #This if statement checks if the user typed in "edit a date"
    elif what == "edit a date":

        #Asks the user which date they'd like to change
        which = int(input("\nwhich date in the list would you like to change?\n(i.e. 2): "))

        #This just prints some intructions
        print("If you'd like to remove this just type \"done\".")

        #This switches the selected item in list with a new input
        list_of_dates[which-1] = input("\nDate + Task: ")

        #checks if "done" is in the list and removes it
        if list_of_dates[which-1] == "done":
            list_of_dates.remove("done")
        
        #Sorts the dates in list
        list_of_dates.sort(key = date_order)

        #Prints the list of important dates in order
        print("\n    [List of Important Dates]")
        for i in range(len(list_of_dates)):
            x=i+1
            print(f"{x}. {list_of_dates[i]}")

    #Checks if user typed "see in reverse order"
    elif what == "see in reverse order":

        #This sorts the list in reverse of the date_order function
        list_of_dates.sort(reverse=True, key=date_order)
        print("\n    [List of Important Dates in Reverse Order]")
        for i in range(len(list_of_dates)):
            x=i+1
            print(f"{x}. {list_of_dates[i]}")

    else:
        print("\n-That's not one of the options-\n")
    
    #Asks the user if they would like to edit 
    #This is to be able to break the while loop, since it depends on "edit" being anything
    #other then "yes" or  "Yes" to stop
    edit = input("Would you like to edit the list above?\n(Yes/No): ")









