from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import random
import string

app = FastAPI()

# Подключение к базе данных
conn = sqlite3.connect('shorturl.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы, если её нет
cursor.execute('''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY,
    short_id TEXT UNIQUE,
    url TEXT
)
''')
conn.commit()

def generate_short_id():
    """Генерация уникального короткого идентификатора"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class URLItem(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(item: URLItem):
    """Создание короткой ссылки с записью в базу данных"""
    short_id = generate_short_id()
    try:
        cursor.execute("INSERT INTO urls (short_id, url) VALUES (?, ?)", (short_id, item.url))
        conn.commit()
        return {"short_url": f"http://localhost:8001/{short_id}"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=500, detail="URL уже существует")

@app.get("/{short_id}")
def redirect_url(short_id: str):
    """Перенаправление по короткому URL"""
    cursor.execute("SELECT url FROM urls WHERE short_id = ?", (short_id,))
    result = cursor.fetchone()
    if result:
        return {"full_url": result[0]}
    else:
        raise HTTPException(status_code=404, detail="URL не найден")