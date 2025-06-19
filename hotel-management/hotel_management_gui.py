import tkinter as tk
from tkinter import messagebox, ttk
import hotel_management
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("700x500")
def refresh_data():
    show_guests()
    show_rooms()
    root.after(2000, refresh_data)  
def add_guest():
    name = name_entry.get()
    phone = phone_entry.get()
    room = room_entry.get()

    if name and phone and room:
        result = hotel_management.add_guest(name, phone, room)
        messagebox.showinfo("Result", result)
    else:
        messagebox.showwarning("Warning", "All fields are required!")
def remove_guest():
    guest_id = guest_id_entry.get()

    if guest_id:
        result = hotel_management.remove_guest(guest_id)
        messagebox.showinfo("Result", result)
    else:
        messagebox.showwarning("Warning", "Enter a Guest ID to remove.")
def show_guests():
    guests = hotel_management.get_guests()
    guest_list.delete(*guest_list.get_children())

    for guest in guests:
        guest_list.insert("", "end", values=(guest[0], guest[1], guest[2], guest[3]))
def show_rooms():
    rooms = hotel_management.get_rooms()
    room_list.delete(*room_list.get_children())

    for room in rooms:
        room_list.insert("", "end", values=(room[1], room[2]))
tk.Label(root, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Room").grid(row=2, column=0, padx=5, pady=5)
room_entry = tk.Entry(root)
room_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Add Guest", command=add_guest).grid(row=3, column=1, pady=10)

tk.Label(root, text="Remove Guest by ID").grid(row=4, column=0, padx=5, pady=5)
guest_id_entry = tk.Entry(root)
guest_id_entry.grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Remove Guest", command=remove_guest).grid(row=5, column=1, pady=10)
guest_list = ttk.Treeview(root, columns=("ID", "Name", "Phone", "Room"), show="headings")
guest_list.heading("ID", text="ID")
guest_list.heading("Name", text="Name")
guest_list.heading("Phone", text="Phone")
guest_list.heading("Room", text="Room Number")
guest_list.grid(row=6, column=0, columnspan=2, pady=10)
room_list = ttk.Treeview(root, columns=("Room", "Status"), show="headings")
room_list.heading("Room", text="Room Number")
room_list.heading("Status", text="Status")
room_list.grid(row=7, column=0, columnspan=2, pady=10)
refresh_data()
root.mainloop()
