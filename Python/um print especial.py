from time import sleep

def escreva(msg):
    tam = len(msg) + 5
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam )

escreva('Ola')
escreva('Tudo bem')
escreva('Como posso te ajudar')