import streamlit as st

st.title('SRHP')

def logout():
    st.session_state.logged_in = False
    st.rerun()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in == False:
    pages = []
    pages.append(st.Page("pages/signin.py", title="Ingreso", icon=":material/add_circle:"))
    pages.append(st.Page("pages/signup.py", title="Registro", icon=":material/add_circle:"))
    pg = st.navigation(pages, position="top")
else:
    dashboard = []
    admin = []
    dashboard.append(st.Page("pages/dashboard.py", title="Peliculas", icon=":material/add_circle:"))
    admin.append(st.Page("pages/user.py", title="Usuarios", icon=":material/add_circle:"))
    
    pg = st.navigation(
        {
            "Dashboards": dashboard,
            "Administración": admin,
        },
    )
    

st.set_page_config(page_title="SRHP", page_icon=":material/add_circle:")
pg.run()


