# Importing the library
import tkinter
import math

# Created the object
root = tkinter.Tk()

# Setting the title and geometry
root.title("Scientific Calculator")
root.geometry("680x486+100+100")

# Setting the background color
root.config(bg="black")


# Entry field
entry = tkinter.Entry(root, font=("arial", 20, "bold"), bg="black", fg="white", bd=10, width=30)
entry.grid(row=0, column=0, columnspan=8)

# buttons list
button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
               "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg",
               "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]
r = 1
c = 0
# Loop to get the buttons on window
for i in button_list:
    # Buttons
    button = tkinter.Button(root, width=5, height=2, bd=2, text=i, bg="black", fg="white",
                            font=("arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    c += 1
    if c > 7:
        r += 1
        c = 0

# Makes window on loop
root.mainloop()
