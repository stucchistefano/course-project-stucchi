import streamlit as st

# Hamburger Menu
st.set_page_config(
    page_title = "KPills",
    layout = "wide",
    initial_sidebar_state = "collapsed",
    menu_items={"About": "Welcome to our application",
    }
)

# Definition of wanted font and colours
primary_color = "#A1289B"  # Esempio: Viola Scuro per i titoli
secondary_color = "#A1289B"  # Esempio: Viola Scuro per il testo normale
white_color = "#FFFFFF" # White
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

h1, h2 {{
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

p {{
    color: {white_color};
    font-family: {main_font};
    text-align: center;
    font-size: 1.3rem !important;
}}

ul, ol, li, h3 {{
    color: {white_color};
    font-family: {main_font};
    text-align: center;
}}


div {{
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

# Possible background image
st.image("SimulationGIF.gif", use_container_width=True)

# Title in possible rectangle
with st.container():
    st.title("KPills\n")

# Explanation in possible container
with st.container():
    st.markdown(
        """
        <style>
        .stContainer > div {
            width: 90%;
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Define your custom CSS
custom_css = """
<style>
.my-container {
 background-color: #A1289B;
 padding: 20px;
 border-radius: 5px;

 color: #FFFFFF;
 font-family: sans-serif;
 text-align: center;
 font-size: 1.3rem !important;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Use the custom class in a container
st.markdown('<div class="my-container">The "must-have" app for <br> coaches & athletes </div>', unsafe_allow_html=True)


# Buttons
# Apply the custom CSS
left, middle, right = st.columns(3)
middle.button("Discover KPills", use_container_width=False)
    #middle.markdown('<p style="color:purple; font-size:20px;">Button Clicked</p>', unsafe_allow_html=True)
#if middle.button("Login", use_container_width=False):
middle.button("Login", use_container_width=False)