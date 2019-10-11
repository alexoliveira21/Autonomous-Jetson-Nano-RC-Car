import pygame
from car import Car
from camera import Camera
import threading

#Axis 0 = left stick: -1 (completely left) -> 1 (completely right)
#Axis 3 = left trigger: -1 (unpressed) -> 1 (completely pressed)
#Axis 4 = right trigger: -1 (unpressed) -> 1 (completely pressed)
right_trigger_axis = 4
left_trigger_axis = 3
left_stick_axis = 0

#Sets a very low max speed, good for training purposes
motor_angle_min = 80
motor_angle_max = 100


servo_angle_min = 20
servo_angle_max = 160


class Controller():

    def __init__(self, car, camera, joystick_number = 0):
        print("Initializing controller...")
        #initialize pygame to be able to listen for events
        pygame.init()

        #initialize controller
        self.controller = pygame.joystick.Joystick(joystick_number)
        self.controller.init()
        self.car = car
        self.camera = camera
        print("Controller ID: {}".format(self.controller.get_id()))

    #convert (-1,1) range to (0,180) range
    def convert_range(self, joystick_value, angle_max, angle_min):
        return (((joystick_value - (-1)) * (angle_max - angle_min)) / (1 - (-1))) + angle_min

    
    #listen for any buttons being pressed
    def listen_for_events(self):

        listening = True
        print("Ready for input...")
        try:

            #loop to catch all button presses
            while listening:

                events = pygame.event.get()

                for event in events:
                    
                    
                    if event.type == pygame.JOYBUTTONDOWN:

                        if self.controller.get_button(0):
                            self.camera.recording = True
                            self.camera.start()
                            print("Square Pressed")

                        elif self.controller.get_button(1):
                            self.camera.recording = False
                            print("X Pressed")

                        elif self.controller.get_button(2):
                            print("Triangle Pressed")

                        elif self.controller.get_button(3):
                            print("Circle Pressed")

                        elif self.controller.get_button(8): #PS4 Share Button
                            print("Now Recording")

                        elif self.controller.get_button(10): #PS4 Power Button

                            #stops listening for buttons being pressed
                            listening = False
                            print("Stopped Listening")

                    #if R2 trigger is pressed it will accelerate car in positive direction
                    if self.controller.get_axis(right_trigger_axis) >= 0:
                        self.car.change_throttle(self.convert_range(self.controller.get_axis(right_trigger_axis), motor_angle_max, motor_angle_min))

                    #if L2 trigger is pressed it will accelerate car in negative direction
                   # elif self.controller.get_axis(left_trigger_axis) >= 0:
                        #self.car.change_throttle(self.convert_range(self.controller.get_axis(left_trigger_axis)))

                    #change steering angle of vehicle based on left stick movement
                    self.car.change_steering(self.convert_range(self.controller.get_axis(left_stick_axis), servo_angle_max, servo_angle_min))

                 

    
        except KeyboardInterrupt:
            print("EXITING NOW")
            self.controller.quit()

    def start(self):
        controller_thread = threading.Thread(target = self.listen_for_events())
        controller_thread.start() 

