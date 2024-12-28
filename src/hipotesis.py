import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def plot_annualIncome_Age(df):
    plt.figure(figsize=(8, 6))
    sns.regplot(x='Age', y='Annual Income ($)', data=df, scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('Relación entre Edad e Ingresos Anuales (con regresión)')
    plt.xlabel('Edad')
    plt.ylabel('Ingresos Anuales')
    plt.show() 
