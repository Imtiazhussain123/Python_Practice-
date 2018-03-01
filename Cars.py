class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 20
    def get_descriptive_name(self):
        long_name =str(self.year)+" "+self.model+" "+self.make
        return long_name.title()

    def read_odometer(self):
        print("this car has "+str(self.odometer)+" mile on it")

    def update_milage(self,milage):
        if milage >= self.odometer:
            self.odometer = milage
        else:
            print("You cant roll back odometer reading")

    def increment_odometer(self,miles):
        self.odometer += miles
class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has " + str(self.battery_size) + " kwh battery")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==  85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class Electric_Car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("This car doesnot fill gas")
