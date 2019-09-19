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
                print("Button Pressed")
                if controller.get_button(6):
                    print(6)
                elif controller.get_button(7):
                    print(7)
            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
