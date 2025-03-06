from DrawingPanel import *

# Create the drawing panel
panel = DrawingPanel(1400, 900, "#E3E3E3")

# Set up the width and height of the rectangles
rect_w = 350
rect_h = 300

# Loop through 3 rows and 4 columns to draw 12 rectangles
for row in range(3):
    for col in range(4):
        # Calculate the position of the rectangle
        x = col * rect_w
        y = row * rect_h
        # Draw the rectangle with black borders
        panel.draw_rect(x, y, x + rect_w, y + rect_h, outline="black")

# First horizontal line with outward arrows
panel.draw_line(75, 100, 275, 100, fill="black")

# Left arrowhead (pointing outward)
panel.draw_line(75, 100, 125, 75, fill="black")   # Upper diag
panel.draw_line(75, 100, 125, 125, fill="black")  # Lower diag

# Right arrowhead (pointing outward)
panel.draw_line(275, 100, 225, 75, fill="black")  # Upper diag
panel.draw_line(275, 100, 225, 125, fill="black") # Lower diag

# Second horizontal line with inward arrows
panel.draw_line(75, 200, 275, 200, fill="black")

# Left arrowhead (pointing inward, touching only the start of the line)
panel.draw_line(25, 175, 75, 200, fill="black")   # Upper diag
panel.draw_line(25, 225, 75, 200, fill="black")   # Lower diag

# Right arrowhead (pointing inward, touching only the end of the line)
panel.draw_line(325, 175, 275, 200, fill="black")  # Upper diag
panel.draw_line(325, 225, 275, 200, fill="black")  # Lower diag

## New black line in the second rectangle from the left on the top row
panel.draw_line(500, 20, 600, 230, fill="black", width=3)

# Blue line inside the second rectangle from the left on the top row
panel.draw_line(550, 100, 610, 210, fill="blue", width=3)

# Gray rectangle in the second rectangle from the left on the top row
panel.draw_rect(525, 30, 30, 200, fill="gray", outline="gray")

# Define the starting position for the grid inside the third rectangle (top row)
start_x = (2 * rect_w) + 10  # 10px from the left edge of the third rectangle
start_y = 10  # 10px from the top edge of the third rectangle

# Define the size and spacing of the squares
sq_W_H = 30
spacing = 20  # Space between squares

# Loop to create 6 rows and 7 columns of black squares
for row in range(6):
    for col in range(7):
        x = start_x + col * (sq_W_H + spacing)
        y = start_y + row * (sq_W_H + spacing)
        panel.draw_rect(x, y, sq_W_H, sq_W_H, fill="black", outline="black")

# Left diagonal line in the second rectangle from the left in the middle row
panel.draw_line(350 + 50, 600, 350 + 130, 300, fill="black", width=4)

# Right diagonal line in the second rectangle from the left in the middle row
panel.draw_line(350 + 300, 600, 350 + 220, 300, fill="black", width=4)

#The horiz lines inside the 2nd rect from the left in the middle row
rect_x = 350  # Left edge of the rectangle
rect_y = 300  # Top edge of the rectangle
rect_center_x = 525 # Center of the rectangle
start_y = 580  # Start 20 from the bottom

# Loop to create 14 centered horizontal black lines
line_length = 270
for i in range(14):
    start_x = rect_center_x - (line_length // 2)  # Center the line
    end_x = start_x + line_length
    panel.draw_line(start_x, start_y, end_x, start_y, fill="black", width=4)
    start_y -= 20  # Move up by 20px for the next line
    line_length -= 10  # Decrease the length by 10px

# Draw the two centered red lines using explicit coordinates
panel.draw_line(430, 570, 620, 570, fill="red", width=4)
panel.draw_line(430, 370, 620, 370, fill="red", width=4)

# Loop to create the second column of gray rectangles covering the blank spaces
for i in range(6):  # Only 5 because it's in between the black rectangles
    panel.draw_rect(
        1300, 325 + (i * 50), 50, 25, fill="gray", outline="gray")

# Loop to create 6 black rectangles inside the last rectangle from the left
# in the second row
for i in range(6):
    panel.draw_rect(
        1050, 300 + (i * 50), 350, 25, fill="black", outline="black")

# Loop to create the first column of gray rectangles covering the black
for i in range(6):
    panel.draw_rect(
        1150, 300 + (i * 50), 50, 25, fill="gray", outline="gray"
    )

# Define the position and size of the bottom-left rectangle
bottom_left_x = 0
bottom_left_y = 600
bottom_left_w = rect_w
bottom_left_h = rect_h

# Draw the gradient using vertical lines
for i in range(0, 350, 2):
    color_value = i // 2  # Increase each RGB component by 1 per step
    hex_color = f"#{color_value:02x}{color_value:02x}{color_value:02x}"
    panel.draw_line(0 + i, 600,0 + i, 600 + 300,fill=hex_color, width=2)

# Draw the overlaying rectangle
overlay_x = bottom_left_x + 50
overlay_y = bottom_left_y + 125
overlay_w = 250
overlay_h = 50
panel.draw_rect(
    overlay_x, overlay_y, overlay_w, overlay_h,
    fill="#7d7d7d", outline="#7d7d7d"  # 125 in hex is 7d
)

# Define the center of the rectangle
center_x = 700 + (350 // 2)  # 700 + 175 = 875
center_y = 600 + (300 // 2)  # 600 + 150 = 750

# Draw 16 diagonal lines from the left edge to the center
for i in range(16):
    start_x = 700  # Left edge of the rectangle
    start_y = 600 + (i * 20)  # Spaced by 20px
    panel.draw_line(start_x, start_y, 875, 750, fill="purple", width=1)

# Draw 16 diagonal lines from the right edge to the center
for i in range(16):
    start_x = 1050  # Right edge of the rectangle (700 + 350)
    start_y = 600 + (i * 20)  # Spaced by 20px
    panel.draw_line(start_x, start_y, 875, 750, fill="purple", width=1)

# First red vertical line, 125 pixels from the left
panel.draw_line(700 + 125, 600, 700 + 125, 900, fill="red", width=3)

# Second red vertical line, 225 pixels from the left
panel.draw_line(700 + 225, 600, 700 + 225, 900, fill="red", width=3)
