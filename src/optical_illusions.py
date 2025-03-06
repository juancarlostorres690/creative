from DrawingPanel import *

# Create the drawing panel
panel = DrawingPanel(1400, 900, "#E3E3E3")

# Set up the width and height of the rectangles
rect_w, rect_h = 350, 300

# Draw 12 rectangles in a 3x4 grid
for row in range(3):
    for col in range(4):
        panel.draw_rect(col * rect_w, row * rect_h, col * rect_w + rect_w,
                        row * rect_h + rect_h, outline="black")

# First horizontal line with outward arrows
panel.draw_line(75, 100, 275, 100, fill="black")
panel.draw_line(75, 100, 125, 75, fill="black")
panel.draw_line(75, 100, 125, 125, fill="black")
panel.draw_line(275, 100, 225, 75, fill="black")
panel.draw_line(275, 100, 225, 125, fill="black")

# Second horizontal line with inward arrows
panel.draw_line(75, 200, 275, 200, fill="black")
panel.draw_line(25, 175, 75, 200, fill="black")
panel.draw_line(25, 225, 75, 200, fill="black")
panel.draw_line(325, 175, 275, 200, fill="black")
panel.draw_line(325, 225, 275, 200, fill="black")

# Elements in the second rectangle from the left in the top row
panel.draw_line(500, 20, 600, 230, fill="black", width=3)
panel.draw_line(550, 100, 610, 210, fill="blue", width=3)
panel.draw_rect(525, 30, 30, 200, fill="gray", outline="gray")

# Grid inside the third rectangle (top row)
for row in range(6):
    for col in range(7):
        panel.draw_rect(710 + col * 50, 10 + row * 50, 30, 30,
                        fill="black", outline="black")

# Elements in the second rectangle from the left in the middle row
panel.draw_line(400, 600, 480, 300, fill="black", width=4)
panel.draw_line(650, 600, 570, 300, fill="black", width=4)

# Horizontal lines inside the second rectangle from the left in the middle row
start_y, line_length = 580, 270
for i in range(14):
    panel.draw_line(525 - line_length // 2, start_y,
                    525 + line_length // 2, start_y, fill="black", width=4)
    start_y -= 20
    line_length -= 10

# Two centered red lines
panel.draw_line(430, 570, 620, 570, fill="red", width=4)
panel.draw_line(430, 370, 620, 370, fill="red", width=4)

# Gray rectangles in the second column of the last rectangle (middle row)
for i in range(6):
    panel.draw_rect(1300, 325 + (i * 50), 50, 25,
                    fill="gray", outline="gray")

# Black & gray rectangles in the last rectangle from the left in the second row
for i in range(6):
    panel.draw_rect(1050, 300 + (i * 50), 350, 25,
                    fill="black", outline="black")
    panel.draw_rect(1150, 300 + (i * 50), 50, 25,
                    fill="gray", outline="gray")

# Gradient effect in the bottom-left rectangle
for i in range(0, 350, 2):
    hex_color = f"#{i//2:02x}{i//2:02x}{i//2:02x}"
    panel.draw_line(i, 600, i, 900, fill=hex_color, width=2)

# Overlaying rectangle in the gradient area
panel.draw_rect(50, 725, 250, 50, fill="#7d7d7d", outline="#7d7d7d")

# Radiating purple lines from the center of the bottom middle rectangle
for i in range(16):
    panel.draw_line(700, 600 + (i * 20), 875, 750,
                    fill="purple", width=1)
    panel.draw_line(1050, 600 + (i * 20), 875, 750,
                    fill="purple", width=1)

# Two red vertical lines inside the bottom middle rectangle
panel.draw_line(825, 600, 825, 900, fill="red", width=3)
panel.draw_line(925, 600, 925, 900, fill="red", width=3)
