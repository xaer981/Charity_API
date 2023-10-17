# QRKot
Учебный проект, позволяющий создавать благотворительные фонды и отправлять нецелевые пожертвования (они автоматически распределяются по фондам (сначала - ранее созданные).


## Технологии
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/)
- [Uvicorn](https://www.uvicorn.org/)
## Установка
Копируем репозиторий:
```
git clone
```
Создаём и активируем виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate (windows) / source venv/bin/activate (mac)
```

Устанавливаем зависимости:
```
pip install -r requirements.txt
```

Запускаем миграции
```
alembic upgrade head
```

Запускаем сервер
```
uvicorn app.main:app
```

<p align=center>
  <a href="url"><img src="https://github.com/xaer981/xaer981/blob/main/main_cat.gif" align="center" height="40" width="128"></a>
</p>
