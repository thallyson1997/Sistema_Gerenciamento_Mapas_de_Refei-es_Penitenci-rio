from functions.firestore_utils import salvar_firestore

# Para salvar um único usuário (dict)
usuario = {"nome": "João", "email": "joao@email.com"}
ids = salvar_firestore("usuarios", usuario)

# Para salvar vários usuários (lista de dicts)
usuarios = [
    {"nome": "Maria", "email": "maria@email.com"},
    {"nome": "Carlos", "email": "carlos@email.com"}
]
ids = salvar_firestore("usuarios", usuarios)