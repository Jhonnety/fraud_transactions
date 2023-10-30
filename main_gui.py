import tkinter as tk
from result_gui import show_result
from model_info import about_model
import fraudulent_transactions

def clear_fields():
    type_operations.set("CASH IN")
    entry_transaction.delete(0, tk.END)
    entry_step.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_oldbalanceOrg.delete(0, tk.END)
    entry_newbalanceOrig.delete(0, tk.END)
    entry_oldbalanceDest.delete(0, tk.END)
    entry_newbalanceDest.delete(0, tk.END)
    alert.delete(0, tk.END)

def check_transaction():
    
    if(entry_transaction.get() == "" or entry_step.get() == "" or type_operations.get() == "" or entry_amount.get() == "" or entry_newbalanceOrig.get() == "" or entry_newbalanceOrig.get() == "" or entry_oldbalanceDest.get() == "" or entry_newbalanceDest.get() == ""):
        alert.set("Fill out all fields")
    else:
        try:
            
            transaction = entry_transaction.get()
            step = float(entry_step.get())
            type_transfer = type_operations.get()
            amount = float(entry_amount.get())
            oldbalanceOrg = float(entry_oldbalanceOrg.get())
            newbalanceOrig = float(entry_newbalanceOrig.get())
            oldbalanceDest = float(entry_oldbalanceDest.get())
            newbalanceDest = float(entry_newbalanceDest.get())
            CASH_IN = 0
            CASH_OUT = 0
            DEBIT = 0
            PAYMENT = 0
            TRANSFER = 0
            
            if( type_transfer == 'CASH IN' ):
                CASH_IN = 1
            elif( type_transfer == 'CASH OUT' ):
                CASH_OUT = 1
            elif( type_transfer == 'DEBIT' ):
                DEBIT = 1
            elif( type_transfer == 'PAYMENT' ):
                PAYMENT = 1
            else:  
                TRANSFER = 1
            
            isFraud = fraudulent_transactions.isFraud([
            step, 
            CASH_IN, 
            CASH_OUT,
            DEBIT,
            PAYMENT, 
            TRANSFER, 
            amount, 
            oldbalanceOrg, 
            newbalanceOrig, 
            oldbalanceDest, 
            newbalanceDest
            ])
            
            if isFraud:
                result = f"The transaction with the ID: {transaction} is fraudulent. Be careful"
            else:
                result = f"The transaction with the ID: {transaction} is valid."
            
            show_result(transaction, step, type_transfer, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, result)
        

        except ValueError:
            alert.set("Error: The entries are invalid")


window = tk.Tk()
window.title("Fraud transations")
window.config(padx=50, pady=20)
window.config(background="#e0daf7")

transaction = tk.StringVar()
step = tk.StringVar()
type_transfer = tk.StringVar()
amount = tk.StringVar()
oldbalanceOrg = tk.StringVar()
newbalanceOrig = tk.StringVar()
oldbalanceDest = tk.StringVar()
newbalanceDest = tk.StringVar()
alert = tk.StringVar()

lbl_title = tk.Label(window, text="FRAUDULENT TRANSACTIONS",foreground="#3d0a49" ,font=("Arial", 16, "bold"), background="#e0daf7")
lbl_title.grid(column=1, row=0, pady=20, columnspan=2, sticky='nsew')


lbl_transaction = tk.Label(window, anchor='e',text="Transaction ID:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_transaction.grid(column=0, row=1,pady=20, sticky='e')
entry_transaction = tk.Entry(window, textvariable=transaction)
entry_transaction.grid(column=1, row=1, padx=5)

lbl_step = tk.Label(window, text="Step:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_step.grid(column=0, row=2, sticky='e')
entry_step = tk.Entry(window, textvariable=step)
entry_step.grid(column=1, row=2)

lbl_type = tk.Label(window, text="Type:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_type.grid(column=0, row=3, sticky='e')

type_operations = tk.StringVar()
type_operations.set("CASH IN")
menu_type = tk.OptionMenu(window ,type_operations, "CASH IN", "CASH OUT", "DEBIT", "PAYMENT", "TRANSFER")
menu_type.grid(column=1, row=3, pady=20)
menu_type.config(background="#e0daf7", foreground="#5015bd",  font=("Arial", 10, "bold"))

lbl_amount = tk.Label(window, text="Amount:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_amount.grid(column=0, row=4, sticky='e')
entry_amount = tk.Entry(window, textvariable=amount)
entry_amount.grid(column=1, row=4)

lbl_oldbalanceOrg = tk.Label(window, text="OldbalanceOrg:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_oldbalanceOrg.grid(column=2, row=1, sticky='e')
entry_oldbalanceOrg = tk.Entry(window, textvariable=oldbalanceOrg)
entry_oldbalanceOrg.grid(column=3, row=1)

lbl_newbalanceOrig = tk.Label(window, text="NewbalanceOrig:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_newbalanceOrig.grid(column=2, row=2, sticky='e')
entry_newbalanceOrig = tk.Entry(window, textvariable=newbalanceOrig)
entry_newbalanceOrig.grid(column=3, row=2)

lbl_oldbalanceDest = tk.Label(window, text="OldbalanceDest:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_oldbalanceDest.grid(column=2, row=3, sticky='e')
entry_oldbalanceDest = tk.Entry(window, textvariable=oldbalanceDest)
entry_oldbalanceDest.grid(column=3, row=3)

lbl_newbalanceDest = tk.Label(window, text="NewbalanceDest:",foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_newbalanceDest.grid(column=2, row=4, sticky='e')
entry_newbalanceDest = tk.Entry(window, textvariable=newbalanceDest)
entry_newbalanceDest.grid(column=3, row=4, pady=20)

btn_check = tk.Button(window, text="Check transaction", command=check_transaction, font=("Arial", 12, "bold"))
btn_check.grid(column=3, row=5)
btn_check.config(background="#3d0a49", foreground="white",  font=("Arial", 10, "bold"))

btn_clear = tk.Button(window, text="Clear fields", command=clear_fields, font=("Arial", 12, "bold"))
btn_clear.grid(column=0, row=5, pady=20)
btn_clear.config(background="#3d0a49", foreground="white",  font=("Arial", 10, "bold"))

lbl_alert = tk.Label(window, wraplength=400, textvariable=alert ,foreground="#cf1500", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_alert.grid(column=0, row=6, columnspan=4)

lbl_model = tk.Label(window, wraplength=400, text=about_model ,foreground="#027fe9", background="#e0daf7", font=("Arial", 12, "bold"))
lbl_model.grid(column=0, row=7, columnspan=4)

window.mainloop()
