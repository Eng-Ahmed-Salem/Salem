from tkinter import *
from PIL import ImageTk



window =Tk()
window.geometry('735x490')
window.resizable(False,False)
window.title("logo")



backgroundImage=ImageTk.PhotoImage(file='logo.png')
bgLabel=Label(window,image=backgroundImage) 
bgLabel.place(x=0,y=-230)





loginfram=Frame(window)
loginfram.place(x=230,y=280)
logoImage=PhotoImage(file='logo 2.png')
logoLabel=Label(loginfram,image=logoImage)
logoLabel.grid(row=0,column=0)




loginButton=Button(window,text='Log In',font=("Goergia"),fg='white',bg='#70BBFE',activebackground='#70BBFE',activeforeground='white')
loginButton.place(x=530,y=420,width=150,height=50)


signupButton=Button(window,text='Sign up',font=("Goergia"),fg='white',bg='#70BBFE',activebackground='#70BBFE',activeforeground='white')
signupButton.place(x=330,y=420,width=150,height=50)



window.mainloop()  