# IntelliTraffic AI 

AI-powered intelligent traffic surveillance and analytics system built using YOLOv8, EasyOCR, OpenCV, and Streamlit.

##  Live Demo

https://intellitraffic-ai.streamlit.app/

---

#  Features

* Real-time vehicle detection using YOLOv8
* Vehicle tracking with ByteTrack
* Vehicle speed estimation
* License plate extraction using EasyOCR
* Overspeeding detection and violation analysis
* Vehicle trajectory tracking
* Interactive Streamlit analytics dashboard
* Vehicle filtering and plate number search
* CSV report generation and download
* Processed traffic video playback
* Upload and process custom traffic videos

---

# 🛠️ Tech Stack

* Python
* YOLOv8
* OpenCV
* EasyOCR
* Streamlit
* Pandas
* NumPy

---

#  Project Structure

```bash
summer_training/
│
├── app/
│   ├── analytics.py
│   ├── detection.py
│   ├── ocr.py
│   ├── tracking.py
│   └── utils.py
│
├── outputs/
│   ├── final_output.mp4
│   └── vehicle_records.csv
│
├── videos/
│   └── uploaded_video.mp4
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Installation

Clone the repository:

```bash
git clone https://github.com/sam-coolshrestha/summer_training.git
cd summer_training
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

#  Run the Application

Start Streamlit dashboard:

```bash
streamlit run app.py
```

Run traffic processing script manually:

```bash
python main.py
```

---

# 📊 Dashboard Features

* Total vehicle analytics
* Average and maximum speed monitoring
* Vehicle type distribution
* Speed trend visualization
* Overspeeding detection
* Search vehicles by plate number
* Downloadable CSV reports
* Processed traffic video visualization

---

#  Future Improvements

* Lane detection and lane change analysis
* Driving behavior profiling
* Accident detection
* Real-time webcam support
* Traffic congestion prediction
* Cloud database integration
* Multi-camera monitoring
* Advanced violation analytics

---

#  Author

Samridhi Kulshrestha

GitHub:
https://github.com/sam-coolshrestha
