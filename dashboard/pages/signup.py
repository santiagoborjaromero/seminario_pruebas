import streamlit as st
import datetime

st.title('Registro')

def func_registro():
    print("Registrado")
    

with st.form(key='my_form'):
    st.write("Por favor ingrese la información solicitada")
    st.text_input("Nombre completo", "", key="name", placeholder="Ingrese el nombre del usuario")
    st.text_input("Correo Electrónico", "", key="email", placeholder="Ingrese el email del usuario")
    st.text_input("Contraseña", "", key="pass", type="password", placeholder="Contraseña del usuario")
    submit = st.form_submit_button(label='Registrar', on_click=func_registro)