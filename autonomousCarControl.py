from controller import Controller
from car import Car
from camera import Camera

image_file_path = "////////"
csv_file_path = "////////"
car = Car(motorPin = 15, servoPin = 0)
camera = Camera(car=car, image_file_path=image_file_path, csv_file_path=csv_file_path)
controller = Controller(car=car)

try:
    controller.listen_for_events()

except KeyboardInterrupt:
    print("EXITING PROGRAM")
    controller.quit()
