# Приветствие с опциями
from tkinter import *

# Константы текста
Answer = ["Супер", "Хорошо", "Так себе", "Плохо", "Ужасно", "Не скажу"]
Diagnose = ["Это здорово!", "Это радует!", "Все возможно.", \
            "Это огорчает!", "Это плохо!", "Раз ты так думаешь ..."]

# Функция события
def buttonClick() :
  Display.config(text=Diagnose[Number.get()])

# Основная программа
Window = Tk()
Window.title("Привет!")
Window.minsize(width=260, height=260)
Display = Label(Window, text="Как это сделать?")
Display.pack()

# Вспомогательная переменная
Number = IntVar()
Number.set(-1)

# Опции
Option = []
for Nr in range(0,6) :
  Option.append(Radiobutton(Window, variable=Number, value=Nr, text=Answer[Nr]))
  Option[Nr].config(command=buttonClick)
  Option[Nr].pack(anchor="w")

# Цикл событий
Window.mainloop()

