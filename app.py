import streamlit as st
import pandas as pd

st.title("Traffic Analytics Dashboard")

df = pd.read_csv("outputs/vehicle_records.csv")

st.metric("Total Vehicles Detected", len(df))

vehicle_counts = df["Vehicle_Type"].value_counts()

st.subheader("Vehicle Type Distribution")

st.bar_chart(vehicle_counts)

st.subheader("Vehicle Records")

st.dataframe(df)

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="vehicle_records.csv",
    mime="text/csv"
)