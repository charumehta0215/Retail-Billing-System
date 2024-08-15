from tkinter import *
from tkinter import Tk, Entry
from tkinter import messagebox
import random, os, tempfile, smtplib


def clear():
    bathsoap_ent.delete(0, END)
    facecream_ent.delete(0, END)
    hairspray_ent.delete(0, END)
    hairgel_ent.delete(0, END)
    bodylotion_ent.delete(0, END)
    facewash_ent.delete(0, END)

    daalent.delete(0, END)
    wheatent.delete(0, END)
    teaent.delete(0, END)
    sugarent.delete(0, END)
    riceent.delete(0, END)
    oilent.delete(0, END)

    maazaent.delete(0, END)
    pepsient.delete(0, END)
    spriteent.delete(0, END)
    Frootient.delete(0, END)
    dewent.delete(0, END)

    cocacolaent.delete(0, END)
    bathsoap_ent.delete(0, END)
    facecream_ent.delete(0, END)
    hairspray_ent.delete(0, END)
    hairgel_ent.delete(0, END)
    bodylotion_ent.delete(0, END)
    facewash_ent.delete(0, END)

    daalent.insert(0, 0)
    wheatent.insert(0, 0)
    teaent.insert(0, 0)
    sugarent.insert(0, 0)
    riceent.insert(0, 0)
    oilent.insert(0, 0)

    maazaent.insert(0, 0)
    pepsient.insert(0, 0)
    spriteent.insert(0, 0)
    Frootient.insert(0, 0)
    dewent.insert(0, 0)
    cocacolaent.insert(0, 0)

    cosmetictaxent.delete(0, END)
    grocerytaxent.delete(0, END)
    colddrinktaxent.delete(0, END)

    cosmeticpriceent.delete(0, END)
    grocerypriceent.delete(0, END)
    colddrinkent.delete(0, END)

    name_entry.delete(0, END)
    phn_entry.delete(0, END)

    textarea.delete(1.0, END)


def send_email():
    def send_email():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttis()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = emailtextarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo("Success", 'Bill is successfully sent', parent=root1)
        except:
            messagebox.showerror('Error", "Something went wrong, Please try again', parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')

    else:
        root1 = Toplevel()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0, 0)
        senderFrame = LabelFrame(root1, text="SENDER", font=("arial", 16, "bold"), bg="gray20", relief=GROOVE)
        senderFrame.grid(row=0, column=0)

        senderLabel = Label(senderFrame, text="Sender's Email", font=("arial", 16, "bold"), bg="gray20", fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=("arial", 14, "bold"), bd=2, width=25, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=16, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg="gray20", fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordrEntry = Entry(senderFrame, font=("arial", 14, 'bold'), bd=2, width=25, relief=RIDGE, show='*')
        passwordrEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text="RECIPIENT", font=("arial", 16, "bold"), bd=6, bg="gray20", fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverlabel = Label(recipientFrame, text="Email Address", font=("arial", 16, 'bold'), bg="gray20", fg='white')
        recieverlabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, "bold"), width=23, relief="ridge")
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=("arial", 16, "bold"), bg="gray20", fg="white")
        messageLabel.grid(row=1, column=0, pady=8, padx=10)

        emailtextarea = Text(recipientFrame, font=('arial', 14, "bold"), width=42, height=11, relief="sunken", bd=2)
        emailtextarea.grid(row=2, column=0, padx=10, pady=8, columnspan=2)
        emailtextarea.delete(1.0, END)
        emailtextarea.insert(END, textarea.get(1.0, END).replace('*', '').replace('\t\t\t', '\t\t'))

        sendbutton = Button(recipientFrame, text="SEND", font=("arial", 16, "bold"), bg="gray20", fg="white",
                            command=send_email)
        sendbutton.grid(row=3, column=0, padx=10, pady=8, columnspan=2)


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir("bills/"):
        if i.split('.')[0] == bill_entry.get():
            f = open(f'bills/{i}', "r")
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid bill number')


if not os.path.exists('bills'):
    os.mkdir('bills')


# for bill

def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'Bill number{billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def bill_area():
    textarea.delete(1.0, END)
    if name_entry.get() == '' or phn_entry.get() == '':
        messagebox.showerror('Error', 'Customer Details are Required')
    elif cosmeticpriceent.get() == '' and grocerypriceent.get() == '' and colddrinkent.get() == '':
        messagebox.showerror('Error', 'No products are selected')
    elif cosmeticpriceent.get() == '0 Rs' and grocerypriceent.get() == '0 Rs' and colddrinkent.get() == '0 Rs':
        messagebox.showerror('Error', 'No products are selected')
    else:
        textarea.insert(END, '  \t  \t**Welcome Customer**\n')
        textarea.insert(END, f'Bill Number:{billnumber}\n')
        textarea.insert(END, f'\nCustomer Name:{name_entry.get()}\n')
        textarea.insert(END, f'\nCustomer phone number:{phn_entry.get()}\n')
        textarea.insert(END, '\n*******************************************************')
        textarea.insert(END, 'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n*******************************************************')

        # cosmetics
        if bathsoap_ent.get() != '0':
            textarea.insert(END, f'\nBath soap\t\t\t{bathsoap_ent.get()}\t\t\t{bathsoapprice}Rs')
        if facecream_ent.get() != '0':
            textarea.insert(END, f'\nFacecream\t\t\t{facecream_ent.get()}\t\t\t{facecreamprice}Rs')
        if facewash_ent.get() != '0':
            textarea.insert(END, f'\nFacewash\t\t\t{facewash_ent.get()}\t\t\t{facewashprice}Rs')
        if hairspray_ent.get() != '0':
            textarea.insert(END, f'\nHair spray\t\t\t{hairspray_ent.get()}\t\t\t{hairsprayprice}Rs')
        if hairgel_ent.get() != '0':
            textarea.insert(END, f'\nHair gel\t\t\t{hairgel_ent.get()}\t\t\t{hairgelprice}Rs')
        if bodylotion_ent.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotion_ent.get()}\t\t\t{bodylotionprice}Rs')
        # grocery
        if riceent.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceent.get()}\t\t\t{riceprice}Rs')
        if oilent.get() != '0':
            textarea.insert(END, f'\noil\t\t\t{oilent.get()}\t\t\t{oilprice}Rs')
        if daalent.get() != '0':
            textarea.insert(END, f'\nDaal\t\t\t{daalent.get()}\t\t\t{daalprice}Rs')
        if wheatent.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatent.get()}\t\t\t{wheatprice}Rs')
        if sugarent.get() != '0':
            textarea.insert(END, f'\nsugar\t\t\t{sugarent.get()}\t\t\t{sugarprice}Rs')
        if teaent.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaent.get()}\t\t\t{teaprice}Rs')
        # colddrinks
        if maazaent.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaent.get()}\t\t\t{Maazaprice}Rs')
        if pepsient.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsient.get()}\t\t\t{pepsiprice}Rs')
        if spriteent.get() != '0':
            textarea.insert(END, f'\nsprite\t\t\t{spriteent.get()}\t\t\t{spriteprice}Rs')
        if dewent.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dewent.get()}\t\t\t{dewprice}Rs')
        if Frootient.get() != '0':
            textarea.insert(END, f'\nFrooti\t\t\t{Frootient.get()}\t\t\t{frootiprice}Rs')
        if cocacolaent.get() != '0':
            textarea.insert(END, f'\nCoca cola\t\t\t{cocacolaent.get()}\t\t\t{cocacolaprice}Rs')
        textarea.insert(END, '\n*******************************************************')
        if cosmetictaxent.get() != '0.0 Rs':
            textarea.insert(END, f'\n Cosmetic Tax\t\t{cosmetictaxent.get()}')
        if grocerytaxent.get() != '0.0 Rs':
            textarea.insert(END, f'\n Grocery Tax\t\t{grocerytaxent.get()}')
        if colddrinktaxent.get() != '0.0 Rs':
            textarea.insert(END, f'\n Cosmetic Tax\t\t{colddrinktaxent.get()}')
        textarea.insert(END, '\n*******************************************************')
        textarea.insert(END, f'\n\n\nTotal Bill \t\t\t\t {totalbill}')
        textarea.insert(END, '\n*******************************************************')
        save_bill()


# for total
# cosmetic price
def total():
    global totalbill
    global bathsoapprice, facecreamprice, facewashprice, hairsprayprice, hairgelprice, bodylotionprice

    bathsoapprice = int(bathsoap_ent.get()) * 20
    facecreamprice = int(facecream_ent.get()) * 50
    facewashprice = int(facewash_ent.get()) * 100
    hairsprayprice = int(hairspray_ent.get()) * 150
    hairgelprice = int(hairgel_ent.get()) * 80
    bodylotionprice = int(bodylotion_ent.get()) * 60

    Total_cosmetic_Price = bathsoapprice + facewashprice + facecreamprice + hairgelprice + hairsprayprice + bodylotionprice
    cosmeticpriceent.delete(0, END)
    cosmeticpriceent.insert(0, f'{Total_cosmetic_Price} Rs')
    cosmeticpricetax = Total_cosmetic_Price * 0.18
    cosmetictaxent.delete(0, END)
    cosmetictaxent.insert(0, f'{cosmeticpricetax}Rs')

    # grocery price
    global riceprice, oilprice, daalprice, wheatprice, sugarprice, teaprice
    riceprice = int(riceent.get()) * 30
    oilprice = int(oilent.get()) * 90
    daalprice = int(daalent.get()) * 130
    wheatprice = int(wheatent.get()) * 70
    sugarprice = int(sugarent.get()) * 80
    teaprice = int(teaent.get()) * 110

    Total_grocery_Price = riceprice + oilprice + daalprice + wheatprice + sugarprice + teaprice
    grocerypriceent.delete(0, END)
    grocerypriceent.insert(0, f'{Total_grocery_Price} Rs')
    grocerytaxlabel = Total_grocery_Price * 0.08
    grocerytaxent.delete(0, END)
    grocerytaxent.insert(0, f'{grocerytaxlabel}Rs')

    # colddrinks price
    global Maazaprice, pepsiprice, spriteprice, dewprice, frootiprice, cocacolaprice
    Maazaprice = int(maazaent.get()) * 20
    pepsiprice = int(pepsient.get()) * 20
    spriteprice = int(spriteent.get()) * 40
    dewprice = int(dewent.get()) * 20
    frootiprice = int(Frootient.get()) * 30
    cocacolaprice = int(cocacolaent.get()) * 20

    Total_colddrinks_price = Maazaprice + pepsiprice + spriteprice + dewprice + frootiprice + cocacolaprice
    colddrinkent.delete(0, END)
    colddrinkent.insert(0, f'{Total_colddrinks_price} Rs')
    colddrinktaxlabel = Total_colddrinks_price * 0.09
    colddrinktaxent.delete(0, END)
    colddrinktaxent.insert(0, f'{colddrinktaxlabel}Rs')
    totalbill = Total_cosmetic_Price + Total_grocery_Price + Total_colddrinks_price + cosmeticpricetax + grocerytaxlabel + colddrinktaxlabel


# gui
root = Tk()

root.title("Retail billing system")
root.geometry('1400x900')
root.resizable(0, 0)
root.iconbitmap('icon.ico')
lbl = Label(root, text='Retail billing system', font=('algeria', 30, 'bold'), bg='GRAY20', fg='gold', bd=12,
            relief=GROOVE)
lbl.pack(fill=X, pady=10)
customer_details_frame = LabelFrame(root, text='Customer details', font=('algeria', 15), bg='GRAY20', fg='gold', bd=20,
                                    )
customer_details_frame.pack(fill=X)
name_label = Label(customer_details_frame, text='Name', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12, fg='white')
name_label.grid(row=0, column=0, padx=20)
Bill_number = Label(customer_details_frame, text='Bill number', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                    fg='white')
Bill_number.grid(row=0, column=4, padx=20)
phn_no = Label(customer_details_frame, text='Phone Number', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
               fg='white')
phn_no.grid(row=0, column=2, padx=20)
name_entry = Entry(customer_details_frame, bd=7, width=18)
name_entry.grid(row=0, column=1, padx=20)
bill_entry = Entry(customer_details_frame, bd=7, width=18)
bill_entry.grid(row=0, column=5, padx=20)
phn_entry = Entry(customer_details_frame, bd=7, width=18)
phn_entry.grid(row=0, column=3, padx=20)
btn = Button(customer_details_frame, text='SEARCH', font=('algeria', 12, 'bold'), bd=8, width=10, command=search_bill)
btn.grid(row=0, column=12, padx=20, pady=8)
products_frame = Frame(root)
products_frame.pack(fill=X)
cosmetics_labelframe = LabelFrame(products_frame, text='Cosmetics', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                                  fg='white')
cosmetics_labelframe.grid(row=0, column=0, pady=9, padx=10)
bathsoap_label = Label(cosmetics_labelframe, text='Bath soap', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                       fg='white')
bathsoap_label.grid(row=0, column=0, pady=9, padx=10)
bathsoap_ent = Entry(cosmetics_labelframe, bd=7, width=18)
bathsoap_ent.grid(row=0, column=1, pady=9, padx=10)
bathsoap_ent.insert(0, 0)
facecream_label = Label(cosmetics_labelframe, text='Facecream', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                        fg='white')
facecream_label.grid(row=1, column=0, pady=9, padx=10)
facecream_ent = Entry(cosmetics_labelframe, bd=7, width=18)
facecream_ent.grid(row=1, column=1, pady=9, padx=10)
facecream_ent.insert(0, 0)
facewash_label = Label(cosmetics_labelframe, text='Face wash', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                       fg='white')
facewash_label.grid(row=2, column=0, pady=9, padx=10)
facewash_ent = Entry(cosmetics_labelframe, bd=7, width=18)
facewash_ent.grid(row=2, column=1, pady=9, padx=10)
facewash_ent.insert(0, 0)

hairspray_label = Label(cosmetics_labelframe, text='Hair spray', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                        fg='white')
hairspray_label.grid(row=3, column=0, pady=9, padx=10)
hairspray_ent = Entry(cosmetics_labelframe, bd=7, width=18)
hairspray_ent.grid(row=3, column=1, pady=9, padx=10)
hairspray_ent.insert(0, 0)

hairgel_label = Label(cosmetics_labelframe, text='Hair gel', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                      fg='white')
hairgel_label.grid(row=4, column=0, pady=9, padx=10)
hairgel_ent = Entry(cosmetics_labelframe, bd=7, width=18)
hairgel_ent.grid(row=4, column=1, pady=9, padx=10)
hairgel_ent.insert(0, 0)
bodylotion_label = Label(cosmetics_labelframe, text='Body Lotion', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                         fg='white')
bodylotion_label.grid(row=5, column=0, pady=9, padx=10)
bodylotion_ent = Entry(cosmetics_labelframe, bd=7, width=18)
bodylotion_ent.grid(row=5, column=1, pady=9, padx=10)
bodylotion_ent.insert(0, 0)

grocerylabelframe = LabelFrame(products_frame, text='Grocery', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                               fg='white')
grocerylabelframe.grid(row=0, column=1, pady=9, padx=10)
ricelabel = Label(grocerylabelframe, text='Rice', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                  fg='white')
ricelabel.grid(row=0, column=0, pady=9, padx=10)
riceent = Entry(grocerylabelframe, bd=7, width=18)
riceent.grid(row=0, column=1, pady=9, padx=10)
riceent.insert(0, 0)
oillabel = Label(grocerylabelframe, text='Oil', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                 fg='white')
oillabel.grid(row=1, column=0, pady=9, padx=10)
oilent = Entry(grocerylabelframe, bd=7, width=18)
oilent.grid(row=1, column=1, pady=9, padx=10)
oilent.insert(0, 0)
daallabel = Label(grocerylabelframe, text='Daal', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                  fg='white')
daallabel.grid(row=2, column=0, pady=9, padx=10)
daalent = Entry(grocerylabelframe, bd=7, width=18)
daalent.grid(row=2, column=1, pady=9, padx=10)
daalent.insert(0, 0)
wheatlabel = Label(grocerylabelframe, text='Wheat', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                   fg='white')
wheatlabel.grid(row=3, column=0, pady=9, padx=10)
wheatent = Entry(grocerylabelframe, bd=7, width=18)
wheatent.grid(row=3, column=1, pady=9, padx=10)
wheatent.insert(0, 0)
sugarlabel = Label(grocerylabelframe, text='Sugar', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                   fg='white')
sugarlabel.grid(row=4, column=0, pady=9, padx=10)
sugarent = Entry(grocerylabelframe, bd=7, width=18)
sugarent.grid(row=4, column=1, pady=9, padx=10)
sugarent.insert(0, 0)
tealabel = Label(grocerylabelframe, text='Tea', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                 fg='white')
tealabel.grid(row=5, column=0, pady=9, padx=10)
teaent = Entry(grocerylabelframe, bd=7, width=18)
teaent.grid(row=5, column=1, pady=9, padx=10)
teaent.insert(0, 0)
colddrinkslabelframe = LabelFrame(products_frame, text='Cold drinks', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                                  fg='white')
colddrinkslabelframe.grid(row=0, column=2, pady=9, padx=10)
maazalabel = Label(colddrinkslabelframe, text='Maaza', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                   fg='white')
maazalabel.grid(row=0, column=0, pady=9, padx=10)
maazaent = Entry(colddrinkslabelframe, bd=7, width=18)
maazaent.grid(row=0, column=1, pady=9, padx=10)
maazaent.insert(0, 0)
pepsilabel = Label(colddrinkslabelframe, text='Pepsi', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                   fg='white')
pepsilabel.grid(row=1, column=0, pady=9, padx=10)
pepsient = Entry(colddrinkslabelframe, bd=7, width=18)
pepsient.grid(row=1, column=1, pady=9, padx=10)
pepsient.insert(0, 0)
spritelabel = Label(colddrinkslabelframe, text='Sprite', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                    fg='white')
spritelabel.grid(row=2, column=0, pady=9, padx=10)
spriteent = Entry(colddrinkslabelframe, bd=7, width=18)
spriteent.grid(row=2, column=1, pady=9, padx=10)
spriteent.insert(0, 0)
dewlabel = Label(colddrinkslabelframe, text='Dew', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                 fg='white')
dewlabel.grid(row=3, column=0, pady=9, padx=10)
dewent = Entry(colddrinkslabelframe, bd=7, width=18)
dewent.grid(row=3, column=1, pady=9, padx=10)
dewent.insert(0, 0)
Frootilabel = Label(colddrinkslabelframe, text='Frooti', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                    fg='white')
Frootilabel.grid(row=4, column=0, pady=9, padx=10)
Frootient = Entry(colddrinkslabelframe, bd=7, width=18)
Frootient.grid(row=4, column=1, pady=9, padx=10)
Frootient.insert(0, 0)
cocacolalabel = Label(colddrinkslabelframe, text='Coka cola', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                      fg='white')
cocacolalabel.grid(row=5, column=0, pady=9, padx=10)
cocacolaent = Entry(colddrinkslabelframe, bd=7, width=18)
cocacolaent.grid(row=5, column=1, pady=9, padx=10)
cocacolaent.insert(0, 0)
bill = Frame(products_frame, bd=8, relief=GROOVE)
bill.grid(row=0, column=3, pady=9, padx=10)
billarea = Label(bill, text='Bill area', font=('algeria', 15, 'bold'), bg='GRAY', bd=7,
                 fg='BLACK', relief=GROOVE)
billarea.pack(fill=X)
scrollbar = Scrollbar(bill, orient=VERTICAL, bd=20)
scrollbar.pack(side="right", fill=Y)

textarea = Text(bill, height=21, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)
billmenulabelframe = LabelFrame(root, text='Bill Menu', font=('algeria', 15, 'bold'), bg='GRAY20', bd=12,
                                fg='white')
billmenulabelframe.pack()
cosmeticpriceLabel = Label(billmenulabelframe, text='Cosmetic Price', font=('algeria', 15, 'bold'), bg='GRAY20', bd=12,
                           fg='white')
cosmeticpriceLabel.grid(row=0, column=0, pady=9, padx=18, sticky='w')
cosmeticpriceent = Entry(billmenulabelframe, bd=7, width=18)
cosmeticpriceent.grid(row=0, column=1, pady=9, padx=10)
cosmetictaxlabel = Label(billmenulabelframe, text='Cosmetic tax', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                         fg='white')
cosmetictaxlabel.grid(row=0, column=2, pady=9, padx=10)
cosmetictaxent = Entry(billmenulabelframe, bd=7, width=18)
cosmetictaxent.grid(row=0, column=3, pady=9, padx=10)
grocerypricelabel = Label(billmenulabelframe, text='Grocery price', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                          fg='white')
grocerypricelabel.grid(row=1, column=0, pady=9, padx=10, )
grocerypriceent = Entry(billmenulabelframe, bd=7, width=18)
grocerypriceent.grid(row=1, column=1, pady=9, padx=10)
grocerytaxlabel = Label(billmenulabelframe, text='Grocery tax', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                        fg='white')
grocerytaxlabel.grid(row=1, column=2, pady=9, padx=10)
grocerytaxent = Entry(billmenulabelframe, bd=7, width=18)
grocerytaxent.grid(row=1, column=3, pady=9, padx=10)
colddrinkpricelabel = Label(billmenulabelframe, text='Cold drink price', font=('algeria', 12, 'bold'), bg='GRAY20',
                            bd=12,
                            fg='white')
colddrinkpricelabel.grid(row=2, column=0, pady=9, padx=10)
colddrinkent = Entry(billmenulabelframe, bd=7, width=18)
colddrinkent.grid(row=2, column=1, pady=9, padx=10)
colddrinktaxlabel = Label(billmenulabelframe, text='Cold drink tax', font=('algeria', 12, 'bold'), bg='GRAY20', bd=12,
                          fg='white')
colddrinktaxlabel.grid(row=2, column=2, pady=9, padx=10)
colddrinktaxent = Entry(billmenulabelframe, bd=7, width=18)
colddrinktaxent.grid(row=2, column=3, pady=9, padx=10)
buttonframe = Frame(billmenulabelframe, bd=8, relief=GROOVE)
buttonframe.grid(row=0, column=4, rowspan=3)
totalbtn = Button(buttonframe, text='TotaL', font=('arial', 16, 'bold'), bg='GRAY20', bd=12,
                  fg='white', width=8, pady=10, command=total)
totalbtn.grid(row=0, column=0, pady=20, padx=5)
billbtn = Button(buttonframe, text='Bill', font=('arial', 16, 'bold'), bg='GRAY20', bd=12,
                 fg='white', width=8, pady=10, command=bill_area)
billbtn.grid(row=0, column=1, pady=20, padx=5)
emailbtn = Button(buttonframe, text='Email', font=('arial', 16, 'bold'), bg='GRAY20', bd=12,
                  fg='white', width=8, pady=10, command=send_email)
emailbtn.grid(row=0, column=3, pady=20, padx=5)
printbtn = Button(buttonframe, text='Print', font=('arial', 16, 'bold'), bg='GRAY20', bd=12,
                  fg='white', width=8, pady=10, command=print_bill)
printbtn.grid(row=0, column=4, pady=20, padx=5, )
clearbtn = Button(buttonframe, text='Clear', font=('arial', 16, 'bold'), bg='GRAY20', bd=12,
                  fg='white', width=8, pady=10, command=clear)
clearbtn.grid(row=0, column=5, pady=20, padx=5)

root.mainloop()
