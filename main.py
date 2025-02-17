from sys import exit
from math import sqrt
from time import sleep
from os import system, name

def cls():
    system('cls') if name == 'nt' else 'clear' # Limpar terminal
cls()

def menu():
    while True:
        try:
            cls()
            print("FORMULAS DA FÍSICA\n[1] Força Gravitacional\n[2] Dilatação temporal\n[3] Sair\n")
            entrada = int(input("Digite: "))

            opcoes = {
                1: forca_grav,
                2: dilatacao,
                3: exit
            }

            if entrada in opcoes:
                opcoes[entrada]()
            else:
                print("Escolha um número válido.")
                sleep(2)
                cls()

        except ValueError:
            print("Escolha apenas números válidos.")
            sleep(2)
            cls()

def forca_grav():
    # Constante gravitacional:
    constante_grav = 6.6743e-11

    massa1 = float(input("A primeira massa é (kg): "))
    massa2 = float(input("A segunda massa é (kg): "))
    distancia = float(input("A distância é (m): "))

    resultado = constante_grav * massa1 * massa2 / distancia**2
    print(f"A força gravitacional é: {resultado:.1e} N")
    system('pause')

def dilatacao():
    observador_horas = float(input("Tempo experimentado pelo observador longe (em horas): "))
    observador_longe = observador_horas * 3600

    constante_gravitacional = 6.67e-11
    massa_buraco_negro = 10 * 1.989e30  # 10 massas solares
    
    raio_buraco_negro = 30_000  # Aproximadamente 30 km

    velocidade_luz = 3.00e8

    # Cálculo da dilatação temporal
    fator_dilatacao = sqrt(1 - (2 * constante_gravitacional * massa_buraco_negro) / (raio_buraco_negro * velocidade_luz**2))
    resultado = observador_longe * fator_dilatacao
    resultado_horas = resultado / 3600

    print(f"O tempo dilatado é: {resultado_horas:.2f} horas")
    system('pause')

menu()
