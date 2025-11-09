# Projet OOP : application de location de film en python
## Equipe
- Ali Belhassen
- Nicolas Papleux

## Lancer le projet
Le lancement se fait en deux commandes :
- `uvicorn app.main:app --reload` (pour lancer le serv)
- `streamlit run streamlit_app.py` (pour lancer le front)
## Arborescence du projet
```
film_rental/
├─ app/                       # Dossier principal du backend FastAPI
│  ├─ main.py                 # Point d'entrée du serveur FastAPI
│  ├─ database.py             # Connexion et configuration de la base SQLite
│  ├─ models.py               # Modèles ORM (structure des tables)
│  ├─ schemas.py              # Modèles Pydantic (validation et structure des données)
│  ├─ crud.py                 # Logique métier et accès à la base (Create, Read, Update, Delete)
│  └─ routers/                # Dossier contenant les routes de l’API
│     └─ movies.py            # Endpoints REST liés aux films (/movies)
│
├─ streamlit_app.py           # Interface web Streamlit (front-end)
│
├─ requirements.txt           # Liste des dépendances Python
│
└─ README.md                  # Documentation du projet
```
## Modules utilisés

- FastAPI: framework web pour créer une API REST.
- Uvicorn: serveur web ASGI utilisé pour exécuter l’application FastAPI.
- SQLAlchemy: ORM équivalent à JPA API en Python.
- Pydantic: pour gèrer la validation et la conversion automatique des données entrantes/sortante.
- Streamlit: framework Python pour un front simple.
- Requests: bibliothèque utilisée par Streamlit pour communiquer avec l’API FastAPI via des requêtes HTTP.
