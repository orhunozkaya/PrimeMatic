from tkinter import *
def click():
    entered_text = textentry.get().strip()
    output.delete(0.0, END)
    try:
        count=0
        for i in range(2,int(entered_text)+1):
            if int(entered_text)%i==0:
                count+=1
        if count==1:
            output.insert(END, str(entered_text) + " is a prime.")
        else:
            output.insert(END, str(entered_text) + " is not a prime.")

    except:
        output.insert(END,"invalid number try again")
def close_window():
    window.destroy()
    exit()
window=Tk()
window.title("Asal SayıMatik")
window.resizable(0,0)
logo=Label(window,text="ASAL SAYIMATİK\n",font="Impact 26").grid(row=1,column=0,sticky=N)
yazi=Label(window,text="Bu bir asal sayı programıdır. \n Aşağıdan istediğiniz rakamı giriniz.\n").grid(row=2,column=0,sticky=N,pady=50)
textentry = Entry(window, width=20, bg="light grey", font="Arial 14")
textentry.grid(row=3, column=0, stick=N)
Button(window, text="Submit", width=6, command=click).grid(row=5, column=0, sticky=N)
output = Text(window, width=18, height=3, wrap=WORD, background="white", fg="black", font="arial 20")
output.grid(row=7, column=0, columnspan=2, stick=N)
sonuc=Text(window,width=20,height=0,bg="light grey").grid(row=6,column=0,sticky=N,pady=50)
window.mainloop()

