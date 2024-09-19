import random
import string
import asyncio
from telegram import Bot

# Введіть ваші дані
TELEGRAM_TOKEN = '6845850635:AAFhOW_uWfJOGyYMBmvYTnOkBlkXIYlKgcU'
TELEGRAM_CHAT_ID = '1306947361'

def generate_strong_password(length=100):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

async def send_telegram_message(token, chat_id, message):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)

async def update_password():
    while True:
        password = generate_strong_password()
        message = f"Ваш новий пароль: {password}"
        
        # Відправка повідомлення в Telegram
        await send_telegram_message(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, message)
        
        # Очікування 5 хвилин
        await asyncio.sleep(300)

# Запуск програми
asyncio.run(update_password())