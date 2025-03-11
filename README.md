# Motion Detection and Face Recognition Alarm System

## 📌 Overview
This project is a **Motion Detection and Face Recognition Alarm System** that:
- Detects motion using a webcam.
- Recognizes known faces and triggers an alarm for unknown faces.
- Sends an email alert with captured frames if an unknown person is detected.
- Plays an alert sound when an unknown face is detected.

---

## 🛠 Installation
Follow the steps below to set up and run the application on your local machine.

### 1️⃣ Install Python
Ensure you have **Python 3.9 or later** installed. You can download it from [Python Official Website](https://www.python.org/downloads/).

Check the Python version:
```bash
python --version
```

---

### 2️⃣ Install Required Dependencies
Run the following command to install all necessary packages:
```bash
pip install -r requirements.txt
```
**OR** manually install them:
```bash
pip install opencv-python numpy imutils face-recognition dlib playsound smtplib
```

If you encounter issues with `dlib`, install CMake first:
```bash
# For MacOS
brew install cmake

# For Ubuntu/Linux
sudo apt-get install cmake
```

---

### 3️⃣ Set Up Email Alerts
To receive email alerts, you need to set up your **Gmail App Password**:

1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords).
2. Select "Mail" as the app and "Other (Custom name)" as the device.
3. Generate a password and **copy it**.
4. Open `mail.py` and replace:
   ```python
   sender_email = 'your-email@gmail.com'
   sender_password = 'your-app-password'
   recipient_email = 'recipient-email@gmail.com'
   ```

---

## 🚀 Running the Application
Once everything is set up, run the script using:
```bash
python main.py
```

### Expected Behavior:
- The webcam will start capturing frames.
- If a **known face** is detected → **No alarm**.
- If an **unknown face** is detected → **Alarm sound & Email Alert Sent**.
- Email will contain the captured frames of the unknown person.

To stop the program, press **'Q'**.

---

## 🛠 Customization
### ✅ Adding Known Faces
1. Create a folder called `known_faces`.
2. Add images of known people inside the folder.
3. Update `main.py` to load these faces automatically.

### ✅ Changing Alert Sound
Replace `alert.mp3` with your custom alert sound.

---

## ⚠️ Troubleshooting
- **No email received?**
  - Check if you've enabled **Less Secure Apps** or used an **App Password**.
  - Make sure your email credentials are correct.
  - Check spam folder.
- **Camera not detected?**
  - Ensure the webcam is properly connected.
  - Try changing the camera index in `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`.
- **Face recognition not working?**
  - Ensure `known_faces` folder has clear images.
  - Improve accuracy by adding more training images per person.

---
