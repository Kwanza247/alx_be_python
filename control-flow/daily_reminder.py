# daily_reminder.py

# Prompt the user to enter a single task
task = input("Enter your task: ")

# Ask for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priority levels (Python 3.10+)
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires " 
            "immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to " 
            "schedule time for it today.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should " 
            "be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to get " 
            "it done soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that still" 
            "requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing " 
            "it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
