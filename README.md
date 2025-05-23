# remind-me-later
This web app does one thing and one thing well. It allows users to setup a reminder with a message.
# 🕒 Remind-me-later API

A simple Django REST API that allows users to set reminders by specifying a date, time, message, and delivery method (Email or SMS). This backend is designed to work with an existing frontend that handles user input.

---

## 📌 Features

- Accepts reminders with:
  - Date
  - Time
  - Message
  - Delivery method (`email` or `sms`)
- Stores reminders in the database
- API built using Django and Django REST Framework
- Clean and extensible structure (easy to support more delivery methods later)

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default)

---

### 1. Clone the repository

```bash
git clone https://github.com/tsakina/remind-me-later.git
cd remind-me-later

### 2. Create and activate virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4.  Run migrations
python manage.py makemigrations
python manage.py migrate

### 5. Start development server
python manage.py runserver

Visit:
http://127.0.0.1:8000/api/reminders/

API Usage
POST /api/reminders/

{
  "date": "2025-05-23",
  "time": "15:00:00",
  "message": "Dentist appointment",
  "remind_by": "sms"
}

Valid values for remind_by:
email
sms





