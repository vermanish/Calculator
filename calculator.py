import sys
from Tkinter import *
s=0
f=""
def clear():
	txtDisplay.delete(0,END)
	return
def dot1():
	txtDisplay.insert(END,'.')
	return

def appen0():
	txtDisplay.insert(END,'0')
	return
def appen1():
	txtDisplay.insert(END,'1')
	return
def appen2():
	txtDisplay.insert(END,'2')
	return
def appen3():
	txtDisplay.insert(END,'3')
	return
def appen4():
	txtDisplay.insert(END,'4')
	return
def appen5():
	txtDisplay.insert(END,'5')
	return
def appen6():
	txtDisplay.insert(END,'6')
	return
def appen7():
	txtDisplay.insert(END,'7')
	return
def appen8():
	txtDisplay.insert(END,'8')
	return

def appen9():
	txtDisplay.insert(END,'9')
	return

def divide1():
	global s
	s=txtDisplay.get()
	global f
	f='/'
	txtDisplay.delete(0,END)
	return
def multiply1():
	global s
	s=txtDisplay.get()
	global f
	f='*'
	txtDisplay.delete(0,END)
	return
def minus1():
	global s
	s=txtDisplay.get()
	global f
	f='-'
	txtDisplay.delete(0,END)
	return
def sum1():
	global s
	s=txtDisplay.get()
	global f
	f='+'
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
button1 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="1",fg="black",command=appen1)
button1.pack(side=LEFT)
button2 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="2",fg="black",command=appen2)
button2.pack(side=LEFT)
button3 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="3",fg="black",command=appen3)
button3.pack(side=LEFT)
button4 = Button(topframe, padx=16, pady=16 ,bd=8 ,text="4",fg="black",command=appen4)
button4.pack(side=LEFT)

frame2=Frame(root)
frame2.pack(side=TOP)
button1 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="5",fg="black",command=appen5)
button1.pack(side=LEFT)
button2 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="6",fg="black",command=appen6)
button2.pack(side=LEFT)
button3 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="7",fg="black",command=appen7)
button3.pack(side=LEFT)
button4 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="8",fg="black",command=appen8)
button4.pack(side=LEFT)

frame3=Frame(root)
frame3.pack(side=TOP)
button1 = Button(frame3, padx=16, pady=16 ,bd=8 ,text="9",fg="black",command=appen9)
button1.pack(side=LEFT)
button2 = Button(frame3, padx=16, pady=16 ,bd=8 ,text="0",fg="black")
button2.pack(side=LEFT)
button3 = Button(frame3, padx=16, pady=16 ,bd=8 ,text=".",fg="black",comman=dot1)
button3.pack(side=LEFT)
button4 = Button(frame3, padx=16, pady=16 ,bd=8 ,text="=",fg="black",command=dequal)
button4.pack(side=LEFT)

frame2=Frame(root)
frame2.pack(side=TOP)
button1 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="+",fg="black",command=sum1)
button1.pack(side=LEFT)
button2 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="-",fg="black",command=minus1)
button2.pack(side=LEFT)
button3 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="*",fg="black",command=multiply1)
button3.pack(side=LEFT)
button4 = Button(frame2, padx=16, pady=16 ,bd=8 ,text="/",fg="black",command=divide1)
button4.pack(side=LEFT)

frame5=Frame(root)
frame5.pack(side=TOP)
button3 = Button(frame5, padx=16, pady=16 ,bd=8 ,text="c",fg="black",comman=clear)
button3.pack(side=LEFT)

root.mainloop()
