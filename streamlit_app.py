import streamlit as st
import pandas as pd
import numpy as np

st.title("Out of Pocket: Thoughts with Marcus")

with st.sidebar:
    st.header("Marcus's conspiracy theories")
    st.write("Chocolate milk does in fact come from brown cows.")
    st.write("Birds are not real. They are government drones.")
    st.write("Jonah Hill is a prodigy.")

st.header('EVIL', divider = 'rainbow')

st.markdown('Every')
st.markdown('Villain')
st.markdown('Is')
st.markdown('Lemons')

st.subheader('Lemon Counter')
col1, col2 = st.columns(2)

with col1:
    x = st.slider('How lemons are you?',1,10)
with col2:
    st.write("The value of :red[***Lemons***] is",x)

st.subheader('Lemons per Moral Compass')
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.area_chart(chart_data)

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Couch Potato", "Regular Vegetable"])
tab1.write("potato go brr")
tab2.write("broccoli")

# You can also use "with" notation:
with tab1:
    st.radio("Select one:", ["X-Men", "Avengers"])

expand = st.expander("My label", icon=":material/info:")
expand.write("Inside the expander.")
pop = st.popover("Button label")
pop.checkbox("Show all")

# You can also use "with" notation:
with expand:
    st.radio("Select one:", [3, 4])


st.button("Click me")
#st.download_button("Download file",data)
st.feedback("thumbs")
url = 'https://www.icegif.com/wp-content/uploads/2023/01/icegif-162.gif'
st.link_button("Click for unlimited moneys", url)
#st.page_link("app.py", label="Home")
#st.data_editor("Edit data", data)
st.checkbox("I agree")
st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.camera_input("Take a picture")
st.color_picker("Pick a color")

# Use widgets' returned values in variables:
# for i in range(int(st.number_input("Num:"))):
#     foo()
# if st.sidebar.selectbox("I:",["f"]) == "f":
#     b()
# my_slider_val = st.slider("Quinn Mallory", 1, 88)
# st.write(slider_val)

# Disable widgets to remove interactivity:
#st.slider("Pick a number", 0, 100, disabled=True)