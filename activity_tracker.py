import time

def track_activity():
    while True:
        activity = input("What are you doing? ")
        print(f"You are doing: {activity}")
        time.sleep(60)  # Wait for 60 seconds

if __name__ == "__main__":
    track_activity()
