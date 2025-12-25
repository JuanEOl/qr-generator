#  QR Code Generator – Python (Desktop App)

A desktop application built with Python that generates and displays QR codes from URLs or text, featuring a simple and functional graphical user interface built with Tkinter.

When the application starts, it automatically generates and displays a QR code pointing to my LinkedIn profile, making it both a personal utility and a portfolio project.

---

## 🚀 Features

- Generate QR codes from URLs  
- Desktop graphical interface (Tkinter)  
- QR preview displayed on screen  
- Automatic URL encoding (supports ñ, accents, etc.)  
- URL validation  
- Modular and scalable project structure  
- Clean, readable, and well-organized code  

---

## 🖥️ Preview

When the application starts, it automatically generates and displays the QR code for my LinkedIn profile.

---

## 🧠 Technologies Used

- Python 3.10+  
- Tkinter (desktop UI)  
- qrcode  
- Pillow (PIL)  
- urllib.parse (URL encoding)  

---

## 📂 Project Structure

```bash
qr-generator/
│
├── src/
│   ├── main.py          # GUI and main application logic
│   ├── qr_generator.py # QR code generation logic
│   └── validators.py   # URL validation
│
├── output/
│   └── qr_code.png     # Generated QR image
│
├── venv/               # Virtual environment
├── requirements.txt
└── README.md
```
---

## ⚙️ Installation & Execution

### 1. Clone the repository

git clone https://github.com/your-username/qr-generator.git
cd qr-generator

### 2. Create and activate a virtual environment

python -m venv venv

Windows (PowerShell):

.\venv\Scripts\activate


### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

cd src
python main.py

---

## 🔗 Default QR

On startup, the application automatically generates a QR code pointing to the following link:

https://www.linkedin.com/in/juan-esteban-ortiz-londoño-027b11272/


The URL is properly encoded to ensure compatibility with all QR readers and browsers.

---

## 🌍 Special Character Support

URLs containing special characters such as ñ, á, é, etc. are automatically encoded using UTF-8 (percent-encoding) to avoid misinterpretation.

Example:

londoño → londo%C3%B1o

This guarantees correct behavior across different systems and devices.

---

## 🧩 Possible Future Improvements

- Export QR as downloadable image  
- QR color customization  
- Logo overlay in the center of the QR  
- Dark mode  
- Windows .exe packaging  
- Web version using Flask  
- Automated tests  

---

##  Author

Juan Esteban Ortiz Londoño  

LinkedIn:  
https://www.linkedin.com/in/juan-esteban-ortiz-londoño-027b11272/

---

##  License

This project is licensed under the MIT License.  
Free to use for learning and demonstration purposes.

---

⭐ If you find this project useful, feel free to give it a star on GitHub!
