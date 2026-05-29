# Traffic Detection and Vehicle Tracking System

## Overview

This project is a computer vision–based traffic monitoring system built using Python, YOLOv8, OpenCV, and EasyOCR.
The system processes a traffic video, detects and tracks vehicles, identifies when vehicles cross a predefined line, extracts possible license plate text using OCR, and stores the results in a CSV file.

The final output includes:

* An annotated output video with tracked vehicles
* Vehicle crossing records with timestamps
* Detected license plate text (when readable)

---

# Features

* Real-time vehicle detection using YOLOv8
* Multi-object tracking using ByteTrack
* Line-crossing detection
* License plate text extraction using EasyOCR
* CSV report generation
* Processed output video generation

---

# Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* EasyOCR
* Pandas
* ByteTrack

---

# Project Workflow

## 1. Install Required Libraries

The notebook first installs the required dependencies:

```python
!pip install ultralytics
!pip install easyocr
!pip install supervision
```

These libraries are used for:

* Object detection
* OCR text recognition
* Video processing
* Object tracking

---

# 2. Upload and Read Video

The traffic video is uploaded and loaded using OpenCV.

```python
cap = cv2.VideoCapture(video_path)
```

The program extracts:

* Frame width
* Frame height
* FPS (frames per second)

These values are later used to generate the output video.

---

# 3. Load YOLO Model

```python
vehicle_model = YOLO("yolov8n.pt")
```

The YOLOv8 Nano model is used to detect vehicles in each video frame.

The model identifies objects such as:

* Cars
* Trucks
* Motorcycles
* Buses

---

# 4. Vehicle Tracking

```python
results = vehicle_model.track(
    frame,
    persist=True,
    tracker="bytetrack.yaml"
)
```

ByteTrack assigns a unique tracking ID to each vehicle so the same vehicle can be followed across multiple frames.

Example:

| Vehicle | Tracking ID |
| ------- | ----------- |
| Car 1   | 5           |
| Truck   | 9           |

This prevents counting the same vehicle multiple times.

---

# 5. Draw Detection Line

```python
LINE_Y = 400
```

A horizontal line is drawn on the video frame.

```python
cv2.line(...)
```

This line acts as a checkpoint for vehicle counting.

---

# 6. Detect Line Crossing

The program monitors the vertical center position of each vehicle.

```python
if previous_y < LINE_Y and center_y >= LINE_Y:
```

When a vehicle crosses the line:

* It is counted once
* OCR processing starts
* Vehicle details are stored

The `crossed_ids` set ensures duplicate counting does not occur.

---

# 7. License Plate Recognition

The lower half of the detected vehicle is cropped:

```python
lower_half = vehicle_crop[h//2:h, :]
```

EasyOCR scans the cropped region:

```python
ocr_result = reader.readtext(lower_half)
```

The detected text is assumed to be the plate number.

If no text is detected:

```python
plate_text = "UNKNOWN"
```

---

# 8. Save Vehicle Records

For every detected crossing, the following data is stored:

* Vehicle ID
* Plate Number
* Timestamp

Example:

| Vehicle_ID | Plate_Number | Timestamp           |
| ---------- | ------------ | ------------------- |
| 3          | UK07AB1234   | 2026-05-29 14:32:11 |

The records are saved into:

```python
vehicle_records.csv
```

---

# 9. Generate Output Video

The processed video with:

* Bounding boxes
* Tracking IDs
* Detection line

is saved as:

```python
final_output.mp4
```

---

# Output Files

| File                  | Description              |
| --------------------- | ------------------------ |
| `final_output.mp4`    | Processed traffic video  |
| `vehicle_records.csv` | Vehicle crossing records |
| `traffic.mp4`         | Input video              |
| `yolov8n.pt`          | YOLO model weights       |

---

# How to Run the Project

## Step 1: Install Dependencies

```bash
pip install ultralytics easyocr supervision opencv-python pandas
```

---

## Step 2: Download YOLO Model

```bash
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt
```

---

## Step 3: Add Input Video

Place your traffic video in the project directory.

Example:

```python
video_path = "traffic.mp4"
```

---

## Step 4: Run the Notebook

Execute all notebook cells sequentially.

---

# Applications

This system can be used in:

* Smart traffic management
* Toll booth automation
* Parking systems
* Vehicle monitoring
* Security surveillance
* Traffic analytics

---

# Limitations

* OCR accuracy depends on video quality
* Small or blurred license plates may not be detected
* Night-time videos may reduce detection accuracy
* Current implementation assumes the plate is in the lower half of the vehicle

---

# Future Improvements

Possible enhancements include:

* Dedicated license plate detection model
* Speed estimation
* Vehicle counting dashboard
* Real-time webcam support
* Database integration
* Automatic violation detection

---

# Conclusion

This project demonstrates how deep learning and computer vision can be combined to build an automated traffic monitoring system. It integrates vehicle detection, tracking, OCR, and data logging into a complete end-to-end workflow suitable for smart transportation applications.
