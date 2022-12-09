import tkinter as tk
import random
import time


class MainWin(tk.Tk):
    def __init__(self):
        super().__init__()
        w = 500
        h = 600
        dw = round((self.winfo_screenwidth() - w) / 2)
        dh = round((self.winfo_screenheight() - h) / 2)
        icon = tk.PhotoImage(file='img/star_2.png')
        self.iconphoto(False, icon)
        self.title('Главное окно')
        self.geometry(f'{w}x{h}+{dw}+{dh}')  # widthxheight+dx+dy
        self.resizable(True, False)
        self.minsize(200, 200)
        self.maxsize(1000, 1000)
        self.config(bg='#464646')

        button1 = tk.Button(self, text='Кнопка 1', command=lambda: Clicker(self))
        button2 = tk.Button(self, text='Кнопка 2')
        button3 = tk.Button(self, text='Кнопка 3')

        button1.grid(row=0, column=0, stick='we', padx=10)
        button2.grid(row=0, column=1)
        button3.grid(row=1, column=0, stick='we', padx=10)


class Clicker(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Кликер')
        self.geometry('500x500+500+300')
        self.resizable(False, False)
        self.config()

        self.points = 0
        self.but_params = {
            0: (100, 100, 15),  # points: (width button, height button, font button)
            5: (80, 100, 15),
            10: (80, 80, 12),
            15: (60, 60, 12),
            20: (40, 40, 8),
            30: (0, 0, 0)
        }
        self.label = tk.Label(self,
                              text='''Points: 0  Level: 0''',
                              font=('Arial', 15),
                              bg='#505050',
                              )
        #                  fg='#6e6e6e',
        #                  anchor='n',  # w/e/n/s/se/sw/ne/nw/center
        #                  justify='left',  # работает только для многострочного текста '''...'''

        self.label.place(x=0,
                         y=0,
                         width=500,
                         height=30)
        self.button_wrong1 = tk.Button(self,
                                       text='''Don't\nclick''',
                                       command=self.game_over)
        self.button_wrong2 = tk.Button(self,
                                       text='''Don't\nclick''',
                                       command=self.game_over)
        self.button = tk.Button(self,
                                text='Click',
                                font=('Arial', self.but_params[0][2], 'bold'),
                                command=self.click)

        self.button.place(x=50,
                          y=50,
                          width=self.but_params[0][0],
                          height=self.but_params[0][1])

        self.buttons_change_array = [self.button]

    def click(self):
        self.points += 1
        self.label['text'] = f'''Points: {self.points}  Level: {round(self.points // 5)} Time: 0'''

        if self.points in self.but_params:
            if self.points == 10:
                self.buttons_change_array.append(self.button_wrong1)
            if self.points == 15:
                self.buttons_change_array.append(self.button_wrong2)
            if self.points == 30:
                self.game_over()
                return None

            for but in self.buttons_change_array:
                but['font'] = ('Arial', self.but_params[self.points][2], 'bold')
                but.place(x=random.randint(0, 400),
                          y=random.randint(30, 400),
                          width=self.but_params[self.points][0],
                          height=self.but_params[self.points][1])
        else:
            for but in self.buttons_change_array:
                but.place(x=random.randint(0, 400), y=random.randint(30, 400))


    def game_over(self):
        self.clear()
        self.label = tk.Label(self,
                              text=f'''GAME OVER!\n\nPoints: {self.points}\nLevel: {round(self.points // 5)}\nTime: 0''',
                              font=('Arial', 15),
                              bg='#505050',
                              )
        self.label.place(x=0,
                         y=0,
                         width=500,
                         height=500)

    def clear(self):
        for i in self.place_slaves():
            i.destroy()





if __name__ == '__main__':
    win_main = MainWin()
    win_main.mainloop()

    # label = tk.Label(win,
    #                  text='''Привет\nмой друг''',
    #                  font=('Arial', 25),
    #                  bg='#323232',
    #                  fg='#6e6e6e',
    #                  anchor='n',  # w/e/n/s/se/sw/ne/nw/center
    #                  justify='left',  # работает только для многострочного текста '''...'''
    #                  width=10,  # задается в кол-ве символов, а не пикселах
    #                  height=5,
    #                  padx=20,
    #                  pady=10
    #                  )
    # label.pack()
