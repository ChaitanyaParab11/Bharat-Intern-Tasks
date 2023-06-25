from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

root = Tk()
root.geometry('980x500')
root.resizable(0,0)
root.title("Language Translator")
root.config(bg = 'sky blue')

Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", fg='black',    bg='sky blue').pack()
Label(root, text="By Chaitanya Vijay Parab", font="arial 12", fg='black', bg='sky blue').pack()


Input_text = Text(root,font = 'arial 14', height = 11, fg= 'black', bg='white', wrap = WORD, padx=5, pady=5, width = 30)
Input_text.place(x=50,y = 100)

Output_text = Text(root,font = 'arial 14', height = 11, fg= 'black', bg='white', wrap = WORD, padx=3, pady=3, width = 30)
Output_text.place(x = 600 , y = 100)
 

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= ('english','hindi','dutch','french'), width =22)
src_lang.place(x=20,y=60)
src_lang.set('Select input language')

dest_lang = ttk.Combobox(root, values= ('english','hindi','dutch','french'), width =22)
dest_lang.place(x=810,y=60)
dest_lang.set('Select output language')

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate ,fg='black', bg = 'white', activebackground = 'green')
trans_btn.place(x = 455, y = 180)


root.mainloop()
