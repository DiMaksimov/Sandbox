import socket
import tkinter as tk


class Window(tk.Frame):
    buttons = {}
    chat_field = None
    user_input = None
    user_input_field = None

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Chat')
        self.pack(fill=tk.BOTH, expand=1)

        self.buttons['quit_button'] = tk.Button(self, text='Quit', command=self.client_exit)
        self.buttons['quit_button'].place(x=0, y=0)

        self.chat_field = tk.Text(self)
        self.chat_field.config(state=tk.DISABLED)
        self.chat_field.pack()

        self.user_input = tk.StringVar()
        self.user_input_field = tk.Entry(self, text=self.user_input)
        self.user_input_field.pack(side=tk.BOTTOM, fill=tk.X)

    def client_exit(self):
        exit()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x600")
    root.resizable(False, False)
    app = Window(master=root)
    root.mainloop()
