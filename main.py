from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import time
import datetime
import os
import threading
import winsound

class App:
    def __init__(self, master):
        self.master = master
        self.tabControl = ttk.Notebook(self.master)
        self.tab_alarm = ttk.Frame(self.tabControl)
        self.tab_timer = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_alarm, text = 'Alarm')
        self.tabControl.add(self.tab_timer, text = 'Timer')
        self.tabControl.pack(expand = 1, fill = 'both')
        App.Tab_alarm(self)
        App.Tab_timer(self)
        App.Realtime(self)
    
    #alarm tab    
    def Tab_alarm(self):
        #labels
        self.Alarm_Label = Label(self.tab_alarm, text = 'Alarm', fg = 'red', font = ("Helvetica", 18, "bold")).place(x = 170, y = 2)
        self.set_time_Label = Label(self.tab_alarm, text = 'Set time in 24h format (HH : MM : SS):', fg = 'blue', 
                                    font = ("Helvetica", 9, "bold")).place(x = 0, y = 60)
        #variables
        self.hour = IntVar()
        self.minute = IntVar()
        self.second = IntVar()
        #Entries
        self.hourtime = ttk.Entry(self.tab_alarm, textvariable = self.hour, width = 5)
        self.hourtime.place(x = 220, y = 60)
        self.mintime = ttk.Entry(self.tab_alarm, textvariable = self.minute, width = 5)
        self.mintime.place(x = 260, y = 60)
        self.sectime = ttk.Entry(self.tab_alarm, textvariable = self.second, width = 5)
        self.sectime.place(x = 300, y = 60)
        #Alarm time
        self.operation_label = Label(self.tab_alarm, text = 'Operation time:', font = ("Helvetica", 9, "bold")).place(x = 0, y = 90)
        self.time_set = Label(self.tab_alarm)
        self.time_set.place(x = 92, y = 90)
        #Operations
        self.operation_label = Label(self.tab_alarm, text = "Select operation:", font = ("Helvetica", 9, "bold")).place(x = 0, y = 120)
        self.options_Var = StringVar()
        self.options_list = ["Alarm", "Shutdown", "Restart", "Sleep"]
        self.optionmenu = ttk.OptionMenu(self.tab_alarm, self.options_Var, "Select an Option", *self.options_list )
        self.optionmenu.place(x = 110, y = 120)
        #submit & cancel button
        self.alarm_running = True
        self.submit_button = ttk.Button(self.tab_alarm, text = "Submit", command = self.Check_Entry)
        self.submit_button.place(x = 140, y = 180)
        self.cancel_button = ttk.Button(self.tab_alarm, text = "Cancel", command = self.Alarm_cancel)
        self.cancel_button.place(x = 220, y = 180)
    
    #timer tab    
    def Tab_timer(self):
        #labels
        self.label_topic = Label(self.tab_timer, text = 'Timer', fg = 'red', font = ("Helvetica", 18,"bold")).place(x = 170, y = 2)
        self.label_set = Label(self.tab_timer, text = "Hour : min : sec ==>", fg = 'blue', font = ("Helvetica", 9,"bold")).place(x = 0, y = 60)
        #variables
        self.hourT_Var = IntVar()
        self.minT_Var = IntVar()
        self.secT_Var = IntVar()
        #Entries
        self.hourT_ent = ttk.Entry(self.tab_timer, textvariable = self.hourT_Var, width = 5)
        self.hourT_ent.place(x = 130, y = 60)
        self.minT_ent = ttk.Entry(self.tab_timer, textvariable = self.minT_Var, width = 5)
        self.minT_ent.place(x = 170, y = 60)
        self.secT_ent = ttk.Entry(self.tab_timer, textvariable = self.secT_Var, width = 5)
        self.secT_ent.place(x = 210, y = 60)
        #countdown button
        self.start_timer_btn = ttk.Button(self.tab_timer, text = "Start", command = lambda: self.Check_Entry(Timer = True))
        self.start_timer_btn.place(x = 260, y = 58)
        self.timer_running = True
        self.cancel_button = ttk.Button(self.tab_timer, text = "Cancel", command = self.Countdown_cancel).place(x = 260, y = 95)
        #Operations
        self.operation_label_T = Label(self.tab_timer, text = "Select operation:", font = ("Helvetica", 9, "bold")).place(x = 0, y = 100)
        self.options_Var_T = StringVar()
        self.optionmenu_T = ttk.OptionMenu(self.tab_timer, self.options_Var_T, "Select an Option", *self.options_list )
        self.optionmenu_T.place(x = 110, y = 100)
        #countdown label
        self.Countdown_Var = StringVar()
        self.Countdown_Var.set("00:00:00")
        self.Countdown_label = Label(self.tab_timer, textvariable = self.Countdown_Var, font = ("Helvetica", 14, "bold"))
        self.Countdown_label.place(x = 155, y = 150)     
    
    #adding clock    
    def Realtime(self):
        self.clock_label = Label(self.master)
        self.clock_label.place(x = 353, y = 280)
        App.Clock(self)
    
    #check clock loop    
    def Clock(self):
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        self.clock_label.config(text = now)
        self.clock_label.after(1000, App.Clock, self)
    
    #by pressing cancel button , countdown stops and resets
    def Countdown_cancel(self):
            self.timer_running = False
            self.start_timer_btn['state'] = 'normal'
            self.Countdown_Var.set("00:00:00")
            self.times = 0
    
    #by pressing cancel button , alarm resets
    def Alarm_cancel(self):
        self.time_set.config(text = "")
        self.alarm_running = False
        self.submit_button ['state'] = 'normal'
    
    #Entries check and timer or alarm starts
    def Check_Entry(self, Timer: bool = False):
        if not Timer:
            try:
                if (self.hour.get() not in range (0, 24)) or (self.minute.get() not in range (0, 60)) or (self.second.get() not in range (0, 60)):
                    msg.showerror("Error", "Wrong entries, please check your inputs.")
                    self.hour.set(0)
                    self.minute.set(0)
                    self.second.set(0)
            except Exception as e:
                msg.showerror("Error", e)
                self.hour.set(0)
                self.minute.set(0)
                self.second.set(0)
            else:
                self.alarm_running = True
                self.submit_button ['state'] = 'disabled'
                set_alarm = f"{self.hour.get():02d}:{self.minute.get():02d}:{self.second.get():02d}"
                self.time_set.config(text = set_alarm)
                threading.Thread(target = lambda : self.Alarm(set_alarm), daemon = True).start()  
        else:
            try:
                if (self.hourT_Var.get() < 0) or (self.minT_Var.get() not in range(0, 60)) or (self.secT_Var.get() not in range(0, 60)):
                    msg.showerror("Error", "Wrong entries, please check your inputs.")
                    self.hourT_Var.set(0)
                    self.minT_Var.set(0)
                    self.secT_Var.set(0)
            except Exception as e:
                msg.showerror("Error", e)
                self.hourT_Var.set(0)
                self.minT_Var.set(0)
                self.secT_Var.set(0)
            else:
                threading.Thread(target = self.Countdown, daemon = True).start() 
    #Alarm function
    def Alarm(self, Time):
        while self.alarm_running:
            time.sleep(1)
            ops = self.options_Var.get()
            if ops == "Select an Option":
                self.options_Var.set("Alarm")
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            if now == Time:
                if ops == 'Alarm':
                    winsound.Beep(1000, 3000)
                    msg.showinfo('Alarm', 'Times Up!')
                    break
                elif ops == 'Shutdown':
                    msg.showwarning('Alarm', 'Shutting down...')
                    os.system("shutdown /s /3")
                elif ops == 'Restart':
                    msg.showwarning('Alarm', 'Restarting...')
                    os.system("shutdown /r /3")
                else:
                    msg.showwarning('Alarm', 'Sleeping...')
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    break
        self.time_set.config(text = "")
        self.submit_button ['state'] = 'normal'       
    #Countdown method for timer
    def Countdown(self):
        self.Times = self.hourT_Var.get()*3600 + self.minT_Var.get()*60 + self.secT_Var.get()
        self.start_timer_btn['state'] = 'disabled'
        self.timer_running = True
        while self.timer_running and self.Times > 0:
            hour, remain = divmod(self.Times, 3600)
            mins, secs = divmod(remain, 60)
            new_time = f"{hour:02d}:{mins:02d}:{secs:02d}"
            self.Countdown_Var.set(new_time)
            time.sleep(1)
            self.Times -= 1
            ops = self.options_Var_T.get()
            if ops == "Select an Option":
                self.options_Var_T.set("Alarm")
            if self.Times == 0:
                self.Countdown_Var.set("00:00:00")
                if ops == 'Alarm':
                    winsound.Beep(1000, 3000)
                    msg.showinfo('Alarm', 'Times Up!')
                elif ops == 'Shutdown':
                    msg.showwarning('Alarm', 'Shutting down...')
                    os.system("shutdown /s /3")
                elif ops == 'Restart':
                    msg.showwarning('Alarm', 'Restarting...')
                    os.system("shutdown /r /3")
                else:
                    msg.showwarning('Alarm', 'Sleeping...')
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        self.start_timer_btn['state'] = 'normal'
        

def main():
    win = Tk()
    win.title("Alarm & Timer")
    win.geometry("400x300")
    win.resizable(False, False)
    app = App(win)
    win.mainloop()
    
if __name__ == '__main__':
    main()