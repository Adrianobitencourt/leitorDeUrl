import urllib.request
from enviarEmail import mensagem
from time import sleep

def lendoURL():
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto  = pagina.read().decode("utf8")
    return texto

def procurandoPreço():
    onde  =  lendoURL().find(">$")
    inicio  = onde + 2
    fim  = inicio + 4
    preco  = lendoURL()[inicio:fim]
    preco = float(preco)
    return preco


if __name__ == '__main__':
    preco = procurandoPreço()
    while preco > 4.74:
        print('Espere! Preço: %5.2f' %preco)
        preco = procurandoPreço()
        sleep(5)
    print('Comprar! Preço: %5.2f' %preco)
    mensagem(preco) 



    





