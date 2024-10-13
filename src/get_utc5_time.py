from datetime import datetime, timedelta

def get_utc5_time():
    # Get the current time in UTC-5
    utc_offset = timedelta(hours=-5)
    current_time = datetime.utcnow() + utc_offset
    final_time = current_time.strftime("%Y-%m-%d %H:%M:%S")  # Time format
    print("get_utc5_time Result:", final_time)  # Print the get_utc5_time result
    return final_time

if __name__ == "__main__":
    result = get_utc5_time()
    print(result)  # Print the time to capture it in the workflow