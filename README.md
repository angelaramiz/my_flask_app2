# 🧪 Mi App Flask con PostgreSQL

Una aplicación Flask básica que se conecta a una base de datos PostgreSQL.

## 📦 Requisitos

- Python 3.12
- PostgreSQL instalado y corriendo
- Base de datos `mi_flask_app` creada

## 🛠️ Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/mi-flask-app.git 
cd mi-flask-app

# 2. Crea el entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Crea la base de datos
sudo -u postgres psql -c "CREATE DATABASE mi_flask_app;"

# 5. Ejecuta la app
python run.py
