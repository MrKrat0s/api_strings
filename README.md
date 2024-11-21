Установить необходимые зависимости
```commandline
pip install requirements.txt
```

Запуск сервера с API:
```commandline
cd string_project
uvicorn main:app --host host --port port
--host  ip адрес сервера
--port  порт сервера
```

Запуск тестов:
```commandline
pytest --host host --port port test_api.py
--host  ip адрес сервера
--port  порт сервера
```