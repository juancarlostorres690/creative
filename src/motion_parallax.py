from DrawingPanel import *

def main():
    # Create the Drawing Panel
    panel = DrawingPanel(500, 400, "lightblue")

    # Store previous positions to track changes
    previous_x, previous_y = panel.get_mouse_x(), panel.get_mouse_y()
    previous_lake_x = 20 + (previous_x * 0.02)
    previous_butterfly_x = 300 + (previous_x * 0.05)
    previous_butterfly_y = 200 + (previous_y * 0.05)

    # Initial drawing of the background (lake)
    panel.fill_oval(previous_lake_x, 350, 200, 100, "blue")

    # Initial drawing of the butterfly
    panel.fill_oval(previous_butterfly_x, previous_butterfly_y, 20, 50, "orange")
    panel.fill_rect(previous_butterfly_x + 15, previous_butterfly_y + 5, 5, 40, "black")

    while True:
        # Get the current mouse position
        mouse_x = panel.get_mouse_x()
        mouse_y = panel.get_mouse_y()

        # Compute new positions
        lake_x = 20 + (mouse_x * 0.02)
        butterfly_x = 300 + (mouse_x * 0.05)
        butterfly_y = 200 + (mouse_y * 0.05)

        # Only update if the mouse position changes
        if (mouse_x, mouse_y) != (previous_x, previous_y):
            # Erase previous butterfly by drawing over it with background color
            panel.fill_oval(previous_butterfly_x, previous_butterfly_y, 20, 50, "lightblue")
            panel.fill_rect(previous_butterfly_x + 15, previous_butterfly_y + 5, 5, 40, "lightblue")

            # Erase previous lake only if it moved
            if lake_x != previous_lake_x:
                panel.fill_oval(previous_lake_x, 350, 200, 100, "lightblue")

            # Draw the updated lake
            panel.fill_oval(lake_x, 350, 200, 100, "blue")

            # Draw the updated butterfly
            panel.fill_oval(butterfly_x, butterfly_y, 20, 50, "orange")
            panel.fill_rect(butterfly_x + 15, butterfly_y + 5, 5, 40, "black")

            # Update previous positions
            previous_x, previous_y = mouse_x, mouse_y
            previous_lake_x = lake_x
            previous_butterfly_x = butterfly_x
            previous_butterfly_y = butterfly_y

        panel.sleep(2)

main()
