# 🌟 Учебный проект по миграциям базы данных с использованием Alembic и FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-brightgreen)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/downloads/release/python-380/)
[![License](https://img.shields.io/badge/License-MIT-yellowgreen)](LICENSE)

## 🎯 Особенности

- **Alembic Миграции**: Управление версиями схемы базы данных и миграции.
- **FastAPI**: Использование быстрого и современного фреймворка Python для создания API.
- **SQLite**: Легковесная база данных, идеально подходящая для учебных проектов.

## 🚀 Как начать

### Требования

- Python 3.8+
- Менеджер пакетов `pip`

### Установка

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/artyoma2000/fastapi-alembic-migrations.git
   cd fastapi-alembic-migrations
   ```

2. **Создание и активация виртуального окружения**:
   ```bash
   python -m venv env
   source env/bin/activate  # Для Windows используйте `env\Scripts\activate`
   ```

3. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

### Запуск проекта

1. **Запуск сервера FastAPI**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Доступ к документации API**:
   - Откройте [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) для Swagger UI.
   - Или [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) для ReDoc.

## 🛠️ Использование

### Создание миграции

1. **Генерация файла миграции**:
   ```bash
   alembic revision --autogenerate -m "Added product table"
   ```

2. **Применение миграции**:
   ```bash
   alembic upgrade head
   ```

### Работа с API

1. **Добавление нового продукта**:
   ```http
   POST /products/
   Content-Type: application/json

   {
     "title": "Новый продукт",
     "price": 100,
     "count": 10
   }
   ```

2. **Получение информации о продукте**:
   ```http
   GET /products/{product_id}
   ```

## 📄 API Эндпоинты

- **`POST /products/`**: Создает новый продукт в базе данных.
- **`GET /products/{product_id}`**: Возвращает информацию о продукте по его ID.

## 🧩 Расширение проекта

- **Добавление новых полей**: Используйте Alembic для добавления новых полей в модели.
- **Интеграция с другими базами данных**: Настройте подключение к PostgreSQL, MySQL и другим СУБД.
- **Расширение функционала API**: Добавьте новые эндпоинты для обновления и удаления продуктов.

## 🤝 Участие

Ваш вклад в проект приветствуется! Если у вас есть идеи по улучшению, пожалуйста, создавайте issue или pull request.


- [Документация FastAPI](https://fastapi.tiangolo.com) [Документация Alembic](https://alembic.sqlalchemy.org/en/latest)