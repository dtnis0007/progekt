from tkinter import *
import sqlite3 as sq


class Application(Frame):
    def __init__(self, master):
        """ иницилизация рамки """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ создание вижетов """
        
        # создание кнопки
        self.submit_bttn = Button(self, text = "Случайная шутка", command = self.get_joke)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

        # создание поля для вывода шутки
        self.joke_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.joke_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def get_joke(self):
        """ Вывод шутки """

        with sq.connect('db.db') as con:
            cur = con.cursor()
    
        cur.execute("SELECT joke FROM jokes ORDER BY RANDOM() LIMIT 1;")    

        joke = cur.fetchall()[0][0]

        self.joke_txt.delete(0.0, END)
        self.joke_txt.insert(0.0, joke)


root = Tk()
root.title("Случайна шутка")
root.geometry("300x150")

app = Application(root)

root.mainloop()
