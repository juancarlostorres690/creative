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
    x, y = radius, radius  # Start at the center
    steps = 0

    print(f"Radius = {radius}")

    # Commented out drawing logic
    # panel = DrawingPanel(size, size)
    # panel.set_color("black")
    # panel.draw_oval(0, 0, size - 1, size - 1)

    while math.sqrt((x - radius) ** 2 + (y - radius) ** 2) < radius:
        dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        x += dx
        y += dy
        steps += 1

        print(f"x={x}, y={y}, moves={steps}")

        # Commented out drawing logic
        # panel.set_color("black")
        # panel.fill_rect(x, y, 1, 1)
        # panel.sleep(5)

    print(f"I escaped in {steps} move(s)")

def main():
    print("Hello tiny world! Behold the tiny particle!")
    radius = get_radius()
    move_particle(radius)

if __name__ == "__main__":
    main()
