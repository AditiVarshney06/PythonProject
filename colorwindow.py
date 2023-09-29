from tkinter import *
root=Tk()
root.geometry("264x344")
root.resizable(0,0)
root.configure(bg='black')
root.title("Colour picker")
def self1():
    e_show.configure(bg='red')

def self2():
    e_show.configure(bg='blue')
def self3():
    e_show.configure(bg='green')
def self4():
    e_show.configure(bg='purple')
def self5():
    e_show.configure(bg='pink')
    
def self6():
    e_show.configure(bg='black')
def self7():
    e_show.configure(bg='white')
def self8():
    e_show.configure(bg='orange')
def self9():
    e_show.configure(bg='violet')
def self10():
    e_show.configure(bg='brown')
    

def self11():
    e_show.configure(bg='yellow')
def self12():
    e_show.configure(bg='grey')
def self13():
    e_show.configure(bg='#00ff40')
def self14():
    e_show.configure(bg='#FBDAC8')
def self15():
    e_show.configure(bg='#D4ECEA')
    
    
e_s=StringVar()
e_show=Entry(root,textvariable='e_s')
e_show.place(x=0,y=0,height=80,width=400)


bf=Button(root,text="red",command=self1,bg='red')
bf.place(x=10,y=100,width=50,height=30)

b1=Button(root,text="blue",command=self2,bg='blue')
b1.place(x=10,y=150,width=50,height=30)

b1=Button(root,text="green",command=self3,bg='green')
b1.place(x=10,y=200,width=50,height=30)

b1=Button(root,text="purple",command=self4,bg='purple')
b1.place(x=10,y=250,width=50,height=30)

b1=Button(root,text="pink",command=self5,bg='pink')
b1.place(x=10,y=300,width=50,height=30)



b1=Button(root,text="black",command=self6,fg='white',bg='black')
b1.place(x=100,y=100,width=50,height=30)

b1=Button(root,text="white",command=self7)
b1.place(x=100,y=150,width=50,height=30)

b1=Button(root,text="orange",command=self8,bg='orange')
b1.place(x=100,y=200,width=50,height=30)

b1=Button(root,text="violet",command=self9,bg='violet')
b1.place(x=100,y=250,width=50,height=30)

b1=Button(root,text="brown",command=self10,bg='brown')
b1.place(x=100,y=300,width=50,height=30)

b1=Button(root,text="yellow",command=self11,bg='yellow')
b1.place(x=200,y=100,width=50,height=30)

b1=Button(root,text="grey",command=self12,bg='grey')
b1.place(x=200,y=150,width=50,height=30)

b1=Button(root,text=" light green",command=self13,bg='#00ff40')
b1.place(x=200,y=200,width=50,height=30)

b1=Button(root,text="BabyPink",command=self14,bg='#FBDAC8')
b1.place(x=200,y=250,width=50,height=30)

b1=Button(root,text="sky blue",command=self15,bg='#D4ECEA')
b1.place(x=200,y=300,width=50,height=30)

root.mainloop()
