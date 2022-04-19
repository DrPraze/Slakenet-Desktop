from tkinter import ttk
from tkinter import *
from ttkbootstrap import Style, widgets
import PIL, webbrowser
from wallet import Wallet
from tkinter.messagebox import showerror

style = Style(theme="superhero")
win = style.master

win.title("Slakenet")
win.geometry("400x500")
win.resizable(False, False)

slakes = "935.027"
def welcome():
	global logo
	welcome_label = Label(win, text = "Welcome to Slakenet", font = ("Helvetica"), foreground = "yellow")
	welcome_label.place(x = 2, y = 2)
	label = Label(win, text = "Login/Signup", font = ('Algerian', 36), foreground = 'white', width = 13)
	label.place(x = 2, y = 20)

	logo = PIL.ImageTk.PhotoImage(PIL.Image.open("banner.jpg"))

	banner = Label(win, image = logo)
	banner.place(x = 8, y = 70)
	login = ttk.LabelFrame(win, text = "Login", width = 150, height = 150)
	login.place(x = 22, y = 310)
	IDlabel = Label(login, text = 'wallet ID:', font = ('Helvetica', 16)).grid(row = 1, column = 0)
	wallet_ID = Entry(login, width= 30, font = ('Calibri', 12))
	wallet_ID.grid(row = 1, column = 1)
	password_label = Label(login, text = 'Password: ', font = ('Helvetica', 16)).grid(row  = 3, column = 0)
	Password = Entry(login, width = 30, show = '*', font = ('Calibri', 12)).grid(row = 3, column = 1)

	btn_label = ttk.LabelFrame(login, width = 128, height = 55)
	btn_label.grid(row = 5, column = 1)	
	btn = ttk.Button(btn_label, text = "Login", style = "primary.Outline.TButton",
		command = lambda :[Authenticate(wallet_ID.get())])
	btn.place(x = 2, y = 2)
	btn1 = ttk.Button(btn_label, text = "Sign up", style = "primary.Outline.TButton",
		command = None)
	btn1.place(x = 60, y = 2)

	btn2 = Button(login, text = 'forgot password...', font = ('Calibri', 10, 'italic'), foreground = 'blue', relief = FLAT, command = None)
	btn2.grid(row = 7, column = 1)

def Authenticate(user):
	if Wallet(user).load_keys()[0] == True:
		print(Wallet(user).load_keys()[1], "\n\n", Wallet(user).load_keys()[2])
		GUI(slakes)
	else:
		showerror("An Error Occured", "Something is invalid")
		# GUI(slakes)#temporary until prototype is ready for deploy testing

def Signup():
	pass
	
def GUI(slakes):
	TabControl = ttk.Notebook(win)
	tab1 = ttk.Frame(TabControl)
	tab2 = ttk.Frame(TabControl)
	tab3 = ttk.Frame(TabControl)
	TabControl.add(tab1, text = "Home")
	TabControl.add(tab2, text = "Earn")
	TabControl.add(tab3, text = "Tools")
	TabControl.pack(fill = "both", expand = 1)

	transact_label = ttk.LabelFrame(tab1, width = 163, height = 51)
	transact_label.place(x = 120, y = 30)
	buy_btn = ttk.Button(transact_label, text = "Buy slakes", style = "primary.Outline.TButton",
		command = None)
	buy_btn.place(x = 2, y = 0)
	sell_btn = ttk.Button(transact_label, text = "Sell slakes", style = "primary.Outline.TButton",
		command = None)
	sell_btn.place(x = 83, y = 0)
	funds_label = Label(tab1, text = f"Slakes: {slakes}\n User: Admin\n Data: 900 GB")
	#Edit The username above
	funds_label.place(x = 300, y = 5)

	Plans_frame = ttk.LabelFrame(tab1, text = "Data Plans", width = 200, height = 270)
	Plans_frame.place(x = 2, y = 100)

	Contact_frame = ttk.LabelFrame(tab1, text = "Contact", width = 130, height = 150)
	Contact_frame.place(x = 260, y = 100)

	friend_frame = ttk.LabelFrame(Contact_frame, text = "ID", width = 120, height = 60)
	friend_frame.place(x = 3, y = 1)

	friend = Entry(friend_frame, width = 17)
	friend.place(x = 5, y = 1)

	view_btn1= ttk.Button(Contact_frame, text="View Profile", style  = "primary.Outline.TButton")
	view_btn1.place(x = 20, y = 51)

	Connect_btn = ttk.Button(tab1, text = "Connect to Slakenet",
		style = "primary.Outline.TButton", command = None)
	Connect_btn.place(x = 260, y = 255)

	Aboutbtn = Button(tab1, text = "About Slakenet",
		relief = "flat", font=("Helvetica", 12, "underline"),
		command = lambda x:[webbrowser.open("drpraze.github.io/about.html")])
	Aboutbtn.place(x = 2, y = 400)
	Reportbtn = Button(tab1, text = "Report a problem.",
		relief = "flat", font=("Helvetica", 12, "underline"),
		command = lambda x:[webbrowser.open("drpraze.github.io/contact.html")])
	Reportbtn.place(x = 122, y = 400)
	FAQbtn = Button(tab1, text = "FAQs.",
		relief = "flat", font = ("Helvetica", 12, "underline"))
	FAQbtn.place(x = 260, y = 400)
	Policybtn = Button(tab1, text = "Policies.",
		relief = "flat", font = ("Helvetica", 12, "underline"))
	Policybtn.place(x = 319, y = 400)

welcome()
if __name__ == '__main__':
	win.mainloop()