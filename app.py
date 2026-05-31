import streamlit as st
import pandas as pd

st.title("Traffic Analytics Dashboard")

df = pd.read_csv("outputs/vehicle_records.csv")

st.metric("Total Vehicles Detected", len(df))

st.metric("Average Speed", round(df["Speed"].mean(), 2))

st.metric("Maximum Speed", df["Speed"].max())

st.metric(
    "Total Cars",
    len(df[df["Vehicle_Type"] == "car"])
)

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

st.dataframe(df)

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="vehicle_records.csv",
    mime="text/csv"
)