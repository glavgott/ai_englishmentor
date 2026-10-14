import sqlite3
def user_data():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT,
        content TEXT)
        """)
def save_messages(user_id,role,content):
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (user_id,role,content) VALUES (?,?,?)", (user_id,role,content))
def get_messages(user_id):
    history=[]
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT role,content FROM messages WHERE user_id=?",(user_id,))
        rows = cursor.fetchall()
        for row in rows:
            role, content = row
            history.append({"role":role,"content":content})
    return history
def update(id, new_prompt):
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE messages SET content = ? WHERE user_id = ? AND role =?", (new_prompt,id,"system"))
user_data()