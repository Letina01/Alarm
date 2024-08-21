import time
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from playsound import playsound

def alarm_sound(file):
    print(f"Playing sound: {file}")  # Debug statement
    playsound(file)

def set_alarm(alarm_time, snooze_interval, alarm_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"Current Time: {current_time}, Alarm Time: {alarm_time}")  # Debug statement
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Wake up! It's time!")
            threading.Thread(target=alarm_sound, args=(alarm_file,)).start()

            snooze = messagebox.askyesno("Snooze", "Do you want to snooze?")
            if snooze:
                snooze_time = time.time() + snooze_interval * 60
                while time.time() < snooze_time:
                    pass
                messagebox.showinfo("Snooze Over", "Snoozing over! It's time again!")
                threading.Thread(target=alarm_sound, args=(alarm_file,)).start()
            break
        time.sleep(1)

def browse_file():
    file_path = filedialog.askopenfilename(title="Select Alarm Tone", filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        alarm_file_entry.delete(0, tk.END)
        alarm_file_entry.insert(0, file_path)

def start_alarm():
    alarm_time = time_entry.get()
    snooze_interval = int(snooze_entry.get())
    alarm_file = alarm_file_entry.get()
    
    if alarm_time and snooze_interval and alarm_file:
        # Show notification that alarm has been set
        messagebox.showinfo("Alarm Set", f"Alarm set successfully for {alarm_time}")
        
        threading.Thread(target=set_alarm, args=(alarm_time, snooze_interval, alarm_file)).start()

        # Clear the input fields after setting the alarm
        time_entry.delete(0, tk.END)
        snooze_entry.delete(0, tk.END)
        alarm_file_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields and select an alarm tone.")

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Time input
time_label = tk.Label(root, text="Enter Time (HH:MM:SS):")
time_label.pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

# Snooze interval input
snooze_label = tk.Label(root, text="Enter Snooze Interval (minutes):")
snooze_label.pack(pady=5)
snooze_entry = tk.Entry(root)
snooze_entry.pack(pady=5)

# Alarm tone selection
alarm_file_label = tk.Label(root, text="Select Alarm Tone:")
alarm_file_label.pack(pady=5)
alarm_file_entry = tk.Entry(root, width=40)
alarm_file_entry.pack(pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# Start alarm button
start_button = tk.Button(root, text="Set Alarm", command=start_alarm)
start_button.pack(pady=20)

# Run the main loop
root.mainloop()
