import streamlit as st
import datetime

st.title('Autorización')

def func_login():
    print("Login")
    st.session_state.logged_in = True
    

with st.form(key='my_form'):
    st.write("Por favor ingrese usuario y contraseña")
    
    st.text_input("Usuario", "", key="user", placeholder="Ingrese del usuario")
    st.text_input("Contraseña", "", key="pass", type="password", placeholder="Contraseña del usuario")
    submit = st.form_submit_button(label='Ingresar', on_click=func_login)