import os
import tkinter as tk



def increment():
    lbl_counter_var.set(lbl_counter_var.get() + 1)


def decrement():
    lbl_counter_var.set(lbl_counter_var.get() - 1)
    



root = tk.Tk()
root.title('TkInter DEMO')
root.geometry('600x400')


lbl_title = tk.Label(root,
                     text='COUNTER',
                     font=('Verdana', 18))
lbl_title.pack(padx=10, pady=10)


lbl_counter_var = tk.DoubleVar(root, 0)
btn_increment = tk.Button(root,
                      textvariable=lbl_counter_var,
                      font=('Verdana', 14),
                      highlightbackground='#108B10',
                      width=10, height=5,
                      command=increment,
                      )
btn_increment.pack(padx=10, pady=10, side=tk.LEFT)


btn_decrement = tk.Button(root,
                              textvariable=lbl_counter_var,
                              font= ('Verdana', 14),
                              highlightbackground='#CD3232',
                              width=10, height=5,
                              command=decrement)
btn_decrement.pack(padx=10, pady=10, side=tk.RIGHT)







root.mainloop()