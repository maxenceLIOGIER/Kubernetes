import requests
import streamlit as st

# URL de l'API serveur
SERVER_URL = "http://server:8000/predict"

# Interface Streamlit pour l'entrée des données
st.title("Prédiction de la fleur Iris")

sepal_length = st.number_input("Longueur du sépale", min_value=0.0, value=5.1)
sepal_width = st.number_input("Largeur du sépale", min_value=0.0, value=3.5)
petal_length = st.number_input("Longueur du pétale", min_value=0.0, value=1.4)
petal_width = st.number_input("Largeur du pétale", min_value=0.0, value=0.2)

# Créer le dictionnaire avec les données saisies par l'utilisateur
data = {
    "sepal_length": sepal_length,
    "sepal_width": sepal_width,
    "petal_length": petal_length,
    "petal_width": petal_width
}

# Envoi de la requête POST à l'API
if st.button("Faire une prédiction"):
    try:
        response = requests.post(SERVER_URL, json=data)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        if response.status_code == 200:
            st.write("Prediction:", response.json()["prediction"])
            st.image(response.json()["image"])
        else:
            st.write(f"Error {response.status_code}: {response.text}")
    
    except requests.exceptions.RequestException as e:
        st.write(f"Erreur pendant la requête: {e}")