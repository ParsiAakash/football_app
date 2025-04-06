# Football Info Backend
A Flask-based backend to serve football teams, players, areas, and matches. This app is built with SQL, Swagger, and Docker.

---

# Tech Stack

- Python 3.10
- Flask
- Flask-SQLAlchemy
- Marshmallow
- Swagger (Flasgger)
- SQLite (for dev; easily switchable)
- Docker
- Pytest + Flake8

---

# Running Locally (without Docker)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
