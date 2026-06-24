# --- 1. FIXED SYNTAX ERROR ---
def greet(name):  # added colon
    print("Hello " + name)

# --- 2. FIXED NAME ERROR ---
def calculate_total():
    price = 10
    quantity = 3
    return price * quantity  # now both variables are defined

# --- 3. FIXED TYPE ERROR ---
def add_numbers():
    num1 = "10"
    num2 = 5
    return int(num1) + num2  # convert string to int

# --- Function Calls ---
greet("Seyi")
print("Total:", calculate_total())
print("Sum:", add_numbers())