from DrawingPanel import *


def draw_flower(panel, x, y, leaves):
    """Draws a flower at (x, y) with the given number of leaves."""

    # Calculate stem height (base height is 20px, grows 20px per 2 leaves)
    stem_height = 20 + (leaves // 2) * 20

    # Draw stem (line with stroke width 5)
    panel.draw_line(x, y - stem_height, x, y, color="green", width=5)

    # Draw leaves (lines at intervals of 10px)
    for i in range(leaves):
        leaf_y = y - stem_height + 10 + (i * 10)  # Leaves positioned every 10px
        if i % 2 == 0:
            # Left leaf (diagonal up-left)
            panel.draw_line(x, leaf_y, x - 10, leaf_y - 10, color="light green",
                            width=5)
        else:
            # Right leaf (diagonal up-right)
            panel.draw_line(x, leaf_y, x + 10, leaf_y - 10, color="light green",
                            width=5)

    # Draw flower petal (50x50 oval centered above the stem)
    panel.fill_oval(x - 25, y - stem_height - 50, 50, 50, "orange")

    # Draw eye of the flower (10x10 circle centered in the petal)
    panel.fill_oval(x - 5, y - stem_height - 25, 10, 10, "black")


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
    draw_flower(panel, start_x + full_flowers * 100, flower_y_position,
                extra_leaves)

print(
    f"You walked {steps} steps! You've earned {full_flowers} full flowers and "
    f"{1 if remaining_steps > 0 else 0} partial flower(s).")
