from controller import Controller
from car import Car

camera = 0
car = Car(motorPin = 15, servoPin = 0, camera=camera)
controller = Controller(car=car)

try:
    controller.listen_for_events()

except KeyboardInterrupt:
    print("EXITING PROGRAM")
    controller.quit()
    
