class Circle:
    __pi = 3.141

    def __init__(self, radius_list):
        self.radius_list = radius_list

    @classmethod
    def calculate_area(cls, radius):
        return cls.__pi * radius**2

    @classmethod
    def calculate_perimeter(cls, radius):
        return 2 * cls.__pi * radius

if __name__ == "__main__":
    given_list = [10, 501, 22, 37, 100, 999, 87, 351]

    # Creating an instance of the Circle class with the given list
    circle_instance = Circle(given_list)

    # Accessing the radius list from the instance
    print("Radius list in the Circle instance:", circle_instance.radius_list)

    # Calculating area and perimeter for each radius
    for radius in circle_instance.radius_list:
        area = Circle.calculate_area(radius)
        perimeter = Circle.calculate_perimeter(radius)
        print(f"For radius {radius}: Area = {area}, Perimeter = {perimeter}")
