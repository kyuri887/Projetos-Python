from inspect import ClosureVars
from traceback import clear_frames
import PySimpleGUI as py

class Telapy:
    def __init__(self):
        py.change_look_and_feel('Black')
        layout = [
            [py.Text('Nome', size=(5,0)), py.Input(size=(15,0), key='Nome')],
            [py.Text('Idade',size=(5,0)), py.Input(size=(15,0), key='Idade')],
            [py.Text('Quais provedores de email são aceitos?')],
            [py.Checkbox('Gmail', key='Gmail'), py.Checkbox('Hotmail', key='Hotmail'), py.Checkbox('Yahoo', key='Yahoo')],
            [py.Text('Aceita Cartão')],
            [py.Radio('Sim', 'Aceito',key='Aceito'), py.Radio('Não', 'não aceito',key='Nãoaceito')],
            [py.Slider(range=(0,100), default_value=0, orientation='h', size=(15,20), key='SliderVelocidade')],
            [py.Button('Enviar Dados')],
            [py.Output(size=(30,20))]
        ]
        self.janela = py.Window('Dados do Usuário').layout(layout)
        
        self.button, self.value = self.janela.read()

    def iniciar(self):
        while True:
            self.button, self.value = self.janela.read()
            nome = self.value['Nome']
            idade = self.value['Idade']
            aceita_gmail = self.value['Gmail']
            aceita_hotmail = self.value['Hotmail']
            aceita_yahoo = self.value['Yahoo']
            aceita_cartão_sim = self.value['Aceito']
            nao_aceito_cartao = self.value['Nãoaceito']
            Slider_Velocidade = self.value['SliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Hotmail: {aceita_hotmail}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita cartão: {aceita_cartão_sim}')
            print(f'Não aceita cartão: {nao_aceito_cartao}')
            print(f'Velocidade do script: {Slider_Velocidade}')
tela = Telapy()
tela.iniciar() 
        