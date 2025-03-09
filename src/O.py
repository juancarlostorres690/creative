from DrawingPanel import *

def draw_flower(panel, x, y, leaves):
    # """Draws a flower at (x, y) with the given number of leaves."""
    stem_height = 80
    panel.fill_rect(x + 10, y - stem_height, 10, stem_height, "green")  # Stem
    panel.fill_oval(x, y - stem_height - 20, 30, 30, "orange")  # Flower head

    # Draw leaves in pairs
    for i in range(leaves // 2):
        offset = i * 10
        panel.fill_oval(x - 15, y - stem_height + 20 + offset, 20, 10,
                        "light green")  # Left leaf
        panel.fill_oval(x + 25, y - stem_height + 20 + offset, 20, 10,
                        "light green")  # Right leaf

# User input
print("Welcome to the step tracker!")
steps = int(input("How many steps have you walked? "))

# Calculate the number of flowers
full_flowers = steps // 5000
remaining_steps = steps % 5000
extra_leaves = (remaining_steps // 1000) * 2 if remaining_steps > 0 else 0

# Panel setup
pan_w, pan_h = 500, 300
panel = DrawingPanel(pan_w, pan_h, "light blue")

# Ground
panel.fill_rect(0, 200, pan_w, 100, "dark green")

# Oval dimensions
oval_w, oval_h = 80, 40
spacing = 10
y_position = 15

# Calculate the x-coordinate for centering the middle ovals
middle_x = (pan_w - (2 * oval_w + spacing)) // 2

# Draw 4 gray ovals
for i in range(4):  # 4 ovals total
    x_position = middle_x + i * (oval_w + spacing)
    offset = 20 if i % 2 == 1 else 0  # Offset for the 2nd and 4th ovals
    panel.fill_oval(x_position, y_position + offset, oval_w, oval_h,
                    "light gray")

# Draw a yellow oval in the top-left corner
panel.fill_oval(10, 10, 70, 70, "yellow")

# Draw flowers
start_x = 50
flower_y_position = 200  # Flowers start from the bottom

# Draw full flowers (10 leaves each)
for i in range(full_flowers):
    draw_flower(panel, start_x + i * 100, flower_y_position, 10)

# Draw partial flower if there are remaining steps
if remaining_steps > 0:
    draw_flower(panel, start_x + full_flowers * 100,
                flower_y_position, extra_leaves)

print(f"You walked {steps} steps! You've earned {full_flowers}"
      f" full flowers and {1 if remaining_steps > 0 else 0} partial flower(s).")
