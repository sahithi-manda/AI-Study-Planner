import hashlib
import hmac
import os
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
def _hash_password(password, salt=None):
    """Return 'salt$hash' using PBKDF2-HMAC-SHA256 so plain passwords are never stored."""
    salt = salt or os.urandom(16).hex()
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 200_000).hex()
    return f"{salt}${digest}"


def create_user(username, password):

    cursor.execute("""
    INSERT INTO users (username, password)
    VALUES (?, ?)
    """, (username, _hash_password(password)))

    conn.commit()

# -----------------------------------
# Login User
# -----------------------------------
def login_user(username, password):

    cursor.execute("""
    SELECT * FROM users
    WHERE username=?
    """, (username,))

    data = cursor.fetchone()
    if data is None or "$" not in data[2]:
        return None

    salt = data[2].split("$", 1)[0]
    if hmac.compare_digest(data[2], _hash_password(password, salt)):
        return data
    return None

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