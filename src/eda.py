import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def plot_age_distribution(df):
    """Grafica la distribución de edades."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Age'], bins=30, kde=True, color='blue', ax=ax)
    ax.set_title('Distribución de Edad')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

def plot_income_vs_spending(df):
    """Grafica Ingreso Anual vs Puntuación de Gasto."""
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Annual Income ($)', y='Spending Score (1-100)', hue='Gender', data=df, ax=ax)
    ax.set_title('Ingreso Anual vs Puntuación de Gasto')
    ax.set_xlabel('Ingreso Anual ($)')
    ax.set_ylabel('Puntuación de Gasto')
    ax.legend(title='Género')
    st.pyplot(fig)

def plot_profession_distribution(df):
    """Grafica la distribución de profesiones."""
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(y='Profession', data=df, order=df['Profession'].value_counts().index, palette='viridis', ax=ax)
    ax.set_title('Distribución de Profesiones')
    ax.set_xlabel('Frecuencia')
    ax.set_ylabel('Profesión')
    st.pyplot(fig)

def plot_heatmap(df):
    """Grafica un heatmap de correlaciones."""
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title('Heatmap de Correlaciones')
    st.pyplot(fig)

def get_gender_description(df):
    """Devuelve la descripción estadística del género y la cantidad de cada género."""
    gender_description = df['Gender'].describe()
    gender_counts = df['Gender'].value_counts()  # Cuenta las ocurrencias de cada valor en la columna 'Gender'
    
    return gender_description, gender_counts

def get_age_description(df):
    """Devuelve la descripción estadística de la edad."""
    return df['Age'].describe()

def get_annual_income_description(df):
    """Devuelve la descripción estadística del ingreso anual."""
    return df['Annual Income ($)'].describe()

def get_spending_score_description(df):
    """Devuelve la descripción estadística de la puntuación de gasto."""
    return df['Spending Score (1-100)'].describe()

def get_profession_description(df):
    """Devuelve la descripción estadística de las profesiones."""
    return df['Profession'].describe()

def get_work_experience_description(df):
    """Devuelve la descripción estadística de la experiencia laboral."""
    return df['Work Experience'].describe()

def get_family_size_description(df):
    """Devuelve la descripción estadística del tamaño de la familia."""
    return df['Family Size'].describe()
