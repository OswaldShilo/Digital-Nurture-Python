def display_coordinates(coords):
    if not isinstance(coords, (list, tuple)) or len(coords) != 2:
        raise ValueError("Provide exactly (x, y) coordinates")
    x, y = coords
    print(f"Coordinates -> X: {x}, Y: {y}")

point = (10.5, 20.3)
display_coordinates(point)
