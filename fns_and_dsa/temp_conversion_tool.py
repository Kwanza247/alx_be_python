
# Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Conversion Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# User Interaction
def main():
    print("Temperature Conversion Tool")
    choice = input("Choose conversion: (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius: ")
    try:
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
        else:
            print("Invalid option. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Entry Point
if __name__ == "__main__":
    main()
