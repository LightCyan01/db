import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def create_table():
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT,
        done BOOLEAN
    )               
    """)
    conn.commit()
    conn.close()

def create_task(title):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, done)
        VALUES (%s, %s)          
    """,(title, False))
    
    task_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return {
        "id": task_id,
        "title": title,
        "done": "False"
    }
    
def update_task(id, title, done):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?",(title, done, id))
    
    if cursor.rowcount == 0:
        conn.close()
        return None
    
    conn.commit()
    conn.close()
    
    return get_task(id)
    
def delete_task(id):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    
    if cursor.rowcount == 0:
        conn.close()
        return None
    
    conn.commit()
    conn.close()
    
    return True

def seed_tasks():
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]
    if count == 0:
        example = [
            ("Test 1", False),
            ("Test 2", True),
            ("Test 3", False)
        ]
        
        cursor.executemany("""
            INSERT INTO tasks (title, done)
            VALUES (?, ?)                   
        """, example)
    conn.commit()
    conn.close()

def get_tasks():
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    
    return tasks

def get_task(id):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    
    task = cursor.fetchone()
    
    conn.close()
    return task