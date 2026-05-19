import sqlite3

# -----------------------------------
# Database Connection
# -----------------------------------
conn = sqlite3.connect(
    "study_planner.db",
    check_same_thread=False
)

cursor = conn.cursor()

# -----------------------------------
# Users Table
# -----------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# -----------------------------------
# Progress Table
# -----------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day INTEGER,
    subject TEXT,
    task TEXT,
    completed INTEGER
)
""")

conn.commit()

# -----------------------------------
# Create User
# -----------------------------------
def create_user(username, password):

    cursor.execute("""
    INSERT INTO users (username, password)
    VALUES (?, ?)
    """, (username, password))

    conn.commit()

# -----------------------------------
# Login User
# -----------------------------------
def login_user(username, password):

    cursor.execute("""
    SELECT * FROM users
    WHERE username=? AND password=?
    """, (username, password))

    data = cursor.fetchone()

    return data

# -----------------------------------
# Save Task Progress
# -----------------------------------
def save_task(day, subject, task, completed):

    cursor.execute("""
    INSERT INTO progress (
        day,
        subject,
        task,
        completed
    )
    VALUES (?, ?, ?, ?)
    """, (
        day,
        subject,
        task,
        completed
    ))

    conn.commit()

# -----------------------------------
# Get Completed Tasks Count
# -----------------------------------
def get_completed_tasks():

    cursor.execute("""
    SELECT COUNT(*)
    FROM progress
    WHERE completed = 1
    """)

    result = cursor.fetchone()

    return result[0]

# -----------------------------------
# Weak Area Analysis
# -----------------------------------
def get_subject_analysis():

    cursor.execute("""
    SELECT subject, COUNT(*) as total
    FROM progress
    GROUP BY subject
    """)

    results = cursor.fetchall()

    return results