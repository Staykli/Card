import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pygame
import os

# Ініціалізація pygame
pygame.mixer.init()

# Функція для завантаження музичного файлу
def load_music():
    global music_file
    music_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if music_file:
        pygame.mixer.music.load(music_file)
        music_label.config(text=os.path.basename(music_file))

# Функція для відтворення музики
def play_music():
    if music_file:
        pygame.mixer.music.play()
    else:
        messagebox.showerror("Error", "No music file loaded")

# Функція для паузи музики
def pause_music():
    pygame.mixer.music.pause()

# Функція для відновлення відтворення музики
def unpause_music():
    pygame.mixer.music.unpause()

# Функція для зупинки музики
def stop_music():
    pygame.mixer.music.stop()

# Створення головного вікна
root = tk.Tk()
root.title("Music Player")
root.geometry("300x300")
root.resizable(False, False)

# Створення стилю
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12))

# Додавання кнопок
btn_load = ttk.Button(root, text="Load Music", command=load_music)
btn_load.pack(pady=10)

btn_play = ttk.Button(root, text="Play", command=play_music)
btn_play.pack(pady=10)

btn_pause = ttk.Button(root, text="Pause", command=pause_music)
btn_pause.pack(pady=10)

btn_unpause = ttk.Button(root, text="Unpause", command=unpause_music)
btn_unpause.pack(pady=10)

btn_stop = ttk.Button(root, text="Stop", command=stop_music)
btn_stop.pack(pady=10)

# Додавання мітки для відображення назви музичного файлу
music_label = ttk.Label(root, text="No music loaded")
music_label.pack(pady=10)

# Запуск головного циклу
root.mainloop()