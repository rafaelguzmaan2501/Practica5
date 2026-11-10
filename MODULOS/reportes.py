import streamlit as st
from config.conexion import obtener_conexion


def mostrar_reportes():
    st.header("Reportes de ventas")
    st.write("Aquí se muestran las ventas registradas en el sistema.")

    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        if conexion is None:
            return

        cursor = conexion.cursor()
        cursor.execute("SELECT Producto, Cantidad FROM VENTAS")
        filas = cursor.fetchall()

        if filas:
            datos = [{"Producto": f[0], "Cantidad": f[1]} for f in filas]
            st.metric("Total de ventas registradas", len(datos))
            st.dataframe(datos, use_container_width=True)
        else:
            st.info("Todavía no hay ventas registradas.")
    except Exception as error:
        st.error(f"Error al cargar los reportes: {error}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()
