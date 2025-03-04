import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Green Rectangle with Black Border")

    # Create a Canvas widget
    canvas = tk.Canvas(root, width=1410, height=910, bg="lightblue")
    canvas.pack()

    # Draw the first green rectangle with a black border
    canvas.create_rectangle(0, 0, 350, 300, fill="green", outline="black", width=2)

    # Draw the second blue rectangle next to the first one
    canvas.create_rectangle(351, 0, 701, 300, fill="blue", outline="black", width=2)

    # Start the Tkinter event loop
    root.mainloop()

# Run the main function
main()
