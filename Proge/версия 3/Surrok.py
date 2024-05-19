import tkinter as tk
#import image
import time
from tkinter import * # подключение библиотеки (заинплртировал модуль)

# "C:\Users\Leraron159\PycharmProjects\Surrok"
win = tk.Tk() # окно
win.title('Surrok')
#win.geometry("1920x1200+0+0")
win.geometry("960x600+1+0") # размер рамки
#win.attributes('-fullscreen', True)
win.resizable(False, False) # не меняется размер экрана
win.wm_attributes("-topmost", 1) # приложение поверх всех окон
win.bind("<Escape>", lambda event: win.destroy()) # event - событие, destroy - закрыть
canvas = tk.Canvas(win, width=960, height=600, bg="Blue") # размер внутринноости рамки
canvas.pack()

Predmet_obj = PhotoImage(file = "Photo/Predmet.png") # запись картинки в переменную
id_predmet = canvas.create_image(50,50,image=Predmet_obj) # вывод сурка, id_img
print(id_predmet)

#PHOTO_COUNTER = 1
x,y = 600,400

photo_list = [
    tk.PhotoImage(file="Photo/Surrok_128.png"),# 0
    tk.PhotoImage(file="Photo/Surrok_spena.png"),# 1
    tk.PhotoImage(file="Photo/Surrok_naLevo.png"),# 2
    tk.PhotoImage(file="Photo/Surrok_naPravo.png") # 3
]

# Surok_128 = PhotoImage(file = photo_list[PHOTO_COUNTER]) # запись картинки в переменную
id_surok_128 = canvas.create_image(x,y,image = photo_list[0],tags = 'surok_128') # вывод сурка

# for i in range(1,100):
#     canvas.move(id_surok,2,0)
#     win.update()
#     time.sleep(0.02)

def move_surok(event): # функция event-события (движение сурка)
    global x,y
    if event.keysym == 'w':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x,y, image=photo_list[1], tags = 'surok_128')
        canvas.move(id_surok_128,0,-5)
        y = y - 5
    elif event.keysym == 's':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x, y, image=photo_list[0], tags='surok_128')
        canvas.move(id_surok_128,0,5)
        y = y + 5
    elif event.keysym == 'a':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x, y, image=photo_list[2], tags='surok_128')
        canvas.move(id_surok_128,-5,0)
        x = x - 5
    elif event.keysym == 'd':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x, y, image=photo_list[3], tags='surok_128')
        canvas.move(id_surok_128,5,0)
        x = x + 5


canvas.bind_all("<w>",move_surok) ############### KeyPress-Up
canvas.bind_all("<s>",move_surok)
canvas.bind_all("<a>",move_surok)
canvas.bind_all("<d>",move_surok)

win.mainloop() # запуск окна (это в конце)