# импортируем библиотеку для работы со случайными числами
import random

# импортируем класс для создания экземпляра FastAPI-приложения
from fastapi import FastAPI

# создаём экземпляр FastAPI-приложения
app = FastAPI()

# обрабатываем запросы к корню приложения
@app.get("/")
def read_root():
    return {"Hello": "World"}

# обрабатываем запросы к специальному пути для получения предсказания модели
# временно имитируем предсказание со случайной генерацией score
@app.get("/api/churn/{user_id}")
def get_prediction_for_item(user_id: str):
    return {"user_id": user_id, "score": random.random()}

# обрабатывает get запросы по специальному пути
@app.get("/service-status")
def health_check():
    return {'status': 'ok'}

@app.get("/api/credit/{client_id}")
def is_credit_approved(user_id: str):
    user_id = user_id
    score = random.random()
    return {"approved": [0, 1][score > 0.8]}