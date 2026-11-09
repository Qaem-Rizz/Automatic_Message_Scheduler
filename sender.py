import time as time_module
import pandas as pd
from twilio.rest import Client
from config import (
    ACCOUNT_SID,
    AUTH_TOKEN,
    TWILIO_SENDER_NUMBER,
    DEFAULT_COUNTRY_CODE,
)
from utils import format_phone_number

# Initialize Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_bulk_broadcast(df, name_col, number_col, message_template):
  """Executes the main broadcast, handles errors, performs automatic retries, and logs failures safely."""
  print(
      "\n[Triggered] Scheduled time reached! Starting main message broadcast..."
  )
  success_count = 0
  failed_records = []

  # 1. Main Broadcast Loop
  for index, row in df.iterrows():
    name = str(row[name_col]).strip()
    raw_number = str(row[number_col]).strip()
    number = format_phone_number(raw_number, DEFAULT_COUNTRY_CODE)

    # Handle both {Name} and {name} placeholders safely
    personalized_message = (
        message_template.replace("{Name}", name)
        .replace("{name}", name)
        .replace("{NAME}", name)
    )

    try:
      message = client.messages.create(
          from_=TWILIO_SENDER_NUMBER,
          to=f"whatsapp:{number}",
          body=personalized_message,
      )
      print(
          f"[Main][{index+1}] Sent to {name} ({number}) successfully! SID:"
          f" {message.sid}"
      )
      success_count += 1
    except Exception as e:
      print(f"[Main][{index+1}] Failed to send to {name} ({number}): {e}")
      failed_records.append({
          "Name": name,
          "Number": number,
          "Error_Reason": str(e).replace("\n", " "),
      })

  # 2. Automatic Retry Mechanism
  retry_success_count = 0
  truly_failed_records = []

  if failed_records:
    print(
        f"\n--- Starting Automatic Retry for {len(failed_records)} failed"
        " message(s) ---"
    )
    time_module.sleep(2)  # Short delay to prevent API rate-limiting

    for record in failed_records:
      name = record["Name"]
      number = record["Number"]
      personalized_message = (
          message_template.replace("{Name}", name)
          .replace("{name}", name)
          .replace("{NAME}", name)
      )

      try:
        message = client.messages.create(
            from_=TWILIO_SENDER_NUMBER,
            to=f"whatsapp:{number}",
            body=personalized_message,
        )
        print(
            f"[Retry] Sent to {name} ({number}) successfully! SID:"
            f" {message.sid}"
        )
        retry_success_count += 1
        success_count += 1
      except Exception as e:
        print(f"[Retry] Failed again for {name} ({number}): {e}")
        truly_failed_records.append({
            "Name": name,
            "Number": number,
            "Error_Reason": str(e).replace("\n", " "),
        })

  # 3. Save permanently failed records to CSV log file
  fail_count = len(truly_failed_records)
  if truly_failed_records:
    failed_df = pd.DataFrame(truly_failed_records)
    failed_filename = "failed_messages.csv"
    failed_df.to_csv(failed_filename, index=False)
    print(
        f"\n[Log Saved] Details of {fail_count} permanently failed messages"
        f" have been saved to '{failed_filename}'."
    )

  print(
      f"\n=== Broadcast Summary ==="
      f"\nTotal Successful Deliveries: {success_count}"
      f" (Main: {success_count - retry_success_count} | Retry:"
      f" {retry_success_count})"
      f"\nPermanently Failed: {fail_count}"
  )