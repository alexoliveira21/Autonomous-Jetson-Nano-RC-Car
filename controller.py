import pygame

#Axis 0 = left stick: -1 (completely left) -> 1 (completely right)
#Axis 2 = left trigger: -1 (unpressed) -> 1 (completely pressed)
#Axis 5 = right trigger: -1 (unpressed) -> 1 (completely pressed)
right_trigger_axis = 5
left_trigger_axis = 2
left_stick_axis = 0

angle_min = 0
angle_max = 180
class Controller():

    def __init__(self, joystick_number = 0, car):
        #initialize pygame to be able to listen for events
        pygame.init()

        #initialize controller
        self.controller = pygame.joystick.Joystick(joystick_number)
        self.controller.init()
        self.car = car
        print("Controller ID: {}".format(self.controller.get_id()))

    #convert (-1,1) range to (0,180) range
    def convert_range(self, joystick_value):
        return (((joystick_value - (-1)) * (angle_max - angle_min)) / (1 - (-1))) + angle_min


    #listen for any buttons being pressed
    def listen_for_events(self):

        listening = True

        try:

            #loop to catch all button presses
            while listening:

                events = pygame.event.get()

                for event in events:

                    #if R2 trigger is pressed it will accelerate car in positive direction
                    if self.controller.get_axis(right_trigger_axis) >= 0:
                        self.car.change_throttle(convert_range(self.controller.get_axis(right_trigger_axis)))

                    #if L2 trigger is pressed it will accelerate car in negative direction
                    elif self.controller.get_axis(left_trigger_axis) >= 0:
                        self.car.change_throttle(convert_range(self.controller.get_axis(left_trigger_axis)))

                    #change steering angle of vehicle based on left stick movement
                    self.car.change_steering(convert_range(self.controller.get_axis(left_stick_axis)))


                    if event.type == pygame.JOYBUTTONDOWN:
                        if controller.get_button(0):
                            print("X Pressed")
                        elif controller.get_button(1):
                            print("Circle Pressed")
                        elif controller.get_button(2):
                            print("Triangle Pressed")
                        elif controller.get_button(3):
                            print("Square Pressed")
                        elif controller.get_button(8): #PS4 Share Button
                            #ADD CODE TO START RECORDING
                            print("Now Recording")
                        elif controller.get_button(10): #PS4 Power Button

                            #stops listening for buttons being pressed
                            listening = False
                            print("Stopped Listening")
