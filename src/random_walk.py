from DrawingPanel import DrawingPanel
import random
import math
import time

def get_radius():
    while True:
        try:
            radius = int(
                input("Enter the radius (in pixels) of the walk area: "))
            if radius > 0:
                return radius
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")

def move_particle(radius):
    size = 2 * radius + 1
    panel = DrawingPanel(size, size)

    x, y = radius, radius  # Start at the center
    steps = 0

    # Draw boundary circle
    panel.set_color("black")
    panel.draw_oval(0, 0, size - 1, size - 1)

    while math.sqrt((x - radius) ** 2 + (y - radius) ** 2) < radius:
        dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        x += dx
        y += dy
        steps += 1

        # Color the pixel at the walker's current location
        panel.set_color("black")
        panel.fill_rect(x, y, 1, 1)

        # Animate by adding a delay
        panel.sleep(5)

    print(f"Walk ended after {steps} moves.")

def main():
    print("Hello tiny world! Behold the tiny particle")
    radius = get_radius()
    move_particle(radius)

if __name__ == "__main__":
    main()
