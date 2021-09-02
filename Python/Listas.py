lista = ['Chocolate', 'Café', 'Leite', 'Pizza', 'Morango']
lista.pop()#Para remover o ultimo valor da lista 
lista.remove('Leite')#Serve para remover qualquer valor da lista 
del lista[0]#Também serve para remover qualquer valor da lista só que por número listado
lista.insert(2, 'Açucar')#adiciona um valor em qualquer lugar da lista
lista.append(0, 'Macarrão')#serve para colocar um valor no fim da lista
if 'Pizza' in lista:
    lista.remove('Pizza')#Essa estrutura serve para remover aa pizza só se ela estiver na lista
valores = [8, 9, 3, 5, 0, 4, 2]
valores.sort()#Serve para colocar os valores em ordem
valores.sort(reverse=True)#serve para colocar em ordem de modo inverso
