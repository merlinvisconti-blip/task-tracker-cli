# This project will ask the user to enter their completed or
# Unfinished task and export them to file to be emailed on a specific
# date


# Gather information from the user

first_name = input("Please enter your first name: ").title()

print(f"Hello and welcome back {first_name}")
tasks = []
while True:
    user_choice = input("\nPlease enter a choice (a) to add task or " 
                        "b to add a task for next week or (exit) to quit ").lower()
    
    if user_choice == 'exit':
        break
    elif user_choice == 'a':
        current_task = input("What task would you like to add for this week: ")
        task = {
            'name': current_task,
            'timeframe': 'current',
        }
        tasks.append(task)
    elif user_choice == 'b':
        future_task = input("What task would you like to add for next week: ")
        
        task = {
            'name': future_task,
            'timeframe': 'future',
        }
        tasks.append(task)
    else:
        print("Please enter one of the choices")

print("\nThese are your task for this week: ")

for item in tasks:
    if item['timeframe'] == 'current':
        print(f'These are your current items: ')
        print(f" {item['name']}")
    else:
        print(f'These are your future events: ')
        print(f" {item['name']}")
        





