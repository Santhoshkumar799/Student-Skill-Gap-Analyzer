import tkinter as tk
from tkinter import ttk, messagebox

from analyzer import analyze_skills


# -----------------------------
# MAIN WINDOW
# -----------------------------

window = tk.Tk()
window.title("Student Skill Gap Analyzer")
window.geometry("700x600")


# -----------------------------
# TITLE
# -----------------------------

title = tk.Label(
    window,
    text="STUDENT SKILL GAP ANALYZER",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)


# -----------------------------
# JOB ROLE
# -----------------------------

role_label = tk.Label(
    window,
    text="Select Job Role:",
    font=("Arial", 12)
)

role_label.pack()

role_box = ttk.Combobox(
    window,
    values=[
        "Python Developer",
        "Data Analyst",
        "Web Developer",
        "Software Developer"
    ],
    state="readonly",
    width=30
)

role_box.pack(pady=10)

role_box.current(0)


# -----------------------------
# SKILLS
# -----------------------------

skills_label = tk.Label(
    window,
    text="Select Your Skills:",
    font=("Arial", 12)
)

skills_label.pack(pady=10)


# Skill variables
python_var = tk.BooleanVar()
sql_var = tk.BooleanVar()
git_var = tk.BooleanVar()
flask_var = tk.BooleanVar()
rest_var = tk.BooleanVar()
linux_var = tk.BooleanVar()
html_var = tk.BooleanVar()
css_var = tk.BooleanVar()
javascript_var = tk.BooleanVar()
pandas_var = tk.BooleanVar()
numpy_var = tk.BooleanVar()
excel_var = tk.BooleanVar()
java_var = tk.BooleanVar()
cpp_var = tk.BooleanVar()


# -----------------------------
# CHECKBOXES
# -----------------------------

skills_frame = tk.Frame(window)
skills_frame.pack()


tk.Checkbutton(
    skills_frame,
    text="Python",
    variable=python_var
).grid(row=0, column=0, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="SQL",
    variable=sql_var
).grid(row=0, column=1, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="Git",
    variable=git_var
).grid(row=1, column=0, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="Flask",
    variable=flask_var
).grid(row=1, column=1, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="REST API",
    variable=rest_var
).grid(row=2, column=0, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="Linux",
    variable=linux_var
).grid(row=2, column=1, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="HTML",
    variable=html_var
).grid(row=3, column=0, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="CSS",
    variable=css_var
).grid(row=3, column=1, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="JavaScript",
    variable=javascript_var
).grid(row=4, column=0, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="Pandas",
    variable=pandas_var
).grid(row=4, column=1, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="NumPy",
    variable=numpy_var
).grid(row=5, column=0, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="Excel",
    variable=excel_var
).grid(row=5, column=1, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="Java",
    variable=java_var
).grid(row=6, column=0, sticky="w", padx=20)

tk.Checkbutton(
    skills_frame,
    text="C++",
    variable=cpp_var
).grid(row=6, column=1, sticky="w", padx=20)


# -----------------------------
# ANALYZE FUNCTION
# -----------------------------

def analyze():

    selected_skills = []

    if python_var.get():
        selected_skills.append("Python")

    if sql_var.get():
        selected_skills.append("SQL")

    if git_var.get():
        selected_skills.append("Git")

    if flask_var.get():
        selected_skills.append("Flask")

    if rest_var.get():
        selected_skills.append("REST API")

    if linux_var.get():
        selected_skills.append("Linux")

    if html_var.get():
        selected_skills.append("HTML")

    if css_var.get():
        selected_skills.append("CSS")

    if javascript_var.get():
        selected_skills.append("JavaScript")

    if pandas_var.get():
        selected_skills.append("Pandas")

    if numpy_var.get():
        selected_skills.append("NumPy")

    if excel_var.get():
        selected_skills.append("Excel")

    if java_var.get():
        selected_skills.append("Java")

    if cpp_var.get():
        selected_skills.append("C++")


    if not selected_skills:
        messagebox.showwarning(
            "No Skills",
            "Please select at least one skill."
        )
        return


    role = role_box.get()

    result = analyze_skills(
        role,
        selected_skills
    )


    # -----------------------------
    # DISPLAY RESULT
    # -----------------------------

    result_text.delete("1.0", tk.END)

    result_text.insert(
        tk.END,
        f"JOB ROLE: {role}\n\n"
    )

    result_text.insert(
        tk.END,
        f"SKILL MATCH: {result['percentage']:.2f}%\n\n"
    )

    result_text.insert(
        tk.END,
        "MATCHED SKILLS:\n"
    )

    for skill in result["matched"]:
        result_text.insert(
            tk.END,
            f"✓ {skill}\n"
        )

    result_text.insert(
        tk.END,
        "\nMISSING SKILLS:\n"
    )

    for skill in result["missing"]:
        result_text.insert(
            tk.END,
            f"✗ {skill}\n"
        )

    result_text.insert(
        tk.END,
        "\nRECOMMENDATION:\n"
    )

    if result["missing"]:

        result_text.insert(
            tk.END,
            "Focus on learning: "
            + ", ".join(result["missing"])
        )

    else:

        result_text.insert(
            tk.END,
            "Excellent! You have all the required skills."
        )


# -----------------------------
# ANALYZE BUTTON
# -----------------------------

analyze_button = tk.Button(
    window,
    text="ANALYZE SKILLS",
    command=analyze,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10
)

analyze_button.pack(pady=20)


# -----------------------------
# RESULT BOX
# -----------------------------

result_text = tk.Text(
    window,
    height=12,
    width=70,
    font=("Consolas", 11)
)

result_text.pack(pady=10)


# -----------------------------
# START APPLICATION
# -----------------------------

window.mainloop()