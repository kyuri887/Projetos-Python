#Balanço patrimonial
from time import sleep

def analise_de_balanços():
    #calculo do ativo
    ativo_circulante = float(input('Ativo circulante da empresa: '))
    ativo_nao_circulante = float(input('Ativo não circulante da empresa: '))
    ativo = ativo_circulante + ativo_nao_circulante

    #calculo da disponibilidade
    caixa = float(input('Caixa da empresa: '))
    aplicação_financeira = float(input('Aplicação financeira da empresa: '))
    disponibilidade = caixa + aplicação_financeira

    #Calculo da divida liquida
    div_bruta = float(input('Divida bruta da empresa: '))
    div_liquida = div_bruta - disponibilidade 
    