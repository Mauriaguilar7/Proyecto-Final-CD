import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.hipotesis import (
    plot_annualIncome_Age,
    plot_SpendingScore_Age,
    plot_AnnualIncome_Gender,
    statistical_testAnnualIncome_Gender,
    plot_SpendingScore_AgeGroup,
    plot_workExperience_AgeGroup
)

# Carga del DataFrame original
@st.cache_data
def load_data():
    return pd.read_csv("data/Customers.csv")

# Configuración de la página
st.title("Validación de hipótesis planteadas")

# Cargar datos
df = load_data()

st.header("Hipótesis 1: Las personas al ser más jóvenes presentan menos ingresos anuales.")
fig = plot_annualIncome_Age(df)  # Solo se retorna una figura
st.pyplot(fig)  # Mostrar la figura usando Streamlit
st.write("""
Se puede observar que la correlación entre el ingreso anual y las edades de los sujetos es aproximadamente nula, lo que significa que no necesariamente si aumenta una variable la otra aumentará tambien. Además podría significar que hay mas que factores que influyen en el ingreso anual de las personas, por lo que no se respalda la hipótesis de que a menor edad menor es el ingreso anual.
""")

st.header("Hipótesis 2: El puntaje de gastos está directamente relacionado con el tamaño de la familia.")
st.write(f"""La correlación entre gastos con tamaño de familia es de: 
         
         {plot_SpendingScore_Age(df)}
""")
st.write("""
         El análisis de los datos indican que no existe una relación significativa entre el puntaje de gastos y el tamaño de la familia. Esto se respalda en el resultado de la correlación, que muestra un valor cercano a cero. Por lo tanto, se puede decir que el tamaño de la familia no tiene un impacto relevante o significativo en el puntaje de gastos.
         """)



st.header("Hipótesis 3: La cantidad de ingresos anuales son indiferentes al genero de las personas.")
fig = plot_AnnualIncome_Gender(df)  
st.pyplot(fig)  # Mostrar la figura usando Streamlit

t_stat, p_value = statistical_testAnnualIncome_Gender(df)

st.write(f"""
Estadístico t: {t_stat}

P-valor: {p_value}
""")


st.write("""
Analizando el gráfico de ingresos anuales vs género es posible observar que las medias de ingresos por género son aproximadamente iguales. Además al realizar el análisis estadístico con la prueba t de Student se puede respaldar la hipótesis de que los ingresos anuales son inderentes al género gracias a la comparación entre medias de cada género.
""")


st.header("Hipótesis 4: El gasto de las personas menores a 30 años es menor a la de las personas de 30 años o más.")
fig = plot_SpendingScore_AgeGroup(df)
st.pyplot(fig)  # Mostrar la figura usando Streamlit

st.write(""" 
Con base en el análisis representado en la gráfica, se observa que el puntaje de gasto promedio de las personas menores de 30 años es ligeramente mayor que el de las personas de 30 años o más, lo que contradice la hipótesis. Esto indica que los datos analizados no respaldan la afirmación planteada, ya que muestran un resultado diferente al esperado.
""")


st.header("Hipótesis 5: Las personas debajo de los 25 años de edad tienen menor cantidad de experiencia laboral que aquellos sobre la edad de 25.")
fig = plot_workExperience_AgeGroup(df)
st.pyplot(fig)  # Mostrar la figura usando Streamlit

st.write(""" 
La gráfica refleja que las personas menores de 25 años presentan un promedio de experiencia laboral mayor al de las personas de 25 años o más. Este resultado es inusual, ya que contradice la tendencia general donde la experiencia laboral tiende a aumentar con la edad, lo que podría responder a factores específicos utilizados para este estudio.
         """)