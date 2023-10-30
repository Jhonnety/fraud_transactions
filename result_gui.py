import tkinter as tk

def show_result(transaction, step, type_transfer, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, result):
    result_window = tk.Tk()
    result_window.title("Result")
    result_window.config(padx=100, pady=20)
    result_window.config(background="#e0daf7")
        
    lbl_title = tk.Label(result_window, text="Results",foreground="#3d0a49" ,font=("Arial", 16, "bold"), background="#e0daf7")
    lbl_title.grid(column=1, row=0, pady=20, columnspan=2)
        
    lbl_result = tk.Label(result_window, wraplength=280, text=result,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_result.grid(column=0, row=1, columnspan=4)
        
    title_transaction = tk.Label(result_window, text="Transaction ID:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_transaction.grid(column=0, row=2)
    
    lbl_step = tk.Label(result_window, text=transaction,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_step.grid(column=1, row=2)
    
    title_step = tk.Label(result_window, text="Step:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_step.grid(column=0, row=3)
       
    lbl_step = tk.Label(result_window, text=step,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_step.grid(column=1, row=3)
       
        
    title_type = tk.Label(result_window, text="Type:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_type.grid(column=0, row=4)
       
    lbl_type = tk.Label(result_window, text=type_transfer,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_type.grid(column=1, row=4)
       
        
        
    title_amount = tk.Label(result_window, text="Amount:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_amount.grid(column=0, row=5)
      
    lbl_amount = tk.Label(result_window, text=amount,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_amount.grid(column=1, row=5)
        
        
    title_oldbalanceOrg = tk.Label(result_window, text="OldbalanceOrg:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_oldbalanceOrg.grid(column=2, row=2)
       
    lbl_oldbalanceOrg = tk.Label(result_window, text=oldbalanceOrg,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_oldbalanceOrg.grid(column=3, row=2)
        
        
    title_newbalanceOrig = tk.Label(result_window, text="NewbalanceOrig:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_newbalanceOrig.grid(column=2, row=3)
        
    lbl_newbalanceOrig = tk.Label(result_window, text=newbalanceOrig,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_newbalanceOrig.grid(column=3, row=3)
       
        
    title_oldbalanceDest = tk.Label(result_window, text="OldbalanceDest:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_oldbalanceDest.grid(column=2, row=4)
     
    lbl_oldbalanceDest = tk.Label(result_window, text=oldbalanceDest,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_oldbalanceDest.grid(column=3, row=4)
        
        
    title_newbalanceDest = tk.Label(result_window, text="NewbalanceDest:",foreground="#3d0a49", background="#e0daf7", font=("Arial", 12, "bold"))
    title_newbalanceDest.grid(column=2, row=5)
       
    lbl_newbalanceDest = tk.Label(result_window, text=newbalanceDest,foreground="#5015bd", background="#e0daf7", font=("Arial", 12, "bold"))
    lbl_newbalanceDest.grid(column=3, row=5)