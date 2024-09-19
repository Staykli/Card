from collections import defaultdict
import cv2
import time
from deepface import DeepFace # type: ignore
from datetime import datetime
import telegram

# Налаштування
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
video_source = 0  # Змінити на файл відео, якщо потрібно
standing_threshold = 300  # 5 хвилин (300 секунд)

# Налаштування Telegram бота
TELEGRAM_TOKEN = '6845850635:AAFhOW_uWfJOGyYMBmvYTnOkBlkXIYlKgcU'
CHAT_ID = '1306947361'
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Відкриття відеопотоку
cap = cv2.VideoCapture(video_source)
last_seen_time = defaultdict(lambda: time.time())
standing_time = defaultdict(int)

def recognize_face(frame, face_region):
    x, y, w, h = face_region
    face = frame[y:y+h, x:x+w]
    result = DeepFace.find(img_path=face, db_path='your_database_path', enforce_detection=False)
    return result

def send_telegram_message(photo_path, message):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=message)

def send_face_info(face_region, message):
    x, y, w, h = face_region
    face_image = f"face_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(face_image, frame[y:y+h, x:x+w])
    send_telegram_message(face_image, message)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Визначення часу, коли особа була останнього разу в кадрі
        current_time = time.time()
        last_seen = last_seen_time[(x, y, w, h)]

        if current_time - last_seen > standing_threshold:
            standing_time[(x, y, w, h)] += current_time - last_seen
            if standing_time[(x, y, w, h)] >= standing_threshold:
                photo_path = f"standing_person_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(photo_path, frame)
                print("Person stood still for more than 5 minutes!")
                
                # Відправити сповіщення з фото
                send_telegram_message(photo_path, 'Person stood still for more than 5 minutes!')
                
                # Відправити деталі обличчя
                face_info = recognize_face(frame, (x, y, w, h))
                if face_info:
                    send_face_info((x, y, w, h), 'Face recognized')
                
                standing_time[(x, y, w, h)] = 0  # Скидання часу для цього об'єкта
        else:
            standing_time[(x, y, w, h)] = 0  # Скидання часу, якщо особа знову в русі

        last_seen_time[(x, y, w, h)] = current_time

    cv2.imshow('Video Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
