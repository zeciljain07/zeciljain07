from tkinter import *

# Creation of a window to be opened
window = Tk()


# Creating a method for the button
# here e1_value is an entry object which is used to fetch any value
# entered by the user using get()


def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get()) * 1.60
    t1.insert(END, miles)


# Creating a button to be shown in the window command attribute here is used to perform some action using that button
# by passing the name of any method created prior to this point


b1 = Button(window, text="Execute", command=km_to_miles)

# Addition of button on the window to make it visible
# This can be done in 2 way, using either pack() or grid()
# Grid is more convenient if you want to have more control over the positions of your objects in the window
# b1.pack()
b1.grid(row=0, column=0)

e1_value = StringVar()
# Creating an entry point where we can enter anything or show some result.
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Creating a placeholder where we can enter any value 
# and then its corresponding button next to it will be used to perform any action based on that input
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# Using a loop to keep the window opened to any duration
window.mainloop()
