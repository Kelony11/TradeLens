# app/database.py

import firebase_admin
from firebase_admin import credentials, firestore

def init_db():
    # Avoid double-initialization when using uvicorn --reload
    if not firebase_admin._apps:
        cred = credentials.Certificate("app/credentials/firebase-key.json")
        firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_db()

def get_db():
    return db
