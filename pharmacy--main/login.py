from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk



window =Tk()

window.geometry('735x490')
window.resizable(False,False)
window.title("pharmacy")



#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------
#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------
#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------

backgroundImage=ImageTk.PhotoImage(file='background login.png')


bgLabel=Label(window,image=backgroundImage) 

bgLabel.place(x=0,y=0)






#-------------------------------------------
#-------------------------------------------
#-------------------------------------------


#------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
def loginButton():

                  if  entry_user.get() == '' or  entry_ID.get() == '':
                      messagebox.showerror('Error','all fields are required')

                  elif entry_user.get() == ('noran nassar') and entry_ID.get() == ('241001233'):
                      messagebox.showinfo('success','login is successful')
                  else:
                      messagebox.showerror('it is wrong')
    







loginfram=Frame(window)
loginfram.place(x=350,y=40)


logoImage=PhotoImage(file='pharmacist.png')

logoLabel=Label(loginfram,image=logoImage)
logoLabel.grid(row=0,column=0)

loginButton=Button(window,text='Log In',font=("Goergia"),fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white')
loginButton.place(x=360,y=400,width=130,height=40)
########################################################  employee Entry ###############################################################

user_label  = Label(window,text='Employee Name', font=('Goergia', 15),fg='Gray')
user_label.place(x=240,y=200)



entry_user = Entry(window, bd=0 ,font=("Goergia", 20))  
entry_user.place(x=240, y=230, width=200, height=30) 

#----------------------------------------------------------------------------------------------------------------------------------

########################################################  employee ID Entry ###############################################################

label1  = Label(window,text='Employee ID', font=('Goergia', 15),fg='Gray')
label1.place(x=240,y=290)

# Add the entry widget on top of the image
entry_ID = Entry(window, bd=0,font=("Goergia", 20))  
entry_ID.place(x=240, y=320, width=200, height=30)  
#----------------------------------------------------------------------------------------------------------------------------------








#----------------------------------------------------------------------------------------------------------------------------------





window.mainloop()  