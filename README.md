# 📱 WhatsApp Smart Scheduler & Bulk Sender

A modular, robust, and secure Python application for scheduling and sending bulk WhatsApp messages using the **Twilio API** and **Pandas**. Built with clean architecture principles, smart CSV column detection, automatic retries for failed messages, and environment-variable security.

---

## 🌟 Key Features

- **📂 Smart CSV Column Detection:** Automatically identifies customer name and phone number columns regardless of column naming conventions.
- **🕒 Precision Scheduling:** Schedule broadcasts for specific dates and times with automatic countdown execution.
- **🔄 Auto-Retry Logic:** Automatically attempts to resend failed messages after a short cooldown period.
- **📊 Error Logging & Diagnostics:** Logs permanently failed messages into a structured `failed_messages.csv` file for easy debugging.
- **🔒 Security-First Architecture:** Keeps API credentials secure using `.env` files and prevents accidental leaks via `.gitignore`.
- **🧩 Clean Modular Design:** Codebase is structured into specialized modules (`config.py`, `utils.py`, `sender.py`, `main.py`).

---

## 🏗️ Project Architecture

```
whatsapp_automation/
│
├── config.py             # Configuration & environment variables setup
├── utils.py              # Helper functions (CSV loading, number formatting, detection)
├── sender.py             # Twilio API broadcast & retry execution logic
├── main.py               # Application entry point & interactive UI logic
│
├── .env                  # Private credentials (Git Ignored)
├── .env.example          # Environment variables template for public repo
├── .gitignore            # Git exclusion rules
├── customers_demo.csv    # Sample data file for local testing
└── README.md             # Project documentation
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Qaem-Rizz/Automatic_Message_Scheduler.git
cd Automatic_Message_Scheduler
```

### 2. Set Up a Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\Activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pandas twilio python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory (refer to `.env.example`):

```env
TWILIO_ACCOUNT_SID=your_actual_account_sid
TWILIO_AUTH_TOKEN=your_actual_auth_token
TWILIO_SENDER_NUMBER=whatsapp:+14155238886
```

---

## 💻 Usage

Run the main application:

```bash
python main.py
```

### Interactive Steps:
1. **Enter CSV Path:** Provide your CSV file (e.g., `customers_demo.csv`).
2. **Confirm Column Mapping:** The system auto-detects name and phone columns; confirm or select if prompted.
3. **Draft Message:** Write your message template. Use `{Name}` to dynamically insert recipient names.
4. **Set Schedule:** Enter the date (`YYYY-MM-DD`) and time (`HH:MM` 24-hr format).
5. **Execution:** Sit back while the application waits for the scheduled time and executes the broadcast!

---

## ⚙️ Twilio Account Notes

- **Sandbox / Trial Account:** Requires recipient numbers to be manually verified via WhatsApp before receiving messages. Ideal for testing and learning.
- **Production / Business Account:** Requires a verified **WhatsApp Business API (WABA)** profile and approved Meta content templates for unconstrained bulk broadcasting.

---

