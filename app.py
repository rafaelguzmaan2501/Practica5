import streamlit as st
from MODULOS.login import login
from MODULOS.ventas import mostrar_venta
from MODULOS.reportes import mostrar_reportes

if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False

if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

if st.session_state["sesion_iniciada"]:
    st.sidebar.title("Menú")
    st.sidebar.write(f"Usuario: {st.session_state['usuario']}")
    st.sidebar.divider()

    opciones = ["Ventas", "Reportes", "Información"]
    seleccion = st.sidebar.radio("Seleccione una opción", opciones)

    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Reportes":
        mostrar_reportes()
    elif seleccion == "Información":
        st.header("Información del sistema")
        st.write("Aplicación desarrollada durante el Laboratorio de SGI.")

    st.sidebar.divider()
    if st.sidebar.button("Cerrar sesión"):
        st.session_state["sesion_iniciada"] = False
        st.session_state["usuario"] = ""
        st.rerun()
else:
    login()
