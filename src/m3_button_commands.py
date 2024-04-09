import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("Form")

window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1, minsize=50)
window.rowconfigure([0, 1], weight=1, minsize=50)

frame1 = tk.Frame(master=window)
frame2 = tk.Frame(master=window)
frame3 = tk.Frame(master=window)
frame4 = tk.Frame(master=window)
frame5 = tk.Frame(master=window)
frame6 = tk.Frame(master=window)
frame7 = tk.Frame(master=window)
frame8 = tk.Frame(master=window)

frame_button = tk.Frame(master=window)

def print_form():
    entry1_t = entry1.get()
    entry2_t = entry2.get()
    entry3_t = entry3.get()
    entry4_t = entry4.get()
    entry5_t = entry5.get()
    entry6_t = entry6.get()
    entry7_t = entry7.get()
    entry8_t = entry8.get()
    print(entry1_t)
    print(entry2_t)
    print(entry3_t)
    print(entry4_t)
    print(entry5_t)
    print(entry6_t)
    print(entry7_t)
    print(entry8_t)


label1 = tk.Label(
    master=frame1, 
    text="Name",
    foreground="white",
    background="blue")

label2 = tk.Label(
    master=frame2, 
    text="Address Line 1",
    foreground="white",
    background="green")

label3 = tk.Label(
    master=frame3, 
    text="Address Line 2",
    foreground="white",
    background="teal")

label4 = tk.Label(
    master=frame4, 
    text="City",
    foreground="white",
    background="purple")

label5 = tk.Label(
    master=frame5, 
    text="State",
    foreground="black",
    background="cyan")

label6 = tk.Label(
    master=frame6, 
    text="Zip Code",
    foreground="white",
    background="red")

label7 = tk.Label(
    master=frame7, 
    text="Phone Number",
    foreground="white",
    background="orange")

label8 = tk.Label(
    master=frame8, 
    text="Email Address",
    foreground="black",
    background="yellow")

button = tk.Button(
    master=frame_button, 
    text="Submit",
    fg="black",
    bg="white",
    command=print_form)

frame1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

frame3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

frame4.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

frame5.grid(row=0, column=5, sticky="nsew", padx=5, pady=5)

frame6.grid(row=0, column=6, sticky="nsew", padx=5, pady=5)

frame7.grid(row=0, column=7, sticky="nsew", padx=5, pady=5)

frame8.grid(row=0, column=8, sticky="nsew", padx=5, pady=5)

frame_button.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)



entry1 = tk.Entry(master=frame1)
entry2 = tk.Entry(master=frame2)
entry3 = tk.Entry(master=frame3)
entry4 = tk.Entry(master=frame4)
entry5 = tk.Entry(master=frame5)
entry6 = tk.Entry(master=frame6)
entry7 = tk.Entry(master=frame7)
entry8 = tk.Entry(master=frame8)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
label5.pack()
entry5.pack()
label6.pack()
entry6.pack()
label7.pack()
entry7.pack()
label8.pack()
entry8.pack()
button.pack()

window.mainloop()