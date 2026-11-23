import os
from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

SITE_URL = "https://y8w9v8y9cz-coder.github.io/telegram-gifts/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        KeyboardButton(
            text="Открыть NOIR GIFTS",
            web_app=WebAppInfo(url=SITE_URL)
        )
    ]]

    await update.message.reply_text(
        "Добро пожаловать в NOIR GIFTS 🖤\n\n"
        "Нажми кнопку ниже, чтобы открыть приложение.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

app = Application.builder().token(
    os.environ["BOT_TOKEN"]
).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
