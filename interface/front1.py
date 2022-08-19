import tkinter as tk

root = tk.Tk()
root.geometry("330x300")

main_frame = tk.Frame(master=root, width=300, height=300)
main_frame.pack()

butt1 = tk.Button(main_frame, text='1', width=10, height=5)
butt2 = tk.Button(main_frame, text='2', width=10, height=5)
butt3 = tk.Button(main_frame, text='3', width=10, height=5)
butt1.grid(row=0,column=0)
butt2.grid(row=0,column=1)
butt3.grid(row=0,column=2)


butt4 = tk.Button(main_frame, text='4', width=10, height=5)
butt5 = tk.Button(main_frame, text='5', width=10, height=5)
butt6 = tk.Button(main_frame, text='6', width=10, height=5)
butt4.grid(row=1,column=0, sticky='nsew')
butt5.grid(row=1,column=1)
butt6.grid(row=1,column=2)


butt7 = tk.Button(main_frame, text='7', width=10, height=5)
butt8 = tk.Button(main_frame, text='8', width=10, height=5)
butt9 = tk.Button(main_frame, text='9', width=10, height=5)
butt7.grid(row=2,column=0)
butt8.grid(row=2,column=1)
butt9.grid(row=2,column=2)

root.mainloop()