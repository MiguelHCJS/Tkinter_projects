from tkinter import *
from multiprocessing import Process


class Calc:

    def __init__(self) -> None:

        """
        Configuração de janelas
        """
        self.window = Tk()
        self.window.title('Calculadora')
        self.window.resizable(False, False)

        self.numscreen = Entry(self.window, font='Times 50 bold', bg='#333', fg='white', width=8)
        self.numscreen.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        """
        Botões numéricos
        """
        self.button1 = Button(self.frame, bg='orange', fg='white', bd=0, text='1', width=5, height=4, command=lambda: self.touch(1))
        self.button2 = Button(self.frame, bg='orange', fg='white', bd=0, text='2', width=5, height=4, command=lambda: self.touch(2))
        self.button3 = Button(self.frame, bg='orange', fg='white', bd=0, text='3', width=5, height=4, command=lambda: self.touch(3))
        self.button4 = Button(self.frame, bg='orange', fg='white', bd=0, text='4', width=5, height=4, command=lambda: self.touch(4))
        self.button5 = Button(self.frame, bg='orange', fg='white', bd=0, text='5', width=5, height=4, command=lambda: self.touch(5))
        self.button6 = Button(self.frame, bg='orange', fg='white', bd=0, text='6', width=5, height=4, command=lambda: self.touch(6))
        self.button7 = Button(self.frame, bg='orange', fg='white', bd=0, text='7', width=5, height=4, command=lambda: self.touch(7))
        self.button8 = Button(self.frame, bg='orange', fg='white', bd=0, text='8', width=5, height=4, command=lambda: self.touch(8))
        self.button9 = Button(self.frame, bg='orange', fg='white', bd=0, text='9', width=5, height=4, command=lambda: self.touch(9))
        self.button0 = Button(self.frame, bg='orange', fg='white', bd=0, text='0', width=5, height=4, command=lambda: self.touch(0))
        
        """
        Botões de operação
        """
        self.button_sum = Button(self.frame, bg='orange', fg='white', bd=0, text='+', width=5, height=4, command=lambda: self.touch("+"))
        self.button_sub = Button(self.frame, bg='orange', fg='white', bd=0, text='-', width=5, height=4, command=lambda: self.touch("-"))
        self.button_multi = Button(self.frame, bg='orange', fg='white', bd=0, text='*', width=5, height=4, command=lambda: self.touch("*"))
        self.button_div = Button(self.frame, bg='orange', fg='white', bd=0, text='/', width=5, height=4, command=lambda: self.touch("/"))
        self.button_result = Button(self.frame, bg='orange', fg='white', bd=0, text='=', width=5, height=4, command=self.result)
        self.button_clean = Button(self.frame, bg='orange', fg='white', bd=0, text='C', width=5, height=4, command=lambda: self.clean())

        """
        Posição dos botões em grid
        """
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.button0.grid(row=3, column=1)

        self.button_sum.grid(row=0, column=3)
        self.button_sub.grid(row=1, column=3)
        self.button_multi.grid(row=2, column=3)
        self.button_div.grid(row=3, column=3)
        self.button_result.grid(row=3, column=2)
        self.button_clean.grid(row=3, column=0)

        self.window.mainloop()

    """
    Funções
    """

    def touch(self, element):
        self.numscreen.insert(END, element)

    def clean(self):
        self.numscreen.delete(0, END)

    def result(self):
        resultado = eval(self.numscreen.get())
        self.numscreen.delete(0, END)
        self.numscreen.insert(0, resultado)


if __name__ == '__main__':
    calculadora = Calc()
