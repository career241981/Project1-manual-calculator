#Importing necessary files
from tkinter import*
from tkinter import END

root=Tk()
root.title("Modern Calculator")
root.iconbitmap("C:\\Users\\DELL\\Desktop\\project1-manual calculator\\calculator-icon-windows-v1.ico")
root.geometry('300x410')
root.resizable(0,0)
root.config(bg='Orange')
entryField=Entry(root,bd=7,fg='black',font=('arial',30,'bold'),relief='groove',width=12)
entryField.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

#GUI Operational Part
def clear():
    entryField.delete(0,END)
def click(number):
    entryField.insert(END,number)
def answer():
    expression=entryField.get()
    try:
        result=eval(expression)
        ans=round(result,1)
        entryField.delete(0,END)
        entryField.insert(0,ans)
    except SyntaxError:
        entryField.delete(0,END)
        entryField.insert(0,"Invalid Data")
    except ZeroDivisionError:
        entryField.delete(0,END)
        entryField.insert(0,"Error")

#Buttons Creation
b7=Button(root,text='7',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('7'))
b7.grid(row=1,column=0,padx=10)
b8=Button(root,text='8',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('8'))
b8.grid(row=1,column=1,padx=10)
b9=Button(root,text='9',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('9'))
b9.grid(row=1,column=2,padx=10)
bplus=Button(root,text='+',bd=5,font=('arial',20,'bold'),bg='firebrick',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('+'))
bplus.grid(row=1,column=3,padx=10)

b4=Button(root,text='4',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('4'))
b4.grid(row=2,column=0,pady=10)
b5=Button(root,text='5',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('5'))
b5.grid(row=2,column=1,pady=10)
b6=Button(root,text='6',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('6'))
b6.grid(row=2,column=2,pady=10)
bminus=Button(root,text='-',bd=5,font=('arial',20,'bold'),bg='firebrick',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('-'))
bminus.grid(row=2,column=3,padx=10,pady=10)

b1=Button(root,text='1',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('1'))
b1.grid(row=3,column=0)
b2=Button(root,text='2',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('2'))
b2.grid(row=3,column=1,padx=10,pady=10)
b3=Button(root,text='3',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('3'))
b3.grid(row=3,column=2,padx=10,pady=10)
bmul=Button(root,text='*',bd=5,font=('arial',20,'bold'),bg='firebrick',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('*'))
bmul.grid(row=3,column=3,padx=10,pady=10)

b0=Button(root,text='0',bd=5,font=('arial',20,'bold'),bg='cyan2',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('0'))
b0.grid(row=4,column=0,padx=10,pady=10)
bclear=Button(root,text='C',bd=5,font=('arial',20,'bold'),bg='firebrick',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=clear)
bclear.grid(row=4,column=1,padx=10,pady=10)
bequal=Button(root,text='=',bd=5,font=('arial',20,'bold'),bg='firebrick',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=answer)
bequal.grid(row=4,column=2,padx=10,pady=10)
bdiv=Button(root,text='/',bd=5,font=('arial',20,'bold'),bg='firebrick',cursor='hand2',relief=GROOVE,width=2,height=1,padx=1,pady=0,command=lambda:click('/'))
bdiv.grid(row=4,column=3,padx=10,pady=10)

root.mainloop()