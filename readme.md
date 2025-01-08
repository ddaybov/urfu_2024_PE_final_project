# FastAPI Microservices Project

Этот проект включает два микросервиса, разработанных на **FastAPI** с использованием **SQLite** для хранения данных. Оба сервиса контейнеризированы с помощью **Docker** и настроены для автоматической сборки через **GitHub Actions** с публикацией образов в **Docker Hub**.

---

## 📌 Оглавление
- [1. Описание сервисов](#1-описание-сервисов)
- [2. Стек технологий](#2-стек-технологий)
- [3. Структура проекта](#3-структура-проекта)
- [4. Локальный запуск через Docker Compose](#4-локальный-запуск-через-docker-compose)
- [5. Эндпоинты API](#5-эндпоинты-api)
- [6. CI/CD и Docker Hub](#6-cicd-и-docker-hub)

---

## 1. Описание сервисов

### **TODO-сервис (`todo_app`)**
- Позволяет добавлять, получать, обновлять и удалять задачи (CRUD).  
- Подключен к SQLite для хранения данных.

### **ShortURL-сервис (`shorturl_app`)**
- Позволяет сокращать ссылки и перенаправлять по короткому URL.  
- Подключен к SQLite для хранения данных.

---

## 2. Стек технологий
- **Python 3.10**
- **FastAPI** — фреймворк для создания API
- **SQLite** — встроенная база данных
- **Docker & Docker Compose**
- **GitHub Actions** — для CI/CD
- **Docker Hub** — для хранения образов

---

## 3. Структура проекта
```plaintext
.
├── todo_app
│   ├── main.py              # Основной код сервиса TODO
│   ├── requirements.txt     # Зависимости
│   └── Dockerfile           # Dockerfile для todo_app
│
├── shorturl_app
│   ├── main.py              # Основной код сервиса ShortURL
│   ├── requirements.txt     # Зависимости
│   └── Dockerfile           # Dockerfile для shorturl_app
│
├── .github
│   └── workflows
│       └── docker-publish.yml  # CI/CD через GitHub Actions
│
├── docker-compose.yml       # Объединение сервисов в один стек
└── README.md
```

---

## 4. Локальный запуск через Docker Compose

### **Запуск всех сервисов:**
```bash
# Запуск и пересборка всех сервисов
docker-compose up -d --build
```

### **Остановка всех сервисов:**
```bash
docker-compose down
```

### **Проверка запущенных контейнеров:**
```bash
docker ps
```

---

## 5. Эндпоинты API

### **TODO-сервис (`localhost:8000`):**
- `GET /docs` — Документация Swagger.  
- `POST /items` — Добавить задачу.  
- `GET /items` — Получить список задач.  
- `PUT /items/{id}` — Обновить задачу.  
- `DELETE /items/{id}` — Удалить задачу.  

### **ShortURL-сервис (`localhost:8001`):**
- `GET /docs` — Документация Swagger.  
- `POST /shorten` — Создать короткую ссылку.  
- `GET /{short_id}` — Перенаправление по короткому URL.  

---

## 6. CI/CD и Docker Hub

### **GitHub Actions:**
- При каждом `push` в `main` происходит автоматическая сборка и публикация образов в **Docker Hub**.

### **Docker Hub репозитории:**
- [daydima/todo_app](https://hub.docker.com/r/daydima/todo_app)  
- [daydima/shorturl_app](https://hub.docker.com/r/daydima/shorturl_app)

---

## **Авторы:**
- Проект разработан в рамках курса по программной инженерии.  
- Автор: [ddaybov](https://github.com/ddaybov)
