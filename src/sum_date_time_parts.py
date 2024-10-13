import sys

def sum_parts(date_time_str):
    # Split the string into two parts by the space
    date_part, time_part = date_time_str.split()

    # Sum the numbers of the date part
    date_numbers = map(int, date_part.split('-'))
    date_sum = sum(date_numbers)

    # Sum the digits of the time part
    time_sum = sum(int(digit) for digit in time_part if digit.isdigit())

    # Return the result as a simple string
    return f"{date_sum},{time_sum}"

def main():
    # Check if the script received the correct number of arguments
    if len(sys.argv) == 2:  # Ensure exactly 1 argument is provided
        # Get the date-time string from command line arguments
        date_time_example = sys.argv[1]
        result = sum_parts(date_time_example)
        print(result)  # Print the result as "date_sum,time_sum"
    else:
        print("Usage: python sum_date_time_parts.py 'YYYY-MM-DD HH:MM:SS'")
        sys.exit(1)

if __name__ == "__main__":
    main()