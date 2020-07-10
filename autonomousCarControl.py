from controller import Controller
from car import Car
from camera import Camera

image_file_path = "/media/alex/ALEX/images/"
csv_file_path = "/media/alex/ALEX/csv_files/"
car = Car(motorPin = 15, servoPin = 0, default_motor_angle = 96)
camera = Camera(car=car, image_file_path=image_file_path, csv_file_path=csv_file_path)
controller = Controller(car=car, camera = camera)

try:
    controller.start()

except KeyboardInterrupt:
    print("EXITING PROGRAM")
    controller.quit()
