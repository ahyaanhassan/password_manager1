import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list=password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    new_data={website:{
                 "email":email,
                 "password":password,

            }
    }
    if len(website)==0:
        messagebox.showinfo(title="OOPS",message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json","r") as data_file:
            #Reading old Data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            #Updating old data 
            data.update(new_data)
            with open("data.json","w") as data_file:
            #Saving new data
                json.dump(new_data,data_file,indent=4)

        finally:
                website_input.delete(0,END)
                password_input.delete(0,END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website=website_input.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="NO data file Found.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\npassword:{password}")

        else:
            messagebox.showinfo(title="Error",message=f"No Details for {website} exist.")
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")

email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

website_input=Entry(width=21)
website_input.grid(column=1,row=1,columnspan=1)
website_input.focus()


email_input=Entry(width=39)
email_input.insert(0,"hassanahyaan0@gmail.com")
email_input.grid(column=1,row=2,columnspan=2)


password_input=Entry(width=21)
password_input.grid(column=1,row=3)

generate_password_button=Button(text="Generate_Password",command=generate_password)
generate_password_button.grid(column=2,row=3)



search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

canvas = Canvas(height=200,width=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)


window.mainloop()