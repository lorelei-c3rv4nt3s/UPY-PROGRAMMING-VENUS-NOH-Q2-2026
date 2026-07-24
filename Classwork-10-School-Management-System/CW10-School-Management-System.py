# Required Structures
users = {
    'jperez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo': {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez': {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc': {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam': {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa': {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# PROCESS 
while True:
    user = input("User: ")
    password = input("Password: ")
    if user in users and password == users[user]["password"]:
        print("Bienvenido,", users[user]["name"])
        break
    else:
        print("User or password invalid")

rol = users[user]["rol"]

if rol == "student":
    passed = set()
    print(f"\nGrades of {users[user]['name']}")
    for subject in subjects:
        print(f"{subject}: {notes[user][subject]}")
        if notes[user][subject] >= 8.0:
            passed.add(subject)
            
    not_passed = set(subjects) - passed
    print("\nPassed:", passed)
    print("Not passed:", not_passed)

elif rol == "professor":
    print("\nRol:", users[user]["rol"])
    print("Students:")
    for estudiante in notes:
        print(f"- {users[estudiante]['name']} ({estudiante})")
    
    print("\nSubjects:")
    for subject in subjects:
        print(f"- {subject}")
        
    change = input("\nDo you want to change a student grade? (yes/no): ")
    while change.lower() == "yes":
        student = input("Student username: ")
        subject = input("Subject name: ")
        
        if student in notes and subject in subjects:
            new = float(input("New grade: "))
            confirmation = input("Sure? (yes/no): ")
            if confirmation.lower() == "yes":
                notes[student][subject] = new
                print("Grade updated successfully.\n")
                print(f"New grades for {users[student]['name']}:")
                for subj in subjects:
                    print(f"{subj}: {notes[student][subj]}")
        else:
            print("Student or Subject invalid")
            
        change = input("\nDo you want to change another grade? (yes/no): ")

elif rol == "coordinator":
    print("\n--- COORDINATOR REPORT ---")
    print("Teachers:")
    for usuario, datos in users.items():
        if datos["rol"] == "professor":
            print(f"- {datos['name']}")
            
    print("\nSubjects:")
    for subject in subjects:
        print(f"- {subject}")
        
    print("\nStudents Grades:")
    for student, student_notes in notes.items():
        print(f"\nStudent: {users[student]['name']}")
        for subject in subjects:
            print(f"  {subject:45} | {student_notes[subject]}")