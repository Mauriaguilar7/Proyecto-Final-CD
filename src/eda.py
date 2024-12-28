import matplotlib.pyplot as plt
import seaborn as sns

# Funciones estadísticas
def get_gender_description(df):
    gender_description = df['Gender'].describe()
    gender_counts = df['Gender'].value_counts()
    return gender_description, gender_counts

def get_age_description(df):
    return df['Age'].describe()

def get_annual_income_description(df):
    return df['Annual Income ($)'].describe()

def get_spending_score_description(df):
    return df['Spending Score (1-100)'].describe()

def get_profession_description(df):
    return df['Profession'].describe()

def get_work_experience_description(df):
    return df['Work Experience'].describe()

def get_family_size_description(df):
    return df['Family Size'].describe()

# Función para graficar la matriz de correlación
def plot_correlation_matrix(df):
    correlation_matrix = df[['Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Family Size']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True)
    plt.title('Matriz de Correlación')
    st.pyplot(plt)  # Muestra la gráfica en Streamlit
    plt.close()  # Cierra la figura para evitar que se muestre dos veces
