from tkinter import *
t=Tk()
t.geometry("222x333")
t.configure(bg='grey')
t.resizable(0,0)

def click(c):
    e_var.set(e_var.get()+c)       
e_var=StringVar()
e=Entry(textvariable=e_var,fg='red',font=("",34))
e.place(x=0,y=0,height=69,width=300)

def c():
#     e.delete(0,END)
    e_var.set("")

def d():
    e.delete(0,1)
 
def equ():
    v=e_var.get()
    e_var.set(eval(v))
    
b1=Button(t,text="1",font=("",26),command=click)
b1.place(x=10,y=80,width=43,height=45)
b1.configure(command=lambda:click("1"))

b1=Button(t,text="2",font=("",26))
b1.place(x=60,y=80,width=43,height=45)
b1.configure(command=lambda:click("2"))
b1=Button(t,text="3",font=("",26))
b1.place(x=110,y=80,width=43,height=45)
b1.configure(command=lambda:click("3"))

# for c
b1=Button(t,text="+",font=("",26))
b1.place(x=160,y=80,width=60,height=45)
b1.configure(command=lambda:click("+"))

b1=Button(t,text="-",font=("",26))
b1.place(x=160,y=130,width=60,height=45)
b1.configure(command=lambda:click("-"))

b1=Button(t,text="X",font=("",26))
b1.place(x=160,y=180,width=60,height=45)
b1.configure(command=lambda:click("*"))


b1=Button(t,text="/",font=("",26))
b1.place(x=160,y=230,width=60,height=45)
b1.configure(command=lambda:click("/"))
# main


b1=Button(t,text="4",font=("",26))
b1.place(x=10,y=130,width=43,height=45)
b1.configure(command=lambda:click("4"))

b1=Button(t,text="5",font=("",26))
b1.place(x=60,y=130,width=43,height=45)
b1.configure(command=lambda:click("5"))

b1=Button(t,text="6",font=("",26))
b1.place(x=110,y=130,width=43,height=45)
b1.configure(command=lambda:click("6"))




b1=Button(t,text="7",font=("",26))
b1.place(x=10,y=180,width=43,height=45)
b1.configure(command=lambda:click("7"))
b1=Button(t,text="8",font=("",26))
b1.configure(command=lambda:click("8"))
b1.place(x=60,y=180,width=43,height=45)
b1=Button(t,text="9",font=("",26))
b1.place(x=110,y=180,width=43,height=45)
b1.configure(command=lambda:click("9"))


b1=Button(t,text="%",font=("",26))
b1.place(x=10,y=230,width=43,height=45)
b1.configure(command=lambda:click("%"))
b1=Button(t,text="0",font=("",26))
b1.place(x=60,y=230,width=43,height=45)
b1.configure(command=lambda:click("0"))
b1=Button(t,text=".",font=("",26))
b1.place(x=110,y=230,width=43,height=45)
b1.configure(command=lambda:click("."))


b1=Button(t,text="C",font=("",26),command=c)
b1.place(x=10,y=280,width=66,height=45)
# b1.configure(command=lambda:click("C"))
b1=Button(t,text="=",font=("",26),command=equ)
b1.place(x=82,y=280,width=66,height=45)
# b1.configure(command=lambda:click("="))
b1=Button(t,text="Delete",font=("",16),command=d)
b1.place(x=160,y=280,width=60,height=45)
# focus
# b1.configure(command=lambda:click("3"))


t.mainloop()
