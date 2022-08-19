import PySimpleGUI as sg
from datetime import datetime


def titulo(tit):
    print('=' * len(tit))
    print(f'{tit:^}')
    print('=' * len(tit))


data = datetime.now()
data_string = data.strftime('%d/%m/%Y %H:%M')

sg.theme('Dark Purple7')

layout = [
    [sg.Text('Calculo IMC, Percentual de gordura e superfície corporal')],
    [sg.Text('Digite seu NOME', size=(14, 1)), sg.Input(size=(30, 1), key='nome')],
    [sg.Text('Digite seu PESO', size=(14, 1)), sg.Input(size=(10, 1), key='peso'), sg.Text('Kg')],
    [sg.Text('Digite sua ALTURA', size=(14, 1)), sg.Input(size=(10, 1), key='altura'), sg.Text('em (cm)')],
    [sg.Text('Digite sua IDADE', size=(14, 1)), sg.Input(size=(4, 1), key='idade')],
    [sg.Radio('Homem', 1, key='sexo'), sg.Radio('Mulher', 0, key='sexo')],
    [sg.Button('Calcular'), sg.Button('Limpar', key='clear'), sg.Button('Sair')],
    [sg.Output(size=(52, 14))],
    [sg.Text('Desenvolvedor: Gustavo Duran', size=(40, 0))]
]

sexo = 'sexo'

janela = sg.Window('Calculo IMC', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    if evento == 'Limpar':
        continue
    if evento == 'Calcular':
        nome_entrada = valores['nome']
        peso_entrada = valores['peso']
        altura_centimetros = valores['altura']
        idade_entrada = valores['idade']
        sexo_entrada = valores['sexo']
        valor_nome = str(nome_entrada)
        valor_peso = float(peso_entrada)
        valor_altura = float(altura_centimetros)
        altura_metros = valor_altura / 100
        valor_idade = int(idade_entrada)
        valor_sexo = int(sexo_entrada)

        if sexo == 'M':
            sexo = 0
        else:
            sexo = 1

        imc = valor_peso / altura_metros ** 2
        pg1 = ((1.20 * imc) + (0.23 * valor_idade) - (10.8 * valor_sexo) - 5.4)
        sc1 = (((valor_peso * 4) + 7) / (valor_peso + 90))

        nome = f'{valor_nome}'
        peso = f'{valor_peso}'
        altura = f'{altura_metros}'
        idade = f'{valor_idade}'
        sc = f'{sc1:.1f}'
        pg = f'{pg1:.1f}'
        pg_teste = f'{int(pg1)}'

        peso_texto = str(peso).replace('.', ',')
        altura_texto = str(altura).replace('.', ',')
        sc_texto = str(sc).replace('.', ',')
        pg_texto = str(pg).replace('.', ',')

        titulo(data_string)
        print(f' • {nome}')
        print(f' • Peso {peso_texto}kg')
        print(f' • Altura {altura_texto}')
        print(f' • Idade {idade} anos')
        print(f' • Superfície Corporal {sc_texto}(m²)')
        print(f' • IMC {imc:.1f}(kg/m²)')

        # IMC
        if imc < 16:
            print(f' • {nome}, você está abaixo do peso (grau I)')
        elif imc < 17:
            print(f' • {nome}, você está abaixo peso (grau II)')
        elif imc < 18.5:
            print(f' • {nome}, você está abaixo peso (grau III)')
        elif imc < 25:
            print(f' • Parabéns {nome}, você está com o Peso ideal')
        elif imc < 30:
            print(f' • {nome}, você está com Sobrepeso')
        elif imc < 35:
            print(f' • {nome}, você está no grau I de Obesidade')
        elif imc < 40:
            print(f' • {nome}, você está no grau II de Obesidade')
        else:
            print(f' • {nome}, você está no grau III de Obesidade')

        print(f' • Percentual de gordura {pg_texto}%')

        # Percentual de Gordura Corporal (Mulher)
        if valor_sexo == 0:
            if valor_idade <= 39:
                if pg1 < 21:
                    print(f' • {nome}, você está com pouca gordura')
                elif pg1 <= 33:
                    print(f' • {nome}, você está saudável')
                elif pg1 <= 39:
                    print(f' • {nome}, você está acima do percentual de gordura')
                else:
                    print(f' • Cuidado {nome}, você está com Obesidade')
            elif valor_idade <= 59:
                if pg1 < 23:
                    print(f' • {nome}, você está com pouca gordura')
                elif pg1 <= 35:
                    print(f' • {nome}, você está saudável')
                elif pg1 <= 40:
                    print(f' • {nome}, você está acima do percentual de gordura')
                else:
                    print(f' • Cuidado {nome}, você está com Obesidade')
            elif valor_idade <= 79:
                if pg1 < 24:
                    print(f' • {nome}, você está com pouca gordura')
                elif pg1 <= 36:
                    print(f' • {nome}, você está saudável')
                elif pg1 <= 42:
                    print(f' • {nome}, você está acima do percentual de gordura')
                else:
                    print(f' • Cuidado {nome}, você está com Obesidade')

        # Percentual de Gordura Corporal (Homem)
        elif valor_sexo == 1:
            if valor_idade <= 39:
                if pg1 < 8:
                    print(f' • {nome}, você está com pouca gordura')
                elif pg1 <= 20:
                    print(f' • {nome}, você está saudável')
                elif pg1 <= 25:
                    print(f' • {nome}, você está acima do percentual de gordura')
                else:
                    print(f' • Cuidado {nome}, você está com Obesidade')
            elif valor_idade <= 59:
                if pg1 < 11:
                    print(f' • {nome}, você está com pouca gordura')
                elif pg1 <= 22:
                    print(f' • {nome}, você está saudável')
                elif pg1 <= 28:
                    print(f' • {nome}, você está acima do percentual de gordura')
                else:
                    print(f' • Cuidado {nome}, você está com Obesidade')
            elif valor_idade <= 79:
                if pg1 < 13:
                    print(f' • {nome}, você está com pouca gordura')
                elif pg1 <= 25:
                    print(f' • {nome}, você está saudável')
                elif pg1 <= 30:
                    print(f' • {nome}, você está acima do percentual de gordura')
                else:
                    print(f' • Cuidado {nome}, você está com Obesidade')
        else:
            print(' • Algo errado não está certo')


janela.close()
