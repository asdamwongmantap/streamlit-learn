import streamlit as st
# import yaml
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth
# from apps import dashboard,analyze,cluster # import your app modules here
# import pandas as pd
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Streamlit learn", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
with st.sidebar:
    selected = option_menu("Main Menu", ["Dashboard","Analisa Produk", 'Klaster Produk'], 
        icons=['house','basket', 'pie-chart'], menu_icon="cast", default_index=0)
    selected

if selected == 'Dashboard':
    st.write("Hello")