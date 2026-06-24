"""BMI and heart rate calculator with user input."""


def calculate_bmi(weight_kg, height_m):
    """Return body mass index from weight in kg and height in meters."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    """Return BMI category: underweight, normal, overweight, or obese."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def estimate_max_heart_rate(age):
    """Estimate maximum heart rate using the formula 220 minus age."""
    return 220 - age


def calculate_target_heart_rate_zone(max_hr, low_pct=0.50, high_pct=0.85):
    """Return target heart rate zone as (low_bpm, high_bpm) at given percentages of max HR."""
    low_bpm = round(max_hr * low_pct)
    high_bpm = round(max_hr * high_pct)
    return low_bpm, high_bpm


def main():
    """Prompt the user for data and display BMI and heart rate results."""
    print("=== BMI & Heart Rate Calculator ===\n")

    weight_kg = float(input("Weight (kg): "))
    height_m = float(input("Height (m): "))
    age = int(input("Age (years): "))

    bmi = calculate_bmi(weight_kg, height_m)
    category = classify_bmi(bmi)
    max_hr = estimate_max_heart_rate(age)
    zone_low, zone_high = calculate_target_heart_rate_zone(max_hr)

    print("\n--- Results ---")
    print(f"BMI:              {bmi:.1f}")
    print(f"Category:         {category}")
    print(f"Max heart rate:   {max_hr} bpm")
    print(f"Target HR zone:   {zone_low}–{zone_high} bpm (50–85% of max)")


if __name__ == "__main__":
    main()
