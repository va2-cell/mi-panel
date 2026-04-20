import streamlit as st
import datetime

st.set_page_config(page_title="Panel de Edwin", page_icon="🛡️")

st.title("🛡️ Panel de Control de Ariar steel")
st.markdown("---")

# Menú lateral
with st.sidebar:
    st.header("Opciones")
    opcion = st.selectbox("Ir a:", ["Inicio", "Presupuestos", "Registro de Horas"])

if opcion == "Inicio":
    st.subheader("Bienvenido")
    st.write("Usa el menú de la izquierda para gestionar tus proyectos de trabajo o tus herramientas de seguridad.")
    st.info("Este panel corre localmente en tu Chromebook.")

elif opcion == "Presupuestos":
    st.header("💰 Generador de Presupuestos")
    col1, col2 = st.columns(2)
    
    with col1:
        cliente = st.text_input("Nombre del Cliente")
        varillas = st.number_input("Cantidad de Varillas", min_value=0, step=1)
    
    with col2:
        precio_v = st.number_input("Precio por Varilla ($)", value=15)
        yardas = st.number_input("Yardas de Concreto", min_value=0)

    if st.button("Generar y Guardar"):
        total = (varillas * precio_v) + (yardas * 110) # Ejemplo 110 por yarda
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Mostrar en pantalla
        st.success(f"Presupuesto calculado: ${total}")
        
        # Guardar en archivo
        filename = f"presupuesto_{cliente}_{fecha}.txt"
        with open(filename, "w") as f:
            f.write(f"CLIENTE: {cliente}\nFECHA: {fecha}\nTOTAL: ${total}")
        st.write(f"Archivo guardado como: `{filename}`")

elif opcion == "Registro de Horas":
    st.header("🕒 Control de Tiempo")
    tarea = st.text_input("¿En qué trabajaste hoy?")
    horas = st.number_input("Cantidad de horas", min_value=0.0, step=0.5)
    
    if st.button("Guardar Jornada"):
        with open("registro_horas.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {tarea} - {horas} horas\n")
        st.success("Horas registradas correctamente.")
