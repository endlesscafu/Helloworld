import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('Uso de st.write con datos personales')

# Ejemplo 1 - Texto en Markdown
st.write("¡Hola, **Carlos**! Bienvenido a tu app :smiley:")

# Ejemplo 2 - Mostrar un número
st.write(2025)

# Ejemplo 3 - DataFrame personalizado con datos ficticios
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [22, 25, 20, 23],
    'Ciudad': ['Puebla', 'CDMX', 'Monterrey', 'Guadalajara']
}
df = pd.DataFrame(datos)
st.write(df)

# Ejemplo 4 - Combinación de texto + DataFrame
st.write("Tabla personalizada", df, "Gracias por verla.")

# Ejemplo 5 - Gráfico con datos aleatorios (puedes cambiarlo por tus datos)
df2 = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['x', 'y', 'tamaño']
)
grafico = alt.Chart(df2).mark_circle().encode(
    x='x',
    y='y',
    size='tamaño',
    color='tamaño',
    tooltip=['x', 'y', 'tamaño']
)
st.write("Gráfico de dispersión con datos aleatorios", grafico)

