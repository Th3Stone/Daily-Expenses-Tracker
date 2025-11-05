from tkinter import *
from tkinter import ttk
import datetime as dt
from mydb import *
from tkinter import messagebox
print('completed')
data = database(db='myexpenses.db')

#global variables
count= 0
selected_rowid = 0

def saveRecord():
    global data 
    data.insertRecord(item_name.get(), item_price=item_amt.get(), purchase_date=transaction_date.get())


def fetch_records():
    f = data.fetchRecord('Select rowid, * from expense_record')
    global count
    for rec in f:
        tv.insert(parent='' , index='0' , iid=count , values=(rec[0], rec[1], rec[2], rec[3]))
        count += 1
    tv.after(400, refreshData)

def refreshData():
    for item in tv.get_children():
        tv.delete(item)
    fetch_records()


def selectRecord(event):
    global selected_rowid
    selected = tv.focus()
    val = tv.item(selected, 'values')

    try:
        selected_rowid = val[0]
        d = val[3]
        namevar.set(val[1])
        amtvar.set[val[2]]
        dopvar.set(str(d))
    except Exception as ep:
        pass


def setDate():
    date = dt.datetime.now()
    dopvar.set(f'{date:%d %B %Y}')

def clearEntries():
    item_name.delete(0, "end")
    item_amt.delete(0, "end")
    transaction_date.delete(0, "end")

def totalBalance():
    f = data.fetchRecord(query="Select sum(item_price) from expense_record")
    for i in f:
        for j in i:
            messagebox.showinfo('Current Balance: ', f"Total Expense: ' {j} \nBalance Remaining: {1500 - j}" )

def update_record():
    global selected_rowid 
    global data
    
    selected = tv.focus()

    try:
        data.updateRecord(namevar.get(), amtvar.get(), dopvar.get(), selected_rowid)
        tv.item(selected, text='', values=(namevar.get(), amtvar.get(), dopvar.get()))
    except Exception as ep:
        messagebox.showerror('Error', ep)

    item_name.delete(0, "end")
    item_amt.delete(0, "end")
    transaction_date.delete(0, "end")
    tv.after(400, refreshData)

def deleteRow():
    global selected_rowid
    data.removeRecord(selected_rowid)
    refreshData()

ws = Tk()
ws.title('Daily Expenses')

# Variables
f = ('poppins', 14)
namevar= StringVar()
amtvar = IntVar()
dopvar = StringVar()

#Frame 
f2 = Frame(ws)
f2.pack()

f1 = Frame(
    ws,
    padx= 10,
    pady = 10,
)
f1.pack(expand= True, fill=BOTH)

# Lables 
Label(f1, text='Item Name', font=f).grid(row=0,column=0, sticky=W)
Label(f1, text='Item Price', font=f).grid(row=1,column=0, sticky=W)
Label(f1, text='Purchase Date', font=f).grid(row=2,column=0, sticky=W)

#Entries 

item_name = Entry(f1, font=f, textvariable=namevar)
item_amt = Entry(f1, font=f, textvariable=amtvar)
transaction_date = Entry(f1, font=f, textvariable=dopvar)

#gid design

item_name.grid(row=0, column=1, sticky=EW, padx=(10,0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10,0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10,0))

#Buttons
cur_date = Button(
    f1,
    text = 'Current Date',
    font=f,
    bg='#04c4d9',
    command= setDate,
    width=15
)

submit_btn = Button(
    f1,
    text = 'Add',
    font=f,
    bg='#42602D',
    command=saveRecord,
    fg='white'
    )

clear_btn = Button(
    f1,
    text='Clear Entry',
    font=f,
    command=clearEntries,
    bg='#D9B036',
    fg='white'
)

quit_btn = Button(
    f1,
    text='Exit',
    font=f,
    command=lambda:ws.destroy(),
    bg='#D33532',
    fg='white'
)

total_bal = Button(
    f1,
    text='Total Balance',
    font=f,
    command=totalBalance,
    bg='#486966',
    fg='white'
)

update_btn = Button(
    f1,
    text='Update/Edit',
    font=f,
    command=update_record,
    bg='#C2BB00',
)

del_btn = Button(
    f1,
    text='Delete',
    font=f,
    command=deleteRow,
    bg='#BD2A2E',
)

#Button Display
cur_date.grid(row=2, column=2, sticky=EW, padx=5, pady=5)
submit_btn.grid(row=0, column=2, sticky=EW, padx=5, pady=5)
clear_btn.grid(row=1, column=2, sticky=EW, padx=5, pady=5)
update_btn.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
total_bal.grid(row=3, column=1, sticky=EW, padx=5, pady=5)
del_btn.grid(row=3, column=2, sticky=EW, padx=5, pady=5)
quit_btn.grid(row=4, column=0, columnspan=3, sticky=EW, padx=5, pady=5)

# TreeView
tv = ttk.Treeview(f2, columns=(1,2,3,4), show= 'headings', height=8)
tv.pack(side='left')

tv.column(1, anchor=CENTER, stretch=NO, width=70)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)
tv.column(4, anchor=CENTER)
tv.heading(1, text= 'Item No')
tv.heading(2, text= 'Item Name')
tv.heading(3, text= 'Item Price')
tv.heading(4, text= 'Purchase Date')

tv.bind('<ButtonRelease-1>', selectRecord)


style = ttk.Style()
style.theme_use('default')
style.map('Treeview')

scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill='y')
tv.config(yscrollcommand=scrollbar.set)

fetch_records()

ws.mainloop()