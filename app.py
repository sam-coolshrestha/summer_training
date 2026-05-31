import streamlit as st
import pandas as pd

st.title("Traffic Analytics Dashboard")

df = pd.read_csv("outputs/vehicle_records.csv")

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

col1, col2, col3, col4, col5 = st.columns(5)

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


vehicle_counts = df["Vehicle_Type"].value_counts()

st.subheader("Vehicle Type Distribution")

st.bar_chart(vehicle_counts)

st.subheader("Vehicle Speed Analysis")

st.line_chart(df["Speed"])

st.subheader("Vehicle Records")

fastest_vehicle = df.loc[df["Speed"].idxmax()]

st.subheader("Fastest Vehicle")

st.write(fastest_vehicle)

st.dataframe(
df.style.highlight_max(
subset=["Speed"]
)
)


csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="vehicle_records.csv",
    mime="text/csv"
)


st.subheader("Processed Traffic Video")

video_file = open(
    "outputs/final_output.mp4",
    "rb"
)

st.video(video_file.read())