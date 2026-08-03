import streamlit as st
import pandas as pd
import subprocess
import os
import sys

st.title("Traffic Analytics Dashboard")

# Ensure required folders exist (they may not be present on a fresh
# deploy since empty folders aren't tracked by Git)
os.makedirs("videos", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

uploaded_file = st.file_uploader(
"Upload Traffic Video",
type=["mp4", "avi", "mov"]
)

if uploaded_file is not None:

    st.success("Video Uploaded Successfully")
    st.write(uploaded_file.name)

if uploaded_file is not None:

    with open(
        "videos/uploaded_video.mp4",
        "wb"
    ) as f:


        f.write(uploaded_file.read())

    if st.button("Process Video"):

        with st.spinner("Processing video... Please wait"):
            result = subprocess.run(
                [sys.executable, "main.py"],
                capture_output=True,
                text=True
            )

        if result.returncode == 0:
            st.success("Video Processing Complete")
        else:
            st.error("main.py failed while processing the video. See details below.")
            st.code(result.stderr or "No error output captured.", language="text")

        if result.stdout:
            with st.expander("Processing log (stdout)"):
                st.code(result.stdout, language="text")

if os.path.exists("outputs/vehicle_records.csv"):
    df = pd.read_csv("outputs/vehicle_records.csv")
else:
    st.warning("No processed records yet. Upload a video and click 'Process Video' above.")
    st.stop()

vehicle_filter = st.sidebar.selectbox(
    "Select Vehicle Type",
    ["All"] + list(df["Vehicle_Type"].unique())
)

if vehicle_filter != "All":
    df = df[df["Vehicle_Type"] == vehicle_filter]

plate_search = st.text_input(
    "Search Plate Number"
)

if plate_search:
    df = df[
        df["Plate_Number"].str.contains(
            plate_search,
            case=False
        )
    ]

if "Display_ID" in df.columns:
    df = df[["Display_ID"] + [col for col in df.columns if col != "Display_ID"]]

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Total Vehicles", len(df))

with col2:
    st.metric(
    "Average Speed",
    round(df["Speed"].mean(), 2)
    )

with col3:
    st.metric(
    "Maximum Speed",
    df["Speed"].max()
    )

with col4:
    st.metric(
    "Total Cars",
    len(df[df["Vehicle_Type"] == "car"])
    )

with col5:
    st.metric(
    "Total Trucks",
    len(df[df["Vehicle_Type"] == "truck"])
    )

with col6:
    st.metric(
    "Overspeed Violations",
    len(df[df["Violation"] == "Overspeeding"])
    )


vehicle_counts = df["Vehicle_Type"].value_counts()

st.subheader("Vehicle Type Distribution")

st.bar_chart(vehicle_counts)

st.subheader("Vehicle Speed Analysis")

st.line_chart(df["Speed"])

st.subheader("Vehicle Records")

if not df.empty:
    fastest_vehicle = df.loc[df["Speed"].idxmax()]
    st.subheader("Fastest Vehicle")
    st.write(fastest_vehicle)

st.dataframe(df)


csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="vehicle_records.csv",
    mime="text/csv"
)


st.subheader("Processed Traffic Video")

video_path = "outputs/final_output.mp4"

if os.path.exists(video_path):

    with open(video_path, "rb") as video_file:
        st.video(video_file.read())

    with open(video_path, "rb") as video_file:
        st.download_button(
            label="Download Processed Video",
            data=video_file.read(),
            file_name="processed_traffic_video.mp4",
            mime="video/mp4"
        )

else:
    st.warning("No processed video available yet.")
