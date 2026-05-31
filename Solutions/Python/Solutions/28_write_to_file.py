# Exercise 28: Write to File
# Objective: Save a greeting message into a text file

def write_greeting(filename="greeting.txt"):
    with open(filename, "w") as f:
        f.write("Hello World")
    print(f"File '{filename}' written successfully.")

write_greeting()
