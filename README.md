# 🎉 Festival Reminder Bot

A Python-based CLI bot that reminds you of upcoming festivals via desktop notifications. You can view, add, and manage festival dates, and the bot will alert you a few days in advance!

---

## 🛠️ Features

- 📅 Store and manage festival dates
- ⏰ Reminders via system notifications using `plyer`
- 🧠 Customizable reminder window (e.g., 3 days before)
- 💾 Saves data persistently using JSON
- ✅ Validates date input format
- 🔁 Optionally runs periodically to check reminders daily

---

## 📦 Requirements

- Python 3.6+
- `plyer` library for notifications

Install dependencies:
```bash
pip install plyer

📂 Project Structure
festival-reminder-bot/
│
├── festivals.json        # Stores all the festival dates
├── main.py               # Main CLI bot logic
└── README.md             # Project documentation

🚀 How to Run
Clone the repository or download the files.

Make sure festivals.json is in the same folder as main.py.

Run the bot using:
python main.py

🎮 Usage Guide
When you run the bot, you’ll see a menu like:

1. View Reminders
2. Add Festival
3. Exit

➕ Add a Festival
Enter the name of the festival.

Enter the date in YYYY-MM-DD format.

Example:
Enter festival name: Diwali
Enter festival date (YYYY-MM-DD): 2025-10-20

🔔 View Reminders
The bot will notify you of any festivals occurring within the next 3 days (configurable).

🔁 Optional: Auto Run Daily
To make the bot run continuously and check reminders every 24 hours, modify main.py to call the run_bot() function instead of the CLI menu:

if __name__ == "__main__":
    run_bot()

⚠️ Error Handling
Invalid date formats are rejected with a helpful message.

Handles missing or corrupted festivals.json file by creating a new one.

🌟 Future Improvements
📧 Send email or SMS reminders

🖼️ GUI version using Tkinter

📆 Sync with Google Calendar

