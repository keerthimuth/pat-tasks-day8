class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

if __name__ == "__main__":
    given_list = [10, 501, 22, 37, 100, 999, 87, 351]

    # Creating an instance of the Circle class with the given list
    circle_instance = Circle(given_list)

    # Accessing the radius list from the instance
    print("Radius list in the Circle instance:", circle_instance.radius_list)
