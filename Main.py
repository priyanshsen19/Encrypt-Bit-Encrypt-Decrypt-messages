from tkinter import messagebox, simpledialog, Tk

def iseven(number):
    return number % 2 == 0

def getEvenL(message):
    EvenL = []
    for counter in range(0, len(message)):
        if iseven(counter):
            EvenL.append(message[counter])
    return EvenL

def getOddL(message):
    OddL = []
    for counter in range(0, len(message)):
        if not iseven(counter):
            OddL.append(message[counter])
    return OddL

def swapL(message):
    letter_list = []
    if not iseven(len(message)):
        message = message + 'x'
    EvenL = getEvenL(message)
    OddL = getOddL(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(OddL[counter])
        letter_list.append(EvenL[counter])
    new_message = ''.join(letter_list)
    return new_message

def gettask():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def getmessage():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()
while True:
    task = gettask()
    if task == 'encrypt':
        message = getmessage()
        encrypted = swapL(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
        
    elif task == 'decrypt':
        message = getmessage()
        decrypted = swapL(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
root.mainloop()
