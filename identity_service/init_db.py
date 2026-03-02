init_db.py:

import sqlite3
from werkzeug.security import generate_password_hash

c=sqlite3.connect("students.db")
cur=c.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
student_id TEXT PRIMARY KEY,
password_hash TEXT,
budget INTEGER)
""")

cur.execute("INSERT OR REPLACE INTO students VALUES (?,?,?)",
("240021127",generate_password_hash("rezwan"),500))

c.commit()
c.close()
print("DB READY")
