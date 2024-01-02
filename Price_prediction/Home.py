import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Home",
    page_icon=None,
    layout="wide",
    
)

st.title("PRICE PREDICTIONS")





selected=option_menu(
       menu_title=None,
       options=["Long-Short Term Memory","Random Forests","Gated Recurrent Unit network"],
       orientation="horizontal",
        )

if selected=="Long-Short Term Memory":
    st.title(f"you have selected {selected}")
if selected=="Random Forests":
    st.title(f"you have selected {selected}")
if selected=="Gated Recurrent Unit network":
    st.title(f"you have selected {selected}")
