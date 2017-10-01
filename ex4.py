cars = 100
# define the number of cars

space_in_a_car = 4.0
# define number of passengers per car

drivers = 30
# define number of drivers

passengers = 90
# define number of actual passengers
cars_not_driven = cars - drivers
# number of cars which are not driven is the total number of cars minus
# the number of drivers available

cars_driven = drivers
# number of cars driven is the number of drivers

carpool_capacity = space_in_a_car * cars_driven
# carpool capacity equals to the number of cars available
# on the road multiplied by passengers per car

average_passenger_per_car = passengers / cars_driven
# total passengers divided by the number of cars
# on the road


print ("There are", cars, "cars available")
print ("There are only", drivers, "drivers available")
print ("We can transport", carpool_capacity,"people today")
print ("We have", passengers, "to carpool today")
print ("We need to put about", average_passenger_per_car, "in each car")

# popular variable names are i, x, j.
# single equal "=" assigns the value on the right to a variable on the left
# double equal "++" tests whether two things have the same value.
