import tkinter as tk
from tkinter import PhotoImage
from tkVideoPlayer import TkinterVideo  # Ensure this library is installed
from tkinter import Canvas
# Define a global variable to store the username
user_input = ""

def play_video():
    for widget in root.winfo_children():
        widget.destroy()

    # Create video player
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-03-31 at 12.10.50_af799974.mp4") 
    videoplayer.pack()
    videoplayer.place(relx=0.5, rely=0.5, anchor="center", width=1550, height=790)  # Exemplu pentru 400x300 # Replace with your video file path
    videoplayer.play()

    # Schedule transition to grid after video ends
    videoplayer.bind("<<Ended>>", lambda e: show_grid())

def show_grid():
    global user_input

    for widget in root.winfo_children():
        widget.destroy()

    # Create a canvas to hold the video background
    canvas = Canvas(root)
    canvas.place(relwidth=1, relheight=1)

    # Load and play video as background
    videoplayer = TkinterVideo(master=canvas, scaled=True)
    videoplayer.load(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Replace with your video file path
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    # Loop the video after it ends
    videoplayer.bind("<<Ended>>", lambda e: videoplayer.play())

    # Form elements placed on top of the video
    container = tk.Frame(root, bg='#711adf')
    container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    title0 = tk.Label(container, text="Welcome to Cosmiccode!", font=('Gill Sans Ultra Bold', 24), fg='#1b219d', bg='#711adf')
    title0.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    title1 = tk.Label(container, text="Enter your username and password and let's start a cosmic game!", font=('Gill Sans Ultra Bold', 15), fg='#1b219d', bg='#711adf', wraplength=400)
    title1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    user_label = tk.Label(container, text='Username', font=('Gill Sans Ultra Bold', 15), fg='#1b219d', bg='#711adf')
    user_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    username = tk.Entry(container, font=('Stencil', 15), fg='white', bg='#180451')
    username.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    user_password = tk.Label(container, text='Password', font=('Gill Sans Ultra Bold', 15), fg='#1b219d', bg='#711adf')
    user_password.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    password = tk.Entry(container, font=('Stencil', 15), fg='white', bg='#180451', show='*')
    password.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    def submit_username():
        global user_input
        user_input = username.get()
        on_submit()

    submit = tk.Button(container, text='Submit', font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=submit_username)
    submit.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="ew")



def on_submit():
    for widget in root.winfo_children():
        widget.destroy()
    canvas = Canvas(root)
    canvas.place(relwidth=1, relheight=1)

    # Load and play video as background
    videoplayer = TkinterVideo(master=canvas, scaled=True)
    videoplayer.load(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Replace with your video file path
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    # Loop the video after it ends
    videoplayer.bind("<<Ended>>", lambda e: videoplayer.play())
    # Frame for coding options
    options_frame = tk.Frame(root, bg='#711adf')
    options_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    options_label = tk.Label(options_frame, text="Learn to code in...", font=('Gill Sans Ultra Bold', 24), fg='#1b219d', bg='#711adf')
    options_label.pack(pady=20)
    
    # Stickers for buttons
    cplusplus_sticker = PhotoImage(file=r"C:\Users\Adriana\Desktop\Altele\ISO_C++_Logo.svg.png")  # Replace with your sticker file path
    python_sticker = PhotoImage(file=r"C:\Users\Adriana\Desktop\Altele\Python.svg.png")        # Replace with your sticker file path
    javascript_sticker = PhotoImage(file=r"C:\Users\Adriana\Desktop\Altele\1698604163003.png")# Replace with your sticker file path

    # Options with stickers
    options = [
        ("C++", cplusplus_sticker),
        ("Python", python_sticker),
        ("JavaScript", javascript_sticker),
    ]

    button_width = 250
    button_height = 50

    for option, sticker in options:
        option_button = tk.Button(
            options_frame,
            text=option,
            font=('Gill Sans Ultra Bold', 14),
            fg='white',
            bg='#180451',
            image=sticker,  # Add the sticker
            compound=tk.LEFT,  # Place the sticker on the left side of the button text
            command=lambda opt=option: navigate_to_page(opt),
            width=button_width,
            height=button_height
        )
        option_button.image = sticker  # Keep a reference to prevent garbage collection
        option_button.pack(pady=10)

    # Undo button
    undo_button = tk.Button(bg_image, text="Undo", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=show_grid)
    undo_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    # Settings button
    settings_button = tk.Button(bg_image, text="Settings", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=open_settings_window)
    settings_button.place(relx=0.9, rely=0.1, anchor=tk.CENTER)


def navigate_to_page(option):
    for widget in root.winfo_children():
        widget.destroy()

    # Background for planet buttons
    canvas = Canvas(root)
    canvas.place(relwidth=1, relheight=1)

    # Load and play video as background
    videoplayer = TkinterVideo(master=canvas, scaled=True)
    videoplayer.load(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Replace with your video file path
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    # Loop the video after it ends
    videoplayer.bind("<<Ended>>", lambda e: videoplayer.play())

    # Example planet images
    planet_images = {
        "Planet A": PhotoImage(file=r"C:\Users\Adriana\AppData\Local\Temp\59262d90-f7f9-497f-aba0-99d48a24949f_iloveimg-converted.zip.49f\WhatsApp Image 2025-03-15 at 22.57.57_426e474f.4.png"),  # Replace paths
        "Planet B": PhotoImage(file=r"C:\Users\Adriana\AppData\Local\Temp\efb8956f-63b9-4f0e-9ef5-1d2978907fe6_iloveimg-converted.zip.fe6\WhatsApp Image 2025-03-15 at 22.57.57_426e474f.3.png"),
        "Planet C": PhotoImage(file=r"C:\Users\Adriana\AppData\Local\Temp\4f0731ba-0f37-4557-b400-700d89710775_iloveimg-converted.zip.775\WhatsApp Image 2025-03-15 at 22.57.57_426e474f1.2.png"),
    }

    # Add planet buttons directly on the background image
    column = 0
    for planet_name, planet_image in planet_images.items():
        planet_button = tk.Button(
            root,
            image=planet_image,
            command=lambda name=planet_name: show_new_options_page(name),  # Navigate to new options page
            borderwidth=0,
            bg='#711adf',
            activebackground='#711adf'
        )
        planet_button.image = planet_image  # Keep a reference
        planet_button.place(relx=0.3 + (column * 0.2), rely=0.5, anchor=tk.CENTER)  # Adjust placement
        column += 1

    # Undo button
    message_label = tk.Label(root, text=f"You selected {option}. Explore planets below!", font=('Gill Sans Ultra Bold', 20), fg='#1b219d', bg='#711adf')
    message_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    undo_button = tk.Button(
        root,
        text="Undo",
        font=('Gill Sans Ultra Bold', 12),
        fg='white',
        bg='#180451',
        command=on_submit
    )
    undo_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)


def show_new_options_page(planet_name):
    for widget in root.winfo_children():
        widget.destroy()

    # Set a background for the new page
    new_page_bg = tk.Label(root, bg='#711adf')  # You can use an image if needed
    new_page_bg.place(relheight=1, relwidth=1)

    # Display title
    title_label = tk.Label(
        new_page_bg,
        text=f"Options for {planet_name}",
        font=('Gill Sans Ultra Bold', 20),
        fg='white',
        bg='#711adf'
    )
    title_label.pack(pady=20)

    # Generate 10 dynamic buttons
    for i in range(10):
        button = tk.Button(
            new_page_bg,
            text=f"Option {i + 1}",
            font=('Gill Sans Ultra Bold', 15),
            fg='white',
            bg='#180451',
            command=lambda opt=i: print(f"Option {opt + 1} selected!")  # Replace with actual functionality
        )
        button.pack(pady=10)

    # Back button
    back_button = tk.Button(
        new_page_bg,
        text="Back",
        font=('Gill Sans Ultra Bold', 15),
        fg='white',
        bg='#180451',
        command=on_submit
    )
    back_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

def open_settings_window():
    global user_input  # Reference the username variable

    # Create a new top-level window for settings
    settings_window = tk.Toplevel(root)
    settings_window.geometry('200x400')  # Small vertical window dimensions
    settings_window.title("Settings")
    settings_window.configure(bg='#711adf')  # Background color

    # Add content to the settings window
    label = tk.Label(settings_window, text="Settings", font=('Gill Sans Ultra Bold', 20), fg='#1b219d', bg='#711adf')
    label.pack(pady=20)

    # Display username
    username_label = tk.Label(settings_window, text=f"Username: {user_input}", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    username_label.pack(pady=10)
    saturn_label = tk.Label(settings_window, text="Saturn:basic skills in the selected language", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    saturn_label.pack(pady=30)
    venus_label = tk.Label(settings_window, text="Venus:intermediate skills in the selected language", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    venus_label.pack(pady=40)
    uranus_label = tk.Label(settings_window, text="Uranus:advanced skills in the selected language", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    uranus_label.pack(pady=50)
    close_button = tk.Button(settings_window, text="Close", font=('Gill Sans Ultra Bold', 12), fg='white', bg='#180451', command=settings_window.destroy)
    close_button.pack(pady=60)

root = tk.Tk()
root.geometry('900x600')  # Adjust for practical size
root.title('Welcome to app!')

grid_image_path = PhotoImage(file=r"C:\Users\Adriana\Desktop\Altele\Captură de ecran din 2025-03-14 la 16.12.48.png")  # Replace with your grid background path
play_video()

root.mainloop()
