from datetime import datetime
import time as time_module
from sender import send_bulk_broadcast
from utils import load_and_map_contacts


def main():
  print("=== Modular Bulk WhatsApp Message Scheduler ===")

  # 1. Load and Map Contacts CSV
  filename = input(
      "Enter your CSV file name/path (e.g., customers.csv): "
  ).strip()
  df, name_col, number_col = load_and_map_contacts(filename)

  if df is None:
    return

  # 2. Take User Inputs for Message and Schedule Time ONCE
  message_template = input(
      "\nEnter the message you want to send (Tip: use {Name} to personalize): "
  )
  date_str = input(
      "Enter the date to send the messages (Format - YYYY-MM-DD): "
  ).strip()
  time_str = input(
      "Enter the time to send the messages (24-hour format - HH:MM): "
  ).strip()

  # 3. Calculate Delay Time
  try:
    datetime_str = f"{date_str} {time_str}"
    scheduled_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
  except ValueError:
    print(
        "Invalid date or time format entered! Please use YYYY-MM-DD and HH:MM."
    )
    return

  current_datetime = datetime.now()
  delay_seconds = (scheduled_datetime - current_datetime).total_seconds()

  if delay_seconds <= 0:
    print(
        "The specified time is in the past! Please enter a future date and"
        " time."
    )
    return

  print(
      f"\nAll messages are successfully scheduled for {scheduled_datetime}."
  )
  print(f"Waiting for {round(delay_seconds, 2)} seconds...")

  # 4. Sleep until target delivery time
  time_module.sleep(delay_seconds)

  # 5. Hand over to Sender module
  send_bulk_broadcast(df, name_col, number_col, message_template)


if __name__ == "__main__":
  main()