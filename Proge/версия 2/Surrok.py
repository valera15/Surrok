import tkinter as tk
#import image
from tkinter import * # подключение библиотеки

# "C:\Users\Leraron159\PycharmProjects\Surrok"
win = tk.Tk() # окно
win.title('Surrok')
#win.geometry("1920x1200+0+0")
win.geometry("960x600+1+0") # размер рамки
#win.attributes('-fullscreen', True)
win.resizable(False, False) # не меняется размер экрана
win.wm_attributes("-topmost", 1) # приложение поверх всех окон
win.bind("<Escape>", lambda event: win.destroy()) # event - событие, destroy - закрыть
canvas = tk.Canvas(win, width=960, height=600, bg="Red") # размер внутринноости рамки
canvas.pack()

our_image = PhotoImage(file = "Photo/Surrok_128.png") # запись картинки в переменную
########our_image = PhotoImage(file = relative_to_assets("Photo/Surrok_128.png"))
#our_image = our_image.subsample(1,1) # уменьшить картинку в сколько то раз по "x" и "y"
our_label = Label(win) # метка для поставить
our_label.image = our_image # запись картинки
our_label['image'] = our_label.image # ссылка image на рисунок
our_label.place(x = 50, y = 50) # расположение картинки на экране



win.mainloop() # запуск окна (это в конце)