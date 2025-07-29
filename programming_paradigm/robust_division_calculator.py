def safe_divide(numerator, denominator):
    try:
        # convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try to dividr the numbers
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # This runs if the denominator is 0
        return "Error: Cannot divide by zero."

    except ValueError:
        #This runs if input cant be converted to float
        return "Error: please enter numeric values only."