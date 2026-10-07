import sqlite3


def analyze_skills(role_name, student_skills):

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # Get job role ID
    cursor.execute(
        "SELECT id FROM job_roles WHERE role_name = ?",
        (role_name,)
    )

    role = cursor.fetchone()

    if role is None:
        connection.close()
        return None

    role_id = role[0]

    # Get required skills
    cursor.execute("""
        SELECT skills.skill_name
        FROM skills
        JOIN required_skills
        ON skills.id = required_skills.skill_id
        WHERE required_skills.role_id = ?
    """, (role_id,))

    required_skills = [row[0] for row in cursor.fetchall()]

    # Convert to lowercase for comparison
    student_skills_lower = [
        skill.lower() for skill in student_skills
    ]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in student_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    # Calculate percentage
    total_skills = len(required_skills)

    if total_skills > 0:
        percentage = (len(matched_skills) / total_skills) * 100
    else:
        percentage = 0

    connection.close()

    return {
        "required": required_skills,
        "matched": matched_skills,
        "missing": missing_skills,
        "percentage": percentage
    }