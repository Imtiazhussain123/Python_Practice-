# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(self.name.title()," is now sitting")
#
#     def roll_over(self):
#         print(self.name.title()," rolled over ")
#
# my_dog = Dog('willie',"6")
# your_dog = Dog('lucy','3')
#
# my_dog.sit()
# print("my dog's name is ",my_dog.name.title())
# print("your dog's age is ",your_dog.age.title())
#
# my_dog.age
# ####################################################
# 9-1. Restaurant: Make a class called Restaurant . The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type .
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.
#
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print('Restaurant Name: ',self.restaurant_name,'\nCuisine Type: ',self.cuisine_type)
#     def open_restaurant(self):
#         print(self.restaurant_name,' is open for you!')
#
# restaurant = Restaurant("Mateen Foods","BBQ")
# print(restaurant.restaurant_name.title())
# print(restaurant.cuisine_type.upper())
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# ##############################################################################
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print('Restaurant Name: ',self.restaurant_name,'\nCuisine Type: ',self.cuisine_type,'\n')
#     def open_restaurant(self):
#         print(self.restaurant_name,' is open for you!')
#
# restaurant1 = Restaurant("mateen foods",'bbq')
# restaurant2 = Restaurant('pizza hut','pizza')
# restaurant3 = Restaurant('karachi haleem','haleem')
#
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# ###########################################################################
# 9-3. Users: Make a class called User . Create two attributes called first_name
# and last_name , and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
# class User():
#     def __init__(self,f_name,l_name,phone,address):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.phone = phone
#         self.address = address
#     def describe_user(self):
#         print('First Name: ',self.f_name.title(),'\nLast Name: ',self.l_name.title(),
#               '\nPhone: ',self.phone,'\nAddress: ',self.address)
#     def greet_user(self):
#         full_name = self.f_name+' '+self.l_name
#         print('\nHello! ',full_name,' welcome to our portal.\n' )
# user1 = User('imtiaz','hussain','03332873813','wsa 10/14')
# user2 = User('Ashmal','Rehman','0123456','gulshan')
# user3 = User('Danial','hussain','03332873813','wsa 10/14')
#
# user1.describe_user()
# user1.greet_user()
#
# user2.describe_user()
# user2.greet_user()
#
# user3.describe_user()
# user3.greet_user()

#################################################################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
# my_new_car = Car('mercedece','E190',1970)
# print(my_new_car.get_descriptive_name())

############################################################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
# my_new_car = Car('mercedece','E190',1970)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
################################################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
# my_new_car = Car('mercedece','E190',1970)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer = 30
# my_new_car.read_odometer()
#########################################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 20
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
# def update_milage(self,milage):
#         if milage >= self.odometer:
#             self.odometer = milage
#         else:
#             print("You cant roll back odometer reading")
#
#     def increment_odometer(self,miles):
#         self.odometer += miles
#
# my_used_car = Car('mercedece','E190',1970)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_milage(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
# ######################################################################
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any num-
# ber you like that could represent how many customers were served in, say, a
# day of business.
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#     def describe_restaurant(self):
#         print('Restaurant Name: ',self.restaurant_name,'\nCuisine Type: ',self.cuisine_type)
#
#     def open_restaurant(self):
#         print(self.restaurant_name,' is open for you!')
#
#     def set_number_served(self,served):
#         self.number_served =served
#
#     def increment_number_served(self,increment):
#         self.number_served += increment
#
# restaurant = Restaurant("Mateen Foods","BBQ")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.increment_number_served(23)
# restaurant.increment_number_served(22)
# print("Number of costumers served :"+str(restaurant.number_served))
# restaurant.increment_number_served(1000)
# print("Number of costumers served :"+str(restaurant.number_served))
# #############################################################################
# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts() . Print login_attempts again to
# make sure it was reset to 0.
# class User():
#     def __init__(self,f_name,l_name,phone,address):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.phone = phone
#         self.address = address
#         self.login_attempt = 0
#     def describe_user(self):
#         print('First Name: ',self.f_name.title(),'\nLast Name: ',self.l_name.title(),
#               '\nPhone: ',self.phone,'\nAddress: ',self.address)
#     def greet_user(self):
#         full_name = self.f_name+' '+self.l_name
#         print('\nHello! ',full_name,' welcome to our portal.\n' )
#
#     def increment_login_attempt(self,increment_login):
#         self.login_attempt +=increment_login
#     def reset_login_attempt(self):
#         self.login_attempt = 0
# user1 = User('imtiaz','hussain','03332873813','wsa 10/14')
#
#
# user1.describe_user()
# user1.greet_user()
# user1.increment_login_attempt(5)
# print("Number of attempts "+str(user1.login_attempt))
# user1.reset_login_attempt()
# print("Number of attempts "+str(user1.login_attempt))

################################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 20
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
#     def update_milage(self,milage):
#         if milage >= self.odometer:
#             self.odometer = milage
#         else:
#             print("You cant roll back odometer reading")
#
#     def increment_odometer(self,miles):
#         self.odometer += miles
#
# my_used_car = Car('mercedece','E190',1970)
# print(my_used_car.get_descriptive_name())
#
# class Electric_Car(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
# my_tesla = Electric_Car('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
#############################################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 20
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
#     def update_milage(self,milage):
#         if milage >= self.odometer:
#             self.odometer = milage
#         else:
#             print("You cant roll back odometer reading")
#
#     def increment_odometer(self,miles):
#         self.odometer += miles
#
# class Electric_Car(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         print("This car has "+str(self.battery_size)+" kwh battery")
# my_tesla = Electric_Car('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

########################################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 20
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
#     def update_milage(self,milage):
#         if milage >= self.odometer:
#             self.odometer = milage
#         else:
#             print("You cant roll back odometer reading")
#
#     def increment_odometer(self,miles):
#         self.odometer += miles
#
# class Electric_Car(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         print("This car has "+str(self.battery_size)+" kwh battery")
#     def fill_gas_tank(self):
#         print("This car doesnot fill gas")
# my_tesla = Electric_Car('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
############################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 20
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
#     def update_milage(self,milage):
#         if milage >= self.odometer:
#             self.odometer = milage
#         else:
#             print("You cant roll back odometer reading")
#
#     def increment_odometer(self,miles):
#         self.odometer += miles
# class Battery():
#     def __init__(self,battery_size = 70):
#         self.battery_size = battery_size
#     def describe_battery(self):
#         print("This car has " + str(self.battery_size) + " kwh battery")
#
#
# class Electric_Car(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#     def fill_gas_tank(self):
#         print("This car doesnot fill gas")
# my_tesla = Electric_Car('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
#############################################################
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 20
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
#     def update_milage(self,milage):
#         if milage >= self.odometer:
#             self.odometer = milage
#         else:
#             print("You cant roll back odometer reading")
#
#     def increment_odometer(self,miles):
#         self.odometer += miles
# class Battery():
#     def __init__(self,battery_size = 70):
#         self.battery_size = battery_size
#     def describe_battery(self):
#         print("This car has " + str(self.battery_size) + " kwh battery")
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size ==  85:
#             range = 270
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#
# class Electric_Car(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#     def fill_gas_tank(self):
#         print("This car doesnot fill gas")
# my_tesla = Electric_Car('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# ##############################################################
# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand , and call this method.
# class Restaurant():
#
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print('Restaurant Name: ',self.restaurant_name,'\nCuisine Type: ',self.cuisine_type)
#
#     def open_restaurant(self):
#         print(self.restaurant_name,' is open for you!')
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self,resturant_name,cuisine_type="Ice Cream"):
#         super().__init__(resturant_name,cuisine_type)
#         self.flavors = []
#
#     def display_flavors(self):
#         print('\nWe have the following flavors:\n')
#         for flavor in self.flavors:
#             print(flavor)
#
# restaurant = IceCreamStand("Ice Cream Stand")
# restaurant.flavors = ["crunch","vanila","mango","straberry"]
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.display_flavors()
# ###########################################################################
# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges , that stores a list
# of strings like "can add post" , "can delete post" , "can ban user" , and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin , and call your method.
# class User():
#     def __init__(self,f_name,l_name,phone,address):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.phone = phone
#         self.address = address
#         self.login_attempt = 0
#     def describe_user(self):
#         print('First Name: ',self.f_name.title(),'\nLast Name: ',self.l_name.title(),
#               '\nPhone: ',self.phone,'\nAddress: ',self.address)
#     def greet_user(self):
#         full_name = self.f_name+' '+self.l_name
#         print('\nHello! ',full_name,' welcome to our portal.\n' )
#
#     def increment_login_attempt(self,increment_login):
#         self.login_attempt +=increment_login
#     def reset_login_attempt(self):
#         self.login_attempt = 0
#
# class Admin(User):
#     def __init__(self,f_name,l_name,phone,address):
#         super().__init__(f_name,l_name,phone,address)
#         self.privilages = []
#     def show_privileges(self):
#         print("Have the following privillages:")
#         x= 0
#         for privilage in self.privilages:
#             x +=1;
#             print(x,'-',privilage)
#
# user1 = Admin('imtiaz','hussain','03332873813','wsa 10/14')
# user1.privilages = ["can add post","can delete post" , "can ban user" ]
# user1.describe_user()
# user1.greet_user()
# user1.show_privileges()

# ################################################
# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges , that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.
# class User():
#     def __init__(self,f_name,l_name,phone,address):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.phone = phone
#         self.address = address
#         self.login_attempt = 0
#     def describe_user(self):
#         print('First Name: ',self.f_name.title(),'\nLast Name: ',self.l_name.title(),
#               '\nPhone: ',self.phone,'\nAddress: ',self.address)
#     def greet_user(self):
#         full_name = self.f_name+' '+self.l_name
#         print('\nHello! ',full_name,' welcome to our portal.\n' )
#
#     def increment_login_attempt(self,increment_login):
#         self.login_attempt +=increment_login
#     def reset_login_attempt(self):
#         self.login_attempt = 0
#
# class Admin(User):
#     def __init__(self,f_name,l_name,phone,address):
#         super().__init__(f_name,l_name,phone,address)
#         self.privilages = Privileges()
#
# class Privileges():
#     def __init__(self):
#         self.privilages = []
#
#     def show_privileges(self):
#         print("Have the following privillages:")
#         x= 0
#         for privilage in self.privilages:
#             x +=1;
#             print(x,'-',privilage)
# my_privillages= Admin('Imtiaz','Hussain','12345667','wsa 10/14')
# my_privillages.describe_user()
#
# my_privillages.privilages.privilages =["can add post","can delete post" , "can ban user" ]
# my_privillages.privilages.show_privileges()

# ############################################################################
# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery() . This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 20
#     def get_descriptive_name(self):
#         long_name =str(self.year)+" "+self.model+" "+self.make
#         return long_name.title()
#
#     def read_odometer(self):
#         print("this car has "+str(self.odometer)+" mile on it")
#
#     def update_milage(self,milage):
#         if milage >= self.odometer:
#             self.odometer = milage
#         else:
#             print("You cant roll back odometer reading")
#
#     def increment_odometer(self,miles):
#         self.odometer += miles
# class Battery():
#
#     def __init__(self,battery_size = 70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has " + str(self.battery_size) + " kwh battery")
#
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size ==  85:
#             range = 270
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         if self.battery_size < 85:
#             self.battery_size = 85
#             print("Battery is set to 85 kwh")
#         else:
#             print('Battery is already Upgrated')
#
#
# class Electric_Car(Car):
#
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#
#     def fill_gas_tank(self):
#         print("This car doesnot fill gas")
# my_tesla = Electric_Car('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()


##########################################################################
# from Cars import Car
# my_new_car = Car("Tesla","model S","2016")
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer = 23
# my_new_car.read_odometer()
# #############################################
# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
# ule. Make a separate file that imports Restaurant . Make a Restaurant instance,
# and call one of Restaurant ’s methods to show that the import statement is work-
# ing properly.
# from restaurant import Restaurant
# new_resaurant = Restaurant("Karachi Haleem","haleem")
# new_resaurant.describe_restaurant()
# new_resaurant.open_restaurant()
# ###############################################################
# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
# Store the classes User , Privileges , and Admin in one module. Create a sepa-
# rate file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.
# from my_user import Admin
# admin = Admin('Imtiaz','Hussain','123234545',"wsa 10/14")
# admin.describe_user()
#
# admin.privilages.privilages =["can add post","can delete post" , "can ban user" ]
# admin.privilages.show_privileges()
# ##################################################################
# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.
# from privilages_admin import Admin,Privileges
# admin =Admin('Imtiaz','Hussain','123234545',"wsa 10/14")
# admin.describe_user()
# admin.privilages.privilages = ["can add post","can delete post" , "can ban user" ]
# admin.privilages.show_privileges()

#####################################################################
# with open('pi_digits.txt') as file_object:
#     content = file_object.read()
#     print(content)
#######################################################
# with open('pi_digits.txt') as file_object:
#     content = file_object.read()
#     print(content.rstrip())
# ###############################################################
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
############################################################
# filename = 'pi_digits.txt'
# with open (filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())
# #############################################################
#working with file File contents
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line
# print(pi_string)
# print(len(pi_string))
###########################################################
# filename = 'pi_digits.txt'
# with open (filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))
####################################################
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string +=line.rstrip()
# print(pi_string[:53],'.....')
# print(len(pi_string))
#################################################################
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string +=line.rstrip()
# print(pi_string[:53],'.....')
# print(len(pi_string))
# bd = input('Entrer your birthday in the form of mmddyyy:')
# if bd in pi_string:
#     print("your Birht day is appear in the million digits of pi")
# else:
#     print('your birthday is not present in pi digits')
# ##############################################################
# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can.... Save the file as learning_python.txt in the
# same directory as your exercises from this chapter. Write a program that reads
# the file and prints what you wrote three times. Print the contents once by read-
# ing in the entire file, once by looping over the file object, and once by storing
# # the lines in a list and then working with them outside the with block.
# filename = 'learning_python.txt'
# with open(filename) as file_object:
#     content = file_object.read()
# print(content.rstrip())
# print("\n")
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())
# print("\n")
# with open(filename) as file_object:
#     for lines in file_object:
#         print(lines.rstrip())
# ##############################################################
# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word. Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C. Print
# each modified line to the screen.
# filename = 'learning_python.txt'
# with open(filename) as f:
#     lines = f.readlines()
# for line in lines:
#     line = line.rstrip()
#     print(line.replace('Python','C'))
# #############################################################
# filename = 'programming.txt'
# with open(filename,'w') as f:
#     f.write('I love programming')
########################################################
# filename = 'programming.txt'
# with open(filename,'w') as f:
#     f.write('first line.')
#     f.write("second line")
# #########################################################
# filename = 'programming.txt'
# with open(filename,'a') as f:
#     f.write("\nhello i am writting my first line\n")
#     f.write('hello again i m writting second line ')
# #########################################################
# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
# user_input = input("What is your name: ")
# filename = 'guest.txt'
# with open(filename,'a') as f_object:
#     f_object.write(user_input)
# ###############################################################
# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.
# filename = 'quest_book.txt'
# while True:
#     print('For quite enter "q"')
#     user_input = input('Enter your name :')
#     if user_input != 'q':
#         with open(filename, 'a') as f:
#             f.write(user_input+"\n")
#     else:
#         break
# #######################################################################
# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.
# filename = 'responses.txt'
# x= 1
# while True:
#     print("write your name and response that why you like python")
#     name = input('Enter Name : ')
#     response = input("Enter a response: ")
#     if name == 'q' or response == 'q':
#         break
#     else:
#         with open(filename,'a')as f:
#             f.write(str(x)+"-"+name+"\t\t\t"+response+"\n")
#     x +=1
##############################################################
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you cant divit by zero")
########################################################
# print("Give me two numbers then i will divide them:")
# print("Enter q to quite: ")
# while True:
#     f_num = input("Enter first num:")
#     if f_num == 'q':
#         break
#     l_num = input("Enter last num:")
#     if l_num == 'q':
#         break
#     try:
#         answer = (int(f_num)/int(l_num))
#     except ZeroDivisionError:
#         print(str(f_num)+" cant be divided by zero ")
#     else:
#         print(answer)
# ##########################################################
# filename = 'alice.txt'
# try:
#     with open(filename) as f:
#         content = f.read()
# except FileNotFoundError:
#     msg = "sorry your file ("+filename+") not found in the list:"
#     print(msg)
########################################################
# filename = 'alice.txt'
# try:
#     with open(filename) as f:
#         content = f.read()
# except FileNotFoundError:
#     msg = "sorry your file ("+filename+") not found in the list:"
#     print(msg)
# else:
#     words = content.split()
#     len_wors = len(words)
#     print("you have a file("+filename+") with "+str(len_wors)+" words")
#################################################################
# def count_words(filename):
#     try:
#         with open(filename) as f:
#             content = f.read()
#     except FileNotFoundError:
#         msg = "sorry your file (" + filename + ") not found in the list:"
#         print(msg)
#     else:
#         words = content.split()
#         len_wors = len(words)
#         print("you have a file(" + filename + ") with " + str(len_wors) + " words")
# filenames = ['responses.txt','alice.txt','no_file.txt','ff.txt']
# for filename in filenames:
#     count_words(filename)
###############################################################
# def count_words(filename):
#     try:
#         with open(filename) as f:
#             content = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = content.split()
#         len_wors = len(words)
#         print("you have a file(" + filename + ") with " + str(len_wors) + " words")
# filenames = ['responses.txt','alice.txt','no_file.txt','ff.txt']
# for filename in filenames:
#     count_words(filename)
# ##############################################################
# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int , you’ll get a TypeError . Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.
# try:
#     num1 = input("Enter first number: ")
#     num1 = int(num1)
#     num2 = input("Enter second number:")
#     num2 = int(num2)
# except ValueError:
#     print("Please type a number not a alphabet")
# else:
#     answer = num1+num2;
#     print("Sum of "+str(num1)+" and "+ str(num2)+" is "+str(answer))
# #######################################################################
# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.
# while True:
#     try:
#         num1 = input("Enter first number: ")
#         if num1 == 'q':
#             break
#
#         num1 = int(num1)
#
#         num2 = input("Enter second number:")
#         if num2 == 'q':
#             break
#
#         num2 = int(num2)
#     except ValueError:
#         print("Please type a number not a alphabet")
#     else:
#         answer = num1+num2;
#         print("Sum of "+str(num1)+" and "+ str(num2)+" is "+str(answer))
# #######################################################################
# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a dif-
# ferent location on your system, and make sure the code in the except block
# executes properly.
