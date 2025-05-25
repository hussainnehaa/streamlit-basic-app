import streamlit as st
from datetime import datetime
import pytz
import time

# Define US time zones
us_timezones = {
    "Eastern Time (ET)": "US/Eastern",
    "Central Time (CT)": "US/Central",
    "Mountain Time (MT)": "US/Mountain",
    "Pacific Time (PT)": "US/Pacific",
    "Alaska Time (AKT)": "US/Alaska",
    "Hawaii Time (HST)": "US/Hawaii",
}

st.set_page_config(page_title="U.S. Time Dashboard", layout="centered")

st.title("🕒 U.S. Time Dashboard")
st.markdown("This dashboard displays the current time across major U.S. time zones.")

# Refresh every 10 seconds (or use a button below)
refresh_interval = 10  # seconds

while True:
    col1, col2 = st.columns(2)
    for i, (label, tz_name) in enumerate(us_timezones.items()):
        tz = pytz.timezone(tz_name)
        now = datetime.now(tz).strftime('%Y-%m-%d %I:%M:%S %p')
        with (col1 if i % 2 == 0 else col2):
            st.metric(label, now)

    # Refresh notice
    st.caption(f"Refreshing every {refresh_interval} seconds...")
    time.sleep(refresh_interval)
    st.rerun()
