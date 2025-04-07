import streamlit as st
# Hamburger Menu
st.set_page_config(
    page_title = "App Description",
    layout = "wide",
    initial_sidebar_state = "collapsed",
    menu_items={"About": "Welcome to our application",
    }
)

# Definition of wanted font and colours
primary_color = "#A1289B"  # Esempio: Viola Scuro per i titoli
secondary_color = "#A1289B"  # Esempio: Viola Scuro per il testo normale
accent_color = "#000000"   # Esempio: Nero per i sottotitoli
main_font = "sans-serif"    # Esempio: Font sans-serif
title_font = "sans-serif"       # Esempio: Font serif per i titoli

# Definition of the background color as a CSS string
custom_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-color: white; 
    opacity: 1;
}}

h1, h2, h3 {{
    color: {primary_color};
    font-family: {title_font};
    text-align: center;
    font-size: 4rem !important;
}}

h4 {{
    color: {accent_color};
    font-family: {main_font};
    text-align: center;
}}

p, div, ul, ol, li {{
    color: {secondary_color};
    font-family: {main_font};
    text-align: center;
}}

</style>
"""

# Other colours (lightblue ones):
# #6B81F2
# #84E4FB
# #C5F8FC

# Report in Streamlit this colour of background
st.markdown(custom_css, unsafe_allow_html=True)
