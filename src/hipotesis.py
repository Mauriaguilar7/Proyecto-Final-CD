import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from scipy.stats import ttest_ind



def plot_annualIncome_Age(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(x='Age', y='Annual Income ($)', data=df, scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'}, ax=ax)
    ax.set_title('Relación entre Edad e Ingresos Anuales (con regresión)')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Ingresos Anuales')
    return fig

def plot_SpendingScore_Age(df):
    return df['Spending Score (1-100)'].corr(df['Family Size'])


def plot_AnnualIncome_Gender(df):
    # Agrupamos los datos y calculamos el promedio
    AnnualIncome_Gender = df.groupby('Gender')['Annual Income ($)'].mean()

    # Crear figura y eje
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=AnnualIncome_Gender.index, y=AnnualIncome_Gender.values, palette="viridis", ax=ax)

    # Configuración del gráfico
    ax.set_title("Ingresos anuales y género")
    ax.set_xlabel("Género")
    ax.set_ylabel("Ingreso anual ($)")
    ax.set_xticks(range(len(AnnualIncome_Gender.index)))
    ax.set_xticklabels(AnnualIncome_Gender.index, rotation=45)

    return fig


def statistical_testAnnualIncome_Gender(df):
    # Filtrar ingresos por género
    male_income = df[df['Gender'] == 'Male']['Annual Income ($)']
    female_income = df[df['Gender'] == 'Female']['Annual Income ($)']

    # Prueba t de Student
    t_stat, p_value = ttest_ind(male_income, female_income)

    return t_stat, p_value


def plot_SpendingScore_AgeGroup(df):
    # Crear una nueva columna que agrupe por menores y mayores de 30 años
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 30, df['Age'].max()], labels=['Menores de 30', '30 o más'])

    # Agrupamos por los intervalos de edad y calculamos el promedio de gasto
    SpendingScore_AgeGroup = df.groupby('Age Group')['Spending Score (1-100)'].mean()

    # Convertimos el índice en cadenas para visualización en el eje X
    SpendingScore_AgeGroup.index = SpendingScore_AgeGroup.index.astype(str)

    # Usar la paleta de colores
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=SpendingScore_AgeGroup.index, y=SpendingScore_AgeGroup.values, palette="viridis")

    # Configuración del gráfico
    plt.title("Promedio de gasto por grupo de edad", fontsize=14)
    plt.xlabel("Grupo de Edad", fontsize=12)
    plt.ylabel("Puntaje de Gasto (1-100)", fontsize=12)
    plt.ylim(0, 100)
    plt.xticks(rotation=0)

    return fig

def plot_workExperience_AgeGroup(df):
    # Crear intervalos de edades de 5 en 5 usando pd.cut()
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 25, df['Age'].max()], labels=['Menores de 25', '25 o más'])

    # Agrupamos por los intervalos de edad y calculamos el promedio
    WorkExperience_AgeGroup = df.groupby('Age Group')['Work Experience'].mean()

    # Convertimos los intervalos en cadenas para visualización en el eje X
    WorkExperience_AgeGroup.index = WorkExperience_AgeGroup.index.astype(str)

    # Usar la paleta de colores de Seaborn automáticamente
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=WorkExperience_AgeGroup.index, y=WorkExperience_AgeGroup.values, palette="viridis")

    # Configuración del gráfico
    plt.title("Experiencia laboral promedio por grupo de edad")
    plt.xlabel("Grupo de Edad")
    plt.ylabel("Experiencia laboral promedio (años)")
    plt.ylim(0, 10)
    plt.xticks(rotation=0)

    return fig