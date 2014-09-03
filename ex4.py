# Define variable cars and assign it a value 100
cars = 100
# define variabel space_in_a_car and assign it a value 4.0
space_in_a_car = 4.0
# define variable drivers and assign it a value 30
drivers = 30
# define variable passengers and assign it a value 90
passengers = 90
# define a variable cars_not_driven and calcualte value from subtracting
# drivers from cars
cars_not_driven = cars - drivers
# define variable cars_driven and assign it value of number of drivers
cars_driven = drivers
# define variabel carpool_capacity and calculate value from cars_driver and
# space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# define variable average_passengers_per_car and calculate value from
# apssengers and cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars available today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
