import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image

# Завантаження моделі розпізнавання облич
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# Функція для розпізнавання облич на зображенні
def detect_faces(image_path):
    # Перевірка, чи файл існує
    if not os.path.exists(image_path):
        messagebox.showerror("Error", "File does not exist")
        return

    # Перевірка, чи файл є зображенням
    try:
        img = Image.open(image_path)
        img.verify()
    except (IOError, SyntaxError) as e:
        messagebox.showerror("Error", "Bad file format")
        return

    # Завантаження зображення
    image = cv2.imread(image_path)
    if image is None:
        messagebox.showerror("Error", "Failed to load image")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Попередня обробка зображення
    gray = cv2.equalizeHist(gray)

    # Розпізнавання облич
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30))

    # Малювання прямокутників навколо розпізнаних облич
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Відображення зображення з розпізнаними обличчями
    cv2.imshow("Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Функція для завантаження зображення
def load_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if image_path:
        detect_faces(image_path)

# Створення головного вікна
root = tk.Tk()
root.title("Face Detection")

# Додавання кнопок
btn_load_image = tk.Button(root, text="Load Image", command=load_image)
btn_load_image.pack(pady=10)

# Запуск головного циклу
root.mainloop()