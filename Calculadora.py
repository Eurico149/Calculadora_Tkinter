from tkinter import *
from tkinter import ttk, messagebox

lista1 = []
lista2 = []
ordem = 1
funcao = 0
r = ""


def dimensaotela(janela):
    # analisa as dimensoes da tela para criar uma janela do tamnaho desejado e no centro da tela
    alturatela = 335
    larguratela = 271

    widthtela = janela.winfo_screenwidth()
    heighttela = janela.winfo_screenheight()
    center_x = int(widthtela / 2 - larguratela / 2)
    center_y = int(heighttela / 2 - alturatela / 2)
    return f'{larguratela}x{alturatela}+{center_x}+{center_y}'


def mensagem():
    return messagebox.showinfo(title="INFO", message="By: Eurico Gabriel Vasconcelos Pereria\n2022")


def zero_esquerda(lista):
    elemento = -1
    if "." in lista:
        arg = True
    else:
        arg = False
    while arg:
        if lista[-1] == "0":
            lista.pop()
        else:
            arg = False


def posicao(lb, lista):
    # Posiciona o texto de maneira progressiva no Frame
    if lista.count(".") == 0:
        x = 222 - ((len(lista)) * 14) + 8
    else:
        x = 222 - ((len(lista)) * 14) + 14
    lb.place(x=x, y=9)


def apagar(lb):
    # Apaga o ultimo item da lista
    lista = []
    if ordem == 1:
        lista = lista1
    elif ordem == 2:
        lista = lista2
    if len(lista) != 0:
        lista.pop()
        s = "".join(lista)
        lb["text"] = s
        posicao(lb, lista)
    if len(lista) == 1 and lista[0] == "0":
        lista.pop()
    if len(lista) == 0:
        lb["text"] = "0"
        lb.place(x=216, y=9)
    print(lista)
    print(ordem)


def numerico(lista):
    # transforma a lista em um numero
    if lista.count(".") > 0:
        numero = float("".join(lista))
    else:
        numero = int("".join(lista))
    return numero


def digitos(bt, lb):
    # Adiicona itens na lista
    lista = []
    if ordem == 1:
        lista = lista1
    elif ordem == 2:
        lista = lista2
    if len(lista) < 14 and (not(bt["text"] == "." and lista.count(".") == 1)):
        if not(bt["text"] == "." and len(lista) == 0):
            lista.append(bt["text"])
        else:
            lista.append("0")
            lista.append(".")
        if lista[0] == "0" and len(lista) > 1 and lista[1] != ".":
            lista.remove("0")
    s = "".join(lista)
    lb["text"] = s
    posicao(lb, lista)
    print(lista)


def principal():
    # Cria a janela
    janela = Tk()
    janela.title("Calculadora")
    janela.geometry(dimensaotela(janela))
    janela.resizable(False, False)
    # janela.iconbitmap("calculator_icon.ico")
    janela.configure(bg="gray10")

    def fictures():
        # Botões, Frames, Label etc
        fr1 = Frame(janela, width=240, height=50, bg="gray25")
        fr1.place(x=15, y=15)
        lb1 = ttk.Label(fr1, text="0", background="gray25", foreground="gray85", font=("times", 20))
        lb1.place(x=216, y=9)
        lb2 = ttk.Label(fr1, text="1", background="gray25", foreground="gray85", font=("times", 10))
        lb2.place(x=1, y=3)
        lb3 = ttk.Label(fr1, text="", background="gray25", foreground="gray85", font=("times", 10))
        lb3.place(x=1, y=25)

        def switch():
            # Troca de uma lista para outra
            global ordem
            lb1["text"] = "0"
            if ordem == 1:
                ordem = 2
            else:
                ordem = 1
            lista = []
            if ordem == 1:
                lista = lista1
            elif ordem == 2:
                lista = lista2
            s = "".join(lista)
            lb1["text"] = s
            posicao(lb1, lista)
            if len(lista) == 0:
                lb1["text"] = "0"
                lb1.place(x=216, y=9)
            lb2["text"] = ordem

        def funcoes(bt):
            # Aloca a operação a ser realizada
            global funcao, r, lista1, lista2
            if bt["text"] == "+":
                if funcao != 1:
                    funcao = 1
                    r = bt["text"]
                    if ordem == 1:
                        switch()
            elif bt["text"] == "-":
                if funcao != 2:
                    funcao = 2
                    r = bt["text"]
                    if ordem == 1:
                        switch()
            elif bt["text"] == "x":
                if funcao != 3:
                    funcao = 3
                    r = bt["text"]
                    if ordem == 1:
                        switch()
            elif bt["text"] == "/":
                if funcao != 4:
                    funcao = 4
                    r = bt["text"]
                    if ordem == 1:
                        switch()

            lb3["text"] = r

        def btx(bt):
            global lista1, lista2
            if bt["text"] == "x²":
                lista = []
                if ordem == 1:
                    lista = lista1
                elif ordem == 2:
                    lista = lista2
                s = numerico(lista) ** 2
                if ordem == 1:
                    lista1 = lista
                else:
                    lista2 = lista
                if s % 1 == 0:
                    s = int(s)
                lista1 = list(str(s))
                if len(lista1) > 14:
                    for i in range(len(lista1) - 14):
                        lista1.pop()
                s = "".join(lista1)
                lb1["text"] = s
                posicao(lb1, lista1)
            elif bt["text"] == "√x":
                lista = []
                if ordem == 1:
                    lista = lista1
                elif ordem == 2:
                    lista = lista2
                s = numerico(lista) ** 0.5
                if ordem == 1:
                    lista1 = lista
                else:
                    lista2 = lista
                if s % 1 == 0:
                    s = int(s)
                lista1 = list(str(s))
                if len(lista1) > 14:
                    for i in range(len(lista1) - 14):
                        lista1.pop()
                s = "".join(lista1)
                lb1["text"] = s
                posicao(lb1, lista1)

        def igualdade():
            # Realiza a operação
            global funcao, lista1, lista2
            if funcao != 0:
                s = 0
                if funcao == 1:
                    s = numerico(lista1) + numerico(lista2)
                elif funcao == 2:
                    s = numerico(lista1) - numerico(lista2)
                elif funcao == 3:
                    s = numerico(lista1) * numerico(lista2)
                elif funcao == 4:
                    if not(numerico(lista1) == 0 or numerico(lista2) == 0):
                        s = numerico(lista1) / numerico(lista2)
                if s % 1 == 0:
                    s = int(s)
                lista1 = list(str(s))
                if len(lista1) > 14:
                    for i in range(len(lista1) - 14):
                        lista1.pop()
                zero_esquerda(lista1)
                s = "".join(lista1)
                lb1["text"] = s
                posicao(lb1, lista1)
                lista2.clear()
                funcao = 0
                lb3["text"] = ""
                switch()

        bt1 = Button(janela, width=7, height=2, bg="gray", text="√x", command=lambda: [btx(bt1)])
        bt1.place(x=15, y=100)
        bt2 = Button(janela, width=7, height=2, bg="gray", text="7", command=lambda: [digitos(bt2, lb1)])
        bt2.place(x=15, y=145)
        bt3 = Button(janela, width=7, height=2, bg="gray", text="4", command=lambda: [digitos(bt3, lb1)])
        bt3.place(x=15, y=190)
        bt4 = Button(janela, width=7, height=2, bg="gray", text="1", command=lambda: [digitos(bt4, lb1)])
        bt4.place(x=15, y=235)
        bt5 = Button(janela, width=7, height=2, bg="gray", text="Creditos", command=lambda: [mensagem()])
        bt5.place(x=15, y=280)

        bt6 = Button(janela, width=7, height=2, bg="gray", text="x²", command=lambda: [btx(bt6)])
        bt6.place(x=75, y=100)
        bt7 = Button(janela, width=7, height=2, bg="gray", text="8", command=lambda: [digitos(bt7, lb1)])
        bt7.place(x=75, y=145)
        bt8 = Button(janela, width=7, height=2, bg="gray", text="5", command=lambda: [digitos(bt8, lb1)])
        bt8.place(x=75, y=190)
        bt9 = Button(janela, width=7, height=2, bg="gray", text="2", command=lambda: [digitos(bt9, lb1)])
        bt9.place(x=75, y=235)
        bt10 = Button(janela, width=7, height=2, bg="gray", text="0", command=lambda: [digitos(bt10, lb1)])
        bt10.place(x=75, y=280)

        bt11 = Button(janela, width=7, height=2, bg="gray", text="/", command=lambda: [funcoes(bt11)])
        bt11.place(x=135, y=100)
        bt12 = Button(janela, width=7, height=2, bg="gray", text="9", command=lambda: [digitos(bt12, lb1)])
        bt12.place(x=135, y=145)
        bt13 = Button(janela, width=7, height=2, bg="gray", text="6", command=lambda: [digitos(bt13, lb1)])
        bt13.place(x=135, y=190)
        bt14 = Button(janela, width=7, height=2, bg="gray", text="3", command=lambda: [digitos(bt14, lb1)])
        bt14.place(x=135, y=235)
        bt15 = Button(janela, width=7, height=2, bg="gray", text=".", command=lambda: [digitos(bt15, lb1)])
        bt15.place(x=135, y=280)

        bt16 = Button(janela, width=7, height=2, bg="gray", text="x", command=lambda: [funcoes(bt16)])
        bt16.place(x=195, y=100)
        bt17 = Button(janela, width=7, height=2, bg="gray", text="-", command=lambda: [funcoes(bt17)])
        bt17.place(x=195, y=145)
        bt18 = Button(janela, width=7, height=2, bg="gray", text="+", command=lambda: [funcoes(bt18)])
        bt18.place(x=195, y=190)
        bt19 = Button(janela, width=7, height=2, bg="gray", text="⍇", command=lambda: [apagar(lb1)])
        bt19.place(x=195, y=235)
        bt20 = Button(janela, width=7, height=2, bg="gray", text="=", command=lambda: [igualdade()])
        bt20.place(x=195, y=280)

    fictures()
    janela.mainloop()


principal()
