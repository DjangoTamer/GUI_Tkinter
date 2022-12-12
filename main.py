import tkinter as tk
from bs4 import BeautifulSoup
import requests
import random
import time

color_bg = '#909090'
color_text = '#E0E0E0'
color_element = '#606060'


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
        self.config(bg=color_bg)

        button1 = tk.Button(self,
                            text='Кликер',
                            font=('Arial', 15, 'bold'),
                            bg=color_element,
                            fg=color_text,
                            width=10,
                            command=lambda: Clicker(self),
                            )
        button2 = tk.Button(self,
                            text='Парсер',
                            font=('Arial', 15, 'bold'),
                            bg=color_element,
                            fg=color_text,
                            width=10,
                            command=lambda: Parser(self)
                            )
        button3 = tk.Button(self,
                            text='Кнопка 3',
                            font=('Arial', 15, 'bold'),
                            bg=color_element,
                            fg=color_text,
                            )
        button4 = tk.Button(self,
                            text='Кнопка 4',
                            font=('Arial', 15, 'bold'),
                            bg=color_element,
                            fg=color_text,
                            )

        button1.grid(row=0, column=0, stick='we', padx=10)
        button2.grid(row=0, column=1)
        button3.grid(row=1, column=0, stick='we', padx=10)
        button4.grid(row=1, column=1)


class Clicker(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Кликер')
        self.geometry('500x500+500+300')
        self.resizable(False, False)
        self.config(bg=color_bg)

        self.points = 0
        self.but_params = {
            0: (100, 100, 15),  # points: (width button, height button, font button)
            5: (80, 100, 15),
            10: (80, 80, 12),
            15: (60, 60, 12),
            20: (40, 40, 8),
            30: (0, 0, 0)
        }

        self.label_points = tk.Label(self,
                                     text='''Points: 0  Level: 0''',
                                     font=('Arial', 15),
                                     bg=color_element,
                                     fg=color_text,
                                     )
        self.label_game_over = tk.Label(self,
                                        text='''...''',
                                        font=('Arial', 20, 'bold'),
                                        bg='#505050',
                                        fg=color_text
                                        )
        self.button_start = tk.Button(self,
                                      text='Start',
                                      font=('Arial', self.but_params[0][2], 'bold'),
                                      bg=color_element,
                                      fg=color_text,
                                      command=self.start
                                      )
        self.button_wrong1 = tk.Button(self,
                                       text='''Don't\nclick''',
                                       font=('Arial', self.but_params[0][2], 'bold'),
                                       bg=color_element,
                                       fg=color_text,
                                       activebackground='#CC0000',
                                       command=self.game_over
                                       )
        self.button_wrong2 = tk.Button(self,
                                       text='''Don't\nclick''',
                                       font=('Arial', self.but_params[0][2], 'bold'),
                                       bg=color_element,
                                       fg=color_text,
                                       activebackground='#CC0000',
                                       command=self.game_over
                                       )
        self.button = tk.Button(self,
                                text='Click',
                                font=('Arial', self.but_params[0][2], 'bold'),
                                bg=color_element,
                                fg=color_text,
                                activebackground='#009900',
                                command=self.click,
                                )

        self.label_points.place(x=0, y=0, width=500, height=40)
        self.button_start.place(x=200, y=200, width=100, height=100)

        self.buttons_change_array = [self.button]  # массив кнопок, которые будут менять свое местоположение

    def start(self):
        self.button.place(x=50, y=50, width=self.but_params[0][0], height=self.but_params[0][1])
        self.button_start.destroy()
        self.start_time = time.time()
        print(self.start_time)

    def click(self):
        self.points += 1
        self.label_points['text'] = f'''Points: {self.points}  Level: {round(self.points // 5)}'''

        if self.points in self.but_params:
            if self.points == 10:
                self.buttons_change_array.append(self.button_wrong1)
            elif self.points == 15:
                self.buttons_change_array.append(self.button_wrong2)
            elif self.points == 30:
                self.game_over()
                return None

            for but in self.buttons_change_array:
                but['font'] = ('Arial', self.but_params[self.points][2], 'bold')
                but.place(x=random.randint(0, 400),
                          y=random.randint(40, 400),
                          width=self.but_params[self.points][0],
                          height=self.but_params[self.points][1])
        else:
            for but in self.buttons_change_array:
                but.place(x=random.randint(0, 400), y=random.randint(40, 400))

    def game_over(self):
        self.end_time = time.time()
        self.clear()
        self.label_game_over[
            'text'] = f'''GAME OVER\n\nPoints: {self.points}\nLevel: {round(self.points // 5)}\nTime: {round(self.end_time - self.start_time, 3)} sec'''
        self.label_game_over.place(x=0, y=0, width=500, height=500)

    def clear(self):
        for i in self.place_slaves():
            i.destroy()


class Parser(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Парсер')
        self.geometry('800x600+500+300')
        self.resizable(False, False)
        self.config(bg=color_bg)

        self.button_start = tk.Button(self,
                                      text="Let's start",
                                      font=('Arial', 15, 'bold'),
                                      bg=color_element,
                                      fg=color_text,
                                      command=self.get_fact
                                      )
        self.button_copy = tk.Button(self,
                                      text="Copy",
                                      font=('Arial', 15, 'bold'),
                                      bg=color_element,
                                      fg=color_text,
                                      command=self.get_fact
                                      )

        self.text = tk.Text(self,
                            width=50,
                            height=10,
                            font=('Arial', 12),
                            wrap='word'
                            )

        self.scrollbar = tk.Scrollbar(self, command=self.text.yview)
        self.button_start.pack()


    def get_fact(self):
        website = 'https://facts.museum/random'
        response = requests.get(website)
        fact_page = BeautifulSoup(response.content, 'html.parser')
        print('Заголовок', fact_page.h2.text)
        print('Текст', fact_page.find('p', class_='content').text)
        print('Фото', r'https://facts.museum/img/facts/' + response.url.split('/')[-1] + '.jpg')

        self.button_start['text'] = 'Next fact'
        self.button_copy.pack()
        self.text.insert(1.0, fact_page.find('p', class_='content').text)
        self.text.pack()
        self.scrollbar.pack()



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

# FFFFFF
# E0E0E0 текст
# C0C0C0
# A0A0A0
# 909090 фон
# 808080
# 606060 элемент
# 404040
# 000000
