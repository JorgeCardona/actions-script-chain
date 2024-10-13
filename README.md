# actions-script-chain
[![Execute Scripts](https://github.com/JorgeCardona/actions-script-chain/actions/workflows/multi_scripts.yml/badge.svg)](https://github.com/JorgeCardona/actions-script-chain/actions/workflows/multi_scripts.yml)
---

# GitHub Actions: Passing Results Between Scripts

This repository contains a GitHub Actions workflow that runs multiple Python scripts in sequence, passing the results from one script to the next.

## Scripts

1. **get_utc5_time.py**: Generates the current time in the UTC-5 timezone.
2. **sum_date_time_parts.py**: Sums the parts of a given date and time.
3. **divide_values.py**: Divides two numerical values resulting from the previous script.

## Project Workflow

The workflow follows these steps:

1. **Get UTC-5 Time**  
   The `get_utc5_time.py` script generates the current date and time in UTC-5, and its result is stored in an environment variable. This allows other scripts to use this information without having to run it again.

2. **Sum Date and Time Parts**  
   Using the generated date and time, the `sum_date_time_parts.py` script separates the date (YYYY-MM-DD) and time (HH:MM:SS) parts, sums the digits of each part, and stores the result as an environment variable.

3. **Divide the Results**  
   Finally, the `divide_values.py` script takes the sums from the previous step and divides them, printing the final division result.

## Workflow Setup

The `.github/workflows/multi_scripts.yml` file manages the execution of these scripts in sequence.

```yaml
name: Execute Scripts

on:
  push:
    branches:
      - main

jobs:
  run_scripts:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v4

    - name: List Files in Directory
      run: |
        echo "Listing files in the repository..."
        ls -R  # List all files recursively

    - name: Run get_utc5_time.py
      id: get_time
      run: |
        output=$(python src/get_utc5_time.py)
        echo "current_time=${output}" >> $GITHUB_ENV  # Store the output in an environment variable
              
    - name: Run sum_date_time_parts.py
      id: sum_parts
      run: |
        # Capture the output from the previous script
        date_time_output="${{ env.current_time }}"
        values=$(python src/sum_date_time_parts.py "$date_time_output")
        echo "tuple_values=$(echo $values | tr -d '() ')" >> $GITHUB_ENV  # Store the output in an environment variable        

    - name: Run divide_values.py
      run: |
        # Capture the sum result from the previous step
        sum_output="${{ env.tuple_values }}"
        date_sum=$(echo "$sum_output" | cut -d',' -f1)  # Obtener la suma de la fecha
        time_sum=$(echo "$sum_output" | cut -d',' -f2)  # Obtener la suma del tiempo
        python src/divide_values.py $date_sum $time_sum
```

### Steps Explanation

- **Checkout Repository**: Clones the repository where the scripts are stored.
- **List Files**: Lists all the files in the repository (optional, but useful for debugging).
- **Run get_utc5_time.py**: Retrieves the current time in UTC-5 and stores it in the `current_time` environment variable.
- **Run sum_date_time_parts.py**: Uses `current_time` to sum the date and time parts, storing the result as `tuple_values`.
- **Run divide_values.py**: Takes the results from `tuple_values` and divides them, printing the final result.

## Scripts

### get_utc5_time.py
Generates the current time in UTC-5.

```python
from datetime import datetime, timedelta, timezone

def get_utc5_time():
    # Get the current time in UTC-5
    utc_offset = timedelta(hours=-5)
    current_time = datetime.now(timezone.utc) + utc_offset
    return current_time.strftime("%Y-%m-%d %H:%M:%S")  # Time format

if __name__ == "__main__":
    result = get_utc5_time()
    print(result)  # This is the one that will be captured in the workflow
```

### sum_date_time_parts.py
Sums the date and time parts by separating and adding the numerical values.

```python
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
```

### divide_values.py
Divides two values, with a check to avoid division by zero.

```python
import sys

def divide_values(value1, value2):
    # Check to avoid division by zero
    if value2 == 0:
        return "Error: Cannot divide by zero."

    print('value1',value1)
    print('value2',value2)
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
```

## How It Works

1. **`get_utc5_time.py`** runs first to generate the current UTC-5 time.
2. **`sum_date_time_parts.py`** takes the date and time, sums the digits of both, and stores the result.
3. **`divide_values.py`** takes the sum results and divides them.

This process ensures that results flow correctly from one script to another in the GitHub Actions workflow.

---
