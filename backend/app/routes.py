from app import app

@app.route('/')
def home():
    return 'Backend da Organização Financeira está online!'