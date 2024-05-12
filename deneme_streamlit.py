import streamlit as st

st.write("Hello world!")

# favourite movie input
fav_movie = st.text_input("Type your favourite movie.")
is_clicked = st.button("Vale")

if fav_movie != "" and is_clicked:
    st.write(f'your favourite movie is: {fav_movie}')

