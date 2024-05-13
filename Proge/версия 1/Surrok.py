import tkinter as tk
# "C:\Users\Leraron159\PycharmProjects\Surrok"
win = tk.Tk() # окно
win.title('Surrok')
#win.geometry("1920x1200+0+0")
win.geometry("960x600+1+0")
#win.attributes('-fullscreen', True)
win.resizable(False, False) # не меняется размер экрана
win.wm_attributes("-topmost", 1) # приложение поверх всех окон
win.bind("<Escape>", lambda event: win.destroy()) # event - событие, destroy - закрыть
#####




win.mainloop() # запуск окна (это в конце)