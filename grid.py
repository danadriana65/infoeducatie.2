import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()

root.geometry('500x600')
root.title('Welcome to app!')
# root.configure(bg='red')
image_path=PhotoImage(file=r"C:\Users\Adriana\Desktop\grid\WhatsApp Image 2025-02-19 at 10.59.07_7ae9aa3c.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)

container = tk.Frame(bg_image)
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Configurăm greutățile pentru rânduri și coloane în container
for i in range(2):
    container.grid_rowconfigure(i, weight=1)
for i in range(3):
    container.grid_columnconfigure(i, weight=1)
user_label = tk.Label(bg_image,text='Username',font=('Gill Sans Ultra Bold',16),fg='#1b219d',bg='#711adf')
user_label.grid(row=0,column=0,padx=5,pady=5)

username = tk.Entry(bg_image,font=('Stencil',16),fg='white',bg='#180451')
username.grid(row=0,column=1,padx=5,pady=5)

user_password = tk.Label(bg_image,text='Password',font=('Gill Sans Ultra Bold',16),fg='#1b219d',bg='#711adf')
user_password.grid(row=1,column=0,padx=5,pady=5)

password = tk.Entry(bg_image,font=('Stencil',16),fg='white',bg='#180451',show='.')
password.grid(row=1,column=1,padx=10,pady=10)

submit = tk.Button(bg_image,text='Submit',font=('Gill Sans Ultra Bold',12),fg='white',bg='#180451')
submit.grid(row=2,column=1,sticky= tk.E + tk.W)


bg_image.grid_propagate(False)

root.mainloop()