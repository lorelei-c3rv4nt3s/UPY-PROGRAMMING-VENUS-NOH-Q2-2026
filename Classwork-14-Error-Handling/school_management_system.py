
users = {
    'cclarisa': {'password': '1234', 'rol': 'student', 'name': 'Clarisa Calderon'},
    'fyamil': {'password': '1234', 'rol': 'student', 'name': 'Yamil Farah'},
    'aluka': {'password': '1234', 'rol': 'student', 'name': 'Luka Aranda'},
    'yroberto': {'password': '1234', 'rol': 'student', 'name': 'Roberto Yerbes'},
    'vmelany': {'password': '1234', 'rol': 'student', 'name': 'Melany Vilchis'},
    'nvenus': {'password': '1234', 'rol': 'student', 'name': 'Venus Noh'},
    'jpedrozo': {'password': '1234', 'rol': 'professor', 'name': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = (
    "Discrete Mathematics", "Programming", "English II", "Differential Calculus",
    "Probability and Statistics", "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'cclarisa': {'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0, 'Differential Calculus': 7.8, 'Probability and Statistics': 8.3, 'Computer and Server Architecture': 6.8, 'Socio-Emotional Skills and Conflict Management': 9.5},
    'fyamil': {'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4, 'Differential Calculus': 6.2, 'Probability and Statistics': 9.1, 'Computer and Server Architecture': 6.5, 'Socio-Emotional Skills and Conflict Management': 9.8},
    'aluka': {'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5, 'Differential Calculus': 7.0, 'Probability and Statistics': 7.8, 'Computer and Server Architecture': 6.2, 'Socio-Emotional Skills and Conflict Management': 8.9},
    'yroberto': {'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2, 'Differential Calculus': 9.0, 'Probability and Statistics': 9.6, 'Computer and Server Architecture': 9.4, 'Socio-Emotional Skills and Conflict Management': 10.0},
    'vmelany': {'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8, 'Differential Calculus': 6.0, 'Probability and Statistics': 6.4, 'Computer and Server Architecture': 8.1, 'Socio-Emotional Skills and Conflict Management': 9.0},
    'nvenus': {'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5, 'Differential Calculus': 6.6, 'Probability and Statistics': 8.9, 'Computer and Server Architecture': 8.7, 'Socio-Emotional Skills and Conflict Management': 9.2}
}

current_user = None
while True:
    username_input = input("Write the user name: ")
    password_input = input("Write the password: ")
    
    if username_input in users and password_input == users[username_input]["password"]:
        print(f"\nWelcome {users[username_input]['name']}")
        current_user = username_input
        break
    else:
        print("User incorrect or password incorrect\n")

rol = users[current_user]["rol"]

if rol == "student":
    approved = set()
    print(f"\nTicket of {users[current_user]['name']}:")
    print("-" * 40)
    
    for subject in subjects:
        grade = notes[current_user][subject]
        print(f"{subject}: {grade}")
        if grade >= 7:
            approved.add(subject)

    pendients = set(subjects) - approved
    print("-" * 40)
    print("Approved:", approved if approved else "None")
    print("Pendients:", pendients if pendients else "None")

elif rol == "professor":
    print(f"\nRol: {users[current_user]['rol']}")
    print("\nStudents:")
    for student_key in notes.keys():
        print(f"- {users[student_key]['name']}")
        
    print("\nSubjects:")
    for subject in subjects:
        print(f"- {subject}")
        
    change = input("\nDo you want to change a student's grade? (yes/no): ").strip().lower()
    while change == "yes":
        student_target = input("Student (username): ").strip()
        subject_target = input("Subject: ").strip()
        
        if student_target in notes and subject_target in subjects:
            try:
                new_note = float(input("New note: "))
                safety = input("Are you sure? (yes/no): ").strip().lower()
                
                if safety == "yes":
                    notes[student_target][subject_target] = new_note
                    print(f"Updated grades of {users[student_target]['name']}:\n")
                    
                    
                    for sub in subjects:
                        print(f"{sub}: {notes[student_target][sub]}")
            except ValueError:
                print("Error: La calificación debe ser un número válido.")
        else:
            print("Student or subject not found.")
            
        change = input("\nDo you want to change another note? (yes/no): ").strip().lower()

elif rol == "coordinator":
    print("\nProfessors:")
    for u_key, u_data in users.items():
        if u_data["rol"] == "professor":
            print(f"- {u_data['name']}")
            
    print("\n" + "-" * 60)
    print(f"{'Student':20}|{'Discrete Math':13}|{'Programming':12}|{'English II':10}")
    print("-" * 60)
    
    for student_key, student_notes in notes.items():
        print(
            f"{users[student_key]['name']:20}|"
            f"{student_notes['Discrete Mathematics']:13}|"
            f"{student_notes['Programming']:12}|"
            f"{student_notes['English II']:10}"
        )
    print("-" * 60)
        
