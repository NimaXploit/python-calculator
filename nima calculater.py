from tkinter import *

def btnClick(number):
    global operator
    operator += str(number)
    text_input.set(operator)

def btnClear():
    global operator
    operator = ''
    text_input.set("")

def btnEquals():
    global operator
    try:
        result = str(eval(operator))
        text_input.set(result)
        operator = ''

    except:
        text_input("Error")
        operator = ''

app = Tk()
app.title("Calculater App")
app.configure(background='#dddddd')
app.resizable(False, False)

operator = ''
text_input = StringVar()
txtDisplay = Entry(app, textvariable=text_input, bd=10, insertwidth=2, bg="#ffffff" ,justify='right')
txtDisplay.grid(row=0, column=0, columnspan=4)

Button(app, text="7", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(7)).grid(row=1, column=0)
Button(app, text="8", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(8)).grid(row=1, column=1)
Button(app, text="9", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(9)).grid(row=1, column=2)
Button(app, text="+", padx=20, pady=20, font=("Arial", 14), bg="#f08080", command=lambda: btnClick("+")).grid(row=1, column=3)



Button(app, text="4", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(4)).grid(row=2, column=0)
Button(app, text="5", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(5)).grid(row=2, column=1)
Button(app, text="6", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(6)).grid(row=2, column=2)
Button(app, text="-", padx=20, pady=20, font=("Arial", 14), bg="#f08080", command=lambda: btnClick("-")).grid(row=2, column=3)


Button(app, text="1", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(1)).grid(row=3, column=0)
Button(app, text="2", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(2)).grid(row=3, column=1)
Button(app, text="3", padx=20, pady=20, font=("Arial", 14), command=lambda: btnClick(3)).grid(row=3, column=2)
Button(app, text="*", padx=20, pady=20, font=("Arial", 14), bg="#f08080", command=lambda: btnClick("*")).grid(row=3, column=3)


Button(app, text="0", padx=47, pady=20, font=("Arial", 14), command=lambda: btnClick(0)).grid(row=4, column=0, columnspan=2)
Button(app, text="C", padx=20, pady=20, font=("Arial", 14), bg="#f08080", command=btnClear).grid(row=4, column=2)
Button(app, text="/", padx=20, pady=20, font=("Arial", 14), bg="#f08080", command=lambda: btnClick("/")).grid(row=4, column=3)


Button(app, text="=", padx=100, pady=20, font=("Arial", 14), bg="#90ee90", command=btnEquals).grid(row=5, column=0, columnspan=4)

app.mainloop()
