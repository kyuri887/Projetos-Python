def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos números {valores} é igual {s}')


soma(2, 2)
soma(3, 4, 2)
soma(3, 7, 9)