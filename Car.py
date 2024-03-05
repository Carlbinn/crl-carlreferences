class Car:
    """An attempt to simulate a Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """An attempt to describe the car"""
        long_name = f'Your {self.make} Car has model {self.model} manufatured in year {self.year}.'
        return long_name.title()

    def read_odometer(self):
        """An attempt to read the car's odometer"""
        odo = f'Your {self.make} has {self.odometer_reading} miles'
        return odo.title()

    def update_odometer(self, mileage):
        """An attempt to update the odo reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't tamper the odometer!")

    def increment_odometer(self, miles):
        """An attempt to increment the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """An attempt to fill the gas tank of a manual car"""
        print(f"Filling in the tank with gas..")

my_car = Car("audi", "a4", "2019")
print(my_car.get_descriptive_name())
print(my_car.read_odometer())

my_car.update_odometer(44)
print(my_car.read_odometer())

my_car.update_odometer(24)
print(my_car.read_odometer())

my_car.increment_odometer(25)
print(my_car.read_odometer())

class Electric_car(Car):
    """An attempt to model an electric car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_power = 150

    def battery_charge(self):
        """An attempt to display battery capacity of an electric car"""
        print(f"Battery capacity is {self.battery_power}")

    def battery_range(self):
        """An attempt to check range in line with battery power"""
        if self.battery_power == 75:
            range = 250
            print(f"Your {self.battery_power} kwh battery can run up to {range} miles")
        elif self.battery_power == 150:
            range = 500
            print(f"Your {self.battery_power} kwh battery can run up to {range} miles")
        else:
            print(f"Sorry that battery power has not been defined.")

    def fill_gas_tank(self):
        """An attempt to check the gas of an electric car"""
        print(f"Electric car does not need gas!")

my_electric_car = Electric_car("tesla", "a4", "2020")
print(my_electric_car.get_descriptive_name())

my_electric_car.battery_charge()
my_car.fill_gas_tank()
my_electric_car.fill_gas_tank()
my_electric_car.battery_range()