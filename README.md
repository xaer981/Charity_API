# Charity API 💰
Проект позволяет создавать благотворительные фонды и отправлять нецелевые пожертвования.


## Возможности:
- Создание и управление проектами.

  У каждого проекта есть название, описание и сумма, которую планируется собрать.
  Все пожертвования идут в проект, открытый раньше других;
  когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

- Создание и просмотр пожертвований.

  Каждый пользователь может сделать пожертвование.
  Пожертвования вносятся в фонд, а не в конкретный проект.

- Создание отчета по закрытым проектам.

  В отчете отображаются закрытые проекты, отсортированные по скорости сбора средств.
  В ответе передается ссылка на созданную электронную таблицу.

- Алгоритм распределения пожертвований.

  Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму.
  Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта.
  При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

- Права пользователей.

  Целевые проекты создаются администраторами сайта.
  Любой пользователь может видеть список всех проектов.
  Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.


## Технологии
- ![Static Badge](https://img.shields.io/badge/FastAPI-green)
- ![Static Badge](https://img.shields.io/badge/SQLAlchemy-green)
- ![Static Badge](https://img.shields.io/badge/Alembic-green)
- ![Static Badge](https://img.shields.io/badge/Pydantic-green)
- ![Static Badge](https://img.shields.io/badge/FastAPIUsers-green)
- ![Static Badge](https://img.shields.io/badge/Uvicorn-green)
## Установка

1. **Копируем репозиторий:**
   ```
   git clone https://github.com/xaer981/QRkot_spreadsheets.git
   ```

2. **Создаём и активируем виртуальное окружение:**

   На Windows:
   ```
   python -m venv venv
   ```

   ```
   source venv/Scripts/activate
   ```

   На Mac:
   ```
   python3 -m venv venv
   ```

   ```
   source venv/bin/activate
   ```

3. **Устанавливаем зависимости:**

   ```
   pip install -r requirements.txt
   ```

4. **Запускаем миграции**

   ```
   alembic upgrade head
   ```

5. **Заполняем .env-файл (скопируйте example.env и переименуйте в .env):**
   - DATABASE_URL - URL для подключения к базе данных. Можно не менять.
   
   **Следующие два пункта необходимы для формирования отчётов по фондам в google spreadsheets**

   - EMAIL - электронная почта пользователя, являющегося администратором в Google Cloud Platform
   - TYPE, PROJECT ID, PROJECT_KEY_ID, PRIVATE_KEY, CLIENT_EMAIL, CLIENT_ID, AUTH_URI, TOKEN_URI, AUTH_PROVIDER_X509_CERT_URL, CLIENT_X509_CERT_URL, UNIVERSE_DOMAIN скопируйте из JSON-файла, полученного в Google Cloud Platform.

7. **Запускаем сервер:**

   ```
   uvicorn app.main:app
   ```

8. **Примеры запросов доступны по адресам:**

   - `http://localhost:8000/docs` (Swagger)
   - `http://localhost:8000/docs` (ReDoc)

9. **Вы великолепны!** 🏆

<p align=center>
  <a href="url"><img src="https://github.com/xaer981/xaer981/blob/main/main_cat.gif" align="center" height="40" width="128"></a>
</p>
