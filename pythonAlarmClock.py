#All the imports
import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading

#Function: Set Alarm
def set_alarm():

    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
    messagebox.showinfo("Alarm", "Time to wake up!")

#Function: Start Alarm
def start_alarm_thread():
    t = threading.Thread(target=set_alarm)
    t.start()

#Use of tkinter
# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and place the widgets
tk.Label(root, text="Set Alarm Time (24-hour format)").pack()

frame = tk.Frame(root)
frame.pack()

hour = tk.StringVar(root)
minute = tk.StringVar(root)
second = tk.StringVar(root)

tk.Entry(frame, textvariable=hour, width=3).pack(side=tk.LEFT)
tk.Label(frame, text=":").pack(side=tk.LEFT)
tk.Entry(frame, textvariable=minute, width=3).pack(side=tk.LEFT)
tk.Label(frame, text=":").pack(side=tk.LEFT)
tk.Entry(frame, textvariable=second, width=3).pack(side=tk.LEFT)

tk.Button(root, text="Set Alarm", command=start_alarm_thread).pack()

# Run the application
root.mainloop()
