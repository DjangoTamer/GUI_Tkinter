import tkinter as tk

win = tk.Tk()

w = 500
h = 600
dw = round((win.winfo_screenwidth() - w) / 2)
dh = round((win.winfo_screenheight() - h) / 2)


icon = tk.PhotoImage(file='img/star_2.png')
win.iconphoto(False, icon)
win.title('Главное окно')
win.geometry(f'{w}x{h}+{dw}+{dh}')  # widthxheight+dx+dy
win.resizable(True, False)
win.minsize(200, 200)
win.maxsize(1000, 1000)
win.config(bg='#464646')

label = tk.Label(win,
                 text='''Привет\nмой друг''',
                 font=('Arial', 25),
                 bg='#323232',
                 fg='#6e6e6e',
                 anchor='n',  # w/e/n/s/se/sw/ne/nw/center
                 justify='left',  # работает только для многострочного текста '''...'''
                 width=10,  # задается в кол-ве символов, а не пикселах
                 height=5,
                 padx=20,
                 pady=10
                 )
label.pack()

button1 = tk.Button(text='Кнопка 1')
button1.pack()

button2 = tk.Button(text='Кнопка 2')
button2.pack()

button3 = tk.Button(text='Кнопка 3')
button3.pack()

win.mainloop()
