import firebase_admin
from firebase_admin import credentials, firestore
import os

# Inicialização do Firebase (garante que só inicializa uma vez)
if not firebase_admin._apps:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DADOS_DIR = os.path.join(BASE_DIR, 'dados')
    cred_path = os.path.join(DADOS_DIR, "serviceAccountKey.json")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()

def carregar_firestore(nome_colecao):
    """
    Carrega todos os documentos de uma coleção do Firestore e retorna como lista de dicts (JSON).
    """
    colecao_ref = db.collection(nome_colecao)
    return [doc.to_dict() | {'id': doc.id} for doc in colecao_ref.stream()]

def salvar_firestore(nome_colecao, dados):
    """
    Salva um documento na coleção do Firestore.
    Se 'dados' for uma lista, salva cada item como documento separado.
    Se 'dados' for dict, salva como um único documento (gera id automático).
    Retorna lista de ids dos documentos salvos.
    """
    colecao_ref = db.collection(nome_colecao)
    ids = []
    if isinstance(dados, list):
        for item in dados:
            doc_ref = colecao_ref.document()
            doc_ref.set(item)
            ids.append(doc_ref.id)
    elif isinstance(dados, dict):
        doc_ref = colecao_ref.document()
        doc_ref.set(dados)
        ids.append(doc_ref.id)
    else:
        raise ValueError("Dados devem ser dict ou lista de dicts")
    return ids
