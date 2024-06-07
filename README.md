# MLE-FastAPI
Приложение на FastAPI для предсказаний оттока клиента:

# Запуск
uvicorn churn_app:app --reload --port 8081 --host 0.0.0.0

Чтобы перейти к интерактивной документации, откройте в браузере страницу http://127.0.0.1:8081/docs. Можно увидеть, что в приложении есть обработчик POST-запросов на URL /api/churn

В запросе нужно отправить два параметра — user_id и model_params. Причём model_params передаётся в теле запроса, оно обозначено как Request Body.


Кликните на Try it out. Заполните произвольной строкой параметр user_id, а в Request Body скопируйте и вставьте свой, например:

{
  "gender": 1,
  "SeniorCitizen": 0,
  "Partner": 0,
  "Dependents": 0,
  "Type": 0.5501916796819537,
  "PaperlessBilling": 1,
  "PaymentMethod": 0.2192247621752094,
  "MonthlyCharges": 50.8,
  "TotalCharges": 288.05,
  "MultipleLines": 0,
  "InternetService": 0.3437455629703251,
  "OnlineSecurity": 0,
  "OnlineBackup": 0,
  "DeviceProtection": 0,
  "TechSupport": 1,
  "StreamingTV": 0,
  "StreamingMovies": 0,
  "days": 245,
  "services": 2
}

Нажмите на кнопку Execute — и POST-запрос уйдёт в FastAPI-приложение на URL /api/churn. Ниже появится ответ приложения
