from BMICalculator import BMICalculator


def main():
    calculator = BMICalculator()

    print("=== BMI Calculator ===")
    choice = input("Use Metric (M) or US (U)? ").upper()

    if choice == "M":
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi = calculator.calculate_metric(weight, height)
        print("Your BMI is:", bmi)

    elif choice == "U":
        weight = float(input("Enter weight in pounds: "))
        feet = int(input("Enter height (feet): "))
        inches = int(input("Enter extra inches: "))
        bmi = calculator.calculate_us(weight, feet, inches)
        print("Your BMI is:", bmi)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

