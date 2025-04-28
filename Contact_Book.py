import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x400")

# List to store contacts
contacts = []

# Function to add contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:  # Make sure name and phone are provided
        messagebox.showerror("Error", "Name and Phone are required!")
        return
    
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    view_contacts()

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to view all contacts
def view_contacts():
    listbox_contacts.delete(0, tk.END)  # Clear current listbox items
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for a contact
def search_contact():
    search_query = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if search_query in contact["Name"].lower() or search_query in contact["Phone"]:
            listbox_contacts.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to update contact
def update_contact():
    selected_contact_index = listbox_contacts.curselection()
    if selected_contact_index:
        contact = contacts[selected_contact_index[0]]
        contact["Name"] = entry_name.get() if entry_name.get() else contact["Name"]
        contact["Phone"] = entry_phone.get() if entry_phone.get() else contact["Phone"]
        contact["Email"] = entry_email.get() if entry_email.get() else contact["Email"]
        contact["Address"] = entry_address.get() if entry_address.get() else contact["Address"]
        
        messagebox.showinfo("Success", "Contact updated successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Select a contact to update.")

# Function to delete a contact
def delete_contact():
    selected_contact_index = listbox_contacts.curselection()
    if selected_contact_index:
        contact = contacts.pop(selected_contact_index[0])
        messagebox.showinfo("Success", f"Contact '{contact['Name']}' deleted successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Select a contact to delete.")

# UI Elements

# Contact Details Section
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root)
entry_address.pack()

# Add Contact Button
button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.pack(pady=10)

# Search Section
tk.Label(root, text="Search by Name or Phone").pack()
entry_search = tk.Entry(root)
entry_search.pack()

button_search = tk.Button(root, text="Search", command=search_contact)
button_search.pack(pady=5)

# Contacts List Section
listbox_contacts = tk.Listbox(root, width=40, height=10)
listbox_contacts.pack(pady=10)

# Update and Delete Buttons
button_update = tk.Button(root, text="Update Contact", command=update_contact)
button_update.pack(pady=5)

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
button_delete.pack(pady=5)

# View Contacts Button (to refresh contact list)
button_view = tk.Button(root, text="View All Contacts", command=view_contacts)
button_view.pack(pady=10)

# Run the application
root.mainloop()
