# 📖 Quran Daily Bot

A Telegram bot that automatically sends a daily Quran reading check-in message to a group — including the date, day name, Ramadan day number, member list, and a rotating Ayah or Du'a in Arabic.

Built with Python and hosted on Railway for 24/7 uptime.

---

## ✨ Features

- 📅 Sends a daily message automatically at 8:00 AM
- 🌙 Tracks and displays the current Ramadan day
- 📋 Lists all group members so they can log their progress
- 🤲 Rotates a different Ayah or Du'a every day
- ☁️ Runs 24/7 on Railway — no need to keep your laptop on

---

## 🛠️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
Create a `.env` file or set these in Railway:
```
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_group_chat_id
```

### 4. Run locally
```bash
python quran_bot.py
```

---

## 🚀 Deploy on Railway

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) and create a new project from this repo
3. Add `BOT_TOKEN` and `CHAT_ID` as environment variables in Railway
4. Deploy — done! 🎉

---

## 📁 File Structure
```
quran-daily-bot/
├── quran_bot.py       # Main bot script
├── requirements.txt   # Python dependencies
├── Procfile           # Railway process config
└── README.md          # This file
```

---

