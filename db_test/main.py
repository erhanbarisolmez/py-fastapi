from fastapi  import FastAPI
from fastapi.testclient import TestClient

from .database import Base, get_db, SessionLocal, engine
from models import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

def override_get_db():
  try:
    db = SessionLocal()
  finally:
    db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@app.post("/create")
def test_create_user():
  response = client.post(
    "/users/",
    json={"email": "deadpool@example.com", "password": "1234"},
  )
  assert response.status_code == 200, response.text
  data = response.json()
  assert data["email"] == "deadpool@example.com"
  user_id = data["id"]
  
  response =client.get(f"/users/{user_id}")
  assert response.status_code == 200, response.text
  data = response.json()
  assert data["email"] == "deadpool@example.com"
  assert data["id"] == user_id

