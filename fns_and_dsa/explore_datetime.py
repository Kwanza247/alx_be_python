# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in the format YYYY-MM-DD HH:MM:SS"""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print("Current date and time:", formatted_date)

def calculate_future_date():
    """Calculates and displays the future date after adding user-specified days"""
    try:
        # Prompt the user to enter number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get current date again
        future_date = current_date + timedelta(days=number_of_days)  # Add days
        print("Future date:", future_date.strftime("%Y-%m-%d"))  # Format and print
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Call the functions
display_current_datetime()
calculate_future_date()
