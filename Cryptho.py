from tkinter import*
from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter.messagebox import*

def change():
    import decrypto2


root = Tk()
root.title('The Encrypter')
root.geometry('500x700+50+50')
root.configure(bg='yellow')
root.resizable(False,True)
root.wm_iconbitmap('download_CE0_icon.ico')

Top_frame =  Frame(root)
Top_frame.pack(side= TOP)
Top_frame.configure(bg='white',width=700,height=70)

top_label = Label(Top_frame,text='The Encrypter',font=('Algerian',30,'italic'),fg='black')
top_label.pack()
##=======================menu========================
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Switch to De-Crypt',command = change)


##====================menu==========================

def reset():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def Quit():
    if askyesno('Quit','Are you sure you want to Quit the Encrypter? '):
        root.destroy()
    

def Choose_message():
    myfile = filedialog.askopenfilename()
    wale = open('C:/Users/TIMIAK/Desktop/timo.key','r+')
    dami = wale.read()
    wale.close()
    print(dami)
    entry1.insert(0,dami)
##    print (myfile)
def Choose_key():
    key2 = Fernet.generate_key()
##    print(key)
    entry2.insert(0,key2)

def encrypt():
    key_used = entry2.get()
    message = entry1.get()
    entry_word = entry3.get()
##    print(key_used)
##    print (message)

##    print(key_used)
##    message = str(input(':'))
    encoded = message.encode()
##    print(encoded)

    f = Fernet(key_used)
    encrypted = f.encrypt(encoded)
##    print (encrypted)
    entry3.delete(0,0)
    entry3.insert(0,encrypted)
    key_file = open('key.key','w')
    key_file.write(key_used)
    key_file.close()
    Encrypt_file = open('encrypt.key','w')
    Encrypt_file.write(entry_word)
    Encrypt_file.close()

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
btn2 = Button(root,text='Generate And use a new Key',command=Choose_key)
btn2.pack()

btn3 = Button(root,text = 'Encrypt',font=('Algerian',20,'italic'),bg='green',fg='yellow',command=encrypt)
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

'''


file = open('key.key','rb')
key = file.read()
file.close()
print('Enter the word')



file = open('key.key','rb')
key = file.read()
file.close()

f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print(decrypted)

original_message = decrypted.decode()
print(original_message)

'''
