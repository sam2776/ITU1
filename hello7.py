# Приветствие с переключателем и флажками
from tkinter import *

# Константы текста
Answer = ["Супер", "Хорошо", "Так себе", "Плохо", "Ужасно", "Не скажу"]
State = ["Духовно", "Морально", "Физически"]
Diagnose = ["Это здорово!", "Это радует!", "Все возможно.", \
            "Это огорчает!", "Это плохо!", "Раз ты так думаешь ..."]

# Функция для события
def buttonClick() :
  Display.config(text=Diagnose[OptNum.get()])
def checkClick() :
  Text = "Привет! "
  for Nr in range (0,3) :
    if ChkNum[Nr].get() == 1 :
      Text = Text + State[Nr] + " ";
  Window.title(Text)

# Основная программа
Window = Tk()
Window.title("Привет!")
Window.minsize(width=420, height=260)
Display = Label(Window, text="Как дела?")
Display.grid(row=0, column=1)

# Вспомогательные переменные
ChkNum = [0,0,0]
OptNum = IntVar()
OptNum.set(-1)

# Опции
Option = []
for Nr in range(0,6) :
  Option.append(Radiobutton(Window, variable=OptNum, value=Nr, text=Answer[Nr]))
  Option[Nr].config(command=buttonClick)
  Option[Nr].grid(row=Nr+1, column=0, sticky="w")

# Управление
Choice = []
for Nr in range(0,3) :
  ChkNum[Nr] = IntVar()
  Choice.append(Checkbutton(Window, variable=ChkNum[Nr], text= State [Nr]))
  Choice[Nr].config(command=checkClick)
  Choice[Nr].grid(row=Nr+1, column=2, sticky="w")

# Цикл событий
Window.mainloop()

