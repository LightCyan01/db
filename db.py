import sqlite3

DB = "tasks.db"

def create_table():
    conn = sqlite3.connect(DB)
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
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, done)
        VALUES (?, ?)          
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
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?",(title, done, id))
    
    if cursor.rowcount == 0:
        conn.close()
        return None
    
    conn.commit()
    conn.close()
    
    return get_task(id)
    
def delete_task(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    
    if cursor.rowcount == 0:
        conn.close()
        return None
    
    conn.commit()
    conn.close()
    
    return True

def seed_tasks():
    conn = sqlite3.connect(DB)
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
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    
    return tasks

def get_task(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    
    task = cursor.fetchone()
    
    conn.close()
    return task