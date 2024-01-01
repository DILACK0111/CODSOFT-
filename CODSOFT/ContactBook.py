import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, index):
        del self.contacts[index]

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact

    def search_contacts(self, search_term):
        search_results = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone):
                search_results.append(contact)
        return search_results

    def get_contact_list(self):
        return self.contacts

class ContactApp:
    def __init__(self, root):
        self.contact_manager = ContactManager()
        self.root = root
        self.root.title("Contact Manager")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label_name = tk.Label(self.frame, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=0, column=1)

        self.label_phone = tk.Label(self.frame, text="Phone:")
        self.label_phone.grid(row=1, column=0)
        self.entry_phone = tk.Entry(self.frame)
        self.entry_phone.grid(row=1, column=1)

        self.label_email = tk.Label(self.frame, text="Email:")
        self.label_email.grid(row=2, column=0)
        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=2, column=1)

        self.label_address = tk.Label(self.frame, text="Address:")
        self.label_address.grid(row=3, column=0)
        self.entry_address = tk.Entry(self.frame)
        self.entry_address.grid(row=3, column=1)

        self.button_add = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, columnspan=2)

        self.button_view = tk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=5, columnspan=2)

        self.search_var = tk.StringVar()
        self.entry_search = tk.Entry(self.frame, textvariable=self.search_var)
        self.entry_search.grid(row=6, column=0)

        self.button_search = tk.Button(self.frame, text="Search", command=self.search_contact)
        self.button_search.grid(row=6, column=1)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=7, columnspan=2)

        self.button_update = tk.Button(self.frame, text="Update", command=self.update_contact)
        self.button_update.grid(row=8, column=0)

        self.button_delete = tk.Button(self.frame, text="Delete", command=self.delete_contact)
        self.button_delete.grid(row=8, column=1)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contact_manager.add_contact(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Name and Phone number are required.")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        contacts = self.contact_manager.get_contact_list()
        for index, contact in enumerate(contacts):
            self.listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = self.search_var.get()
        if search_term:
            search_results = self.contact_manager.search_contacts(search_term)
            self.listbox.delete(0, tk.END)
            for contact in search_results:
                self.listbox.insert(tk.END, f"{contact.name} - {contact.phone}")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def update_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            contact_index = selected_index[0]
            name = self.entry_name.get()
            phone = self.entry_phone.get()
            email = self.entry_email.get()
            address = self.entry_address.get()

            if name and phone:
                updated_contact = Contact(name, phone, email, address)
                self.contact_manager.update_contact(contact_index, updated_contact)
                self.clear_entries()
                self.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully.")
            else:
                messagebox.showwarning("Warning", "Name and Phone number are required.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            contact_index = selected_index[0]
            self.contact_manager.delete_contact(contact_index)
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
