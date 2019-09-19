import pygame

#initializes pygame
pygame.init()

#creates a controller object
controller = pygame.joystick.Joystick(0)

#initializes the controller
controller.init()
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if controller.get_button(0):
                    print("Square Pressed")
                elif controller.get_button(1):
                    print("X Pressed")
                elif controller.get_button(2):
                    print("Circle Pressed")
                elif controller.get_button(3)
                    print("Triangle Pressed")
                elif controller.get_button(4):
                    print("L1 Pressed")
                elif controller.get_button(5):
                    print("R1 Pressed")
                elif controller.get_button(6):
                    print("L2 Pressed")
                elif controller.get_button(7):
                    print("R2 Pressed")
                elif controller.get_button(8):
                    print("SHARE Pressed")
                elif controller.get_button(9):
                    print("OPTIONS Pressed")
                elif controller.get_button(10):
                    print("Left Analog Pressed")
                elif controller.get_button(11):
                    print("Right Analog Pressed")
                elif controller.get_button(12):
                    print("Power Button Pressed")
                elif controller.get_button(13):
                    print("Touchpad Pressed")

            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
