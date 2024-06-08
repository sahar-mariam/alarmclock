import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from playsound import playsound

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_time_obj = datetime.strptime(alarm_time, '%H:%M:%S')
        current_time = datetime.now().strftime('%H:%M:%S')
        while current_time != alarm_time:
            current_time = datetime.now().strftime('%H:%M:%S')
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Wake up!")
                play_alarm()  # Call function to play the alarm sound continuously
                break
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please enter time in HH:MM:SS format.")

def play_alarm():
    # Continuously play the alarm sound until the stop button is clicked
    while True:
        playsound('/home/sahar/Downloads/alarm.wav')  # Replace 'alarm_sound.wav' with your audio file
        root.update()  # Update the Tkinter window to handle button click events

def stop_alarm():
    # Function to stop the alarm
    messagebox.showinfo("Alarm Stopped", "You stopped the alarm.")
    root.quit()  # Quit the Tkinter application

# Create GUI
root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (HH:MM:SS):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button_set = tk.Button(root, text="Set Alarm", command=set_alarm)
button_set.pack()

button_stop = tk.Button(root, text="Stop Alarm", command=stop_alarm)
button_stop.pack()

root.mainloop()
