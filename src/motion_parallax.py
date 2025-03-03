from DrawingPanel import *


def main():
    # Create the Drawing Panel
    panel = DrawingPanel(500, 400, "lightblue")
    previous_x, previous_y = panel.get_mouse_x(), panel.get_mouse_y()

    
    while True:
        # Get the current mouse position
        mouse_x = panel.get_mouse_x()
        mouse_y = panel.get_mouse_y()
        # Clear the panel
        # panel.clear()
        # Draw the lake (moves slower due to being further away
        if (mouse_x, mouse_y) != (previous_x, previous_y):
            lake_x = 20 + (mouse_x * 0.02)
            panel.fill_rect(lake_x, 350, 200, 100, "blue")
            # Draw the butterfly (closer, so it moves faster)
            butterfly_x = 300 + (mouse_x * 0.05)
            butterfly_y = 200 + (mouse_y * 0.05)
            panel.fill_oval(butterfly_x, butterfly_y, 20, 50, "orange")
            panel.fill_rect(butterfly_x + 15, butterfly_y + 5, 5, 40, "black")
            # Pause for smooth animation
            previous_x, previous_y = mouse_x, mouse_y
        panel.sleep(50)
main()
