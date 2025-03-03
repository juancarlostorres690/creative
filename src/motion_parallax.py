from DrawingPanel import *

def main():
    panel = DrawingPanel(500, 400, "lightblue")

    previous_x, previous_y = panel.get_mouse_x(), panel.get_mouse_y()
    previous_hill_1_x = 0 + (previous_x * 0.015)
    previous_hill_1_y = 100 + (previous_y * 0.015)
    previous_hill_2_x = -200 + (previous_x * 0.015)
    previous_hill_2_y = 80 + (previous_y * 0.015)
    previous_lake_x = 20 + (previous_x * 0.02)
    previous_butterfly_x = 300 + (previous_x * 0.05)
    previous_butterfly_y = 200 + (previous_y * 0.05)
    previous_bush_1_x = 300 + (previous_x * 0.03)
    previous_bush_1_y = 250 + (previous_y * 0.03)
    previous_bush_2_x = 340 + (previous_x * 0.03)
    previous_bush_2_y = 240 + (previous_y * 0.03)
    previous_bush_3_x = 380 + (previous_x * 0.03)
    previous_bush_3_y = 260 + (previous_y * 0.03)
    previous_tree_trunk_x = 115 + (previous_x * 0.025)  # Centered trunk under leaves
    previous_tree_trunk_y = 180 + (previous_y * 0.025)
    previous_tree_leaves_x = 85 + (previous_x * 0.025)
    previous_tree_leaves_y = 80 + (previous_y * 0.025)

    panel.fill_oval(450, 10, 50, 50, "yellow")  # Sun
    panel.fill_oval(previous_hill_1_x, previous_hill_1_y, 700, 1000, "lightgreen")
    panel.fill_oval(previous_hill_2_x, previous_hill_2_y, 700, 1000, "forestgreen")
    panel.fill_oval(previous_butterfly_x, previous_butterfly_y, 20, 50, "orange")
    panel.fill_rect(previous_butterfly_x + 15, previous_butterfly_y + 5, 5, 40, "black")
    panel.fill_oval(previous_bush_1_x, previous_bush_1_y, 50, 90, "green")
    panel.fill_oval(previous_bush_2_x, previous_bush_2_y, 60, 150, "green")
    panel.fill_oval(previous_bush_3_x, previous_bush_3_y, 80, 100, "green")
    panel.fill_oval(previous_tree_leaves_x, previous_tree_leaves_y, 80, 100, "green")  # Leaves
    panel.fill_rect(previous_tree_trunk_x, previous_tree_trunk_y, 20, 50, "brown")  # Trunk
    panel.fill_rect(0, 300, 500, 100, "darkgreen")  # Grass (Draws only once, doesn't move or erase)
    panel.fill_oval(previous_lake_x, 350, 200, 100, "blue")

    while True:
        mouse_x = panel.get_mouse_x()
        mouse_y = panel.get_mouse_y()

        hill_1_x = 0 + (mouse_x * 0.015)
        hill_1_y = 100 + (mouse_y * 0.015)
        hill_2_x = -200 + (mouse_x * 0.015)
        hill_2_y = 80 + (mouse_y * 0.015)
        lake_x = 20 + (mouse_x * 0.02)
        butterfly_x = 300 + (mouse_x * 0.05)
        butterfly_y = 200 + (mouse_y * 0.05)
        bush_1_x = 300 + (mouse_x * 0.03)
        bush_1_y = 250 + (mouse_y * 0.03)
        bush_2_x = 340 + (mouse_x * 0.03)
        bush_2_y = 240 + (mouse_y * 0.03)
        bush_3_x = 380 + (mouse_x * 0.03)
        bush_3_y = 260 + (mouse_y * 0.03)
        tree_trunk_x = 115 + (mouse_x * 0.025)
        tree_trunk_y = 180 + (mouse_y * 0.025)
        tree_leaves_x = 85 + (mouse_x * 0.025)
        tree_leaves_y = 80 + (mouse_y * 0.025)

        if (mouse_x, mouse_y) != (previous_x, previous_y):
            panel.fill_rect(previous_tree_trunk_x, previous_tree_trunk_y, 20, 50, "lightblue")  # Erase trunk
            panel.fill_oval(previous_tree_leaves_x, previous_tree_leaves_y, 80, 100, "lightblue")  # Erase leaves
            panel.fill_oval(previous_butterfly_x, previous_butterfly_y, 20, 50, "lightblue")
            panel.fill_rect(previous_butterfly_x + 15, previous_butterfly_y + 5, 5, 40, "lightblue")
            panel.fill_oval(previous_bush_1_x, previous_bush_1_y, 50, 90, "lightblue")
            panel.fill_oval(previous_bush_2_x, previous_bush_2_y, 60, 150, "lightblue")
            panel.fill_oval(previous_bush_3_x, previous_bush_3_y, 80, 100, "lightblue")
            panel.fill_oval(previous_hill_1_x, previous_hill_1_y, 700, 1000, "lightblue")
            panel.fill_oval(previous_hill_2_x, previous_hill_2_y, 700, 1000, "lightblue")
            panel.fill_oval(previous_lake_x, 350, 200, 100, "lightblue")
            panel.fill_oval(hill_1_x, hill_1_y, 700, 1000, "lightgreen")
            panel.fill_oval(hill_2_x, hill_2_y, 700, 1000, "forestgreen")
            panel.fill_oval(butterfly_x, butterfly_y, 20, 50, "orange")
            panel.fill_rect(butterfly_x + 15, butterfly_y + 5, 5, 40, "black")
            panel.fill_oval(bush_1_x, bush_1_y, 50, 90, "green")
            panel.fill_oval(bush_2_x, bush_2_y, 60, 150, "green")
            panel.fill_oval(bush_3_x, bush_3_y, 80, 100, "green")
            panel.fill_oval(tree_leaves_x, tree_leaves_y, 80, 100, "green")  # Draw tree leaves
            panel.fill_rect(tree_trunk_x, tree_trunk_y, 20, 50, "brown")  # Draw tree trunk
            panel.fill_rect(0, 300, 500, 100, "darkgreen")  # Grass (Draws only once, doesn't move or erase)
            panel.fill_oval(lake_x, 350, 200, 100, "blue")

            previous_hill_1_x = hill_1_x
            previous_hill_1_y = hill_1_y
            previous_hill_2_x = hill_2_x
            previous_hill_2_y = hill_2_y
            previous_x, previous_y = mouse_x, mouse_y
            previous_lake_x = lake_x
            previous_butterfly_x = butterfly_x
            previous_butterfly_y = butterfly_y
            previous_bush_1_x = bush_1_x
            previous_bush_1_y = bush_1_y
            previous_bush_2_x = bush_2_x
            previous_bush_2_y = bush_2_y
            previous_bush_3_x = bush_3_x
            previous_bush_3_y = bush_3_y
            previous_tree_trunk_x = tree_trunk_x
            previous_tree_trunk_y = tree_trunk_y
            previous_tree_leaves_x = tree_leaves_x
            previous_tree_leaves_y = tree_leaves_y
        panel.sleep(2)
main()
