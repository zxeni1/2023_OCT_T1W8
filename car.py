class Car:
    # Constructor
    def __init__(self, color, make):
        self._color = color
        self.make = make
        print("Hello")
        print(self)

    def get_color(self):
        # conditions fulfilled
        return self._color
    
    def set_color(self, color):
        # conditions fulfilled
        self._color = color
    
    def run(self):
        print(f"{self.make} is running!! Vrooooom Vrrrooommmm!!!!")


my_car = Car("black", "honda")

print(my_car.get_color())

my_car.set_color("red")

print(my_car.get_color())

# print(my_car.make)

# my_car.run()


# your_car = Car("white", "Toyota")
# print(your_car.make)

# your_car.run()


class PetrolCar(Car):
    def __init__(self, color, make, capacity_of_tank):
        super().__init__(color, make)
        self.capacity_of_tank = capacity_of_tank

    def make_turn(self):
        print("I am making a turn")


my_petrol_car = PetrolCar("silver", "BMW", 40)

print(my_petrol_car.make)

my_petrol_car.run()
print(my_petrol_car.capacity_of_tank)


class ElectricCar(Car):
    # Overriding
    def run(self):
        print("I run silently. No Vrroooming!!")

    # Overloading
    # def run(self, distance):
        # print(f"I ran for {distance} km")

my_electric_car = ElectricCar("yellow", "Tesla")

my_electric_car.run()
# my_electric_car.run(10)
