# Exercise 35: Create Tuple
# Objective: Store fixed coordinates in a tuple and display them

def display_coordinates(coords):
    if not isinstance(coords, tuple) or len(coords) != 2:
        raise ValueError("Coordinates must be a tuple of (x, y)")
    x, y = coords
    print(f"Coordinates -> X: {x}, Y: {y}")

location = (28.6139, 77.2090)
display_coordinates(location)
