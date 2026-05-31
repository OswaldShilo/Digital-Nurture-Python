# Exercise 49: Temperature Converter
# Objective: Convert between Celsius, Fahrenheit, Kelvin with menu input

class TemperatureConverter:
    def c_to_f(self, c): return (c * 9/5) + 32
    def c_to_k(self, c): return c + 273.15
    def f_to_c(self, f): return (f - 32) * 5/9
    def f_to_k(self, f): return self.f_to_c(f) + 273.15
    def k_to_c(self, k): return k - 273.15
    def k_to_f(self, k): return self.c_to_f(self.k_to_c(k))

conv = TemperatureConverter()
menu = {
    "1": ("Celsius -> Fahrenheit",  "C", conv.c_to_f, "F"),
    "2": ("Celsius -> Kelvin",      "C", conv.c_to_k, "K"),
    "3": ("Fahrenheit -> Celsius",  "F", conv.f_to_c, "C"),
    "4": ("Fahrenheit -> Kelvin",   "F", conv.f_to_k, "K"),
    "5": ("Kelvin -> Celsius",      "K", conv.k_to_c, "C"),
    "6": ("Kelvin -> Fahrenheit",   "K", conv.k_to_f, "F"),
}

print("Temperature Converter")
for key, (label, *_) in menu.items():
    print(f"  {key}. {label}")

choice = input("Select option (1-6): ").strip()
if choice not in menu:
    print("Invalid option.")
else:
    label, unit, fn, out_unit = menu[choice]
    try:
        value  = float(input(f"Enter temperature ({unit}): "))
        result = fn(value)
        print(f"Result: {value:.2f} {unit} = {result:.2f} {out_unit}")
    except ValueError:
        print("Error: Enter a valid number.")
