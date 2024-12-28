import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.eda import (
    get_gender_description,
    get_age_description,
    get_annual_income_description,
    get_spending_score_description,
    get_profession_description,
    get_work_experience_description,
    get_family_size_description
)

# Carga del DataFrame original
@st.cache_data
def load_data():
    return pd.read_csv("data/Customers.csv")

# Configuración de la página
st.title("Análisis Exploratorio de Datos (EDA)")

# Cargar datos
df = load_data()

# Vista previa del dataset
st.write("Vista previa del dataset")
st.dataframe(pd.concat([df.head(), df.tail()]))

# Información de las columnas
if st.checkbox("Mostrar descripción del Género"):
    gender_description, gender_counts = get_gender_description(df)
    st.write("Información estadística del Género:")
    st.table(gender_description)
    st.write("Cantidad de cada género:")
    st.table(gender_counts)

if st.checkbox("Mostrar descripción de la Edad"):
    age_description = get_age_description(df)
    st.write("Información estadística de la Edad:")
    st.table(age_description)

if st.checkbox("Mostrar descripción del Ingreso Anual"):
    annual_income_description = get_annual_income_description(df)
    st.write("Información estadística del Ingreso Anual:")
    st.table(annual_income_description)

if st.checkbox("Mostrar descripción de la Puntuación de Gasto"):
    spending_score_description = get_spending_score_description(df)
    st.write("Información estadística de la Puntuación de Gasto:")
    st.table(spending_score_description)

if st.checkbox("Mostrar descripción de la Profesión"):
    profession_description = get_profession_description(df)
    st.write("Información estadística de la Profesión:")
    st.table(profession_description)

if st.checkbox("Mostrar descripción de la Experiencia Laboral"):
    work_experience_description = get_work_experience_description(df)
    st.write("Información estadística de la Experiencia Laboral:")
    st.table(work_experience_description)

if st.checkbox("Mostrar descripción del Tamaño de la Familia"):
    family_size_description = get_family_size_description(df)
    st.write("Información estadística del Tamaño de la Familia:")
    st.table(family_size_description)

# Agregar la preparación de los datos con una descripción
st.write("""
### Preparación de los datos para su posterior análisis

Primero se verifica si hay valores perdidos en el conjunto de datos, y en dado caso estos se encuentren en columnas o variables que no serán de utilidad, estas columnas pueden ser removidas. Para este análisis en específico se decidió remover del conjunto de datos las siguientes columnas:

* Profession
* CustomerID

Ya que no son de interés para el análisis que se desea realizar.
""")

# Eliminar las columnas no relevantes
df_clean = df.drop(columns=['Profession', 'CustomerID'])

# Mostrar información del dataset limpio (sin columnas eliminadas)
st.write("Información del dataset limpio:")
info_clean = pd.DataFrame({
    'Column': df_clean.columns,
    'Non-Null Count': df_clean.notnull().sum(),
    'Dtype': df_clean.dtypes,
})
info_clean['Non-Null Count'] = info_clean['Non-Null Count'].astype(int)
st.dataframe(info_clean)

# Verificando valores perdidos en el dataset limpio
st.write("Valores perdidos en el dataset limpio:")
st.write(df_clean.isna().sum())

# Matriz general de correlaciones de edad, ingreso anual, puntuaje de gasto, tamaño de familia
st.write("""
### Matriz general de correlaciones de edad, ingreso anual, puntuaje de gasto, tamaño de familia
""")

correlation_matrix = df_clean[['Age','Annual Income ($)','Spending Score (1-100)', 'Family Size']].corr()

# Graficar la matriz de correlación
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
st.pyplot(plt)
