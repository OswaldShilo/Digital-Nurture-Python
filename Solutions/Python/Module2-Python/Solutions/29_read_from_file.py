# Exercise 29: Read from File
# Objective: Open and display file contents with error handling

def read_file(filename="greeting.txt"):
    try:
        with open(filename, "r") as f:
            content = f.read()
        print(f"Contents of '{filename}':")
        print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

read_file()
