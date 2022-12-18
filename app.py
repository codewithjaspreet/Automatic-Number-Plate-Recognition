import streamlit as st

from report_page import intro
from team_members import team

from demo import demo


page_Selection = st.sidebar.selectbox(
    "Select", ("Demo", "Report", 'Team Members'))

if page_Selection == "Demo":
    demo()

elif page_Selection == "Report":
    intro()


elif page_Selection == "Team Members":
    team()
