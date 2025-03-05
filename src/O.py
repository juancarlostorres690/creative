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

# Coordinates for the top-left rectangle
x = 0
y = 0

# Length of the lines
line_l = 200

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
