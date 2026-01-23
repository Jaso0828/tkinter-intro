import random
import tkinter as tk


# 33 - 126 su svi znakovi


# chr()
def password_generator():
    password_limit = 15
    characters = [chr(i) for i in range(33, 127)]
    random.shuffle(characters)
    password = ''
    for letter in characters[ : password_limit]:
        password += letter

    lbl_generator_var.set(password)


root = tk.Tk()
root.title('Password generator')
root.geometry('600x400')


lbl_title = tk.Label(root,
                     text='Password generator',
                     font=('Verdana', 15))
lbl_title.pack(padx=10, pady=10)


lbl_generator_var=tk.StringVar(root, '!Pa$$w0rd')
btn_generator = tk.Button(root,
                          textvariable=lbl_generator_var,
                          font= ('Verdana', 14),
                          command=password_generator,
                          )
btn_generator.pack(padx=10, pady=10)




root.mainloop()





