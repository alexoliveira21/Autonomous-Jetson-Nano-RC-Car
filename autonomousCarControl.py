from controller import Controller
from car import Car
from camera import Camera

image_file_path = '/Alex/Desktop/'
camera =
car = Car(camera=camera)
controller = Controller(car=car)

try:
    controller.listen_for_events()

except KeyboardInterrupt:
    print("EXITING PROGRAM")
    controller.quit()
