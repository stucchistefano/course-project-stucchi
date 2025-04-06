import streamlit as st

# Definition of wanted font and colours
primary_color = "#A1289B"  # Esempio: Grigio scuro per i titoli
secondary_color = "#A1289B"  # Esempio: Grigio per il testo normale
accent_color = "#000000"   # Esempio: Arancione per i sottotitoli
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

st.title("KPills")