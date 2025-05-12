
def Level_selecter(option):
    for widget in root.winfo_children():
        widget.destroy()

    # Background for planet buttons
    canvas = Canvas(root)
    canvas.place(relwidth=1, relheight=1)

    # Load and play video as background
    videoplayer = TkinterVideo(master=canvas, scaled=True)
    videoplayer.load(r" ")  # Replace with your video file path // WIll do later
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    # Loop the video after it ends
    videoplayer.bind("<<Ended>>", lambda e: videoplayer.play())

    # Example planet images
    level_images = {
        "Level A": PhotoImage(file=r" "),
        "Level B": PhotoImage(file=r" "),
        "Level C": PhotoImage(file=r" "),
        "Level D": PhotoImage(file=r" "),
        "Level E": PhotoImage(file=r" "),
        "Level F": PhotoImage(file=r" "),
    }

    # Add planet buttons directly on the background image
    order = 0; # FOR BUTTON ORDER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for level_name, level_image in level_images.items():
        level_button = tk.Button(
            root,
            image=level_image,
            command=lambda name=level_name: show_new_options_page(name),  # Navigate to new options page
            borderwidth=0,
            bg='#711adf',
            activebackground='#711adf'
        )
        level_button.image = level_image  # Keep a reference
        level_button.place( )  # WILL CALCULATE LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Undo button
    message_label = tk.Label(root, text=f"You selected {option}. Explore planets below!", font=('Gill Sans Ultra Bold', 20), fg='#1b219d', bg='#711adf')
    message_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    undo_button = tk.Button(
        root,
        text="Go Back",
        font=('Gill Sans Ultra Bold', 12),
        fg='white',
        bg='#180451',
        command=on_submit
    )
    undo_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)



def Level():
    for widget in root.winfo_children():
        widget.destroy()

    # Background for planet buttons
    canvas = Canvas(root)
    canvas.place(relwidth=1, relheight=1)

    # Load and play video as background
    videoplayer = TkinterVideo(master=canvas, scaled=True)
    videoplayer.load(r" ")  # Replace with your video file path // WIll do later
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    # Loop the video after it ends
    videoplayer.bind("<<Ended>>", lambda e: videoplayer.play())

    # NEED TO FIND OUT HOW TO READ AN EXCES FOR QUESTIONS

    level_images = {
        "Answer 1": PhotoImage(file=r" "),
        "Answer 2": PhotoImage(file=r" "),
        "Answer 3": PhotoImage(file=r" "),
        "Answer 4": PhotoImage(file=r" "),
    }



    # Add planet buttons directly on the background image
    column = 0
    
    for HUI, HUI_image in HUI_image.items():
        HUI_button = tk.Button(
            root,
            image=HUI_image,
            command=lambda name=HUI: show_new_options_page(name),  # Navigate to new options page ??????????
            borderwidth=0,
            bg='#711adf',
            activebackground='#711adf'
        )
        HUI_button.image = HUI_image  # Keep a reference
        HUI_button.place(relx=0.3 + (column * 0.2), rely=0.5, anchor=tk.CENTER)  # Adjust placement
        column += 1
    
    label = tk.Label(settings_window, text=" ", font=('Gill Sans Ultra Bold', 20), fg='#1b219d', bg='#711adf')  # NEED VARIABLE FOR QUESTION
    label.pack(pady=20)
    
    for level_name, level_image in level_images.items():
        level_button = tk.Button(
            root,
            image=level_image,
            command=lambda name=level_name: show_new_options_page(name),  # Navigate to new options page
            borderwidth=0,
            bg='#711adf',
            activebackground='#711adf'
        )
        level_button.image = level_image    
    
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