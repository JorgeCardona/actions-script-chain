from datetime import datetime, timedelta

def main():
    # Get the current time in UTC-5
    utc_offset = timedelta(hours=-5)
    current_time = datetime.utcnow() + utc_offset
    return current_time.strftime("%Y-%m-%d %H:%M:%S")  # Time format

if __name__ == "__main__":
    result = main()
    print(result)  # Print the time to capture it in the workflow