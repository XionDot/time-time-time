import tkinter as tk
from datetime import datetime

# Function to update the time
def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)  # Update every second

# Function to handle key press events
def on_key_press(event):
    if event.keysym == 'Escape':
        root.destroy()

# Create the main window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')


###### FONT : standard arial #######
# Time label
time_label = tk.Label(root, font=('Cascadia Pro ', 300, 'bold'), fg='white', bg='black')
time_label.pack(expand=True)

# Date label
date_label = tk.Label(root, font=('Consolas', 30), fg='white', bg='black', anchor='ne')
date_label.pack(side=tk.TOP, anchor='ne')

# Bind key press events
root.bind('<KeyPress>', on_key_press)

# Start updating the time
update_time()

# Run the application
root.mainloop()
 # type: ignore
