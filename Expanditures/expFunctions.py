import datetime
import string

def store_date():
    while True:  # Loop until a valid date is entered
        try:
            name = input("What is the name of the expenditure? Enter value: ")
            cost = float(input("How much was the expenditure? Enter value in euro: "))
            year = int(input("What year was the expenditure? Enter year: "))
            month = int(input("What month (1-12) was the expenditure? Enter month: "))
            day = int(input("What day (1-31) was the expenditure? Enter day: "))
            # Check if the date is valid
            datetime.date(year, month, day)
            if not(datetime.datetime.now().year >= year): # Checks if input year is greater than current year.
                raise ValueError("Input year can't be larger than the current year.")
            if not(12 >= month > 0): # Makes sure month can't be greatar than 12 or less than 1..
                raise ValueError("Input month can't be larger than 12 or less than 1.")
            if not(31 >= day > 0): # Makes sure date is 31 or less, and greater than 0.
                raise ValueError("Input day can't be larger than 31 or smaller than 1.")
            return [name, cost, datetime.date(year, month, day)]
        except ValueError as e: # In case datetime.date still returns an error (i.e., February 31 is not a valid date)
            print("Error: Please enter a valid value for the year, month, and day. ", e)