from tkinter import *
#---Раздел функций---


def new_window():
    root.destroy()
    secondWindow()

def secondWindow():
    def proizv():
        a = EntryA.get()  # берем текст из первого поля
        a = int(a)  # преобразуем в число целого типа
        b = EntryB.get()
        b = int(b)
        result = str(a * b)  # результат переведем в строку для дальнейшего вывода
        EntryC.delete(0, END)  # очищаем текстовое поле полностью
        EntryC.insert(0, result)  # вставляем результат в начало

    root1 = Tk()
    root1.title('Калькулятор')

    # первая метка в строке 0, столбце 0 (0 по умолчанию)
    # парамет sticky  означает выравнивание. W, E,N,S — запад, восток, север, юг
    Label(root1, text='Первое число').grid(row=0, sticky=W)

    # вторая метка в строке 1
    Label(root1, text='Второе число').grid(row=1, sticky=W)

    # создаем виджеты текстовых полей

    EntryA = Entry(root1, width=10, font='Arial 16')
    EntryB = Entry(root1, width=10, font='Arial 16')
    EntryC = Entry(root1, width=20, font='Arial 16')

    # размещаем первые два поля справа от меток, второй столбец (отсчет от нуля)
    EntryA.grid(row=0, column=1, sticky=E)
    EntryB.grid(row=1, column=1, sticky=E)

    # третье текстовое поле ввода занимает всю ширину строки 2
    # columnspan — объединение ячеек по столбцам; rowspan — по строкам
    EntryC.grid(row=2, columnspan=2)

    # размещаем кнопку в строке 3 во втором столбце
    but = Button(root1, text='Произведение', command=proizv)
    but.grid(row=3, column=1, sticky=E)
    root1.mainloop()
#---Основная программа-----
root=Tk()
root.geometry('200x100+300+200')
Label(root,text="Калькулятор", font="Verdana 16").grid()
but=Button(root, text="Начать", command=new_window)
but.grid()
root.mainloop()


