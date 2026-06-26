#INPUT
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

# PROCESS
while True:
    user=  input("Write the user name: ")
    password = input("Write the password: ")
    if user in users and password == users[user]["password"]:
        print("Welcome", users[user]["name"])
        break
    else:
        print("User incorrect or password incorrect")
rol = users[user]["rol"]
if rol == "student":
    approved = set()
    print("ticket of", users[user]["name"])
    for subject in subjects:
        print(subject, notes[user][subject])
        if notes[user][subject] >= 7:
            approve.add(subject)

    pendientes = set(materias) - aprobadas
    print("Approved:", approved)
    print("Pendients:", pendients)


elif rol == "professor":
    print("Rol:", users[user]["rol"])
    print("students:")
    for users in notes:
        print("-", users[user]["name"])
        print()
    print("\nSubjects:")
    for subjects in subjects:
        print("-", subject)
    change = input("¿Do you want change calification of student? (yes/no)")
    while change == "yes":
        student = input("Student: ")
        Subject = input("Subject: ")
        if student in notes and subject in subjects:
            new = float(input("New note: "))
            safety = input("¿Are you sure(yes/no):  ")
            if seguridad == "yes":
                notes[student][subject] = new
                print("updated grades of", users[student]["name"])
                for student in subjects:
                    print(subject, notes[student][subject])
        else:
            print("student not found")
        cambio = input("¿Do you want change other note? (yes/no)")

elif rol == "coordinator":

    print("Professor: ")
    for users, data in users.items():
        if data["rol"] == "professor":
            print(datos["name"])
    print()
    print("\n" + "-" * 60)
    print(f"{'student':20}|{'Discrete Mathematics':12}|{'Programming':12}|{'English II':8}")
    print("-" * 60)
    
    for student, notes in calificaciones.items():
        print(
            f"{user[student]['name']:20}|"
            f"{notes['Discrete Mathematics']:12}|"
            f"{notes['Programming']:12}|"
            f"{notes['Englis II']:8}"
            )
        print("-" * 60)

        
