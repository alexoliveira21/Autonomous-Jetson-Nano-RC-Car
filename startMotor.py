from car import Car

car = Car()

while True:
    angle = int(input())
    car.change_steering(angle)
    car.change_throttle(angle)
