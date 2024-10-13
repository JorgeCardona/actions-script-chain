from datetime import datetime, timedelta

def get_utc5_time():
    # Get the current time in UTC-5
    utc_offset = timedelta(hours=-5)
    current_time = datetime.utcnow() + utc_offset
    return current_time.strftime("%Y-%m-%d %H:%M:%S")  # Time format

if __name__ == "__main__":
    result = get_utc5_time()
    print("Current UTC-5 Time:", result)  # This is for reference only
    print(result)  # This is the one that will be captured in the workflow