class RestaurantMeal:
    def __init__(self):
        self.food = ""
        self.price = 0

    def display(self):
        print("Food Item:", self.food)
        print("Price:", self.price)
        print("------------------")


meal1 = RestaurantMeal()
meal1.food = "Pizza"
meal1.price = 150


meal2 = RestaurantMeal()
meal2.food = "Burger"
meal2.price = 80


meal1.display()
meal2.display()