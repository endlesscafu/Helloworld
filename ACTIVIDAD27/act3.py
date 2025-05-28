import streamlit as st

st.header("Mi app con 3 botones")

# Botón 1
if st.button("Botón 1"):
    st.write("¡Hola! Presionaste el Botón 1 😊")
else:
    st.write("ADIOS")

st.write("---")  # separador visual

# Botón 2
if st.button("Botón 2"):
    st.write("¡Bienvenido al Botón 2! 🚀")
else:
    st.write("ADIOS")

st.write("---")  # separador visual

# Botón 3
if st.button("Botón 3"):
    st.write("¡Has activado el Botón 3! 🎉")
else:
    st.write("ADIOS")
