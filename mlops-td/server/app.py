from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import joblib
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import traceback

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# load the pre-trained model
model = joblib.load("model.pkl")

# Créer une instance de l'application FastAPI
app = FastAPI()

# Dictionnaire de correspondance entre les indices et les noms des fleurs
class_mapping = {
    0: {"name": "setosa", "image": "setosa.jpg"},
    1: {"name": "versicolor", "image": "versicolor.jpg"},
    2: {"name": "virginica", "image": "virginica.jpg"}
}

@app.post("/predict")
def predict(item: Item):
    try:
        # Convertir l'item reçu en données compatibles avec le modèle
        item_data = jsonable_encoder(item)
        
        # Préparer les données sous forme de liste pour la prédiction
        input_data = [[item_data['sepal_length'], item_data['sepal_width'],
                       item_data['petal_length'], item_data['petal_width']]]
        
        # Effectuer la prédiction avec le modèle
        prediction = int(model.predict(input_data))

        # Récupérer le nom de la classe à partir de l'indice retourné
        class_name = model.classes_[prediction] 
        # Utiliser l'indice pour obtenir le nom de la classe
        
        # Utiliser le dictionnaire pour obtenir le nom de la fleur et l'image correspondante
        class_info = class_mapping.get(prediction, {"name": "Unknown", "image": "unknown.jpg"})

        # Retourner le nom de la classe et l'URL de l'image comme réponse JSON
        return {"prediction": class_info["name"], "image": class_info["image"]}
    
    except Exception as e:
        # Capturer l'erreur et renvoyer un message d'erreur détaillé
        print("Error during prediction:", e)
        print(traceback.format_exc())
        return JSONResponse(status_code=500, content={"message": str(e)})