import streamlit as st

from report_page import intro

from demo import demo


page_Selection = st.sidebar.selectbox("Select" , ("Demo" , "Report",'About Algorithm' ,'Team Members'))

if page_Selection == "Demo":
    demo()

elif page_Selection == "Report":
    intro()

elif page_Selection == "About Algorithm":
    intro()

elif page_Selection == "Team Members":
     intro()   