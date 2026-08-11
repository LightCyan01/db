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
        id SERIAL PRIMARY KEY,
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
        RETURNING id          
    """,(title, False))
    
    task_id = cursor.fetchone[0]
    
    conn.commit()
    conn.close()
    
    return {
        "id": task_id,
        "title": title,
        "done": False
    }
    
def update_task(id, title, done):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE tasks SET title = %s, done = %s WHERE id = %s",(title, done, id))
    
    if cursor.rowcount == 0:
        conn.close()
        return None
    
    conn.commit()
    conn.close()
    
    return get_task(id)
    
def delete_task(id):
    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    
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
            VALUES (%s, %s)                   
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
    
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    
    task = cursor.fetchone()
    
    conn.close()
    return task