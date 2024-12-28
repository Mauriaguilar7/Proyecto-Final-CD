import streamlit as st

# Configuración inicial
st.set_page_config(
    page_title="Proyecto Final",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Página de inicio
st.title("Proyecto Final")

st.markdown("""
## Bienvenido
Este proyecto incluye las siguientes páginas:

- **Inicio**
- **Análisis Exploratorio**: Gráficas y análisis EDA de los datos.
""")
