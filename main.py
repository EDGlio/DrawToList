import tkinter

lst = [0] * 5 * 5

master=tkinter.Tk()
master.title("grid() method")
master.geometry("350x275")

def colorChange(x, y):
  lst[x-1 + (y-1) * 5] = 1
  print(lst)

button1_1=tkinter.Button(master, text="", command=lambda : colorChange(1,1))
button1_1.grid(row=1,column=1)
button2_1=tkinter.Button(master, text="", command=lambda : colorChange(2,1))
button2_1.grid(row=2,column=1)
button3_1=tkinter.Button(master, text="", command=lambda : colorChange(3,1))
button3_1.grid(row=3,column=1)
button4_1=tkinter.Button(master, text="", command=lambda : colorChange(4,1)) 
button4_1.grid(row=4,column=1)
button5_1=tkinter.Button(master, text="", command=lambda : colorChange(5,1))
button5_1.grid(row=5,column=1)

button1_2=tkinter.Button(master, text="", command=lambda : colorChange(1, 2))
button1_2.grid(row=1,column=2)
button2_2=tkinter.Button(master, text="", command=lambda : colorChange(2, 2))
button2_2.grid(row=2,column=2)
button3_2=tkinter.Button(master, text="", command=lambda : colorChange(3, 2))
button3_2.grid(row=3,column=2)
button4_2=tkinter.Button(master, text="", command=lambda : colorChange(4, 2))
button4_2.grid(row=4,column=2)
button5_2=tkinter.Button(master, text="", command=lambda : colorChange(5, 2))
button5_2.grid(row=5,column=2)

button1_3=tkinter.Button(master, text="", command=lambda : colorChange(1, 3))
button1_3.grid(row=1,column=3)
button2_3=tkinter.Button(master, text="", command=lambda : colorChange(2, 3))
button2_3.grid(row=2,column=3)
button3_3=tkinter.Button(master, text="", command=lambda : colorChange(3, 3))
button3_3.grid(row=3,column=3)
button4_3=tkinter.Button(master, text="", command=lambda : colorChange(4, 3))
button4_3.grid(row=4,column=3)
button5_3=tkinter.Button(master, text="", command=lambda : colorChange(5, 3))
button5_3.grid(row=5,column=3)

button1_4=tkinter.Button(master, text="", command=lambda : colorChange(1, 4))
button1_4.grid(row=1,column=4)
button2_4=tkinter.Button(master, text="", command=lambda : colorChange(2, 4))
button2_4.grid(row=2,column=4)
button3_4=tkinter.Button(master, text="", command=lambda : colorChange(3,4))
button3_4.grid(row=3,column=4)
button4_4=tkinter.Button(master, text="", command=lambda : colorChange(4,4))
button4_4.grid(row=4,column=4)
button5_4=tkinter.Button(master, text="", command=lambda : colorChange(5,4))
button5_4.grid(row=5,column=4)

button1_5=tkinter.Button(master, text="", command=lambda : colorChange(1,5))
button1_5.grid(row=1,column=5)
button2_5=tkinter.Button(master, text="", command=lambda : colorChange(2,5))
button2_5.grid(row=2,column=5)
button3_5=tkinter.Button(master, text="", command=lambda : colorChange(3,5))
button3_5.grid(row=3,column=5)
button4_5=tkinter.Button(master, text="", command=lambda : colorChange(4,5))
button4_5.grid(row=4,column=5)
button5_5=tkinter.Button(master, text="", command=lambda : colorChange(5,5))
button5_5.grid(row=5,column=5)


master.mainloop()
