# 1. Add function
def add(a, b):
    return a + b

# 2. Subtract function
def subtract(a, b):
    return a - b

# 3. BMI calculation
def bmi_calculate(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

# 4. Max heart rate (common formula: 220 - age)
def heart_rate_max(age):
    return 220 - age

# 5. Greet function
def greet(name):
    return f"Hello, {name}! Welcome!"

# ---- Function calls ----
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))

bmi = bmi_calculate(70, 1.75)
print(f"BMI: {bmi:.2f}")

print("Max Heart Rate:", heart_rate_max(25))

print(greet("Seyi"))