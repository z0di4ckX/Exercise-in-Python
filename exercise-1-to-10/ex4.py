cars = 100
space_in_a_car = 4.0
drivers = 30
passenger = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passenger / cars_driven

print("There are ", cars, " cars availabe.")
print("There are only ", drivers, " drivers availabe.")
print("There will be ", cars_not_driven, " empty cars today.")
print("We can transport", carpool_capacity, " people today.")
print("We have", passenger, " to carpool today")
print("We need to put about", average_passenger_per_car, " in each car.")