FROM python:3.11-slim

# Définir le répertoire de travail
COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Copier les fichiers du client
COPY app.py app.py

# Installer les dépendances
RUN pip install -r requirements.txt

# Commande par défaut : exécuter le client
CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "app:app"]
