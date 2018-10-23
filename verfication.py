
	
	

from tkinter import *
from tkinter import messagebox
from polyy import *
from what import *
import random as r
import string
root=Tk()
root.title("Verifying Captcha")

def poli():
  poli5()

def what():
  what1()
  
def cancel():
  answer=messagebox.askquestion("Cancel?","Do you really want to Cancel")
  if(answer=='yes'):
    root.destroy()

def capcha():
    c.delete("all")
    h=[]
    for i in range(0,8):
        h.append(chr(r.randint(65,90)))
    ayan=["black","purple","red","blue","green","gray"]
    fnt=["monaco","Arial","italic","papyrus","Bold Oblique","Script"]
    t1 = c.create_text(115 + r.randint(0,6),70+r.randint(0,8),text=h[0],font=fnt[r.randint(0,3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    t2 = c.create_text(138 + r.randint(0,6), 80 + r.randint(0, 9), text=h[1], font=fnt[r.randint(0,3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    t3 = c.create_text(164 + r.randint(0,6), 95+ r.randint(0, 8), text=h[2], font=fnt[r.randint(0,3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    t4 = c.create_text(179 + r.randint(0,6), 90+ r.randint(0, 8), text=h[3], font=fnt[r.randint(0,3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    t5 = c.create_text(198 + r.randint(0,6), 70 + r.randint(0, 8), text=h[4], font=fnt[r.randint(0,3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    t6 = c.create_text(223 + r.randint(0,6), 75 + r.randint(0, 8), text=h[5], font=fnt[r.randint(0,3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    t7 = c.create_text(249 + r.randint(0,6), 65 + r.randint(0, 8), text=h[6], font=fnt[r.randint(0,3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    t8 = c.create_text(274 + r.randint(0,6), 70+ r.randint(0, 8), text=h[7], font=fnt[r.randint(0, 3)]+" 32 bold",fill=ayan[r.randint(0,5)])
    for i in range(0,6):
      line=c.create_line(r.randint(25,300),r.randint(20,170),r.randint(20,240),r.randint(25,300),width=r.randint(1,3))
    capcha.a="".join(h)
    print(capcha.a)

head=Frame(root,width=1366,height=45,bg='#3b5998')
head.place(x=0,y=0)

heading=Label(head,text="Password Remider",bg='#3b5998',fg='white',font=('Segoe UI',20,'bold'))
heading.place(x=5,y=5)

second=Frame(root,width=400,height=45,bg='white')
second.place(x=40,y=60)

reg=Label(second,text="Reg No.",bg='white',fg='black',font=('Segoe UI',18,'bold'))
reg.place(x=3,y=5)

reg_entry=Entry(second,font=('Seogoe UI',17,'bold'),bd=5,relief='groove',bg='white')
reg_entry.place(x=110,y=3)

security=Frame(root,width=400,height=45,bg='white')
security.place(x=40,y=100)

sec_text=Label(security,text="Security Check",bg='white',fg='black',font=('Segoe UI',22,'bold'))
sec_text.place(x=3,y=0)

plz=Frame(root,width=400,height=38,bg='white')
plz.place(x=40,y=142)

plz_text=Label(plz,text="Please enter the text below",bg='white',fg='black',font=('Segoe UI',20))
plz_text.place(x=3,y=0)

captcha=Frame(root,width=395,height=200,bg='white',relief='ridge',bd=8)
captcha.place(x=40,y=187)

c=Canvas(width=375,height=180,bg="light grey")
c.place(x=48,y=195)


cant=Label(root,text="Can't read the text above?",font=('Segoe UI',20),bg='white')
cant.place(x=40,y=390)

ano=Button(root,text="Generate New captcha",font=('Segoe UI',20),bg='white',fg='blue',bd=0,padx=0,pady=0,command=capcha)
ano.place(x=40,y=425)

text=Label(root,text="Text in the box",font=('Segoe UI',18),bg='white',fg='black')
text.place(x=40,y=480)

fourth=Frame(root,width=400,height=45,bg='white')
fourth.place(x=40,y=525)

s=StringVar()
verify=Entry(fourth,font=('Segoe UI',17,'bold'),bd=5,textvariable=s,relief='groove',bg='white')
verify.place(x=5,y=5)


def verif():
  veri=s.get()
  
  if veri==capcha.a:
    n=Tk()
    head=Frame(n,width=1366,height=45,bg='#3b5998')
    head.place(x=0,y=0)
    heading=Label(head,text="Succesfully Verified",bg='#3b5998',fg='white',font=('Segoe UI',20,'bold'),justify="center")
    heading.place(x=5,y=5)
    n.configure(bg='white')
    n.geometry("1366x700+0+0")
    n1b1=Label(n,text='\nYou have been succesfully Logged in.',font="vardana 16 bold",bg='white')
    n1b1.place(x=55,y=55)
    n.mainloop()
  else:
    e=Tk()
    head=Frame(e,width=1366,height=45,bg='#3b5998')
    head.place(x=0,y=0)
    heading=Label(head,text="Try Again",bg='#3b5998',fg='white',font=('Segoe UI',20,'bold'),justify="center")
    heading.place(x=5,y=5)
    e.configure(bg="white")
    e.geometry("1366x700+0+0")
    n1b1 = Label(e, text='\nInvalid Captcha.Try again!!!', font="vardana 16 bold", bg='white',fg='red')
    n1b1.place(x=55,y=55)
    e.mainloop()
    
star=Label(root,text="*",fg='red',font=('Segoe UI',20,'bold'),bg='white')
star.place(x=315,y=525)

what=Button(root,text="What's This?",font=('Segoe UI',20),bg='white',fg='blue',bd=0,command=what)
what.place(x=40,y=570)

bott=Frame(root,width=1366,height=45,bg='light grey')
bott.place(x=0,y=650)

bot_text=Label(bott,text="By proceeding, you agree to our",bg='light grey',fg='black',font=('Segoe Ui',20,'bold'))
bot_text.place(x=5,y=5)

poli_bot=Button(bott,text="Platform policies ",bg='light grey',fg='#3b5998',font=('Segoe UI',19,'bold'),pady=0,padx=0,bd=0,command=poli)
poli_bot.place(x=440, y=0)

contin=Button(bott,text="Continue",font=('arial'),fg='white',bg='#3b5998',padx=0,pady=0,command=verif)
contin.place(x=1182,y=2)

canc=Button(bott,text="Cancel",font=('arial'),fg='white',bg='grey',padx=0,pady=0,command=cancel)
canc.place(x=1280,y=2)

root.configure(bg='white')
root.geometry("1366x700+0+0")
root.mainloop()

