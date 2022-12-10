
# Write a small python script that shows an 800x600 box with a black background, and when a user clicks and drags it will draw a blue line. Use PyGame

# Here is a small Python script that uses PyGame to show an 800x600 box with a black background, and draws a blue line when the user clicks and drags:

# Copy code

import pygame

# Initialize PyGame
pygame.init()

# Set the window size
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the background color
bg_color = (0, 0, 0)

# Set the line color
line_color = (0, 0, 255)

# Set the starting point for the line
line_start = None

# Set the ending point for the line
line_end = None

# Main loop
while True:
    # Check for events
    for event in pygame.event.get():
        # Handle the QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Handle the MOUSEBUTTONDOWN event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Set the starting point for the line
            line_start = event.pos

        # Handle the MOUSEBUTTONUP event
        elif event.type == pygame.MOUSEBUTTONUP:
            # Set the ending point for the line
            line_end = event.pos

    # Fill the window with the background color
    window.fill(bg_color)

    # If the starting and ending points are set, draw the line
    if line_start and line_end:
        pygame.draw.line(window, line_color, line_start, line_end, 2)

    # Update the display
    pygame.display.update()

# This script creates a PyGame window with the specified size and background color, and listens for events such as mouse clicks and button presses. When the user clicks the mouse button and starts dragging, the script sets the starting and ending points for the line, and uses the PyGame function pygame.draw.line() to draw the line between these points. The script continues to run until the user closes the window or quits the program.