class Circle:
    __pi = 3.141

    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_circumference(self):
        circumferences = [2 * Circle.__pi * radius for radius in self.radius_list]
        return circumferences

if __name__ == "__main__":
    given_list = [10, 501, 22, 37, 100, 999, 87, 351]

    # Creating an instance of the Circle class with the given list
    circle_instance = Circle(given_list)

    # Accessing the radius list from the instance
    print("Radius list in the Circle instance:", circle_instance.radius_list)

    # Calculating circumferences using the __pi variable
    circumferences = circle_instance.calculate_circumference()
    print("Circumferences calculated using Pi:", circumferences)
