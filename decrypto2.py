from tkinter import*
from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter.messagebox import*
def change():
    root.destroy
    import Cryptho

root = Tk()
root.title('The De-crypter')
root.geometry('500x700+50+50')
root.configure(bg='yellow')
root.resizable(False,True)
root.wm_iconbitmap('download_CE0_icon.ico')

Top_frame =  Frame(root)
Top_frame.pack(side= TOP)
Top_frame.configure(bg='white',width=700,height=70)

top_label = Label(Top_frame,text='The Decrypter',font=('Algerian',30,'italic'),fg='black')
top_label.pack()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='\t\t\tSwitch to En-Crypt',command = change)

def reset():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def Quit():
    if askyesno('Quit','Are you sure you want to Quit the Encrypter? '):
        root.destroy()

def Choose_message():
    root.filename = filedialog.askopenfilename()
    print (root.filename)
def Choose_key():
    file = open('key.key','rb')
    key_used = file.read()
    file.close()
    entry2.insert(0,key_used)
def decrypt():
    entry3.delete(0,END)
    file = open('key.key','rb')
    key_used = file.read()
    file.close()
    
    
    message = entry1.get()
##    message = str(input(':'))
    decoded = message.encode() 
##    print(encoded)

    f2 = Fernet(key_used)
    decrypted = f2.decrypt(decoded)                     
##    print (decrypted)
    original_message = decrypted.decode()
    entry3.insert(0,original_message)
    Deecrypt_file = open('Decrypt.txt','w')
    Decrypt_file.write(original_message)
    Decrypt_file.close()
 
lbl1 = Label(root,text='Enter your Message ')
lbl1.pack(pady=50)
lbl1.configure(fg='green',font=('Algerian',20,'bold'))
entry1 = Entry(root,bd=4)
entry1.pack()
entry1.configure(width=40,font=('Algerian',20,'italic'))
btn1 = Button(root,text='Choose from file',command=Choose_message)
btn1.pack()

lbl2 = Label(root,text='Enter your Key ')
lbl2.pack(pady=50)
lbl2.configure(fg='green',font=('Algerian',20,'bold'))
entry2 = Entry(root,bd=4)
entry2.pack()
entry2.configure(width=40,font=('Algerian',20,'italic'))
btn2 = Button(root,text='Get Key',command=Choose_key)
btn2.pack()

btn3 = Button(root,text = 'De-Crypt',font=('Algerian',20,'italic'),bg='green',fg='yellow',command=decrypt)
btn3.pack()

entry3 = Entry(root)
entry3.configure(font=('Algerian',30,'italic'))
entry3.pack()

resetBtn = Button(root,text='    Reset all    ',command=reset)
resetBtn.configure(bg='yellow',fg='green',bd=5,font=('Arial',15,'italic'))
resetBtn.pack(side=LEFT)

QuitBtn = Button(root,text='   Quit   ',command=Quit)
QuitBtn.configure(bg='yellow',fg='green',bd=5,font=('Arial',15,'italic'))
QuitBtn.pack(side=RIGHT)

