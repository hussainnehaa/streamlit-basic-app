import streamlit as st
from datetime import datetime
import pytz
import time

st.set_page_config(page_title="US Time Dashboard", layout="centered")
st.title("🕒 US Time Zone Dashboard")

us_timezones = {
    "Eastern Time (ET)": "US/Eastern",
    "Central Time (CT)": "US/Central",
    "Mountain Time (MT)": "US/Mountain",
    "Pacific Time (PT)": "US/Pacific"
}

placeholder = st.empty()

while True:
    with placeholder.container():
        st.subheader("Current Time in U.S. Time Zones:")
        cols = st.columns(2)
        for i, (tz_name, tz_zone) in enumerate(us_timezones.items()):
            now = datetime.now(pytz.timezone(tz_zone)).strftime("%Y-%m-%d %H:%M:%S")
            with cols[i % 2]:
                st.metric(label=tz_name, value=now)
    time.sleep(1)
