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
canvas = tk.Canvas(win, width = 960, height = 600) # размер внутринноости рамки
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
    tk.PhotoImage(file="Photo/Fon_Gore.png"),# 5

    tk.PhotoImage(file="Photo/Fon_Boy_komare.png"),# 6         БОЙ
    tk.PhotoImage(file="Photo/Fon_Boy_korsak.png"),# 7
    tk.PhotoImage(file="Photo/Fon_Boy_zmeia.png"),# 8
    tk.PhotoImage(file="Photo/Fon_Boy_orel.png"),# 9

    tk.PhotoImage(file="Photo/Nadpes_Nora.png"),# 10           НАДПИСИ
    tk.PhotoImage(file="Photo/Nadpes_Razvelka.png"),# 11
    tk.PhotoImage(file="Photo/Nadpes_Ozero.png"),# 12
    tk.PhotoImage(file="Photo/Nadpes_Tsvetochnaia.png"),# 13
    tk.PhotoImage(file="Photo/Nadpes_Pole.png"),# 14
    tk.PhotoImage(file="Photo/Nadpes_Gore.png"),# 15
    # tk.PhotoImage(file="Photo/Nadpes_knopke.png"),# 16

    # tk.PhotoImage(file="Photo/Menie.png"),# 17                 МЕНЮ
    # tk.PhotoImage(file="Photo/Menie_Pravela.png"),# 18

    # tk.PhotoImage(file="Photo/Proegrish.png"),# 19             ПОЯСНЯЮЩИЕ
    # tk.PhotoImage(file="Photo/Veegriash.png"),# 20
    # tk.PhotoImage(file="Photo/Mesiats.png"),# 21
]
photo_list = [
    tk.PhotoImage(file="Photo/Surrok_128.png"),# 0                СУРОК
    tk.PhotoImage(file="Photo/Surrok_spena.png"),# 1
    tk.PhotoImage(file="Photo/Surrok_naLevo.png"),# 2
    tk.PhotoImage(file="Photo/Surrok_naPravo.png"), # 3

    tk.PhotoImage(file="Photo/Predmet_1.png"),# 4                   ПРЕДМЕТЫ
    tk.PhotoImage(file="Photo/Predmet_2.png"),# 5
    tk.PhotoImage(file="Photo/Predmet_3.png"),# 6
    tk.PhotoImage(file="Photo/Predmet.png"),# 7

    tk.PhotoImage(file="Photo/Tablechka_naPravo.png"),# 8         ТАБЛИЧКИ
    tk.PhotoImage(file="Photo/Tablechka_naLevo.png"),# 9
    tk.PhotoImage(file="Photo/Tablechka_naVerh.png"),# 10
    tk.PhotoImage(file="Photo/Tablechka_naNez.png"),# 11

    tk.PhotoImage(file="Photo/Nora.png"),# 12                     НОРА
    tk.PhotoImage(file="Photo/Luch.png"),# 13

    tk.PhotoImage(file="Photo/000.png"),# 14                      КОРЗИНА
    tk.PhotoImage(file="Photo/Korzena_2.png"),# 15

    tk.PhotoImage(file="Photo/Serdechko.png"),# 16                ДЛЯ БОЯ
    tk.PhotoImage(file="Photo/Okno_boia.png"),# 17
    tk.PhotoImage(file="Photo/Ataka.png")# 18

]
x, y = 500, 350
x1, y1 = 480, 450
k1 = 5
k2 = 5
k3 = 5
k4 = 5
id_predmets_1 = [] # просто координаты (рандом)
id_predmets_2 = []
id_predmets_3 = []
id_predmets_4 = []
predmets_1 = [] # координаты и пнг ([[1.png,50(x),60(y)],[2.png,60,40],[3.png,300,80]])
predmets_2 = []
predmets_3 = []
predmets_4 = []

boy_active = False

def lokatsee_nora():
    global x, y, d, b
    d = 1
    b = 0
    canvas.delete("all")
    canvas.create_image(480, 300, image = photo_list_fon[1], tags = 'Fon_Nora')
    # Predmet_obj = PhotoImage(file = "Photo/Predmet.png")
    id_korzena_1 = canvas.create_image(300, 150, image = photo_list[14], tags = 'korzena_1')
    id_luch = canvas.create_image(600, 350, image = photo_list[13],
                                  tags = 'luch')  # вывод луча
    canvas.create_image(480, 15, image=photo_list_fon[10], tags='Nadpes_Nora')
    x, y = 540, 320
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')  # вывод сурка

def lokatsee_razvelka():
    global x, y, d, b
    d = 2
    b = 0
    canvas.delete("all")
    canvas.create_image(480, 300, image = photo_list_fon[0], tags = 'Fon_Razvelka')
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
    canvas.create_image(480, 15, image = photo_list_fon[11], tags = 'Nadpes_Razvelka')

def lokatsee_ozero():
    global x, y, predmets_1, k1, d, b
    d = 0
    b = 1
    chestka_location() # обращение к функции
    canvas.delete("all")
    canvas.create_image(480, 300, image = photo_list_fon[2], tags = 'Fon_Ozero')
    id_tablechka_napravo_exit = canvas.create_image(910, 300, image = photo_list[8],
                                                    tags = 'tablechka_napravo_exit')
    for i in range(0,len(id_predmets_1),2): # от 0 до len(длина_списка) шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_1.append(canvas.create_image(id_predmets_1[i], id_predmets_1[i+1], image = photo_list[4],
                                              tags = 'predmets_1'))
    canvas.create_image(480, 15, image = photo_list_fon[12], tags = 'Nadpes_Ozero')
    x, y = 830, 300
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0],tags = 'surok_128')
    #check_gde_boy()

def lokatsee_tsvetochnaia():
    global x, y, predmets_2, k2, d, b
    d = 0
    b = 2
    chestka_location()  # обращение к функции
    canvas.delete("all")
    canvas.create_image(480, 300, image = photo_list_fon[3], tags = 'Fon_Tsvetochnaia')
    id_tablechka_nalevo_exit = canvas.create_image(50, 300, image = photo_list[9],
                                                   tags = 'tablechka_nalevo_exit')
    for i in range(0,len(id_predmets_2),2): # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_2.append(canvas.create_image(id_predmets_2[i], id_predmets_2[i+1], image = photo_list[5],
                                              tags = 'predmets_2'))
    canvas.create_image(480, 15, image = photo_list_fon[13], tags = 'Nadpes_Tsvetochnaia')
    x, y = 130, 300
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

def lokatsee_pole():
    global x, y, predmets_3, d, b
    d = 0
    b = 3
    chestka_location()  # обращение к функции
    canvas.delete("all")
    canvas.create_image(480, 300, image = photo_list_fon[4], tags = 'Fon_Pole')
    id_tablechka_naverh_exit = canvas.create_image(480, 50, image = photo_list[10],
                                                   tags = 'tablechka_naverh_exit')
    for i in range(0,len(id_predmets_3),2): # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_3.append(canvas.create_image(id_predmets_3[i], id_predmets_3[i+1], image = photo_list[6],
                                              tags = 'predmets_3'))
    canvas.create_image(480, 15, image = photo_list_fon[14], tags='Nadpes_Pole')
    x, y = 480, 130
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

def lokatsee_gore():
    global x, y, predmets_4, d, b
    d = 0
    b = 4
    chestka_location()  # обращение к функции
    canvas.delete("all")
    canvas.create_image(480, 300, image = photo_list_fon[5], tags = 'Fon_Gore')
    id_tablechka_nanez_exit = canvas.create_image(480, 550, image = photo_list[11],
                                                   tags = 'tablechka_nanez_exit')
    for i in range(0,len(id_predmets_4),2): # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
        predmets_4.append(canvas.create_image(id_predmets_4[i], id_predmets_4[i+1], image = photo_list[7],
                                              tags = 'predmets_4'))
    canvas.create_image(480, 15, image = photo_list_fon[15], tags = 'Nadpes_Gore')
    x, y = 480, 470
    id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

def boy_komare():
    global x1, y1
    start_boy()
    canvas.delete("all")
    canvas.create_image(480, 300, image = photo_list_fon[0], tags = 'Fon_Boy_komare') # 6
    id_okno_boia = canvas.create_image(480, 450, image = photo_list[17],
                                       tags = 'okno_boia')
    ochke_count_label = Label(win, text = "Этап 1", bg = "#000000", fg = "#FFFFFF", font = ("Helvetica", 12))
    ochke_count_label.place(x = 455, y = 330)
    ochke_count_label = Label(win, text = "5/5 HP", bg = "#000000", fg = "#FFFFFF", font = ("Helvetica", 12))
    ochke_count_label.place(x = 455, y = 550)
    # for i in range(0, len(id_predmets_4), 2):  # от 0 до 10 шаг 2 ([x,y], [x,y], [x,y], [x,y], [x,y] - лист предметов)
    #     predmets_4.append(canvas.create_image(id_predmets_4[i], id_predmets_4[i + 1], image=photo_list[4],
    #                                           tags='predmets_4'))
    # x, y = 480, 470
    # id_surok_128 = canvas.create_image(x, y, image=photo_list[0], tags='surok_128')
    id_ataka = canvas.create_image(50, 50, image=photo_list[18],
                                       tags='ataka')
    id_serdechko = canvas.create_image(x1, y1, image=photo_list[16], tags='serdechko')  # вывод сердечка
    ataka_1()

    # while a1 == 1:
    #     # Обновляем координаты для анимации
    #     x_a += 5
    #     y_a = k1 * x_a + k2
    #
    #     # Перемещаем объект `ataka` на новые координаты
    #     canvas.move(id_ataka, 5, y_a - canvas.coords(id_ataka)[1])
    #     win.update()  # Обновляем окно для отображения анимации
    #     print(x_a, y_a)
    #     # Условие выхода из цикла
    #     if x_a > 500:
    #         a1 = 0
        #if a1 == 1:
         #   canvas.delete('ataka')
          #  id_ataka = canvas.create_image(x_a, y_a, image=photo_list[18], tags='ataka')
           # canvas.lift(id_ataka, id_okno_boia) # - - - (что, над чем)
            #x_a = x_a + 5  # Пример шага по оси x
            #y_a = k1 * x_a + k2
            #canvas.move(id_ataka, x_a, y_a)
            #position_sur = canvas.coords('ataka')
    # y = k1 * x + k2


    # lower() lift()
    # canvas.lower(rect1,rect2) - - - (что, под что)
    # canvas.lift(rect1,rect2) - - - (что, над чем)

    # for i in range(1,100):
    #     canvas.move(id_ataka,2,0)
    #     win.update()
    #     time.sleep(0.02)
    #
    end_boy

def ataka_1():
    x_a = 367
    y_a = random.randint(375, 525)
    id_ataka = canvas.create_image(x_a, y_a, image=photo_list[18],
                                   tags='ataka')
    print(x_a, y_a)
    a1 = 1
    k1 = 1.5
    k2 = 5
    for i in range(1, 100):
        canvas.move(id_ataka, 2, 0)
        win.update()
        time.sleep(0.02)

def start_boy(): # функция (переключатель для боя)
    global boy_active
    boy_active = True

def end_boy(): # функция (переключатель для боя)
    global boy_active
    boy_active = False

def rand():
    global id_predmets_1, id_predmets_2, id_predmets_3, id_predmets_4
    for i in range(5):
        id_predmets_2.append(random.randint(50, 910))
        id_predmets_2.append(random.randint(50, 550))
        id_predmets_3.append(random.randint(50, 910))
        id_predmets_3.append(random.randint(50, 550))
        id_predmets_4.append(random.randint(50, 910))
        id_predmets_4.append(random.randint(50, 550))

    id_predmets_1.append(random.randint(50, 300))
    id_predmets_1.append(random.randint(50, 175))

    id_predmets_1.append(random.randint(50, 160))
    id_predmets_1.append(random.randint(400, 550))

    id_predmets_1.append(random.randint(672, 910))
    id_predmets_1.append(random.randint(50,200))

    id_predmets_1.append(random.randint(672, 910))
    id_predmets_1.append(random.randint(400, 550))

    id_predmets_1.append(random.randint(480, 600))
    id_predmets_1.append(random.randint(525, 550))
rand()
boy_komare()
#lokatsee_nora()

def move_surok(event): # функция event-события (движение сурка)
    global x, y, b, boy_active
    if boy_active == False:
        if event.keysym == 'W':
           canvas.delete('surok_128')
           id_surok_128 = canvas.create_image(x,y, image = photo_list[1], tags = 'surok_128')
           canvas.move(id_surok_128,0,-5)
           y = y - 5
           position_sur = canvas.coords('surok_128')
           if position_sur[0] <= 480 and b == 1:
            boy_komare()
        elif event.keysym == 'S':
             canvas.delete('surok_128')
             id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')
             canvas.move(id_surok_128,0,5)
             y = y + 5
             position_sur = canvas.coords('surok_128')
             if position_sur[0] <= 480 and b == 1:
                 boy_komare()
        elif event.keysym == 'A':
            canvas.delete('surok_128')
            id_surok_128 = canvas.create_image(x, y, image = photo_list[2], tags = 'surok_128')
            canvas.move(id_surok_128,-5,0)
            x = x - 5
            position_sur = canvas.coords('surok_128')
            if position_sur[0] <= 480 and b == 1:
                boy_komare()
        elif event.keysym == 'D':
            canvas.delete('surok_128')
            id_surok_128 = canvas.create_image(x, y, image = photo_list[3], tags = 'surok_128')
            canvas.move(id_surok_128,5,0)
            x = x + 5
            position_sur = canvas.coords('surok_128')
            if position_sur[0] <= 480 and b == 1:
                boy_komare()
        check_gran()
    return

def move_serdechko(event): # функция event-события (движение сердечка)
    global x1, y1, boy_active
    if boy_active:
        if event.keysym == 'Up':
            canvas.delete('serdechko')
            id_serdechko = canvas.create_image(x1,y1, image = photo_list[16], tags = 'serdechko')
            canvas.move(id_serdechko,0,-5)
            y1 = y1 - 5
        elif event.keysym == 'Down':
            canvas.delete('serdechko')
            id_serdechko = canvas.create_image(x1, y1, image = photo_list[16], tags = 'serdechko')
            canvas.move(id_serdechko,0,5)
            y1 = y1 + 5
        elif event.keysym == 'Left':
            canvas.delete('serdechko')
            id_serdechko = canvas.create_image(x1, y1, image = photo_list[16], tags = 'serdechko')
            canvas.move(id_serdechko,-5,0)
            x1 = x1 - 5
        elif event.keysym == 'Right':
            canvas.delete('serdechko')
            id_serdechko = canvas.create_image(x1, y1, image = photo_list[16], tags = 'serdechko')
            canvas.move(id_serdechko,5,0)
            x1 = x1 + 5
        check_gran_2()
    return

# def move_serdechko(event):
#     global x1, y1, boy_active
#     if boy_active:
#        if event.keysym == 'Up':
#           y1 -= 5
#        elif event.keysym == 'Down':
#           y1 += 5
#        elif event.keysym == 'Left':
#           x1 -= 5
#        elif event.keysym == 'Right':
#           x1 += 5
#     return
def chestka_location(): # функция (чистка списков с координатами)
    global predmets_1, predmets_2, predmets_3, predmets_4
    predmets_1.clear() # clear - очистка с экрана
    predmets_2.clear()
    predmets_3.clear()
    predmets_4.clear()

def check_predmet():  # функция (сбор предмета сурком)
    global predmets_1,predmets_2,predmets_3,predmets_4,id_predmets_1, \
        id_predmets_2, id_predmets_3, id_predmets_4, k1, k2, k3, k4, boy_active
    if boy_active == False:
        position_sur = canvas.coords('surok_128')
        for predmet_1 in predmets_1:
            position_predmets_1 = canvas.coords(predmet_1)
            if ((k2 == 5 or k2 == 8) and (k3 == 5 or k3 == 8) and (k4 == 5 or k4 == 8) and
               position_predmets_1[0]-55 < position_sur[0] < position_predmets_1[0]+55 and
               position_predmets_1[1]-55 < position_sur[1] < position_predmets_1[1]+55):
                id_predmets_1.remove(position_predmets_1[0]) # remove - удаление (работает только со списком)
                id_predmets_1.remove(position_predmets_1[1])
                predmets_1.remove(predmet_1)
                canvas.delete(predmet_1)  # delete - удаление (canvas)
                k1 = k1 - 1
        for predmet_2 in predmets_2:
            position_predmets_2 = canvas.coords(predmet_2)
            if ((k1 == 5 or k1 == 8) and (k3 == 5 or k3 == 8) and (k4 == 5 or k4 == 8) and
               position_predmets_2[0]-55 < position_sur[0] < position_predmets_2[0]+55 and
               position_predmets_2[1]-55 < position_sur[1] < position_predmets_2[1]+55):
                id_predmets_2.remove(position_predmets_2[0])  # remove - удаление (работает только со списком)
                id_predmets_2.remove(position_predmets_2[1])
                predmets_2.remove(predmet_2)
                canvas.delete(predmet_2)  # delete - удаление (canvas)
                k2 = k2 - 1
        for predmet_3 in predmets_3:
            position_predmets_3 = canvas.coords(predmet_3)
            if ((k1 == 5 or k1 == 8) and (k2 == 5 or k2 == 8) and (k4 == 5 or k4 == 8) and
               position_predmets_3[0]-55 < position_sur[0] < position_predmets_3[0]+55 and
               position_predmets_3[1]-55 < position_sur[1] < position_predmets_3[1]+55):
                id_predmets_3.remove(position_predmets_3[0])  # remove - удаление (работает только со списком)
                id_predmets_3.remove(position_predmets_3[1])
                predmets_3.remove(predmet_3)
                canvas.delete(predmet_3)  # delete - удаление (canvas)
                k3 = k3 - 1
        for predmet_4 in predmets_4:
            position_predmets_4 = canvas.coords(predmet_4)
            if ((k1 == 5 or k1 == 8) and (k2 == 5 or k2 == 8) and (k3 == 5 or k3 == 8) and
               position_predmets_4[0]-55 < position_sur[0] < position_predmets_4[0]+55 and
               position_predmets_4[1]-55 < position_sur[1] < position_predmets_4[1]+55):
                id_predmets_4.remove(position_predmets_4[0])  # remove - удаление (работает только со списком)
                id_predmets_4.remove(position_predmets_4[1])
                predmets_4.remove(predmet_4)
                canvas.delete(predmet_4)  # delete - удаление (canvas)
                k4 = k4 - 1
    return

def check_korzena(): # функция (складывание в корзину)
    global k1, k2, k3, k4, boy_active
    if boy_active == False:
        position_sur = canvas.coords('surok_128')
        position_korzena_1 = canvas.coords('korzena_1')
        if ((k1 == 0) and
            position_korzena_1[0] - 55 < position_sur[0] < position_korzena_1[0] + 55 and
            position_korzena_1[1] - 55 < position_sur[1] < position_korzena_1[1] + 55):
             canvas.delete('korzena_1')  # delete - удаление (canvas)
             id_korzena_2 = canvas.create_image(300, 150, image = photo_list[15], tags = 'korzena_2')
             k1 = 8
        elif ((k2 == 0) and
              position_korzena_1[0] - 55 < position_sur[0] < position_korzena_1[0] + 55 and
              position_korzena_1[1] - 55 < position_sur[1] < position_korzena_1[1] + 55):
               canvas.delete('korzena_1')  # delete - удаление (canvas)
               id_korzena_2 = canvas.create_image(300, 150, image = photo_list[15], tags = 'korzena_2')
               k2 = 8
        elif ((k3 == 0) and
              position_korzena_1[0] - 55 < position_sur[0] < position_korzena_1[0] + 55 and
              position_korzena_1[1] - 55 < position_sur[1] < position_korzena_1[1] + 55):
               canvas.delete('korzena_1')  # delete - удаление (canvas)
               id_korzena_2 = canvas.create_image(300, 150, image = photo_list[15], tags = 'korzena_2')
               k3 = 8
        elif ((k4 == 0) and
              position_korzena_1[0] - 55 < position_sur[0] < position_korzena_1[0] + 55 and
              position_korzena_1[1] - 55 < position_sur[1] < position_korzena_1[1] + 55):
               canvas.delete('korzena_1')  # delete - удаление (canvas)
               id_korzena_2 = canvas.create_image(300, 150, image = photo_list[15], tags = 'korzena_2')
               k4 = 8
        canvas.lift('surok_128', id_korzena_2)  # canvas.lift(rect1,rect2) - - - (что, над чем)
    return

def check_deestvee(event): # функция (проверка действия)
    if d == 0:
        check_predmet()
    elif d == 1:
        check_korzena()

def check_tablechka(event): # функция (координаты таблички и сурка)
    global x, y, boy_active
    if boy_active == False:
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

        if (position_tablechka_nalevo != [] and
            position_tablechka_nalevo[0]-105 < position_sur[0] < position_tablechka_nalevo[0]+105 and
            position_tablechka_nalevo[1]-105 < position_sur[1] < position_tablechka_nalevo[1]+105):
             lokatsee_ozero()
        elif (position_tablechka_napravo_exit != [] and
              position_tablechka_napravo_exit[0]-105 < position_sur[0] < position_tablechka_napravo_exit[0]+105 and
              position_tablechka_napravo_exit[1]-105 < position_sur[1] < position_tablechka_napravo_exit[1]+105):
               lokatsee_razvelka()
               x, y = 130, 300
               id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

        elif (position_tablechka_napravo != [] and
              position_tablechka_napravo[0]-105 < position_sur[0] < position_tablechka_napravo[0]+105 and
              position_tablechka_napravo[1]-105 < position_sur[1] < position_tablechka_napravo[1]+105):
               lokatsee_tsvetochnaia()
        elif (position_tablechka_nalevo_exit != [] and
              position_tablechka_nalevo_exit[0]-105 < position_sur[0] < position_tablechka_nalevo_exit[0]+105 and
              position_tablechka_nalevo_exit[1]-105 < position_sur[1] < position_tablechka_nalevo_exit[1]+105):
               lokatsee_razvelka()
               x, y = 830, 300
               id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

        elif (position_tablechka_nanez != [] and
              position_tablechka_nanez[0]-105 < position_sur[0] < position_tablechka_nanez[0]+105 and
              position_tablechka_nanez[1]-105 < position_sur[1] < position_tablechka_nanez[1]+105):
               lokatsee_pole()
        elif (position_tablechka_naverh_exit != [] and
              position_tablechka_naverh_exit[0]-105 < position_sur[0] < position_tablechka_naverh_exit[0]+105 and
              position_tablechka_naverh_exit[1]-105 < position_sur[1] < position_tablechka_naverh_exit[1]+105):
               lokatsee_razvelka()
               x, y = 480, 470
               id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

        elif (position_tablechka_naverh != [] and
              position_tablechka_naverh[0]-105 < position_sur[0] < position_tablechka_naverh[0]+105 and
              position_tablechka_naverh[1]-105 < position_sur[1] < position_tablechka_naverh[1]+105):
               lokatsee_gore()
        elif (position_tablechka_nanez_exit != [] and
              position_tablechka_nanez_exit[0]-105 < position_sur[0] < position_tablechka_nanez_exit[0]+105 and
              position_tablechka_nanez_exit[1]-105 < position_sur[1] < position_tablechka_nanez_exit[1]+105):
               lokatsee_razvelka()
               x, y = 480, 130
               id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')

        elif (position_nora != [] and
              position_nora[0]-105 < position_sur[0] < position_nora[0]+105 and
              position_nora[1]-105 < position_sur[1] < position_nora[1]+105):
               lokatsee_nora()
        elif (position_luch != [] and
              position_luch[0]-105 < position_sur[0] < position_luch[0]+105 and
              position_luch[1]-105 < position_sur[1] < position_luch[1]+105):
               lokatsee_razvelka()
               x, y = 540, 320
               id_surok_128 = canvas.create_image(x, y, image = photo_list[0], tags = 'surok_128')
    return

def check_gran(): # функция (не заходить за границы)
    global x, y, boy_active
    if boy_active == False:
        position_sur = canvas.coords('surok_128')
        if position_sur[0]+60 > 960: # правая граница
           canvas.coords('surok_128', 900, position_sur[1]) # 900 - на сколько откатить
           # ([0] - позиция по x) + (60 - ширина [подобрана] сурка по x) > (960 - размер экрана)
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
    return

def check_gran_2(): # функция (не заходить за границы)
    global x1, y1, boy_active
    if boy_active:
        #      + = -       - = +
        position_ser = canvas.coords('serdechko')
        if position_ser[0]+5 > 560: # правая граница
           canvas.coords('serdechko', 560 - 5, position_ser[1]) # 900 - на сколько откатить
           # ([0] - позиция по x) + (60 - ширина [подобрана] сурка по x) > (555 - размер экрана)
           x1 = 560 - 5
        if position_ser[0]-5 < 400: # левая граница
           canvas.coords('serdechko', 400 + 5, position_ser[1])
           x1 = 400 + 5
        if position_ser[1]+5 > 530: # нижняя граница
           canvas.coords('serdechko', position_ser[0], 530 - 5)
           y1 = 530 - 5
        if position_ser[1]-5 < 365: # верхняя граница
           canvas.coords('serdechko', position_ser[0], 365 + 5)
           y1 = 365 + 5
    return
# КАК ИСПРАВИТЬ ЧТОБЫ В УГЛАХ НОРМАЛЬНО ПЕРЕДВИГАЛОСЬ СЕРДЕЧКО -------------------------------------
canvas.bind_all("<W>",move_surok)
canvas.bind_all("<S>",move_surok)
canvas.bind_all("<A>",move_surok)
canvas.bind_all("<D>",move_surok)
canvas.bind_all("<J>",check_deestvee)
canvas.bind_all("<H>",check_tablechka)
# canvas.bind_all("<P>",)
canvas.bind_all("<KeyPress-Up>",move_serdechko)
canvas.bind_all("<KeyPress-Down>",move_serdechko)
canvas.bind_all("<KeyPress-Left>",move_serdechko)
canvas.bind_all("<KeyPress-Right>",move_serdechko)

win.mainloop() # запуск окна (это в конце)