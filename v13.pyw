import tkinter as tk
from tkinter import PhotoImage
from tkVideoPlayer import TkinterVideo  # Ensure this library is installed
from tkinter import Canvas
from tkinter import messagebox  # Import pentru popup-uri
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import Image, ImageTk, ImageDraw
import os
import sys
import json  
# Define a global variable to store the username
user_input = ""
def get_asset_path(filename):
    """
    Returns the path of a file, whether the script is run normally or packaged with PyInstaller.
    """
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller's temp directory
        return os.path.join(sys._MEIPASS, filename)
    return filename

def play_video():
    for widget in root.winfo_children():
        widget.destroy()
    default_video_path = get_asset_path(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-03-31 at 12.10.50_af799974.mp4")  # Place the default video file in the same directory
    if not os.path.exists(default_video_path):
        messagebox.showerror("Error", "Default video file not found! Please select a file.")
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if file_path:
            default_video_path = file_path
        else:
            return
    # Create video player
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-03-31 at 12.10.50_af799974.mp4") 
    videoplayer.pack()
    videoplayer.place(relx=0.5, rely=0.5, anchor="center", width=1550, height=791)  # Exemplu pentru 400x300 # Replace with your video file path
    videoplayer.play()

    # Schedule transition to grid after video ends
    videoplayer.bind("<<Ended>>", lambda e: show_grid())

def show_grid():
    global user_input
    global username, password, your_email
    background_video_path =get_asset_path(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Default video file for background
    if not os.path.exists(background_video_path):
        messagebox.showerror("Error", "Background video file not found! Please select a file.")
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if file_path:
            background_video_path = file_path
        else:
            return
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

    username = tk.Entry(container, font=('Arial', 15), fg='white', bg='#180451')
    username.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    user_email = tk.Label(container, text='Your e-mail', font=('Gill Sans Ultra Bold', 15), fg='#1b219d', bg='#711adf')
    user_email.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    your_email = tk.Entry(container, font=('Arial', 15), fg='white', bg='#180451')
    your_email.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    user_password = tk.Label(container, text='Password', font=('Gill Sans Ultra Bold', 15), fg='#1b219d', bg='#711adf')
    user_password.grid(row=4, column=0, padx=5, pady=5, sticky="e")

    password = tk.Entry(container, font=('Arial', 15), fg='white', bg='#180451', show='*')
    password.grid(row=4, column=1, padx=5, pady=5, sticky="w")
    
    submit = tk.Button(container, text='Submit', font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=submit_username)
    submit.grid(row=5, column=0, columnspan=2, padx=10, pady=20, sticky="ew")
   
def submit_username():
    entered_username = username.get()
    entered_password = password.get()
    entered_email = your_email.get()

    # Verify if all fields are completed
    if not entered_username or not entered_password or not entered_email:
        # Show an error popup with the message
        messagebox.showerror("Eroare de Autentificare", "Autentifică-te!")
    else:
        # If all fields are valid, proceed
        global user_input
        global user_mail
        user_input = entered_username
        user_mail = entered_email
        on_submit()

     # Continuă jocul



def on_submit():
    for widget in root.winfo_children():
        widget.destroy()
    canvas = Canvas(root)
    canvas.place(relwidth=1, relheight=1)
    
    default_video_path = get_asset_path(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")
    if not os.path.exists(default_video_path):
        # Prompt the user to select a file if missing
        messagebox.showerror("Error", "Background video file not found! Please select a file.")
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if file_path:
            default_video_path = file_path
        else:
            return
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
    undo_button = tk.Button(root, text="Undo", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=show_grid)
    undo_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    # Settings button
    settings_button = tk.Button(root, text="Settings", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=open_settings_window)
    settings_button.place(relx=0.9, rely=0.1, anchor=tk.CENTER)


def navigate_to_page(option):
    for widget in root.winfo_children():
        widget.destroy()
    background_video_path = get_asset_path(r"C:\Users\Adriana\Desktop\Altele\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")
    if not os.path.exists(background_video_path):
        messagebox.showerror("Error", "Background video file not found! Please select a file.")
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if file_path:
            background_video_path = file_path
        else:
            return
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

    top_bar = tk.Frame(root, bg='#711adf', height=50)
    top_bar.pack(side=tk.TOP, fill=tk.X)

    # Add three buttons to the top bar
    button1 = tk.Button(top_bar, text="Progress", font=('Gill Sans Ultra Bold', 12), fg='white', bg='#180451', command=lambda: print("Button 1 pressed"))
    button1.pack(side=tk.LEFT, padx=10, pady=5)

    button2 = tk.Button(top_bar, text="LeaderBoard", font=('Gill Sans Ultra Bold', 12), fg='white', bg='#180451', command=lambda: print("Button 2 pressed"))
    button2.pack(side=tk.LEFT, padx=20, pady=5)

    button3 = tk.Button(top_bar, text="Profile", font=('Gill Sans Ultra Bold', 12), fg='white', bg='#180451', command=open_profile_window)
    button3.pack(side=tk.LEFT, padx=50, pady=5)
    # Example planet images
    planet_images = {
        "Planet A": PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-03-15 at 22.57.57_426e474f1.2.png"),  # Replace paths
        "Planet B": PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-03-15 at 22.57.57_426e474f.3.png"),
        "Planet C": PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-03-15 at 22.57.57_426e474f.4.png"),}

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
    bg_image = tk.Label(root, image=grid_image_path)
    bg_image.place(relheight=1, relwidth=1)
    
    # Display title
    title_label = tk.Label(
        bg_image,
        text=f"Options for {planet_name}",
        font=('Gill Sans Ultra Bold', 20),
        fg='white',
        bg='#711adf'
    )
    title_label.pack(pady=20)

    # Generate 10 dynamic buttons
    for i in range(10):
        button = tk.Button(
            bg_image,
            text=f"Option {i + 1}",
            font=('Gill Sans Ultra Bold', 15),
            fg='white',
            bg='#180451',
            command=lambda opt=i: print(f"Option {opt + 1} selected!")  # Replace with actual functionality
        )
        button.pack(pady=10)

    # Back button
    back_button = tk.Button(
       bg_image,
        text="Back",
        font=('Gill Sans Ultra Bold', 15),
        fg='white',
        bg='#180451',
        command=on_submit
    )
    back_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

def save_user_data(data):
    with open("user_data.json", "w") as f:
        json.dump(data, f)

def load_user_data():
    try:
        with open("user_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Initialize user data
user_data = load_user_data()
def choose_profile_picture():
    global profile_label  # Referim profile_label
    # Permite utilizatorului să selecteze un fișier imagine
    file_path = filedialog.askopenfilename(title="Choose a Profile Picture", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    if file_path:
        try:
            # Încarcă imaginea selectată
            profile_picture = Image.open(file_path).convert("RGBA")  # Convertim în format RGBA
            
            # Creăm o mască circulară
            mask = Image.new("L", profile_picture.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, profile_picture.size[0], profile_picture.size[1]), fill=255)
            
            # Aplicăm masca circulară
            circular_profile = Image.new("RGBA", profile_picture.size)
            circular_profile.paste(profile_picture, (0, 0), mask)
            
            # Redimensionăm imaginea rotundă
            circular_profile = circular_profile.resize((100, 100))  # Redimensionare (opțional)
            profile_picture_tk = ImageTk.PhotoImage(circular_profile)

            # Afișează imaginea rotundă în fereastra de "Settings"
            profile_label.config(image=profile_picture_tk)
            profile_label.image = profile_picture_tk
            
            user_data["profile_picture"] = file_path  # Save the file path
            save_user_data(user_data)  # Salvează referința pentru a evita garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

def remove_profile_picture():
    global profile_label
    profile_label.config(image="", text="No profile picture selected")
    user_data.pop("profile_picture", None)  # Remove profile picture from user data
    save_user_data(user_data)
def open_settings_window():
    global user_input  # Reference the username variable
    global user_mail
    global profile_label

    # Create a new top-level window for settings
    settings_window = tk.Toplevel(root)
    settings_window.geometry('200x400')  # Small vertical window dimensions
    settings_window.title("Settings")
    settings_window.configure(bg='#711adf')  # Background color

    # Add content to the settings window
    label = tk.Label(settings_window, text="Settings", font=('Gill Sans Ultra Bold', 20), fg='#1b219d', bg='#711adf')
    label.pack(pady=20)

    # Display username and email
    username_label = tk.Label(settings_window, text=f"Username: {user_input}", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    username_label.pack(pady=10)
    email_label = tk.Label(settings_window, text=f"E-mail: {user_mail}", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    email_label.pack(pady=30)
    
    # Profile picture label
    profile_label = tk.Label(settings_window, bg='#711adf', text="No profile picture selected")
    profile_label.pack(pady=20)
    
    if "profile_picture" in user_data:
        try:
            profile_picture = Image.open(user_data["profile_picture"]).convert("RGBA")
            mask = Image.new("L", profile_picture.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, profile_picture.size[0], profile_picture.size[1]), fill=255)
            circular_profile = Image.new("RGBA", profile_picture.size)
            circular_profile.paste(profile_picture, (0, 0), mask)
            circular_profile = circular_profile.resize((100, 100))
            profile_picture_tk = ImageTk.PhotoImage(circular_profile)

            # Display profile picture
            profile_label.config(image=profile_picture_tk, text="")
            profile_label.image = profile_picture_tk
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load saved image: {e}")
    # Button to choose profile picture
    choose_picture_button = tk.Button(
        settings_window,
        text="Choose Profile Picture",
        font=('Gill Sans Ultra Bold', 15),
        fg='white',
        bg='#180451',
        command=choose_profile_picture
    )
    choose_picture_button.pack(pady=20)

    remove_picture_button = tk.Button(
        settings_window,
        text="Remove Profile Picture",
        font=('Gill Sans Ultra Bold', 15),
        fg='white',
        bg='#180451',
        command=remove_profile_picture
    )
    remove_picture_button.pack(pady=20)

root = tk.Tk()
root.geometry('900x600')  # Adjust for practical size
root.title('Welcome to app!')

settings_button = tk.Button(
    root,
    text="Settings",
    font=('Gill Sans Ultra Bold', 15),
    fg='white',
    bg='#180451',
    command=open_settings_window
)
settings_button.pack(pady=20)
def open_profile_window():
    global profile_label  # Referim profile_label

    # Creare fereastră nouă pentru profil
    profile_window = tk.Toplevel(root)
    profile_window.geometry('300x400')  # Dimensiuni ajustate
    profile_window.title("Profile")
    profile_window.configure(bg='#711adf')  # Culoare de fundal

    # Adăugare etichetă pentru titlu
    title_label = tk.Label(profile_window, text="Profile", font=('Gill Sans Ultra Bold', 20), fg='#1b219d', bg='#711adf')
    title_label.pack(pady=20)

    # Afișare poza de profil
    profile_display_label = tk.Label(profile_window, bg='#711adf', text="No profile picture selected")
    profile_display_label.pack(pady=20)

    if "profile_picture" in user_data:
        try:
            # Încărcare poza de profil salvată
            profile_picture = Image.open(user_data["profile_picture"]).convert("RGBA")
            mask = Image.new("L", profile_picture.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, profile_picture.size[0], profile_picture.size[1]), fill=255)
            circular_profile = Image.new("RGBA", profile_picture.size)
            circular_profile.paste(profile_picture, (0, 0), mask)
            circular_profile = circular_profile.resize((100, 100))  # Redimensionare
            profile_picture_tk = ImageTk.PhotoImage(circular_profile)

            # Afișare poza de profil în fereastră
            profile_display_label.config(image=profile_picture_tk, text="")
            profile_display_label.image = profile_picture_tk  # Păstrare referință pentru a evita garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load saved image: {e}")

    # Afișare username și e-mail
    username_label = tk.Label(profile_window, text=f"Username: {user_input}", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    username_label.pack(pady=10)
    email_label = tk.Label(profile_window, text=f"E-mail: {user_mail}", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#711adf')
    email_label.pack(pady=10)

# Adaugă butonul "Profile" în fereastra principală
button_profile = tk.Button(
    root,
    text="Profile",
    font=('Gill Sans Ultra Bold', 12),
    fg='white',
    bg='#180451',
    command=open_profile_window
)
button_profile.pack(side=tk.LEFT, padx=50, pady=5)

grid_image_path = PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-04-05 at 22.02.28_9d96eb52.png")  # Replace with your grid background path
play_video()

root.mainloop()
