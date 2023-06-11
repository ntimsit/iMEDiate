import tkinter as tk
# from PIL import ImageTk, Image
import main

def run_chatbot():
    button.pack_forget()# Hide the "Run Chatbot" button
    end_button.pack(side=tk.BOTTOM, pady=10)  # Show the "End Session" button
    main.main(window)


def end_session():
    window.destroy()  # Close the program

def resize_canvas(event):
    canvas.config(width=event.width, height=event.height)

    # Calculate the size of the background image based on the canvas size
    bg_width = event.width
    bg_height = int(event.height * 0.8)  # Adjust the height as desired

    # Resize the background image
    # bg_image_resized = background_image.resize((bg_width, bg_height), Image.ANTIALIAS)

    # Update the background image
    # background_photo = ImageTk.PhotoImage(bg_image_resized)
    # canvas.create_image(0, event.height - bg_height, anchor=tk.NW, image=background_photo)
    # canvas.image = background_photo  # Store a reference to the image to prevent garbage collection

# Create the main window
window = tk.Tk()


# Set window title
window.title("Chatbot UI")

# Set window size
window.geometry("470x800")  # Width x Height

# Set background color
window.configure(bg="light blue")

# Load the background image
# background_image = Image.open(r"images\our_logo.png")

# Create a label widget
label = tk.Label(window, text="Hello user!", font=("Arial", 14))
label.pack()

# Create a button widget
button = tk.Button(window, text="Run Chatbot", command=run_chatbot, width=20, height=3, relief=tk.RAISED, font=("Arial", 12, "bold"))
button.pack(side=tk.BOTTOM, pady=10)  # Place at the bottom

# Create an "End Session" button but hide it initially
end_button = tk.Button(window, text="End Session", command=end_session, width=20, height=3, relief=tk.RAISED, font=("Arial", 12, "bold"))
button.pack(side=tk.BOTTOM, pady=10)  # Place at the bottom

# Create a canvas to place the background image
canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height(), bg="light blue", highlightthickness=0)
canvas.pack()

# Bind the resize_canvas function to the Configure event of the window
window.bind("<Configure>", resize_canvas)

# Start the main event loop
window.mainloop()
