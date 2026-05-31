# Exercise 27: Len Function
# Objective: Get the length of a string using len()

def string_length(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    length = len(text)
    print(f"String : '{text}'")
    print(f"Length : {length}")
    return length

string_length("Hello, World!")
