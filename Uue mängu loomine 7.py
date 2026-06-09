import pygame

pygame.init()

# 1. Get the display information object
screen_info = pygame.display.Info()

# 2. Extract the current width and height of the user's desktop
screen_width = screen_info.current_w
screen_height = screen_info.current_h

print(f"Detected screen resolution: {screen_width}x{screen_height}")

# 3. Create the fullscreen window using those exact dimensions
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)