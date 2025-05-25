import streamlit as st
from datetime import datetime
import pytz

# Auto-refresh every 1 second
st.experimental_rerun()  # This is one way (loopless), but deprecated

# Better way (new API)
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1000, limit=None, key="time_refresh")

st.set_page_config(page_title="US Time Dashboard", layout="centered")
st.title("🕒 US Time Zone Dashboard")

us_timezones = {
    "Eastern Time (ET)": "US/Eastern",
    "Central Time (CT)": "US/Central",
    "Mountain Time (MT)": "US/Mountain",
    "Pacific Time (PT)": "US/Pacific"
}

st.subheader("Current Time in U.S. Time Zones:")
cols = st.columns(2)
for i, (tz_name, tz_zone) in enumerate(us_timezones.items()):
    now = datetime.now(pytz.timezone(tz_zone)).strftime("%Y-%m-%d %H:%M:%S")
    with cols[i % 2]:
        st.metric(label=tz_name, value=now)
