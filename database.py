import sqlite3

# Connect to database
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# -----------------------------
# CREATE TABLES
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS job_roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS required_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_id INTEGER,
    skill_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES job_roles(id),
    FOREIGN KEY (skill_id) REFERENCES skills(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id INTEGER,
    FOREIGN KEY (skill_id) REFERENCES skills(id)
)
""")

# -----------------------------
# INSERT JOB ROLES
# -----------------------------

roles = [
    ("Python Developer",),
    ("Data Analyst",),
    ("Web Developer",),
    ("Software Developer",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO job_roles (role_name) VALUES (?)",
    roles
)

# -----------------------------
# INSERT SKILLS
# -----------------------------

skills = [
    ("Python",),
    ("SQL",),
    ("Git",),
    ("Flask",),
    ("REST API",),
    ("Linux",),
    ("HTML",),
    ("CSS",),
    ("JavaScript",),
    ("Pandas",),
    ("NumPy",),
    ("Excel",),
    ("Java",),
    ("C++",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO skills (skill_name) VALUES (?)",
    skills
)

# -----------------------------
# SAVE DATABASE
# -----------------------------

connection.commit()

print("Job roles and skills added successfully!")

# Python Developer skills
python_skills = [
    "Python",
    "SQL",
    "Git",
    "Flask",
    "REST API",
    "Linux"
]

for skill in python_skills:
    cursor.execute("""
        INSERT INTO required_skills (role_id, skill_id)
        SELECT
            (SELECT id FROM job_roles WHERE role_name = 'Python Developer'),
            id
        FROM skills
        WHERE skill_name = ?
    """, (skill,))

# Data Analyst skills
data_skills = [
    "Python",
    "SQL",
    "Pandas",
    "NumPy",
    "Excel"
]

for skill in data_skills:
    cursor.execute("""
        INSERT INTO required_skills (role_id, skill_id)
        SELECT
            (SELECT id FROM job_roles WHERE role_name = 'Data Analyst'),
            id
        FROM skills
        WHERE skill_name = ?
    """, (skill,))

# Web Developer skills
web_skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "Python",
    "SQL"
]

for skill in web_skills:
    cursor.execute("""
        INSERT INTO required_skills (role_id, skill_id)
        SELECT
            (SELECT id FROM job_roles WHERE role_name = 'Web Developer'),
            id
        FROM skills
        WHERE skill_name = ?
    """, (skill,))

# Software Developer skills
software_skills = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Git",
    "Linux"
]

for skill in software_skills:
    cursor.execute("""
        INSERT INTO required_skills (role_id, skill_id)
        SELECT
            (SELECT id FROM job_roles WHERE role_name = 'Software Developer'),
            id
        FROM skills
        WHERE skill_name = ?
    """, (skill,))

connection.commit()

connection.close()