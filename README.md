# 🖐️ Computer Vision Projects with OpenCV – Hand Tracking, Face Detection & Virtual Painter

![Screenshot 2025-06-26 120510](https://github.com/user-attachments/assets/430b8106-4ffa-481d-87ea-55ebda321e2d)


---

## 📌 Overview

This project bundle contains 3 real-time **computer vision applications** built using **OpenCV**, **MediaPipe**, and **Haar Cascade**. It showcases gesture control, hand tracking, object drawing, and face detection with live webcam input. The highlight is a **Virtual Painter** that allows you to draw using your fingers!

---

## 🎯 Project Features

| Project              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 🖼️ **Virtual Painter**    | Draw with your index finger, change colors with gestures, erase with a flick |
| ✋ **Hand Tracking**       | Track hand and finger landmarks in real time using MediaPipe             |
| 🙂 **Face Detection**      | Detect faces using Haar Cascade on static images                         |

---

## 🧠 Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Haar Cascade Classifier

---

## 🖌️ Project 1: Virtual Painter with Finger Gestures

### 🧠 Concept:
Draw on a virtual canvas using your hand.  
- Use **2 fingers** to enter selection mode (choose brush color or eraser)
- Use **1 finger (index)** to draw
- Uses hand landmarks from **MediaPipe** via custom `handtrackingmodule.py`

### 🎨 Controls:
| Action                        | Gesture                        |
|-------------------------------|--------------------------------|
| Select Brush Color (Pink, Blue, Green) | Two fingers + tap on color icon |
| Select Eraser (Black)         | Two fingers + tap on eraser icon |
| Draw on Canvas                | One finger (index)             |
| Erase                         | One finger in eraser mode      |


---

## ✋ Project 2: Real-Time Hand Tracking

Tracks and draws landmarks of fingers using MediaPipe.

### Features:
- Tracks all 21 hand landmarks
- Detects which fingers are up
- Displays live FPS

📂 Code:
- `handtrackingmodule.py` – Reusable module for all hand detection
- `main_handtracking.py` – Main script to test hand tracking

---

## 🙂 Project 3: Face Detection (Haar Cascade)

Detects and marks faces in an image using Haar Cascade Classifier.

### Features:
- Reads image file
- Converts to grayscale
- Detects faces
- Draws rectangle over detected faces

⚙️ Requirements
Install required libraries:
pip install opencv-python
pip install mediapipe
pip install numpy

🚀 Run Instructions

🎨 Run Virtual Painter:

- python virtual_painter/virtual_painter.py

✋ Run Hand Tracking:

- python hand_tracking/main_handtracking.py

🙂 Run Face Detection:

- Make sure you have a valid Haar XML file and test image:
- python face_detection/face_detection.py

📸 Screenshots

- Virtual Painter Demo ![Screenshot 2025-06-26 120510](https://github.com/user-attachments/assets/c4ba0129-4cc4-48f7-a6b4-5d93dfbd9c73)
- Drawing Mode ![Screenshot 2025-06-26 120610](https://github.com/user-attachments/assets/50640d40-bb32-4944-af4b-54c38763cb74)
- Eeaser Mode ![Screenshot 2025-06-26 120705](https://github.com/user-attachments/assets/bfd1159d-e8cc-4147-935d-5b47464a1be1)
- Face Detection Output ![Screenshot 2025-06-26 122014](https://github.com/user-attachments/assets/47ab22b0-eac8-497f-8204-fd2659039b9f)

✍️ Author

- Shivam Punia – Developer & Designer
- 📬 [linkedin](shivam-punia-a033a6279)
- 💻 [GitHub](https://github.com/Shivampunia)

