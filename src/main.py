# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from urllib.parse import quote

from qr_generator import generate_qr
from validators import is_valid_url

# -----------------------------
# CONFFIGURATION
# -----------------------------
DEFAULT_URL = "https://www.linkedin.com/in/juan-esteban-ortiz-londoño-027b11272/"
OUTPUT_PATH = "../output/qr_code.png"


def generate_and_show_qr(url: str):
    if not is_valid_url(url):
        messagebox.showerror("Error", "La URL no es válida")
        return

    encoded_url = quote(url, safe=":/")
    generate_qr(encoded_url, OUTPUT_PATH)

    show_qr_image()


def show_qr_image():
    img = Image.open(OUTPUT_PATH)
    img = img.resize((250, 250))
    qr_img = ImageTk.PhotoImage(img)

    qr_label.config(image=qr_img)
    qr_label.image = qr_img


def on_generate_click():
    url = url_entry.get().strip()
    generate_and_show_qr(url)


# -----------------------------
# UI (TKINTER)
# -----------------------------
root = tk.Tk()
root.title("Generador de QR - Juan Esteban")
root.geometry("350x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="QR",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

url_entry = tk.Entry(root, width=45)
url_entry.pack(pady=10)
url_entry.insert(0, DEFAULT_URL)

generate_button = tk.Button(
    root,
    text="Generar QR",
    command=on_generate_click,
    width=20
)
generate_button.pack(pady=10)

footer = tk.Label(
    root,
    text="Proyecto de Portafolio - Python",
    font=("Arial", 9),
    fg="gray"
)
footer.pack(side="bottom", pady=10)

# -----------------------------
# QR DEFAULT
# -----------------------------
generate_and_show_qr(DEFAULT_URL)

root.mainloop()
