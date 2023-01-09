from tkinter import *
# just fonts
import tkinter.font as tkFont
# to run shell scripts
import subprocess
# library for the icons
from PIL import ImageTk, Image
# library for messageboxes
from tkinter import messagebox
# lib to handle errors
import sys

# definition of clicked used with radiobuttons
def clicked(n):
	return

# just the parameters
root = Tk()
root.title(" By: Joseph")
root.geometry("345x120")
#root.iconphoto(False, PhotoImage(file='icons/icon.png'))
root.configure(bg="grey")

# font styles
fontStyle = tkFont.Font(family="Lucida Grande", size=7)
titleFont = tkFont.Font(family="Lucida Grande", size=10)

# frame for the radiobuttons
left_frame = LabelFrame(root, text="Type of Execution", pady=24)
left_frame.grid(row=0, column=0)

# frame for the dropdown and entry
middle_frame = LabelFrame(root, text="Timing Options", padx=20, pady=11)
middle_frame.grid(row=0, column=1)

# frame for the start button
right_frame = LabelFrame(root, text="Ready?", padx=15, pady=16)
right_frame.grid(row=0, column=2)

# frame for current time
#clock_frame = LabelFrame(root, text="Current Time", padx=25, pady=15)
#clock_frame.grid(row=0, column=3)

# frame for labels the and the language sellection
lower_frame = LabelFrame(root, padx=20, pady=20)
lower_frame.grid(row=1, column=0, columnspan=3)

# variables
boot_type = StringVar()

# subprocess for reboot
def rebt(theTime):
	t = str(theTime)

	cmd = 'shutdown /r /t ' + t
	return subprocess.call(cmd, shell=False)

# subprocess for shutdown
def shtdwn(theTime):
	t = str(theTime)
	
	cmd = 'shutdown /s /t ' + t
	return subprocess.call(cmd, shell=False)

# subprocess to stop all existing shutdown processes
def stop():
	cmd = 'shutdown /a'
	
	return subprocess.call(cmd, shell=False)

# the definition of start, when everything is set
def start():

	rp1 = IntVar()
	value = ent.get()
	try:
		value = int(value)
	except ValueError:
		messagebox.showerror("Error!", "The value of this entry must be an integer.")
	rValue = r.get()

	if(rValue == 1): #restart
		rp1 = messagebox.askyesno("Caution!", "Before the timer starts, please make sure all your files are saved! Ready?")
		if(rp1 == 1):
			if value >= 0:
				if selected.get() == "Seconds":
					time_remaining = value
					
				elif selected.get() == "Minutes":
					time_remaining = (value * 60)
					
				elif selected.get() == "Hours":
					time_remaining = (value * 3600)
					
				elif selected.get() == "Days":
					time_remaining = (value * 86400)
				#clock(time_remaining)
				rebt(time_remaining)
			else:
				messagebox.showerror("Error!", "The value of the entry must be positive.")	


	elif(rValue == 2): #shutdown
		rp1 = messagebox.askyesno("Caution!", "Before the timer starts, please make sure all your files are saved! Ready?")
		if(rp1 == 1):
			if value >= 0:
				if selected.get() == "Seconds":
					time_remaining = value
					
				elif selected.get() == "Minutes":
					time_remaining = (value * 60)
					
				elif selected.get() == "Hours":
					time_remaining = (value * 3600)
					
				elif selected.get() == "Days":
					time_remaining = (value * 86400)
				#clock(time_remaining)
				shtdwn(time_remaining)
			else:
				messagebox.showerror("Error!", "The value of the entry must be positive.")
	else:
		messagebox.showerror("Error!", "Select a type of execution!")

# actual radiobuttons
r = IntVar()
Radiobutton(left_frame, text="Restart", variable=r, value=1).pack(anchor=W)
Radiobutton(left_frame, text="Shutdown", variable=r ,value=2).pack(anchor=W)
# Radiobutton(left_frame, text="Restart twice", variable=r, value=3, command=lambda:clicked(r.get())).pack()

# a custom entry
instruct = Label(middle_frame, text="Instert value", font=fontStyle)
instruct.grid(row=0, column=0, sticky=N)
value = IntVar(root)
ent = Entry(middle_frame, width=15, borderwidth=5, justify=CENTER)
ent.insert(0, "0")
#ent.insert(0, "0")
ent.grid(row=1, column=0, sticky=N)
# ent.place(x=0, y=21, height=29)

# the predefined droopdown menu
selected = StringVar(root)
selected.set("Seconds")

quantities = OptionMenu(middle_frame, selected, "Seconds", "Minutes", "Hours", "Days")
quantities.grid(row=2, column=0, sticky=N)
quantities.config(width=10)

'''
clockwatch = Label(lower_frame, font=('Arial', 12), fg="Red")
clockwatch.pack()

def clock(a):

	days = a // 86400
	a -= days * 86400
	hours = a // 3600
	a -= hours * 3600
	mins = a // 60
	a -= mins * 60
	secs = a 
	a -= 1
	clockwatch.config(text="Remaining: " + str(days) + "DD" + str(hours) + "HH" + str(mins) + "MM" + str(secs) + "SS")
	clockwatch.after(1000, clock(a))
'''

# the "firestarter"
strt_btn = Button(right_frame, text="Start", command=start, padx=11, pady=5)
strt_btn.grid(row=0, column=0, sticky=N)

# the exit
stp_btn = Button(right_frame, text="Stop", command=stop, padx=11, pady=5)
stp_btn.grid(row=2, column=0, sticky=S)

root.mainloop()
