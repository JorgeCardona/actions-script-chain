import sys

def sum_parts(date_time_str):
    try:
        # Split the string into two parts by the space
        date_part, time_part = date_time_str.split()

        # Sum the numbers of the date part
        date_numbers = map(int, date_part.split('-'))
        date_sum = sum(date_numbers)

        # Sum the digits of the time part
        time_sum = sum(int(digit) for digit in time_part if digit.isdigit())

        # Return the tuple with the two values
        return (date_sum, time_sum)

    except ValueError:
        # Handle cases where the string format is incorrect
        print("Error: Invalid date-time format. Expected 'YYYY-MM-DD HH:MM:SS'")
        sys.exit(1)

def main():
    # Print the name of the script
    script_name = sys.argv[0]
    print(f"Running script: {script_name}")

    # Check if the script received the correct number of arguments
    if len(sys.argv) == 2:  # Ensure exactly 1 argument is provided
        # Get the date-time string from command line arguments
        date_time_example = sys.argv[1]
        result = sum_parts(date_time_example)
        #print("sum_parts Result:", result)  # Print the sum_parts result
        print(f"{result[0]},{result[1]}")  # Print the result as comma-separated values
    else:
        print("Usage: python sum_date_time_parts.py 'YYYY-MM-DD HH:MM:SS'")
        sys.exit(1)

if __name__ == "__main__":
    main()