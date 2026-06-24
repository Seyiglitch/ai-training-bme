import time

# --- Function to classify heart rate ---
def classify_heart_rate(hr):
    if hr < 60:
        return "Resting (Low)"
    elif 60 <= hr <= 100:
        return "Resting (Normal)"
    elif 101 <= hr <= 140:
        return "Active"
    else:
        return "High"

# --- 1. Get 5 heart rate values using range() ---
heart_rates = []

print("Enter 5 heart rate readings (bpm):")
for i in range(5):  # range() used here
    hr = int(input(f"Reading {i + 1}: "))
    heart_rates.append(hr)

# --- 2. Classify each using a for loop ---
print("\nHeart Rate Classifications:")
for hr in heart_rates:
    category = classify_heart_rate(hr)
    print(f"{hr} bpm -> {category}")

# --- 3. While loop countdown timer ---
print("\nStarting countdown before next check...")
count = 5

while count > 0:  # while loop used here
    print(f"{count}...")
    time.sleep(1)  # waits 1 second
    count -= 1

print("Done! Ready for next measurement.")