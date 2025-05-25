from datetime import datetime, timedelta
from plyer import notification
import time
import json
def load_festivals(filename='festivals.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def check_upcoming_festivals(festivals, days_notice=3):
    today = datetime.now().date()
    for name, date_str in festivals.items():
        fest_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        delta = (fest_date - today).days
        if 0 <= delta <= days_notice:
            send_notification(name, fest_date, delta)
def send_notification(name, date, days_left):
    message = f"{name} is in {days_left} day(s) on {date.strftime('%d %B %Y')}!"
    notification.notify(
        title="Festival Reminder 🎉",
        message=message,
        timeout=10
    )
def add_festival(festivals, filename='festivals.json'):
    name = input("Enter festival name: ")
    date_str = input("Enter festival date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")  # Validate date
        festivals[name] = date_str
        with open(filename, 'w') as file:
            json.dump(festivals, file, indent=4)
        print(f"Added {name} on {date_str}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
def run_bot():
    festivals = load_festivals()
    while True:
        check_upcoming_festivals(festivals)
        print("Checked reminders. Sleeping for 24 hours...")
        time.sleep(86400)  # 24 hours
def main():
    festivals = load_festivals()
    while True:
        print("\n1. View Reminders\n2. Add Festival\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            check_upcoming_festivals(festivals)
        elif choice == '2':
            add_festival(festivals)
            festivals = load_festivals()  # Reload after adding
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
