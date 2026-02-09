from BMICalculator import BMICalculator

def main():
    calc = BMICalculator()
    print("--- BMI Calculator ---")
    mode = input("Use (M)etric or (U)S units? ").strip().upper()

    if mode == 'M':
        kg = float(input("Weight (kg): "))
        m = float(input("Height (m): "))
        print(f"Your BMI is: {calc.calculate_metric(kg, m)}")
    elif mode == 'U':
        lbs = float(input("Weight (lbs): "))
        ft = int(input("Height (ft): "))
        inches = int(input("Height (in): "))
        print(f"Your BMI is: {calc.calculate_us(lbs, ft, inches)}")

if __name__ == "__main__":
    main()
