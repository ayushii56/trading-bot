# Binance Futures Testnet Trading Bot

A structured Python trading bot that places MARKET, LIMIT, and STOP-LIMIT orders on the **Binance Futures Testnet (USDT-M)**.
Built with clean architecture, validation, logging, and both CLI + lightweight web UI.

This project demonstrates API integration, defensive validation, structured logging, and production-style error handling — designed as a submission task for a Python developer role.

---

## 🚀 Features

### Core Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Support **BUY / SELL**
* CLI input validation
* Structured logging to file
* Robust error handling
* Clean layered architecture

### Bonus Enhancements

* ⭐ STOP-LIMIT conditional orders
* ⭐ Interactive CLI confirmation preview
* ⭐ Lightweight web interface (Flask)
* ⭐ User guidance hints in UI
* ⭐ Smart response formatting

---

## 🏗 Architecture Overview

```
CLI / Web UI
      ↓
Validation Layer
      ↓
Order Service
      ↓
Binance Client Wrapper
      ↓
Binance Futures Testnet API
```

This separation improves maintainability, testability, and clarity.

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── web_app.py             # Flask UI
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/main.css
│   └── images/bg.png
│
├── logs/bot.log           # Runtime logs
├── requirements.txt
├── .env                   # API credentials (not committed)
└── README.md
```

---

## ⚙ Setup Instructions

### 1. Clone repository

```
git clone <your-repo-url>
cd trading_bot
```

---

### 2. Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Binance Testnet Setup

1. Visit:
   👉 https://testnet.binancefuture.com

2. Login / register

3. Generate API keys

4. Create `.env` file:

```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

---

## 💻 CLI Usage

### MARKET order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

---

### LIMIT order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

---

### STOP-LIMIT order (bonus)

```
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.01 --price 120000 --stop-price 115000
```

CLI provides:

* order preview
* confirmation prompt
* formatted response

---

## 🌐 Web Interface

Run:
python web_app.py

Open browser:
http://127.0.0.1:5000

Features:

* guided input fields
* helper hints
* error feedback
* background UI styling

---

## 📝 Logging

All API interactions are logged to:

```
logs/bot.log
```

Includes:

* order requests
* Binance responses
* error traces

Useful for debugging and audit tracking.

---

## ⚠ Validation Rules

* Symbol must be valid (e.g., BTCUSDT)
* Quantity must be positive
* LIMIT requires price
* STOP-LIMIT requires price + stop price
* Binance API errors are surfaced to user

---

## 🧠 Order Type Explanation

| Type       | Behavior                         |
| ---------- | -------------------------------- |
| MARKET     | Executes immediately             |
| LIMIT      | Executes only at specified price |
| STOP-LIMIT | Triggered conditional order      |

---

## 📌 Assumptions

* Binance Futures Testnet environment
* Python 3.10+
* Internet connectivity required
* Orders may remain NEW on testnet due to simulated liquidity

---

## 🏆 Evaluation Highlights

This implementation demonstrates:

* Clean architecture separation
* Defensive validation
* Structured logging
* Real API integration
* CLI UX design
* Optional web interface

---

## 📬 Submission Notes

Log examples are included in `/logs`.

This project exceeds baseline requirements by implementing bonus trading logic and UI enhancements.

---

## 👨‍💻 Author

Ayushi Pandey

---

## 📄 License

Educational / demonstration project.
