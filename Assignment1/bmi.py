"""
BMI Calculator Program
Author: Shayan Sikandar
Description: Calculates Body Mass Index based on user input.
"""

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI using formula weight / height^2."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    """Return BMI category based on value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def main():
    """Main program execution."""
    print("=== BMI Calculator ===")

    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
