class BMI:
    """Class to calculate and interpret Body Mass Index."""
    
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        # Formula: weight (kg) / [height (m)]^2
        if self.height <= 0:
            return 0
        return round(self.weight / (self.height ** 2), 2)

    def get_category(self):
        score = self.calculate_bmi()
        if score < 18.5:
            return "Underweight"
        elif score < 25:
            return "Normal weight"
        else:
            return "Overweight"