from datetime import datetime, timedelta

def get_utc5_time():
    # Get the current time in UTC-5
    utc_offset = timedelta(hours=-5)
    current_time = datetime.utcnow() + utc_offset
    return current_time.strftime("%Y-%m-%d %H:%M:%S")  # Time format

if __name__ == "__main__":
    result = get_utc5_time()
    print("sum_parts Result:", result)  # Print the sum_parts result
    print(result)  # Print the time to capture it in the workflow