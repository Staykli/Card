import random
import string
import time
from threading import Timer
from telegram import Bot
from twilio.rest import Client

# Введіть ваші дані
TELEGRAM_TOKEN = 'your_telegram_token'
TELEGRAM_CHAT_ID = 'your_chat_id'
TWILIO_SID = 'your_twilio_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_FROM_NUMBER = 'your_twilio_from_number'
TWILIO_TO_NUMBER = 'your_phone_number'

def generate_strong_password(length=100):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def send_telegram_message(token, chat_id, message):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message)

def send_sms(account_sid, auth_token, from_number, to_number, message):
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=from_number, to=to_number)

def update_password():
    password = generate_strong_password()
    message = f"Ваш новий пароль: {password}"
    
    # Відправка повідомлення в Telegram
    send_telegram_message(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, message)
    
    # Відправка SMS
    send_sms(TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, TWILIO_TO_NUMBER, message)
    
    # Запуск таймера на 5 хвилин
    Timer(300, update_password).start()

# Запуск програми
update_password()