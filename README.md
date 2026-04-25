# 📊 Stock Data Desktop App

> Desktop application for stock market data analysis, news tracking, and user personalization — built with Python & PySide6.

---

## 🚀 Overview

This project is a modular desktop application designed to simplify access to stock market data.

It targets users who need a **clean, modern, and accessible tool** for:

* tracking market data
* reading financial news
* managing personalized watchlists

The application is built with scalability in mind and prepared for future commercialization (subscription model).

---

## ✨ Features

* 📈 Market data (global & local)
* 📰 Financial news system
* 👤 User authentication (login/register)
* ⭐ Watchlist (tracked assets)
* ⚙️ User settings (theme, language)
* 🌐 Online / offline modes
* 🔄 Auto-update system (GitHub Releases)

---

## 🧱 Tech Stack

**Frontend**

* PySide6 (Qt for Python)
* Qt Style Sheets (CSS-like styling)

**Backend / Logic**

* Python
* requests (API communication)
* PyMySQL (database access)
* cryptography (security layer)

**Database**

* Amazon RDS (MySQL)
* Stored procedures

**Other**

* JSON (config & localization)
* SVG assets (icons, flags)

---

## 🏗️ Architecture

Modular structure:

```bash
__core__.py
assets/
package/
  ├── login/
  ├── main/
  ├── news/
  ├── object/
```

Each module contains:

* `Ui.py` → interface
* `Logic.py` → business logic
* `Structure.py` → data models

---

## 🔄 Application Flow

1. App start (`__core__.py`)
2. Network check (Ping)
3. Authentication (Login/Register)
4. Load user config (DB)
5. Main dashboard
6. Fetch data (API / DB)
7. Render UI

---

## 🔗 Integrations

* External stock data APIs
* Amazon RDS (MySQL database)
* Secret Manager (secure credentials)
* GitHub Releases (updates system)

---

## ⚙️ Installation

In progress

## 🔐 Security

* No credentials stored in source code
* Secret Manager integration
* Stored procedures for DB access
* Encryption via cryptography

---

## 📦 Project Status

🛠️ In development

Planned:

* charts & technical analysis
* recommendation system
* subscription model
* extended market data

---

## 💡 Motivation

Only ~6% of people in Poland invest in the stock market.

Existing tools are often:

* too expensive
* outdated in UI/UX
* too complex for beginners

This project aims to **lower the entry barrier** and provide a modern alternative.

---

## 👤 Author

Built as a full-stack desktop application project, including:

* system architecture
* UI/UX design
* backend logic
* database design
* API integrations

---

## 📄 License

For educational and portfolio purposes.
Further use depends on the author.
