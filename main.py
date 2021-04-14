import os
from tkinter import *
from tkinter import ttk
import time
import datetime
from tkinter import messagebox as msg
import threading

# Alarm function
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        operation = sp.get()
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            if operation == 'Alarm':
                msg.showinfo('Alarm', 'Times up!')
            elif operation == 'Shutdown':
                msg.showwarning('Alarm',
                                       'Shutting down...')
                os.system("shutdown /s /t")
            elif operation == 'Restart':
                msg.showwarning('Alarm', 'Restaring...')
                os.system("shutdown /r /t")
            else:
                msg.showwarning('Alarm', 'Sleeping...')
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            pass

# check entries for true values
def check_entry():
    if (hour.get() not in range (0, 24)) or (Min.get() not in range (0, 59)) or (sec.get() not in range (0, 59)):
        msg.showerror("Error","Wrong entries!")
        hourtime.delete(0,END)
        hour.set(0)
        mintime.delete(0,END)
        Min.set(0)
        sectime.delete(0,END)
        sec.set(0)
    else:
        actual_time()

# add time for operation
def actual_time():
    set_alarm_timer = f"{hour.get():02d}:{Min.get():02d}:{sec.get():02d}"
    time_set.config(text=set_alarm_timer)
    alarm(set_alarm_timer)

# real time clock
def real_time():
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    time_update.config(text = now)
    time_update.after(1000, real_time)

def run():
    threading.Thread(target=check_entry, daemon=True).start()

win = Tk()
win.title("Alarm")
win.geometry("400x200")
win.resizable(False,False)
#tab control
tabControl = ttk.Notebook(win)
tab_alarm = ttk.Frame(tabControl)
tab_timer = ttk.Frame(tabControl)
tabControl.add(tab_alarm, text= 'Alarm')
tabControl.add(tab_timer, text = 'Timer')
tabControl.pack(expand = 1, fill = "both")

#labels
time_format = Label(tab_alarm, text="Enter time in 24 hour format!", fg="red", bg="black"
                    , font="Times")
time_format.place(x = 110, y = 120)
addtime = Label(tab_alarm, text = "Hour   Min     Sec", font = 60).place(x = 110)
set_your_alarm = Label(tab_alarm, text = "when to operate: ", fg= "blue", relief = "solid",
                     font = ("Helvetica", 9, "bold")).place(x = 0, y = 29)

# Variables for entries
hour = IntVar()
Min = IntVar()
sec = IntVar()
# Entries
hourtime = Entry(tab_alarm, textvariable = hour, bg = "pink", width = 15)
hourtime.place(x = 110, y = 30)
mintime = Entry(tab_alarm, textvariable = Min, bg = "pink", width = 15)
mintime.place(x = 150, y = 30)
sectime = Entry(tab_alarm, textvariable = sec, bg = "pink", width = 15)
sectime.place(x = 200, y = 30)

# submit button
submit = ttk.Button(tab_alarm, text = "Submit", command = run)
submit.place(x = 255, y = 90)

# Real time Label
time_update = Label(tab_alarm)
time_update.place(x = 353, y = 180)
real_time()

# Alarm time
operation_label = Label(tab_alarm, text = 'operation time:', font = ("Helvetica", 9, "bold"))
operation_label.place(x = 0, y = 60)
time_set = Label(tab_alarm)
time_set.place(x = 90, y = 60)

# spin box
spin_label = Label(tab_alarm, text = 'Select Operation: ',
                   font = ("Helvetica", 9, "bold"))
spin_label.place(x = 0, y = 90)
spin_Vars = StringVar()
spin_Vars.set('Alarm')
sp = ttk.Spinbox(tab_alarm, values=('Shutdown', 'Restart', 'Sleep', 'Alarm'),
                 textvariable=spin_Vars, state='readonly')
sp.place(x = 110, y = 92)

win.mainloop()