import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    subject TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

students = [
    ("Rahul", "Math", 40),
    ("Sneha", "Math", 42),
    ("Amit", "Science", 66),
    ("Priya", "Science", 48),
    ("Kiran", "English", 81),
    ("Anjali", "English", 55)
]

cursor.executemany(
    "INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)",
    students
)

conn.commit()
conn.close()

print("Database created & sample data inserted successfully!")