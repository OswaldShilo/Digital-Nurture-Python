# Exercise 15: Nested If
# Objective: Validate username and password using nested if

def authenticate(username, password):
    if not username or not password:
        print("Error: Username and password cannot be blank.")
        return
    if username == "admin":
        if password == "pass123":
            print("Access granted. Welcome, admin!")
        else:
            print("Access denied. Incorrect password.")
    else:
        print("Access denied. Unknown username.")

user = "admin"
pwd  = "pass123"
authenticate(user, pwd)
