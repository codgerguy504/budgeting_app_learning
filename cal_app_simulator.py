
#import necessary libraries
import random #for generating random numbers to simulate AI behavior
import datetime #for managing dates
import time #to simulate the passage of time for notifications

# create function to simulate the user entering a new event into their calendar
def add_event(events):
    event_name = input("Enter a name for your event: ")
    while True:
        try:
            event_date_str = input("Enter a date for your event in the following format (YYYY-MM-DD): ")
            event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d").date() # strptime converts event date string into an date time object
            break
        except ValueError:
            print("Invalid input. Please enter a valid date.")
    #event_cost = random.randint(10,100) if event_name.lower() == "dinner" else 0 # creates random cost for dinner to simulate AI
    if event_name.lower() == "dinner":
        event_cost = random.randint(10,100)
    elif event_name.lower() == "lunch":
        event_cost = random.randint(10,100)
    else: event_cost = 0

    events.append({"name": event_name, "date": event_date, "cost": event_cost})
    print(f"Event '{event_name}' added for {event_date} with an estimated cost of ${event_cost}.")

def track_budget(income, events):
    total_expenses = 0
    print("\n --- Upcoming Events ---")

    for event in events:
        print(f"{event ['name']} on {event ['date']}| Estimated Cost: ${event ['cost']}")
        total_expenses += event ['cost']

    balance = income - total_expenses
    print("\n --- Budget Summary ---")
    print(f"Total Income: ${income: .2f}")
    print(f"Total Expenses: ${total_expenses: .2f}")
    print(f"Balance: ${balance: .2f}")

"""Use random number generator to simulate using
    an AI to average the dinner cost for a restaurant"""
def ai_dinner_costs(events):
    for event in events:
        if event["name"].lower() == "dinner":
            avg_dinner_cost = random.randint(20,50)
            print(f"Your upcoming bill will likely cost around ${avg_dinner_cost}.")
            event['cost'] = avg_dinner_cost
        elif event["name"].lower() == "lunch":
            avg_lunch_cost = random.randint(20,50)
            print(f"Your upcoming bill will likely cost around ${avg_lunch_cost}.")
            event['cost'] = avg_lunch_cost

"""simulate sending reminders if 
the event happens the day of"""
def send_reminder(events, current_date):
    for event in events:
        if event["date"] == current_date:
            print(f"Reminder! You have an event today: {event['name']} that will cost about ${event['cost']}.")

#put the entire program together
def main_program():
    income = float(input("Enter your total income: "))
    events = []

    while True:
        action = input("\n Choose action: \n1. Add Event\n2. Track Budget\n3. AI Prediction\n4. Send Reminder\n5. Exit\nYour Choice: ")
        if action == "1":
            add_event(events)
        elif action == "2":
            track_budget(income, events)
        elif action == "3":
            ai_dinner_costs(events)
        elif action == "4":
            current_date_str = input("Enter current date in the following format (YYYY-MM-DD): ")
            current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
            send_reminder(events, current_date)
        elif action == "5":
            print("Goodbye! :)")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main_program()