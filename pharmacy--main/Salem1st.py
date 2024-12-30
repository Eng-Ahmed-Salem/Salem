from tkinter import *
from PIL import ImageTk, Image


def open_login():
    login_window = Toplevel(window)
    login_window.geometry('400x300')
    login_window.title("Log In")

    Label(login_window, text="User Name", font=("Arial", 12)).pack(pady=10)
    entry_username = Entry(login_window, font=("Arial", 12))
    entry_username.pack(pady=5)

    Label(login_window, text="Password", font=("Arial", 12)).pack(pady=10)
    entry_password = Entry(login_window, show="*", font=("Arial", 12))
    entry_password.pack(pady=5)

    Button(login_window, text="Enter", font=("Arial", 12), command=lambda: print("Login successful")).pack(pady=20)


def open_signup():
    signup_window = Toplevel(window)
    signup_window.geometry('400x300')
    signup_window.title("Sign Up")

    Label(signup_window, text="User Name", font=("Arial", 12)).pack(pady=10)
    entry_username = Entry(signup_window, font=("Arial", 12))
    entry_username.pack(pady=5)

    Label(signup_window, text="Password", font=("Arial", 12)).pack(pady=10)
    entry_password = Entry(signup_window, show="*", font=("Arial", 12))
    entry_password.pack(pady=5)

    Label(signup_window, text="Confirm Password", font=("Arial", 12)).pack(pady=10)
    entry_confirm_password = Entry(signup_window, show="*", font=("Arial", 12))
    entry_confirm_password.pack(pady=5)

    Button(signup_window, text="Sign Up", font=("Arial", 12), command=lambda: print("Sign up successful")).pack(pady=20)

window = Tk()
window.state('zoomed')
window.title("User System")

background_image = Image.open("back2.png") 
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)  
background_image = ImageTk.PhotoImage(background_image)

bg_label = Label(window, image=background_image)
bg_label.place(relwidth=1, relheight=1)  


logo_frame = Frame(window, bg="#ffffff", bd=2)
logo_frame.place(relx=0.5, rely=0.2, anchor=CENTER)  


logo_image = Image.open('MD logo.png')
logo_image = logo_image.resize((200, 200), Image.LANCZOS)  
logo_image = ImageTk.PhotoImage(logo_image)

logo_label = Label(logo_frame, image=logo_image, bg="white")
logo_label.pack()

login_button = Button(window, text='Log In', font=("Georgia", 14), fg='white', bg='#1A73E8', activebackground='#1A73E8', activeforeground='white', command=open_login)
login_button.place(relx=0.55, rely=0.75, anchor=CENTER, width=150, height=50)

signup_button = Button(window, text='Sign up', font=("Georgia", 14), fg='white', bg='#1A73E8', activebackground='#1A73E8', activeforeground='white', command=open_signup)
signup_button.place(relx=0.45, rely=0.75, anchor=CENTER, width=150, height=50)

window.mainloop()
