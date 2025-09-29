from app import app, db
from app.models import User # Importe o modelo de usuário

with app.app_context():
    db.create_all()
    print("Banco de dados e tabelas criadas com sucesso!")