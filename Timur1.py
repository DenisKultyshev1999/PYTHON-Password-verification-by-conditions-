"""
В поле ввода пароля есть ограничения, а именно пароль обязан:
1.	Содержать символы верхнего и нижнего регистров.
2.	Состоять только из цифр, букв латинского алфавита, нижнего подчеркивания, тире, точки.
3.	В начале и в конце пароля должны находиться латинские символы.
4.	Длина пароля от 8 до 25 символов.
Напишите приложение, которое будет определять соответствие введенной строки условиям.
"""
from tkinter import *
import tkinter.messagebox as mb
import re

root = Tk ()
root.geometry("500x500")
root.title("Ввести пароль")

def condition():
    parol = password.get()     #getting values from an input field

#....................................condition 1
    if re.match(r'(?=.*[a-z])(?=.*[A-Z])', parol):      
        str1 = "Условие 1 выполнено\n"
    else:
        str1 = "Условие 1 не выполнено\n"

#....................................condition 2
    if re.match(r'.+[^A-Za-z0-9._-]', parol)==None:
        str2 = "Условие 2 выполнено\n"
    else:
        str2 = "Условие 2 не выполнено\n"

#....................................condition 3
    if re.findall(r'[A-Za-z]',parol[-1]) and re.findall(r'[A-Za-z]',parol[0]):
        str3 = "Условие 3 выполнено\n"
    else:
        str3 = "Условие 3 не выполнено\n"
#....................................condition 4
    if 7 < len(parol) < 26:
        str4="Условие 4 выполнено\n"
    else:
        str4="Условие 4 не выполнено\n"

    str=str1+str2+str3+str4
    mb.showinfo("Результат", str)


text = Label(text="Введите пароль с условиями:") 
text1 = Label(text="1.Содержать символы верхнего и нижнего регистров.")
text2 = Label(text="2.Состоять только из цифр, букв латинского алфавита,")
text21 = Label(text= "нижнего подчеркивания, тире, точки.")
text3 = Label(text="3.В начале и в конце пароля должны находиться латинские символы.")
text4 = Label(text="4.Длина пароля от 8 до 25 символов.")

password = Entry()

button_test = Button(text="Проверка пароля", command=condition)

text.pack()
text1.pack()
text2.pack()
text21.pack()
text3.pack()
text4.pack()
password.pack()
button_test.pack()

root.mainloop()
