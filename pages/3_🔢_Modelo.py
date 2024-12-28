import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Definir una función para entrenar el modelo
@st.cache_resource
def train_model(data):
    # Eliminar columnas innecesarias
    data = data.drop(columns=["CustomerID", "Gender", "Profession"])

    # Preparar las características (X) y el objetivo (y)
    X = data.drop(columns=["Spending Score (1-100)"])
    y = data["Spending Score (1-100)"]

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar el modelo de Regresión Lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Guardar el modelo entrenado
    model_path = "models/LinearRegression_model.pkl"
    joblib.dump(model, model_path)

    # Evaluar el modelo
    y_pred = model.predict(X_test)
    metrics = {
        "r2_score": r2_score(y_test, y_pred),
        "mean_squared_error": mean_squared_error(y_test, y_pred),
    }

    return model, metrics

# Definir una función para cargar el conjunto de datos
@st.cache_data
def load_data():
    # Cargar el conjunto de datos
    data = pd.read_csv("data/Customers.csv")
    st.write("Vista previa del conjunto de datos cargado desde el archivo local:")
    st.dataframe(data.head())
    return data

try:
    # Cargar el conjunto de datos
    data = load_data()

    # Entrenar el modelo
    model, metrics = train_model(data)

    # Mostrar métricas del modelo
    st.title("Métricas del Modelo")
    st.metric("R² Score", f"{metrics['r2_score']:.2f}")
    st.metric("Mean Squared Error", f"{metrics['mean_squared_error']:.2f}")

except FileNotFoundError:
    st.error("El archivo Customers.csv no se encontró. Verifica que exista en el folder especificado.")
except Exception as e:
    st.error(f"Ocurrió un error: {e}")

# Sección para cargar nuevos datos para predicciones
st.title("Realizar predicciones con nuevos datos")
prediction_file = st.file_uploader("Sube un archivo CSV para realizar predicciones", type=["csv"])

if prediction_file is not None:
    try:
        # Cargar el archivo subido
        prediction_data = pd.read_csv(prediction_file)
        st.write("Vista previa del archivo cargado para predicciones:")
        st.dataframe(prediction_data.head())

        # Eliminar columnas innecesarias si existen
        for col in ["CustomerID", "Gender", "Profession"]:
            if col in prediction_data.columns:
                prediction_data = prediction_data.drop(columns=[col])

        # Asegurar que la columna objetivo no esté incluida como característica
        if "Spending Score (1-100)" in prediction_data.columns:
            prediction_data = prediction_data.drop(columns=["Spending Score (1-100)"])

        # Verificar si todas las características necesarias están presentes
        required_features = model.feature_names_in_
        missing_features = set(required_features) - set(prediction_data.columns)
        if missing_features:
            st.error(f"Faltan las siguientes columnas necesarias: {missing_features}")
        else:
            # Predecir nuevos datos
            predictions = model.predict(prediction_data)

            # Mostrar predicciones
            st.write("Predicciones realizadas exitosamente:")
            st.dataframe(pd.DataFrame({
                "Predicción de Spending Score": predictions
            }))
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo de predicción: {e}")
