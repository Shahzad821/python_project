from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_=[choice(letters) for _ in range(randint(8,10))]
    numbers_=[choice(numbers) for _ in range(randint(2,4))]
    symbols_=[choice(symbols) for _ in range(randint(2,4))]

    password_list = letters_ + symbols_ + numbers_
    shuffle(password_list)
    pasword="".join(password_list)
    password_entry.insert(0,pasword)
    pyperclip.copy(pasword)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website=website_entry.get()
    email=user_name_entry.get()
    password=password_entry.get()
    new_data={
        website: {
            "email":email,
            "password":password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="please make sure you do not have left anything empty.")
    else:
    
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
       
# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website__=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website__ in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website__, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website__} exists.")




# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas=Canvas(width=200,height=200)
logo_pic=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_pic)
canvas.grid(column=1,row=0)
# Labels
website=Label(text="Website:",font=("Arial",10,"bold"))
website.grid(column=0,row=1)
user_name=Label(text="Email/Username:",font=("Arial",10,"bold"))
user_name.grid(column=0,row=2)
password=Label(text="Password:",font=("Arial",10,"bold"))
password.grid(column=0,row=3)
# Entry
website_entry=Entry(width=32)
website_entry.grid(column=1,row=1)
website_entry.focus()
user_name_entry=Entry(width=43)
user_name_entry.grid(column=1,row=2,columnspan=2)
user_name_entry.insert(0,"shahzad@gmail.com")
password_entry=Entry(width=32)
password_entry.grid(column=1,row=3)
# Buttons
search_button=Button(text="Search",width=7,command=find_password)
search_button.grid(column=2,row=1)
generate_button=Button(text="Generate",width=7,command=generate_password)
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)
window.mainloop()