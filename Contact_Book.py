from tkinter import *
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.contacts = [] 
        self.root = root
        self.root.title("Contact Manager")
        
        form_frame = Frame(self.root)
        form_frame.pack(pady=10) 
        

        Label(form_frame, text="Store Name").grid(row=0, column=0, padx=5, pady=5)
        self.store_name = Entry(form_frame)
        self.store_name.grid(row=0, column=1, padx=5, pady=5)
        
        Label(form_frame, text="Phone Number").grid(row=1, column=0, padx=5, pady=5)
        self.phone_no = Entry(form_frame)
        self.phone_no.grid(row=1, column=1, padx=5, pady=5)
        
        Label(form_frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
        self.email = Entry(form_frame)
        self.email.grid(row=2, column=1, padx=5, pady=5)
        
        Label(form_frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
        self.address = Entry(form_frame)
        self.address.grid(row=3, column=1, padx=5, pady=5)
        
        
        Button(form_frame, text="Add Contact", command=self.add_contact).grid(row=4, column=0, pady=10)
        Button(form_frame, text="Update Contact", command=self.update_contact).grid(row=4, column=1, pady=10)
        Button(form_frame, text="Delete Contact", command=self.delete_contact).grid(row=4, column=2, pady=10)
        

        list_frame = Frame(self.root)
        list_frame.pack(pady=10)
        
        self.contact_lb = Listbox(list_frame, width=50, height=10)
        self.contact_lb.grid(row=0, column=0, padx=10, pady=10)
        self.contact_lb.bind('<<ListboxSelect>>', self.load_selected_contact)
        
    
        Label(self.root, text="Search by Name or Phone").pack(pady=5)
        self.search_cont = Entry(self.root)
        self.search_cont.pack(pady=5)
        Button(self.root, text="Search", command=self.search_contact).pack(pady=5)
        
    def add_contact(self):
        
        contact = {
            "name": self.store_name.get(),
            "phone": self.phone_no.get(),
            "email": self.email.get(),
            "address": self.address.get()
        }
        self.contacts.append(contact)
        self.update_contact_listbox()
        self.clear_form()
        
    def update_contact_listbox(self):
    
        self.contact_lb.delete(0, END)
        for contact in self.contacts:
            self.contact_lb.insert(END, f"{contact['name']} - {contact['phone']}")
    
    def load_selected_contact(self, event):
        
        selection = self.contact_lb.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]
            self.store_name.delete(0, END)
            self.store_name.insert(0, contact["name"])
            self.phone_no.delete(0, END)
            self.phone_no.insert(0, contact["phone"])
            self.email.delete(0, END)
            self.email.insert(0, contact["email"])
            self.address.delete(0, END)
            self.address.insert(0, contact["address"])
    
    def update_contact(self):
        
        selection = self.contact_lb.curselection()
        if selection:
            index = selection[0]
            self.contacts[index] = {
                "name": self.store_name.get(),
                "phone": self.phone_no.get(),
                "email": self.email.get(),
                "address": self.address.get()
            }
            self.update_contact_listbox()
            self.clear_form()
        else:
            messagebox.showwarning("Update Contact", "No contact selected to update.")
    
    def delete_contact(self):
        
        selection = self.contact_lb.curselection()
        if selection:
            index = selection[0]
            del self.contacts[index]
            self.update_contact_listbox()
            self.clear_form()
        else:
            messagebox.showwarning("Delete Contact", "No contact selected to delete.")
    
    def search_contact(self):
        search_query = self.search_cont.get()
        if search_query:
            filtered_contacts = [c for c in self.contacts if search_query in c["name"] or search_query in c["phone"]]
            self.contact_lb.delete(0, END)
            for contact in filtered_contacts:
                self.contact_lb.insert(END, f"{contact['name']} - {contact['phone']}")
        else:
            self.update_contact_listbox()
    
    def clear_form(self):
        
        self.store_name.delete(0, END)
        self.phone_no.delete(0, END)
        self.email.delete(0, END)
        self.address.delete(0, END)


root = Tk()
app = ContactManager(root)

root.configure(background="#D3D3D3")   
Button(text="Close",command=root.destroy,width=7,font ="Arial 10 bold").pack(pady=20)
root.mainloop()
