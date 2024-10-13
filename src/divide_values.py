import sys

def divide_values(value1, value2):
    # Check to avoid division by zero
    if value2 == 0:
        return "Error: Cannot divide by zero."

    # Divide the first value by the second
    division_result = float(value1) / float(value2)
    
    # Check if the result is an exact integer
    if division_result.is_integer():
        return int(division_result)  # Return as integer if exact
    else:
        return round(division_result, 2)  # Round to 2 decimal places

def main():
    # Print the name of the script
    script_name = sys.argv[0]
    print(f"Running script: {script_name}")

    # Check if exactly 2 values are provided (script name + 2 values)
    if len(sys.argv) == 3:  # Length must be 3: script name + 2 arguments
        try:
            value1 = sys.argv[1]  # First argument
            value2 = sys.argv[2]  # Second argument
        except ValueError:
            print("Please enter valid numbers for value1 and value2.")
            sys.exit(1)
        
        # Call the divide function and print the result
        result = divide_values(value1, value2)
        print("Division Result:", result)  # Print the division result
        print(result)  # Print the division result
    else:
        print("Usage: python divide_values.py <value1> <value2>")
        sys.exit(1)

if __name__ == "__main__":
    main()