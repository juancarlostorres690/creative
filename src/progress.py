from DrawingPanel import *

# Panel dimensions
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
    panel.fill_oval(x_position, y_position + offset, oval_w, oval_h, "light gray")

# Draw a yellow oval in the top-left corner
panel.fill_oval(10, 10, 70, 70, "yellow")
