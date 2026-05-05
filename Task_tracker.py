# This project will ask the user to enter their completed or
# Unfinished task and export them to file to be emailed on a specific
# date


# Gather information from the user

first_name = input("Please enter your first name: ").title()

print(f"Hello and welcome back {first_name}")
tasks = []
while True:
    user_choice = input("\nPlease enter a choice.\n "
                        "(a) to add task.\n " 
                        "(b) to add a task for next week.\n "
                        "(v) to view the task.\n "
                        "(exit) to quit.\n ").strip().lower()
    
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
    
    elif user_choice == 'v':
        print(f'\nThese are your current items: ')
        for item in tasks:
            if item['timeframe'] == 'current':
               print(f" {item['name']}")

        print(f'\nThese are your future events: ')     
        for item in tasks:
            if item['timeframe'] == 'future':
               print(f" {item['name']}")
    else:
        print("Please enter one of the choices")


"""
for item in tasks:
    if item['timeframe'] == 'current':
        print(f'These are your current items: ')
        print(f" {item['name']}")
    else:
        print(f'These are your future events: ')
        print(f" {item['name']}")
        """





