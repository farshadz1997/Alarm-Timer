from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import time
import datetime

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
        #submit button
        self.submit_button = ttk.Button(self.tab_alarm, text = "Submit", command = self.Check_Entry).place(x = 170, y = 180)
        
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
        #countdown label
        self.Countdown_Var = StringVar()
        self.Countdown_label = Label(self.tab_timer, textvariable = self.Countdown_Var, font = ("Helvetica", 14, "bold"))
        self.Countdown_label.place(x = 155, y = 150)
        #countdown button
        self.start_timer_btn = ttk.Button(self.tab_timer, text = "Start", command = lambda: self.Check_Entry(Timer = True)).place(x = 260, y = 58)
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
    #Entries check in this method
    def Check_Entry(self, Timer: bool = False):
        if not Timer:
            if (self.hour.get() not in range (0, 24)) or (self.minute.get() not in range (0, 59)) or (self.second.get() not in range (0, 59)):
                msg.showerror("Error", "Wrong entries, please check your inputs.")
                self.hour.set(0)
                self.minute.set(0)
                self.second.set(0)
            else:
                set_alarm = f"{self.hour.get():02d}:{self.minute.get():02d}:{self.second.get():02d}"
                self.time_set.config(text = set_alarm)
                pass #*TODO: jaye tabe set kardn alarme  
        else:
            if (self.hourT_Var.get() < 0) or (self.minT_Var.get() not in range(0, 59)) or (self.secT_Var.get() not in range(0, 59)):
                msg.showerror("Error", "Wrong entries, please check your inputs.")
                self.hourT_Var.set(0)
                self.minT_Var.set(0)
                self.secT_Var.set(0)
            else:
                pass #*TODO: jaye tabe start countdown
    #Alarm function
    def Alarm(self, time):
        

def main():
    win = Tk()
    win.geometry("400x300")
    app = App(win)
    win.mainloop()
    
if __name__ == '__main__':
    main()