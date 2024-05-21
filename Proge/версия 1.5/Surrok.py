import tkinter as tk
#import image
import random
import time
from tkinter import * # подключение библиотеки

# "C:\Users\Leraron159\PycharmProjects\Surrok"
win = tk.Tk() # окно
win.title('Суррок')
win.geometry("960x600+150+60") # размер рамки
#win.attributes('-fullscreen', True) # фулскрин
win.resizable(False, False) # не меняется размер экрана
win.wm_attributes("-topmost", 1) # приложение поверх всех окон
win.bind("<Escape>", lambda event: win.destroy()) # event - событие, destroy - закрыть
canvas = tk.Canvas(win, width=960, height=600, bg="Pink") # размер внутринноости рамки
#x = win.winfo_screenwidth() # ширина 1280
#y = win.winfo_screenheight() # высота 800
#print(x,y)
canvas.pack()

#PHOTO_COUNTER = 1
x,y = 600,400

photo_list = [
    tk.PhotoImage(file="Photo/Surrok_128.png"),# 0
    tk.PhotoImage(file="Photo/Surrok_spena.png"),# 1
    tk.PhotoImage(file="Photo/Surrok_naLevo.png"),# 2
    tk.PhotoImage(file="Photo/Surrok_naPravo.png"), # 3

    tk.PhotoImage(file="Photo/Predmet.png") # 4
]

# Surok_128 = PhotoImage(file = photo_list[PHOTO_COUNTER]) # запись картинки в переменную
id_surok_128 = canvas.create_image(x,y,image = photo_list[0],tags = 'surok_128') # вывод сурка
#Predmet_obj = PhotoImage(file = "Photo/Predmet.png") # запись картинки в переменную
predmets_1 = []
for i in range(5):
    predmets_1.append(canvas.create_image(random.randint(50,910),random.randint(
                                  50,550),image = photo_list[4],tags = 'predmets_1')) # вывод предмета

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
    check_gde()

def check(event): # функция (координаты предмета и сурка)
    position_sur = canvas.coords('surok_128')
    for predmet_1 in predmets_1:
        position_predmets_1 = canvas.coords(predmet_1)
        if position_predmets_1[0]-55<position_sur[0] and position_predmets_1[
           0]+55>position_sur[0] and position_predmets_1[1]-55<position_sur[
           1] and position_predmets_1[1]+55>position_sur[1]:
           canvas.delete(predmet_1)
           predmets_1.remove(predmet_1)
# Проблема: КАК ПОДКЛЮЧИТЬ НАЖАТИЕ КНОПКИ "J" Проблема решена

canvas.bind_all("<w>",move_surok) ############### KeyPress-Up
canvas.bind_all("<s>",move_surok)
canvas.bind_all("<a>",move_surok)
canvas.bind_all("<d>",move_surok)
canvas.bind_all("<j>",check)
#canvas.bind_all("<>")

def check_gde(): # функция (не заходить за границы)
    global x,y
    position_sur = canvas.coords('surok_128')
    if position_sur[0]+60 > 960: # правая граница
       canvas.coords('surok_128', 900, position_sur[1]) # 900 - на сколько откатить
       # ([0] - позиция по x)+(60 - ширина [подобрана] сурка по x)>(960 - размер экрана)
       x = 900
    if position_sur[0]-60 < 0: # левая граница
       canvas.coords('surok_128', 55, position_sur[1])
       x = 55
    if position_sur[1]+60 > 600: # нижняя граница
       canvas.coords('surok_128', position_sur[0], 540)
       y = 540
    if position_sur[1]-60 < 0: # верхняя граница
       canvas.coords('surok_128', position_sur[0], 60)
       y = 60
# Проблема: ОН ТЕЛЕПОРТИРУЕТСЯ НА УГЛАХ Проблема решена

# +++ КАК УБРАТЬ ЗАДЕРЖКУ

win.mainloop() # запуск окна (это в конце)