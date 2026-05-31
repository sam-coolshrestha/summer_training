# AI-Based Traffic Analytics System

## Overview

This project is an AI-powered traffic analytics and vehicle monitoring system built using YOLOv8, OpenCV, EasyOCR, ByteTrack, and Streamlit.

The system performs real-time vehicle detection, tracking, speed estimation, trajectory analysis, and license plate recognition from uploaded traffic videos. It also provides an interactive dashboard for traffic analytics visualization.

---

# Features

* Real-time vehicle detection using YOLOv8
* Multi-object vehicle tracking using ByteTrack
* Vehicle trajectory visualization
* Vehicle speed estimation
* Direction analysis
* Acceleration estimation
* Vehicle type classification
* License plate recognition using EasyOCR
* Line crossing detection
* CSV report generation
* Interactive Streamlit dashboard
* Video upload and automatic processing
* Vehicle analytics filtering and search

---

# Technologies Used

* Python
* YOLOv8
* OpenCV
* EasyOCR
* Streamlit
* Pandas
* ByteTrack

---

# Project Structure

```bash
summer_training/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── yolov8n.pt
│
├── videos/
│   └── uploaded_video.mp4
│
├── outputs/
│   ├── vehicle_records.csv
│   └── final_output.mp4
```

---

# How It Works

1. User uploads a traffic video through the Streamlit dashboard.
2. The uploaded video is saved locally.
3. YOLOv8 detects vehicles frame-by-frame.
4. ByteTrack assigns unique IDs to vehicles.
5. Vehicle trajectories and movement paths are tracked.
6. Speed, acceleration, and direction are estimated.
7. EasyOCR extracts vehicle number plates.
8. Processed results are saved into a CSV report.
9. Dashboard visualizes analytics and processed video output.

---

# Dashboard Features

* Vehicle type filtering
* Plate number search
* Vehicle speed analytics
* Vehicle distribution charts
* Fastest vehicle analysis
* CSV report download
* Processed video playback

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

## Start Streamlit Dashboard

```bash
streamlit run app.py
```

## Process Uploaded Video

Upload a video from the dashboard and click:

```text
Process Video
```

The system will automatically:

* process the video,
* generate analytics,
* save CSV reports,
* generate processed output video.

---

# Output Files

## CSV Report

Generated at:

```text
outputs/vehicle_records.csv
```

Contains:

* Vehicle ID
* Vehicle Type
* Speed
* Direction
* Acceleration
* Plate Number
* Timestamp

---

## Processed Video

Generated at:

```text
outputs/final_output.mp4
```

Includes:

* Bounding boxes
* Vehicle IDs
* Speed visualization
* Trajectory paths
* Detection overlays

---

# Future Improvements

* Overspeed violation detection
* Lane change detection
* Traffic heatmaps
* Live webcam support
* Red-light violation detection
* Helmet detection
* Cloud deployment
* Database integration

---

# Author

Samridhi Kulshrestha
