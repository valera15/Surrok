import tkinter as tk
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
canvas = tk.Canvas(win, width=960, height=600) # размер внутринноости рамки
# canvas = tk.Canvas(win, width=960, height=600, bg="Pink") # размер внутринноости рамки
#x = win.winfo_screenwidth() # ширина 1280
#y = win.winfo_screenheight() # высота 800
#print(x,y)
canvas.pack()

photo_list_fon = [
    tk.PhotoImage(file="Photo/Fon_Razvelka.png"),# 0             ЛОКАЦИИ
    tk.PhotoImage(file="Photo/Fon_Nora.png"),# 1
    tk.PhotoImage(file="Photo/Fon_Ozero.png"),# 2
    tk.PhotoImage(file="Photo/Fon_Tsvetochnaia.png"),# 3
    tk.PhotoImage(file="Photo/Fon_Pole.png"),# 4
    tk.PhotoImage(file="Photo/Fon_Gori.png"),# 5

    # tk.PhotoImage(file="Photo/Fon_Boy_komare.png"),# 6         БОЙ
    # tk.PhotoImage(file="Photo/Fon_Boy_korsak.png"),# 7
    # tk.PhotoImage(file="Photo/Fon_Boy_zmeia.png"),# 8
    # tk.PhotoImage(file="Photo/Fon_Boy_orel.png"),# 9

    # tk.PhotoImage(file="Photo/Menie.png"),# 10                 МЕНЮ
    # tk.PhotoImage(file="Photo/Menie_Pravela.png"),# 11

    # tk.PhotoImage(file="Photo/Proegrish.png"),# 12             ПОЯСНЯЮЩИЕ
    # tk.PhotoImage(file="Photo/Veegriash.png"),# 13
    # tk.PhotoImage(file="Photo/Mesiats.png"),# 14
]
photo_list = [
    tk.PhotoImage(file="Photo/Surrok_128.png"),# 0                СУРОК
    tk.PhotoImage(file="Photo/Surrok_spena.png"),# 1
    tk.PhotoImage(file="Photo/Surrok_naLevo.png"),# 2
    tk.PhotoImage(file="Photo/Surrok_naPravo.png"), # 3

    tk.PhotoImage(file="Photo/Predmet.png"),# 4                   ПРЕДМЕТЫ
    tk.PhotoImage(file="Photo/Predmet.png"),# 5
    tk.PhotoImage(file="Photo/Predmet.png"),# 6
    tk.PhotoImage(file="Photo/Predmet.png"),# 7

    tk.PhotoImage(file="Photo/Tablechka_naPravo.png"),# 8         ТАБЛИЧКИ
    tk.PhotoImage(file="Photo/Tablechka_naLevo.png"),# 9
    tk.PhotoImage(file="Photo/Tablechka_naVerh.png"),# 10
    tk.PhotoImage(file="Photo/Tablechka_naNez.png"),# 11

    tk.PhotoImage(file="Photo/Nora.png"),# 12                     НОРА
    tk.PhotoImage(file="Photo/Luch.png"),# 13
]
x, y = 500, 350
id_predmets_1 = []
id_predmets_2 = []
id_predmets_3 = []
id_predmets_4 = []

def lokatsee_nora():
    global x, y
    canvas.delete("all")
    canvas.create_image(0,0,image = photo_list_fon[1], tags = 'Fon_Nora')
    # Predmet_obj = PhotoImage(file = "Photo/Predmet.png")
    id_luch = canvas.create_image(600, 350, image = photo_list[13],
                                  tags = 'luch')  # вывод луча
    x, y = 540, 320
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')  # вывод сурка

def lokatsee_razvelka():
    global x, y
    canvas.delete("all")
    canvas.create_image(0,0,image = photo_list_fon[0],tags = 'Fon_Razvelka')
    id_nora = canvas.create_image(600, 350, image = photo_list[12],
                                  tags = 'nora')  # вывод норы
    id_tablechka_napravo = canvas.create_image(910, 300, image = photo_list[8],
                                               tags = 'tablechka_napravo')
    id_tablechka_nalevo = canvas.create_image(50, 300, image = photo_list[9],
                                              tags = 'tablechka_nalevo')
    id_tablechka_naverh = canvas.create_image(480, 50, image = photo_list[10],
                                              tags = 'tablechka_naverh')
    id_tablechka_nanez = canvas.create_image(480, 550, image = photo_list[11],
                                             tags = 'tablechka_nanez')

def lokatsee_ozero():
    global x, y, predmets_1
    canvas.delete("all")
    canvas.create_image(0,0,image = photo_list_fon[2],tags = 'Fon_Ozero')
    id_tablechka_napravo_exit = canvas.create_image(910, 300, image = photo_list[8],
                                                    tags = 'tablechka_napravo_exit')
    for i in range(0,10,2): # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_1.append(canvas.create_image(id_predmets_1[i], id_predmets_1[i+1], image = photo_list[4],
                                              tags = 'predmets_1'))
    x, y = 830, 300
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0],tags = 'surok_128')

def lokatsee_tsvetochnaia():
    global x, y, predmets_2
    canvas.delete("all")
    canvas.create_image(0, 0, image = photo_list_fon[3],tags = 'Fon_Tsvetochnaia')
    id_tablechka_nalevo_exit = canvas.create_image(50, 300, image = photo_list[9],
                                                   tags = 'tablechka_nalevo_exit')
    for i in range(0,10,2): # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_2.append(canvas.create_image(id_predmets_2[i], id_predmets_2[i+1], image = photo_list[4],
                                              tags = 'predmets_2'))
    x, y = 130, 300
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

def lokatsee_pole():
    global x, y, predmets_3
    canvas.delete("all")
    canvas.create_image(0,0,image = photo_list_fon[4],tags = 'Fon_Pole')
    id_tablechka_naverh_exit = canvas.create_image(480, 50, image = photo_list[10],
                                                   tags = 'tablechka_naverh_exit')
    for i in range(0,10,2): # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_3.append(canvas.create_image(id_predmets_3[i], id_predmets_3[i+1], image = photo_list[4],
                                              tags = 'predmets_3'))
    x, y = 480, 130
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

def lokatsee_gori():
    global x, y, predmets_4
    canvas.delete("all")
    canvas.create_image(0,0,image = photo_list_fon[5],tags = 'Fon_Gori')
    id_tablechka_nanez_exit = canvas.create_image(480, 550, image = photo_list[11],
                                                   tags = 'tablechka_nanez_exit')
    for i in range(0,10,2): # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_4.append(canvas.create_image(id_predmets_4[i], id_predmets_4[i+1], image = photo_list[4],
                                              tags = 'predmets_4'))
    x, y = 480, 470
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

predmets_1 = []
predmets_2 = []
predmets_3 = []
predmets_4 = []

def rand():
    global id_predmets_1, id_predmets_2, id_predmets_3, id_predmets_4
    for i in range(5):
        id_predmets_1.append(random.randint(50, 910))
        id_predmets_1.append(random.randint(50, 550))
        id_predmets_2.append(random.randint(50, 910))
        id_predmets_2.append(random.randint(50, 550))
        id_predmets_3.append(random.randint(50, 910))
        id_predmets_3.append(random.randint(50, 550))
        id_predmets_4.append(random.randint(50, 910))
        id_predmets_4.append(random.randint(50, 550))
rand()

lokatsee_nora()

def move_surok(event): # функция event-события (движение сурка)
    global x, y
    if event.keysym == 'W':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x,y, image = photo_list[1], tags = 'surok_128')
        canvas.move(id_surok_128,0,-5)
        y = y - 5
    elif event.keysym == 'S':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')
        canvas.move(id_surok_128,0,5)
        y = y + 5
    elif event.keysym == 'A':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x, y, image = photo_list[2], tags = 'surok_128')
        canvas.move(id_surok_128,-5,0)
        x = x - 5
    elif event.keysym == 'D':
        canvas.delete('surok_128')
        id_surok_128 = canvas.create_image(x, y, image = photo_list[3], tags = 'surok_128')
        canvas.move(id_surok_128,5,0)
        x = x + 5
    check_gran()

def check_predmet(event): # функция (координаты предмета и сурка)
    global predmets_1,predmets_2,predmets_3,predmets_4
    position_sur = canvas.coords('surok_128')
    for predmet_1 in predmets_1:
        position_predmets_1 = canvas.coords(predmet_1)
        if position_predmets_1[0]-55<position_sur[0] and position_predmets_1[
           0]+55>position_sur[0] and position_predmets_1[1]-55<position_sur[
           1] and position_predmets_1[1]+55>position_sur[1]:
           canvas.delete(predmet_1)
           predmets_1.remove(predmet_1)
    for predmet_2 in predmets_2:
        position_predmets_2 = canvas.coords(predmet_2)
        if position_predmets_2[0]-55<position_sur[0] and position_predmets_2[
           0]+55>position_sur[0] and position_predmets_2[1]-55<position_sur[
           1] and position_predmets_2[1]+55>position_sur[1]:
           canvas.delete(predmet_2)
           predmets_2.remove(predmet_2)
    for predmet_3 in predmets_3:
        position_predmets_3 = canvas.coords(predmet_3)
        if position_predmets_3[0]-55<position_sur[0] and position_predmets_3[
           0]+55>position_sur[0] and position_predmets_3[1]-55<position_sur[
           1] and position_predmets_3[1]+55>position_sur[1]:
           canvas.delete(predmet_3)
           predmets_3.remove(predmet_3)
    for predmet_4 in predmets_4:
        position_predmets_4 = canvas.coords(predmet_4)
        if position_predmets_4[0]-55<position_sur[0] and position_predmets_4[
           0]+55>position_sur[0] and position_predmets_4[1]-55<position_sur[
           1] and position_predmets_4[1]+55>position_sur[1]:
           canvas.delete(predmet_4)
           predmets_4.remove(predmet_4)

# Проблема: КАК ПОДКЛЮЧИТЬ НАЖАТИЕ КНОПКИ "J" Проблема решена

def check_tablechka(event): # функция (координаты таблички и сурка)
    global x, y
    position_sur = canvas.coords('surok_128')
    position_tablechka_nalevo = canvas.coords('tablechka_nalevo')
    position_tablechka_napravo_exit = canvas.coords('tablechka_napravo_exit')
    position_tablechka_napravo = canvas.coords('tablechka_napravo')
    position_tablechka_nalevo_exit = canvas.coords('tablechka_nalevo_exit')
    position_tablechka_nanez = canvas.coords('tablechka_nanez')
    position_tablechka_naverh_exit = canvas.coords('tablechka_naverh_exit')
    position_tablechka_naverh = canvas.coords('tablechka_naverh')
    position_tablechka_nanez_exit = canvas.coords('tablechka_nanez_exit')
    position_nora = canvas.coords('nora')
    position_luch = canvas.coords('luch')

    if position_tablechka_nalevo != [] and position_tablechka_nalevo[
        0]-105 < position_sur[0] and position_tablechka_nalevo[
        0]+105 > position_sur[0] and position_tablechka_nalevo[1]-105 < position_sur[
        1] and position_tablechka_nalevo[1]+105 > position_sur[1]:
        lokatsee_ozero()
    elif position_tablechka_napravo_exit != [] and position_tablechka_napravo_exit[
        0]-105 < position_sur[0] and position_tablechka_napravo_exit[
        0]+105 > position_sur[0] and position_tablechka_napravo_exit[1]-105 < position_sur[
        1] and position_tablechka_napravo_exit[1]+105 > position_sur[1]:
        lokatsee_razvelka()
        x, y = 130, 300
        id_surok_128 = canvas.create_image(x, y, image=photo_list[0], tags='surok_128')

    elif position_tablechka_napravo != [] and position_tablechka_napravo[
        0]-105 < position_sur[0] and position_tablechka_napravo[
        0]+105 > position_sur[0] and position_tablechka_napravo[1]-105 < position_sur[
        1] and position_tablechka_napravo[1]+105 > position_sur[1]:
        lokatsee_tsvetochnaia()
    elif position_tablechka_nalevo_exit != [] and position_tablechka_nalevo_exit[
        0]-105 < position_sur[0] and position_tablechka_nalevo_exit[
        0]+105 > position_sur[0] and position_tablechka_nalevo_exit[1]-105 < position_sur[
        1] and position_tablechka_nalevo_exit[1]+105 > position_sur[1]:
        lokatsee_razvelka()
        x, y = 830, 300
        id_surok_128 = canvas.create_image(x, y, image=photo_list[0], tags='surok_128')

    elif position_tablechka_nanez != [] and position_tablechka_nanez[
        0]-105 < position_sur[0] and position_tablechka_nanez[
        0]+105 > position_sur[0] and position_tablechka_nanez[1]-105 < position_sur[
        1] and position_tablechka_nanez[1]+105 > position_sur[1]:
        lokatsee_pole()
    elif position_tablechka_naverh_exit != [] and position_tablechka_naverh_exit[
        0]-105 < position_sur[0] and position_tablechka_naverh_exit[
        0]+105 > position_sur[0] and position_tablechka_naverh_exit[1]-105 < position_sur[
        1] and position_tablechka_naverh_exit[1]+105 > position_sur[1]:
        lokatsee_razvelka()
        x, y = 480, 470
        id_surok_128 = canvas.create_image(x, y, image=photo_list[0], tags='surok_128')

    elif position_tablechka_naverh != [] and position_tablechka_naverh[
        0]-105 < position_sur[0] and position_tablechka_naverh[
        0]+105 > position_sur[0] and position_tablechka_naverh[1]-105 < position_sur[
        1] and position_tablechka_naverh[1]+105 > position_sur[1]:
        lokatsee_gori()
    elif position_tablechka_nanez_exit != [] and position_tablechka_nanez_exit[
        0]-105 < position_sur[0] and position_tablechka_nanez_exit[
        0]+105 > position_sur[0] and position_tablechka_nanez_exit[1]-105 < position_sur[
        1] and position_tablechka_nanez_exit[1]+105 > position_sur[1]:
        lokatsee_razvelka()
        x, y = 480, 130
        id_surok_128 = canvas.create_image(x, y, image=photo_list[0], tags='surok_128')

    elif position_nora != [] and position_nora[
        0]-105 < position_sur[0] and position_nora[
        0]+105 > position_sur[0] and position_nora[1]-105 < position_sur[
        1] and position_nora[1]+105 > position_sur[1]:
        lokatsee_nora()
    elif position_luch != [] and position_luch[
        0]-105 < position_sur[0] and position_luch[
        0]+105 > position_sur[0] and position_luch[1]-105 < position_sur[
        1] and position_luch[1]+105 > position_sur[1]:
        lokatsee_razvelka()
        x, y = 540, 320
        id_surok_128 = canvas.create_image(x, y, image=photo_list[0], tags='surok_128')

def check_gran(): # функция (не заходить за границы)
    global x, y
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

canvas.bind_all("<W>",move_surok) ############### KeyPress-Up
canvas.bind_all("<S>",move_surok)
canvas.bind_all("<A>",move_surok)
canvas.bind_all("<D>",move_surok)
canvas.bind_all("<J>",check_predmet)
canvas.bind_all("<H>",check_tablechka)
# +++ КАК УБРАТЬ ЗАДЕРЖКУ

win.mainloop() # запуск окна (это в конце)