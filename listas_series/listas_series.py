import tkinter as tk
from client.gui_app import Frame, barra_menu


def main():
    root = tk.Tk()
    root.title('lista de series')
    root.iconbitmap('img/icono_series.ico')
    root.resizable(0, 0)
    barra_menu(root)
    app = Frame(root = root)    


    app.mainloop()


if __name__ == '__main__':
    main()

