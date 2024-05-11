import expFunctions
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates
import datetime

expenditures = []

expenditures.append(["Food", 23, datetime.date(2023, 4, 28)])
expenditures.append(["Video-games", 122, datetime.date(2023, 8, 13)])
expenditures.append(["Coffee", 14, datetime.date(2024, 2, 24)])
expenditures.append(["New TV", 632, datetime.date(2024, 3, 9)])
expenditures.append(["A nice shirt", 42, datetime.date(2024, 4, 6)])
expenditures.append(["Watch repair", 42, datetime.date(2024, 4, 17)])
expenditures.append(["A nice shirt", 42, datetime.date(2024, 5, 3)])
expenditures.append(["A few beers", 17, datetime.date(2024, 5, 7)])

should_continue = True

while should_continue:
    print("Add an expanditure: \n")
    expenditures.append(expFunctions.store_date())
    invalid_input = True
    while invalid_input:
        keep_going = input("Expanditure added. Do you want to add another expanditure?(y/n) Enter: ")
        if(keep_going == "y"):
            invalid_input = False
        elif(keep_going == "n"):
            invalid_input = False
            should_continue = False
        else:
            print("Invalid input, answer should be y or n.\n")


if __name__ == "__main__":
    tot = 0
    xvalues = []
    yvalues = []
    for n in expenditures:
        xvalues.append(n[2])
        yvalues.append(n[1])
    for n in expenditures:
        tot = tot + n[1]
    if expenditures is not None:
        print("Current expanditures:\n", pd.DataFrame(expenditures, columns=['Expanditure', 'Cost', 'Date']))
        print("Total expanditures: ", tot, "€")
    plt.plot(xvalues, yvalues, marker='o')  # Plot the expenditures
    plt.xlabel('Date')
    plt.ylabel('Cost (€)')
    plt.title('Expenditures Over Time')
    plt.show()