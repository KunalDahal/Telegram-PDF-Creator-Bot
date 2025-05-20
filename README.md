# 🖼️ Image to PDF Telegram Bot

This is a simple Telegram bot built with Python that converts images sent by users into PDF files and sends them back. It's powered by the Python Telegram Bot library and Pillow for image processing.

## 🚀 Features

- Accepts images from users (as photos or image files)
- Converts the highest resolution version to PDF
- Sends the converted PDF back to the user instantly

## 📦 Requirements

- Python 3.7+
- `python-telegram-bot` v20+
- `Pillow`

## 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/image-to-pdf-telegram-bot.git
cd image-to-pdf-telegram-bot
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add your Telegram bot token:**

Open `main.py` and replace the `TOKEN` value with your actual bot token from [BotFather](https://t.me/BotFather).

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

## ▶️ Running the Bot

```bash
python main.py
```

Once running, open your bot on Telegram and send it an image. It will reply with a PDF version.

## 📝 Example

**User:** 📷 *sends image*  
**Bot:** 📄 *returns PDF file*

## 🤝 Contributing

Feel free to fork this repo and submit pull requests if you'd like to improve the bot.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> Created with ❤️ using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
