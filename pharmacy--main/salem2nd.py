from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

# دالة لفتح الصفحة التالية بعد الدخول بنجاح
def open_home_page():
    # إنشاء نافذة جديدة بعد تسجيل الدخول بنجاح
    home_window = Toplevel(window)
    home_window.geometry('735x490')
    home_window.resizable(False, False)
    home_window.title("Home Page")

    # إضافة محتوى للصفحة الرئيسية (مثال على ذلك إضافة نص أو عناصر أخرى)
    home_label = Label(home_window, text="Welcome to the Pharmacy System", font=("Goergia", 20), fg="black")
    home_label.place(x=200, y=200)

# دالة التحقق من البيانات عند الضغط على زر "Log In"
def loginButton():
    # التحقق من أن الحقول غير فارغة
    if entry_user.get() == '' or entry_ID.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif entry_user.get() == 'noran nassar' and entry_ID.get() == '241001233':  # التحقق من البيانات
        messagebox.showinfo('Success', 'Login is successful')
        open_home_page()  # فتح الصفحة التالية بعد الدخول بنجاح
    else:
        messagebox.showerror('Error', 'Incorrect credentials')

# إنشاء نافذة تسجيل الدخول
window = Tk()
window.geometry('735x490')
window.resizable(False, False)
window.title("Pharmacy")

# إضافة صورة الخلفية
backgroundImage = ImageTk.PhotoImage(file='background login.png')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

# إطار اللوجو
loginfram = Frame(window)
loginfram.place(x=350, y=40)

logoImage = PhotoImage(file='pharmacist.png')
logoLabel = Label(loginfram, image=logoImage)
logoLabel.grid(row=0, column=0)

# زر "Log In"
loginButton = Button(window, text='Log In', font=("Goergia"), fg='white', bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white', command=loginButton)
loginButton.place(x=360, y=400, width=130, height=40)

# إدخال اسم الموظف
user_label = Label(window, text='Employee Name', font=('Goergia', 15), fg='Gray')
user_label.place(x=240, y=200)
entry_user = Entry(window, bd=0, font=("Goergia", 20))
entry_user.place(x=240, y=230, width=200, height=30)

# إدخال ID الموظف
label1 = Label(window, text='Employee ID', font=('Goergia', 15), fg='Gray')
label1.place(x=240, y=290)
entry_ID = Entry(window, bd=0, font=("Goergia", 20))
entry_ID.place(x=240, y=320, width=200, height=30)

# تشغيل التطبيق
window.mainloop()
