Установить необходимые зависимости
```commandline
pip install requirements.txt
```

Запуск сервера с API:
```commandline
uvicorn main:app --host 0.0.0.0 --port 1234
```

Запуск тестов:
```commandline
pytest api_testing/test_api.py 
```