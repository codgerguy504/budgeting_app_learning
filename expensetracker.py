# ask for users income:

#Function to make sure a positive number is entered:
def get_positive_number(prompt):
    while True:
        try: 
            number = float(input(prompt))
            if number < 0:
                print("Please enter a positive number for your income.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get Income
income = get_positive_number("Enter your total income: ")

# ask for expenses

#1. create a list called expenses that you can add all the user's expenses to
expenses = []
#2. use a while loop to continuously perform a function until the break quality is fulfilled
while True:
    try:
        expense = input("Enter an expense or type 'done' to finish: ")
        if expense.lower() == 'done':
            break
    # use the try and except function to avoid crashing your program if an invalid value is submitted
        else:
            positive_number = float(expense)
            if positive_number >= 0:
                expenses.append(float(expense))
            else:
                print("Please enter a positive number for your expense.")
    except ValueError:
        print("Please enter valid number for the expense")
        
#3. sum all the expenses and calculate the difference
total_expenses = sum(expenses)
balance = income - total_expenses

"""print summary of the results, the f function allows to format 
and insert values into a string, and the .2f 
that there are 2 more decimals added to the end of the Value
 to make it look like a dollar sign"""

print("Budget Summary:")
print(f"Total income: ${income: .2f}")
print(f"Total expenses: ${total_expenses: .2f}")
print(f"Final balance: ${balance: .2f}")





    