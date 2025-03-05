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