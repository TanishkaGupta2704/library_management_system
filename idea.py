import tkinter as tk

# Global variable to keep track of the popup window
popup_open = False

def show_popup(notification_text):
    global popup_open
    
    # Check if popup is already open, if yes, return
    if popup_open:
        return
    
    # Set flag to indicate popup is open
    popup_open = True
    
    # Create a popup window
    popup = tk.Toplevel(root)
    popup.geometry("200x100")
    popup.title("Notification Details")
    
    # Function to close popup and reset flag
    def close_popup():
        global popup_open
        popup_open = False
        popup.destroy()
    
    # Display the notification text
    notification_label = tk.Label(popup, text=notification_text)
    notification_label.pack(pady=10)
    
    # Bind the popup window to close when mouse leaves
    popup.bind("<Leave>", lambda event: close_popup())

def create_notification(notification_text, row):
    # Create the notification label
    notification_label = tk.Label(root, text=notification_text, bg="lightgray", padx=10, pady=5)
    notification_label.grid(row=row, column=0, sticky="w")
    
    # Bind the hover event to show the popup
    notification_label.bind("<Enter>", lambda event, notification_text=notification_text: show_popup(notification_text))

# Create the main Tkinter window
root = tk.Tk()
root.geometry("300x200")
root.title("Notification Popup")

# Create 5 notifications
notifications = [
    "Notification 1",
    "Notification 2",
    "Notification 3",
    "Notification 4",
    "Notification 5"
]

# Create notifications and corresponding popups
for i, notification_text in enumerate(notifications, start=1):
    create_notification(notification_text, i-1)

root.mainloop()