import sys
from Tkinter import *
s=0
f=""
def clear():
	txtDisplay.delete(0,END)
	return


def appen(x):
	txtDisplay.insert(END,x)
	return

def operation(x):
	global s
	s=txtDisplay.get()
	global f
	f=x
	txtDisplay.delete(0,END)
	return



def dequal():
	r=int(txtDisplay.get())
	
	global s
	global f
	t=float(s)
	txtDisplay.insert(END,f)
	if f=='/' :
		t=t/r;
	if f=='*':
		t=t*r;
	if f=='-':
		t=t-r;
	if f=='+':
		t=t+r;
	if f=='':
		t=40
	txtDisplay.delete(0,END)

	txtDisplay.insert(END,t)
	return
	
root = Tk()
frame = Frame(root)
frame.pack()

root.title('Calculator')
num1=StringVar()

topframe=Frame(root)
topframe.pack(side=TOP)
txtDisplay=Entry(frame,textvariable = num1, bd =20 , insertwidth =1 ,font= 30 )
txtDisplay.pack(side=TOP)
button1 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="1",fg="black",command=lambda: appen('1'))
button1.pack(side=LEFT)
button2 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="2",fg="black",command=lambda: appen('2'))
button2.pack(side=LEFT)
button3 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="3",fg="black",command=lambda: appen('3'))
button3.pack(side=LEFT)
button4 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="4",fg="black",command=lambda: appen('4'))
button4.pack(side=LEFT)

frame2=Frame(root)
frame2.pack(side=TOP)
button1 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="5",fg="black",command=lambda: appen('5'))
button1.pack(side=LEFT)
button2 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="6",fg="black",command=lambda: appen('6'))
button2.pack(side=LEFT)
button3 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="7",fg="black",command=lambda: appen('7'))
button3.pack(side=LEFT)
button4 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="8",fg="black",command=lambda: appen('8'))
button4.pack(side=LEFT)

frame3=Frame(root)
frame3.pack(side=TOP)
button1 = Button(frame3, padx=16, pady=16 ,bd=8 ,text="9",fg="black",command=lambda: appen('9'))
button1.pack(side=LEFT)
button2 = Button(frame3, padx=16, pady=16 ,bd=8 ,text="0",fg="black",command=lambda: appen('0'))
button2.pack(side=LEFT)
button3 = Button(frame3, padx=16, pady=16 ,bd=8 ,text=".",fg="black",command=lambda: appen('.'))
button3.pack(side=LEFT)
button4 = Button(frame3, padx=16, pady=16 ,bd=8 ,text="=",fg="black",command= dequal)
button4.pack(side=LEFT)

frame2=Frame(root)
frame2.pack(side=TOP)
button1 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="+",fg="black",command=lambda: operation('+'))
button1.pack(side=LEFT)
button2 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="-",fg="black",command=lambda: operation('-'))
button2.pack(side=LEFT)
button3 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="*",fg="black",command=lambda: operation('*'))
button3.pack(side=LEFT)
button4 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="/",fg="black",command=lambda: operation('/'))
button4.pack(side=LEFT)

frame5=Frame(root)
frame5.pack(side=TOP)
button3 = Button(frame5, padx=16, pady=16 ,bd=8 ,text="c",fg="black",comman=clear)
button3.pack(side=LEFT)

root.mainloop()
