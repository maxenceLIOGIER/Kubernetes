FROM python:3.11-slim

# Définir le répertoire de travail
COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Copier les fichiers du client
COPY app.py app.py

# copie des images
COPY setosa.jpg setosa.jpg
COPY versicolor.jpg versicolor.jpg
COPY virginica.jpg virginica.jpg


# Installer les dépendances
RUN pip install -r requirements.txt

# Commande par défaut : exécuter le client
CMD ["streamlit", "run", "app.py"]
