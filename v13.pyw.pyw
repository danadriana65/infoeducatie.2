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
import smtplib
from email.mime.text import MIMEText
from functools import partial
import pandas as pd
from pathlib import Path
import bcrypt

# Define a global variable to store the username
user_input = ""
root = tk.Tk()
root.geometry('900x600')  # Adjust for practical size
root.title('Welcome to app!')


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
    default_video_path = get_asset_path(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-03-31 at 12.10.50_af799974.mp4")  # Place the default video file in the same directory
    if not os.path.exists(default_video_path):
        messagebox.showerror("Error", "Default video file not found! Please select a file.")
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if file_path:
            default_video_path = file_path
        else:
            return
    # Create video player
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-03-31 at 12.10.50_af799974.mp4") 
    videoplayer.pack()
    videoplayer.place(relx=0.5, rely=0.5, anchor="center", width=1550, height=791)  # Exemplu pentru 400x300 # Replace with your video file path
    videoplayer.play()

    # Schedule transition to grid after video ends
    videoplayer.bind("<<Ended>>", lambda e: show_grid())

def show_grid():
    global user_input
    global username, password, your_email
    background_video_path =get_asset_path(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Default video file for background
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
    videoplayer.load(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Replace with your video file path
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
    
    submit = tk.Button(container, text='Crează Cont', font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=submit_username)
    submit.grid(row=5, column=0, columnspan=2, padx=10, pady=20, sticky="ew")
    login_button = tk.Button(container, text='Login', font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=login)
    login_button.grid(row=6, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

    sign_out_button = tk.Button(
    root,
    text="Sign Out",
    font=('Gill Sans Ultra Bold', 12),
    fg='white',
    bg='#180451',
    command=sign_out
)
    sign_out_button.pack(side=tk.BOTTOM, padx=10, pady=5)

# Funcție pentru salvarea datelor utilizatorului în JSON

def sign_out():
    global user_input, user_mail
    user_input = ""
    user_mail = ""

    # Ștergem utilizatorul curent din JSON
    user_data = load_user_data()
    if user_input in user_data:
        del user_data[user_input]  # Eliminăm doar utilizatorul curent

        # Salvăm datele actualizate
        with open("user_date.json", "w") as f:
            json.dump(user_data, f, indent=4)

    # Resetăm câmpurile de autentificare
    username.delete(0, tk.END)
    your_email.delete(0, tk.END)
    password.delete(0, tk.END)

    # Reîncărcăm pagina de login
    show_grid()

def load_user_data():
    try:
        with open("user_credentials.json", "r") as f:
            data = json.load(f)
            return data if data else {}  # Dacă fișierul e gol, returnează un dicționar gol
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Dacă fișierul nu există sau nu se poate citi, inițializăm un dicționar gol


def store_user_info(username, password, email):
    user_data = load_user_data()  # Încărcăm datele existente
    
    if username in user_data:
        messagebox.showerror("Eroare", "Utilizatorul există deja! Încearcă să te autentifici.")
    else:
        user_data[username] = {"password": password, "email": email}

        # ✅ Salvăm permanent datele
        with open("user_credentials.json", "w") as f:
            json.dump(user_data, f, indent=4)

        messagebox.showinfo("Succes", "Contul a fost creat!")

def verify_user(username, password):
    user_data = load_user_data()

    if username not in user_data:
        return False  # Username-ul nu există
    if "password" not in user_data[username]:
        return False  # Parola nu este salvată corect

    return user_data[username]["password"] == password


def submit_username():
    global user_mail
    global user_input
    entered_username = username.get().strip()
    entered_password = password.get().strip()
    entered_email = your_email.get().strip()

    if not entered_username or not entered_password or not entered_email:
        messagebox.showerror("Eroare de Autentificare", "Autentifică-te!")
    else:
        store_user_info(entered_username, entered_password, entered_email)
        user_mail = entered_email  # Setăm email-ul utilizatorului
        user_input = entered_username   # Modificat aici
        messagebox.showinfo("Succes", "Contul a fost creat!")
        on_submit()  

def login():
    global user_mail, user_input
    entered_username = username.get().strip()
    entered_password = password.get().strip()

    user_data = load_user_data()  # ✅ Încărcăm datele salvate

    if entered_username in user_data:
        if verify_user(entered_username, entered_password):
            messagebox.showinfo("Autentificare reușită", "Te-ai conectat cu succes!")
            user_mail = user_data[entered_username]["email"]  # Setăm email-ul
            user_input = entered_username
            on_submit()
        else:
            messagebox.showerror("Eroare", "Parolă incorectă! Încearcă din nou.")
            password.delete(0, tk.END)  
    else:
        messagebox.showerror("Eroare", "Nu există acest cont! Creează unul mai întâi.")


def on_submit():
    for widget in root.winfo_children():
        widget.destroy()
    canvas = Canvas(root)
    canvas.place(relwidth=1, relheight=1)
    
    default_video_path = get_asset_path(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")
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
    videoplayer.load(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Replace with your video file path
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
    cplusplus_sticker = PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\ISO_C++_Logo.svg(1).png")  # Replace with your sticker file path
    python_sticker = PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\Python.svg(1).png")        # Replace with your sticker file path
    javascript_sticker = PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\1698604163003(1).png")# Replace with your sticker file path

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
    background_video_path = get_asset_path(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")
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
    videoplayer.load(r"C:\Users\Adriana\Desktop\grid\WhatsApp Video 2025-04-05 at 20.39.03_78657a3f.mp4")  # Replace with your video file path
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    # Loop the video after it ends
    videoplayer.bind("<<Ended>>", lambda e: videoplayer.play())

    top_bar = tk.Frame(root, bg='#711adf', height=50)
    top_bar.pack(side=tk.TOP, fill=tk.X)

    # Add three buttons to the top bar
    button1 = tk.Button(top_bar, text="Progress", font=('Gill Sans Ultra Bold', 12), fg='white', bg='#180451', command=show_progress)
    button1.pack(side=tk.LEFT, padx=10, pady=5)

    button2 = tk.Button(top_bar, text="LeaderBoard", font=('Gill Sans Ultra Bold', 12), fg='white', bg='#180451', command=show_leaderboard)
    button2.pack(side=tk.LEFT, padx=20, pady=5)

    button3 = tk.Button(top_bar, text="Profile", font=('Gill Sans Ultra Bold', 12), fg='white', bg='#180451', command=open_profile_window)
    button3.pack(side=tk.LEFT, padx=50, pady=5)
    # Example planet images
    planet_images = {
        "Uranus": PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-03-15 at 22.57.57_426e474f1.2.png"),  # Replace paths
        "Venus": PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-03-15 at 22.57.57_426e474f.3.png"),
        "Saturn": PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-03-15 at 22.57.57_426e474f.4.png"),}

    # Add planet buttons directly on the background image
    column = 0
    for planet_name, planet_image in planet_images.items():
        if option == "Python":
            planet_button_command = lambda name=planet_name: show_new_options_page(name, option)
        elif option == "C++":
            planet_button_command = lambda name=planet_name: show_new_options_page(name, option)
        else:
            planet_button_command = lambda name=planet_name: show_new_options_page(name, None)
        planet_button = tk.Button(
            root,
            image=planet_image,
           command=lambda name=planet_name, option=option: show_new_options_page(name, option),    # Navigate to new options page
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


def show_new_options_page(planet_name, selected_option):
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
    buttons_frame = tk.Frame(root, bg='#711adf')
    buttons_frame.pack(pady=70)
    # Generate 7 dynamic buttons
    for i in range(7):
        if planet_name == "Uranus" and selected_option == "Python":
            button_command = partial(show_question_page, planet_name, selected_option, questions[i], answers[i], correct_answers[i])
        elif planet_name == "Venus" and selected_option == "Python":
            button_command = partial(show_question_page, planet_name, selected_option, questions_python_b[i], answers_python_b[i], correct_answers_python_b[i])
        elif planet_name == "Saturn" and selected_option == "Python":
            button_command = partial(show_question_page_with_code, planet_name, selected_option, questions_python_c[i], code_samples_python_c[i], answers_python_c[i], correct_answers_python_c[i])
        elif planet_name == "Uranus" and selected_option == "JavaScript":
            button_command = partial(show_question_page, planet_name, selected_option, questions_javascript_a[i], answers_javascript_a[i], correct_answers_javascript_a[i])
        elif planet_name == "Venus" and selected_option == "JavaScript":
            button_command = partial(show_question_page, planet_name, selected_option, questions_javascript_code[i], answers_javascript_code[i], correct_answers_javascript_code[i])
        elif planet_name == "Saturn" and selected_option == "JavaScript":
            button_command = partial(show_question_page_with_code, planet_name, selected_option, questions_python_c[i], code_samples_python_c[i], answers_python_c[i], correct_answers_python_c[i])
        elif planet_name == "Uranus" and selected_option == "C++":
            button_command = partial(show_question_page, planet_name, selected_option, questions_cpp[i], answers_cpp[i], correct_answers_cpp[i])
        elif planet_name == "Venus" and selected_option == "C++":
            button_command = partial(show_question_page, planet_name, selected_option, questions_cpp_code[i], answers_cpp_code[i], correct_answers_cpp_code[i])
        elif planet_name == "Saturn" and selected_option == "C++":
            button_command = partial(show_question_page_with_code, planet_name, selected_option, questions_cpp1[i], code_cpp1[i], answers_cpp1[i],correct_answers_cpp1[i])
        else:
            button_command = lambda: print(f"Exercițiu {i + 1} selectat pentru {planet_name}, dar fără întrebări.")
        button = tk.Button(buttons_frame, text=f"Exercițiu {i + 1}", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=button_command)
        button.grid(row=i//2, column=i%2, padx=40, pady=50)  # 2 coloane
        

    # Buton "Înapoi" care revine la pagina principală
    back_button = tk.Button(
       bg_image,
        text="Undo",
        font=('Gill Sans Ultra Bold', 15),
        fg='white',
        bg='#180451',
        command=lambda: on_submit()
    )
    back_button.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

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
questions_cpp1 = [
    "Care dintre următoarele declară corect o funcție în Python?",
    "Care dintre următoarele este sintaxa corectă pentru un `for loop`?",
    "Care este modul corect de a accesa un element dintr-o listă?",
    "Care dintre următoarele alocă corect memorie dinamică?",
    "Care dintre următoarele clase implementează corect moștenirea?",
    "Care este forma corectă de a citi un număr de la tastatură?",
    "Care dintre următoarele definește corect un destructor?"
]

# Vectorul de cod Python asociat fiecărei întrebări
code_cpp1 = [
    "def my_function():\n    pass",
    "for i in range(n):\n    print(i)",
    "my_list = [1, 2, 3]\nprint(my_list[2])",
    "import numpy as np\narr = np.zeros(5)",
    "class Child(Parent):\n    pass",
    "x = int(input(\"Introdu un număr: \"))",
    "class MyClass:\n    def __del__(self):\n        print(\"Destructor apelat\")"
]
answers_cpp1 = [
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 2", "Linia 3", "Linia 1", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"]
]

correct_answers_cpp1 = [
    "Linia 1",
    "Linia 1",
    "Linia 1",
    "Linia 2",
    "Linia 1",
    "Linia 2",
    "Linia 3"
]
questions_cpp_code = [
    "Care dintre următoarele declară corect o funcție în C++?",
    "Care dintre următoarele este sintaxa corectă pentru un `for loop`?",
    "Care este modul corect de a accesa un element dintr-un vector?",
    "Care dintre următoarele alocă corect memorie dinamică?",
    "Care dintre următoarele clase implementează corect moștenirea?",
    "Care este forma corectă de a citi un număr de la tastatură?",
    "Care dintre următoarele definește corect un destructor?"
]

answers_cpp_code = [
    ["void myFunction();", "function myFunction();", "func myFunction();"],
    ["for (i = 0; i < n; i++)", "for i in range(0, n)", "loop (i; i < n; i++)"],
    ["vector[2]", "vector(2)", "vector -> 2"],
    ["int *ptr = new int;", "int ptr = malloc(sizeof(int));", "alloc<int> ptr;"],
    ["class Child : Parent {}", "class Parent -> Child {}", "inherit Parent -> Child {}"],
    ["cin >> x;", "input(x);", "x = scan();"],
    ["~MyClass() {}", "destructor MyClass() {}", "destroy MyClass();"]
]

correct_answers_cpp_code = [
    "void myFunction();",
    "for (i = 0; i < n; i++)",
    "vector[2]",
    "int *ptr = new int;",
    "class Child : Parent {}",
    "cin >> x;",
    "~MyClass() {}"
]

questions_cpp = [
    "Care dintre următoarele este un mod corect de a declara o variabilă în C++?",
    "Ce cuvânt-cheie folosim pentru a aloca dinamic memorie în C++?",
    "Ce tip de date folosim pentru a stoca un singur caracter în C++?",
    "Care dintre următoarele bucle NU există în C++?",
    "Care dintre următoarele operatori este folosit pentru accesarea membrilor unei structuri sau clase?",
    "Care este scopul funcției `main()` în C++?",
    "Ce se întâmplă când apelăm `delete` pe un pointer valid?"
]

answers_cpp = [
    ["int x;", "variable x;", "x = 5;", "declare x;"],
    ["alloc", "new", "malloc", "allocate"],
    ["char", "string", "character", "text"],
    ["for", "while", "repeat-until", "do-while"],
    [".", "->", "*", "&"],
    ["Inițializarea tuturor variabilelor", "Stabilirea punctului de intrare al programului", "Afișarea rezultatelor", "Crearea de obiecte"],
    ["Memoria asociată cu pointerul este eliberată", "Pointerul se șterge automat din cod", "Programul se oprește imediat", "Pointerul este resetat la zero"]
]

correct_answers_cpp = [
    "int x;", "new", "char", "repeat-until", ".", "Stabilirea punctului de intrare al programului", "Memoria asociată cu pointerul este eliberată"
]

questions = [
    "Ce este metoda __new__() în Python?",
    "Ce face @staticmethod în Python?",
    "Care este diferența dintre deepcopy() și copy()?",
    "Ce va returna list(map(lambda x: x**2, range(3)))?",
    'Ce face expresia if __name__ == "__main__": în Python?',
    "Care dintre următoarele NU este o metodă validă pentru sincronizarea thread-urilor în Python?",
    "Ce rezultat va avea print(bool([]) == False)?" ]
  

answers = [
    ["O metodă care creează o instanță înainte de __init__()", "O metodă folosită doar în moștenirea multiplă", "O metodă specială care returnează self", "O metodă de conversie între tipuri de date"],
    ["Creează o metodă care poate fi apelată doar de alte clase", "Definește o metodă statică care nu are acces la self", "Permite accesul la metodele private din clasă", "Transformă metoda într-o variabilă de clasă"],
    ["deepcopy() face conversia tipurilor de date", "copy() elimină referințele către obiectele originale", "deepcopy() este mai rapid decât copy()", "copy() creează o copie superficială, iar deepcopy() copiază recursiv obiectele"],
    ["[1, 4, 9]", "[0, 2, 4]", "[0, 1, 4]", "[1, 2, 3]"],
    ["Creează o variabilă globală numită __main__", "Permite executarea în paralel a mai multor funcții", "Determină dacă scriptul este executat direct", "Verifică dacă scriptul este importat din alt modul"],
    ["threading.Event()", "threading.pause()", "threading.Lock()", "threading.Semaphore()"],
    ["True", "False", "Va genera o eroare", "None"]
]

correct_answers = ["O metodă care creează o instanță înainte de __init__()", "Definește o metodă statică care nu are acces la self", "copy() creează o copie superficială, iar deepcopy() copiază recursiv obiectele", "[0, 1, 4]", "Determină dacă scriptul este executat direct", "threading.pause()", "True"]
questions_javascript_a = [
    "Cum declarăm o variabilă în JavaScript?",
    "Care dintre următoarele NU este un mod valid de a declara o funcție?",
    "Cum verificăm tipul unei variabile în JavaScript?",
    "Ce va afișa `console.log(2 + '2')`?",
    "Care dintre următoarele structuri de date NU există în JavaScript?",
    "Cum iterăm peste un array folosind `map()`?",
    "Cum facem o copie superficială a unui obiect în JavaScript?"
]

answers_javascript_a = [
    ["var x = 10;", "let x = 10;", "const x = 10;", "int x = 10;"],
    ["function myFunc() {}", "const myFunc = function() {}", "myFunc = () => {}", "def myFunc() {}"],
    ["typeof x", "x.type()", "getType(x)", "x.kind"],
    ["22", "'22'", "4", "Error"],
    ["Array", "Set", "Tuple", "Map"],
    ["array.map(x => x * 2)", "map(array, x => x * 2)", "array.map(function(x) { return x * 2 })", "array.forEach(x => x * 2)"],
    ["Object.assign({}, obj)", "obj.copy()", "{...obj}", "clone(obj)"]
]

correct_answers_javascript_a = [
    "int x = 10;",  # Varianta greșită (to test knowledge)
    "def myFunc() {}",  # Varianta greșită (nu există în JS)
    "typeof x",
    "'22'",
    "Tuple",
    "array.map(x => x * 2)",
    "{...obj}"
]
questions_javascript_code = [
    "Cum declarăm o funcție anonimă în JavaScript?",
    "Care este sintaxa corectă pentru Arrow Function?",
    "Cum definim un obiect JavaScript?",
    "Care este modul corect de a itera printr-o listă cu `forEach`?",
    "Cum verificăm dacă un element există într-un array?",
    "Cum facem destructurarea unui obiect?",
    "Cum adăugăm un nou element într-un array?"
]

answers_javascript_code = [
    ["let func = function() {}", "let func() {}", "function = func() {}"],
    ["const add = (a, b) => a + b;", "add = (a, b) { return a + b; }", "function add(a, b) => a + b;"],
    ["const obj = { name: 'Alex', age: 25 }", "object obj = { 'name': 'Alex', 'age': 25 }", "let obj = object { name: 'Alex', age: 25 };"],
    ["array.forEach(item => console.log(item));", "for (item in array) { console.log(item); }", "array.each(item => console.log(item));"],
    ["array.includes(5)", "array.has(5)", "array.exists(5)"],
    ["const { name, age } = obj;", "destructure(obj).get('name', 'age');", "let name, age = obj.extract();"],
    ["array.push('newItem')", "array.add('newItem')", "array.insert('newItem')"]
]

correct_answers_javascript_code = [
    "let func = function() {}",
    "const add = (a, b) => a + b;",
    "const obj = { name: 'Alex', age: 25 }",
    "array.forEach(item => console.log(item));",
    "array.includes(5)",
    "const { name, age } = obj;",
    "array.push('newItem')"
]
questions_javascript_error = [
    "Unde este eroarea de sintaxă?",
    "În ce linie apare eroarea de tip?",
    "Unde se află eroarea de referință?",
    "Pe ce linie se află eroarea de index?",
    "Unde apare eroarea de funcție nedefinită?",
    "Pe ce linie este eroarea de acces la obiect?",
    "În ce linie este eroarea de scoping?"
]

code_samples_javascript_error = [
    "console.log('Hello World'\nconsole.log('JS Error')",   # Lipsă paranteză închidere
    "let x = 'text' + 5;\nconsole.log(x);",                # Concatenare greșită
    "console.log(y);\nlet y = 10;",                         # Variabilă folosită înainte de declarare
    "let array = [1, 2, 3];\nconsole.log(array[5]);",       # Acces invalid la index
    "myFunction();\nfunction notDeclared() { console.log('Error') }",  # Apelare înainte de definire
    "let obj = { name: 'Alice' };\nconsole.log(obj.age.length);",      # Acces invalid la proprietăți
    "function test() {\n    let x = 10;\n}\nconsole.log(x);"  # Variabilă în afara scoping-ului funcției
]

answers_javascript_error = [
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 2", "Linia 3", "Linia 1", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"]
]

correct_answers_javascript_error = [
    "Linia 1",
    "Linia 1",
    "Linia 1",
    "Linia 2",
    "Linia 1",
    "Linia 2",
    "Linia 3"
]

user_progress = {
    "Python": {"Uranus": 0, "Venus": 0, "Saturn": 0},
    "JavaScript": {"Uranus": 0, "Venus": 0, "Saturn": 0},
    "C++": {"Uranus": 0, "Venus": 0, "Saturn": 0}
}

# Funcție de salvare a progresului în JSON
def save_progress():
    with open("user_progress.json", "w") as f:
        json.dump(user_progress, f, indent=4)

# Funcție de încărcare a progresului din JSON
def load_progress():
    try:
        with open("user_progress.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return user_progress  # Dacă fișierul nu există, folosește progresul inițial
def reset_progress():
    global user_progress
    user_progress = {
        "Python": {"Uranus": 0, "Venus": 0, "Saturn": 0},
        "JavaScript": {"Uranus": 0, "Venus": 0, "Saturn": 0},
        "C++": {"Uranus": 0, "Venus": 0, "Saturn": 0}
    }  # Resetăm progresul

    with open("user_progress.json", "w") as f:
        json.dump(user_progress, f, indent=4)  # Salvăm progresul resetat în fișier

    root.destroy()  # Închidem aplicația după resetare
  # Închidem aplicația după resetare
# Încărcăm progresul utilizatorului
user_progress = load_progress()

# Modificăm `handle_answer()` pentru a înregistra răspunsurile corecte

def show_leaderboard():
    total_correct = sum(correct_count for planets in user_progress.values() for correct_count in planets.values())

    # Determinăm premiul
    if total_correct >= 21:
        award = "🏆 Aur"
    elif total_correct >= 14:
        award = "🥈 Argint"
    elif total_correct >= 7:
        award = "🥉 Bronz"
    else:
        award = "🔹 Fără medalie - mai încearcă!"

    messagebox.showinfo("Leaderboard", f"Premiul tău: {award}\nAi răspuns corect la {total_correct} întrebări!")

# Funcție pentru a afișa progresul utilizatorului
def show_progress():
    progress_message = "Progresul tău:\n"
    for option, planets in user_progress.items():
        progress_message += f"\n{option}:\n"
        for planet, correct_count in planets.items():
            progress_message += f"  {planet}: {correct_count} întrebări corecte\n"
    
    messagebox.showinfo("Progress", progress_message)

    root.protocol("WM_DELETE_WINDOW", reset_progress)
def play_question_video(video_path, question_function, planet_name, selected_option):
    # Creăm o fereastră nouă de ecran complet
    window_video = tk.Toplevel()
    window_video.attributes('-fullscreen', True)  # Setăm fereastra pe ecran complet
    window_video.title("Videoclip")

    # Creăm playerul video
    video_player = TkinterVideo(master=window_video, scaled=True)
    video_player.load(video_path)
    video_player.pack(fill="both", expand=True)

    # Redăm videoclipul automat
    video_player.play()

    # Detectăm când videoclipul s-a terminat
    def on_video_end(event):
        window_video.destroy()  # Închide fereastra videoclipului
        question_function(planet_name, selected_option)  # Revenim la întrebare

    video_player.bind("<<Ended>>", on_video_end)
    # Verificăm manual când videoclipul s-a terminat (pentru cazuri unde `<<Ended>>` nu funcționează)
    def check_video_status():
        if video_player.has_ended():  # Dacă videoclipul s-a terminat
           window_video.destroy()
           question_function(planet_name, selected_option)
        else:
           window_video.after(1000, check_video_status)  # Verificăm periodic

    check_video_status()

# Funcție pentru afișarea paginii cu întrebări
def handle_answer(selected_answer, button, planet_name, selected_option, correct_answer):
    global user_progress, buttons  # Acces la variabilele globale
    
    for btn in buttons:
        btn.config(state="disabled")
    if selected_answer == correct_answer:
        button.config(bg="green")
        
        # Contorizăm răspunsul corect
        if selected_option not in user_progress:
            user_progress[selected_option] = {}
        if planet_name not in user_progress[selected_option]:
            user_progress[selected_option][planet_name] = 0
        
        user_progress[selected_option][planet_name] += 1  # Incrementăm numărul de răspunsuri corecte
        save_progress()  # Salvăm progresul utilizatorului

        play_question_video(r"C:\Users\Adriana\infoeducatie.2-1\WhatsApp Video 2025-05-17 at 22.04.13_3d19574a.mp4", show_question_page, planet_name, selected_option)
    else:
        button.config(bg="red")
        play_question_video(r"C:\Users\Adriana\infoeducatie.2-1\WhatsApp Video 2025-05-17 at 22.12.34_8b843c0c.mp4", show_question_page, planet_name, selected_option)

    # Dezactivăm toate butoanele din listă

def show_question_page(planet_name, selected_option, question, answer_options, correct_answer):
    for widget in root.winfo_children():
        widget.destroy()
    
    bg_image = tk.Label(root, image=grid_image_path)
    bg_image.place(relheight=1, relwidth=1)

    title_label = tk.Label(root, text=question, font=('Gill Sans Ultra Bold', 18), fg='white', bg='#711adf', wraplength=500)
    title_label.pack(pady=20)

    global buttons
    buttons = []  # Inițializăm lista de butoane înainte de crearea lor

    for answer in answer_options:
        btn = tk.Button(root, text=answer, font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451')
        btn.config(command=lambda a=answer, b=btn: handle_answer(a, b, planet_name, selected_option, correct_answer))
        btn.pack(pady=5)
        buttons.append(btn)  # Adăugăm fiecare buton în listă

    # Buton "Înapoi" care revine la pagina de exerciții
    back_button = tk.Button(root, text="Undo", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451',
                            command=lambda: show_new_options_page(planet_name, selected_option))
    back_button.pack(pady=20)


questions_python_b = [
    "Cum declari o funcție în Python?",
    "Cum citești un fișier în Python?",
    "Cum iterăm peste o listă folosind list comprehension?",
    "Cum creezi o clasă în Python?",
    "Cum verifici dacă un element există într-un dicționar?",
    "Cum folosești `try-except` pentru gestionarea erorilor?",
    "Cum sortezi o listă în Python?"
]

answers_python_b = [
    ["def my_function():\n    print('Hello!')", "function my_function():\n    print('Hello!')", "def myFunction() print('Hello!')", "fun my_function():\n    print('Hello!')"],
    ["with open('file.txt', 'r') as f:\n    data = f.read()", "file = open('file.txt', 'r')\n    file.read()", "open('file.txt', 'read')", "readfile('file.txt')"],
    ["[x**2 for x in range(10)]", "for x in range(10):\n    x**2", "[for x in range(10): x**2]", "map(lambda x: x**2, range(10))"],
    ["class MyClass:\n    def __init__(self):\n        self.name = 'Example'", "def MyClass:\n    self.name = 'Example'", "new Class MyClass:\n    name = 'Example'", "class = MyClass()"],
    ["if 'key' in my_dict:", "my_dict.has_key('key')", "my_dict.contains('key')", "my_dict.find('key')"],
    ["try:\n    x = int(input('Număr:'))\nexcept ValueError:\n    print('Eroare!')", "try x = int(input('Număr')) except ValueError: print('Eroare!')", "except ValueError:\n    x = int(input('Număr'))", "catch ValueError:\n    x = int(input('Număr'))"],
    ["sorted(my_list)", "my_list.sort()", "sort(my_list)", "my_list.sorted()"]
]

correct_answers_python_b = [
    "def my_function():\n    print('Hello!')",
    "with open('file.txt', 'r') as f:\n    data = f.read()",
    "[x**2 for x in range(10)]",
    "class MyClass:\n    def __init__(self):\n        self.name = 'Example'",
    "if 'key' in my_dict:",
    "try:\n    x = int(input('Număr:'))\nexcept ValueError:\n    print('Eroare!')",
    "sorted(my_list)"
]

  # Testăm în consolă dacă se transmit
questions_python_c = [
    "În ce linie apare eroarea de indentare?",
    "Unde este eroarea de tip?",
    "Pe ce linie se află eroarea de atribuție?",
    "Unde este eroarea de import?",
    "Pe ce linie este eroarea de index?",
    "Unde este eroarea de sintaxă?",
    "Pe ce linie este eroarea de acces la fișier?"
]

code_samples_python_c = [
    "def my_function():\nprint('Hello!')\n  print('Indentation Error!')",
    "x = 'text' + 5\nprint(x)",
    "a, b = (1, 2, 3)\nprint(a, b)",
    "import non_existent_module\nprint('This should fail')",
    "my_list = [1, 2, 3]\nprint(my_list[5])",
    "print('Hello'\nprint('World')",
    "with open('missing_file.txt', 'r') as f:\n    data = f.read()"
]

answers_python_c = [
    ["Linia 2", "Linia 3", "Linia 1", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 2", "Linia 3", "Linia 1", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"],
    ["Linia 1", "Linia 2", "Linia 3", "Nicio eroare"]
]

correct_answers_python_c = [
    "Linia 2",
    "Linia 1",
    "Linia 1",
    "Linia 1",
    "Linia 2",
    "Linia 1",
    "Linia 1"
]
def handle_answer(selected_answer, button, planet_name, selected_option, correct_answer):
    global user_progress, buttons  # Acces la variabilele globale
    
    for btn in buttons:
        btn.config(state="disabled")
    if selected_answer == correct_answer:
        button.config(bg="green")
        
        # Contorizăm răspunsul corect
        if selected_option not in user_progress:
            user_progress[selected_option] = {}
        if planet_name not in user_progress[selected_option]:
            user_progress[selected_option][planet_name] = 0
        
        user_progress[selected_option][planet_name] += 1  # Incrementăm numărul de răspunsuri corecte
        save_progress()  # Salvăm progresul utilizatorului

        play_question_video(r"C:\Users\Adriana\infoeducatie.2-1\WhatsApp Video 2025-05-17 at 22.04.13_3d19574a.mp4", show_question_page, planet_name, selected_option)
    else:
        button.config(bg="red")
        play_question_video(r"C:\Users\Adriana\infoeducatie.2-1\WhatsApp Video 2025-05-17 at 22.12.34_8b843c0c.mp4", show_question_page, planet_name, selected_option)
       
def show_question_page_with_code(planet_name, selected_option,question, code_sample, answer_options, correct_answer):
    """Afișează codul și permite utilizatorului să aleagă unde este eroarea."""
    for widget in root.winfo_children():
        widget.destroy()
    bg_image = tk.Label(root, image=grid_image_path)
    bg_image.place(relheight=1, relwidth=1)

    title_label = tk.Label(root, text=question, font=('Gill Sans Ultra Bold', 18), fg='white', bg='#711adf', wraplength=500)
    title_label.pack(pady=20)

    code_label = tk.Label(root, text=code_sample, font=('Courier', 14), fg='white', bg='#180451', justify="left")
    code_label.pack(pady=20)
    global buttons
    buttons = []
    for answer in answer_options:
        btn = tk.Button(root, text=answer, font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451')
        btn.config(command=lambda a=answer, b=btn: handle_answer(a, b, planet_name, selected_option, correct_answer))
        btn.pack(pady=5)
        buttons.append(btn)

    back_button = tk.Button(root, text="Undo", font=('Gill Sans Ultra Bold', 15), fg='white', bg='#180451', command=lambda: show_new_options_page(planet_name, selected_option))
    back_button.pack(pady=20)


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
    user_data = load_user_data()  # Adăugat pentru acces la datele utilizatorului

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


settings_button = tk.Button(
    root,
    text="Settings",
    font=('Gill Sans Ultra Bold', 15),
    fg='white',
    bg='#180451',
    command=open_settings_window
)
settings_button.pack(pady=20)
def save_credentials(username, password, email):
    file_path = r"C:\Users\Adriana\Desktop\grid\credentials.txt"
    try:
       with open(file_path, "a") as file:
        file.write(f"Username: {username}, Email: {email}, Password: {password}\n")
       print("Parola a fost salvată cu succes!")  # Mesaj de confirmare
    except Exception as e:
       print(f"Eroare la salvarea parolei: {e}") 
 # Mesaj de eroare
def send_email_confirmation(user_email):
    sender_email = "your-email@example.com"
    sender_password = "your-email-password"

    msg = MIMEText(f"Hello {user_email}, your account has been successfully created!")
    msg["Subject"] = "Confirmation Email"
    msg["From"] = sender_email
    msg["To"] = user_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


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
