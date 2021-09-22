from random import randint
import time

count = 0
sala = "1"

print("\tOlá, bem vindo ao jogo Python Dangeon!\n")
time.sleep(2)
print("\tHoje você será o líder de uma guilda de heróis.\n")
time.sleep(3)
print("\tComo todo bom líder, você deverá guiar os guerreiros através do labirinto.\n")
time.sleep(3)
print("\tBoa Sorte!\n")
time.sleep(1)


def caminho1():
    caminho = {
        "1": "2", 
        "2": "3"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

def caminho2():
    caminho = {
        "1": "3", 
        "2": "4"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

def caminho3():
    caminho = {
        "1": "4", 
        "2": "5"
    }
    escolheu = input("[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

def caminho4():
    caminho = {
        "1": "5", 
        "2": "6"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

def caminho5():
    caminho = {
        "1": "6", 
        "2": "7"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

def caminho6():
    input("\n[1] - Caminho preto\n\n")
    return "8"

def caminho7():
    caminho = {
        "1": "8", 
        "2": "9"
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

def caminho8():
    caminho = {
        "1": "9", 
        "2": str(randint(1, 5))
    }
    escolheu = input("\n[1] - Caminho vermelho\n[2] - Caminho preto\n\n")
    return caminho[escolheu]

def caminho9():
    print("\nParabéns!! Você encontrou o fim da Caverna!!")
    return True

caminhos = {
    "1": caminho1,
    "2": caminho2,
    "3": caminho3,
    "4": caminho4,
    "5": caminho5,
    "6": caminho6,
    "7": caminho7,
    "8": caminho8,
    "9": caminho9
}

while sala != True:

    print("Você está na sala ", sala)

    try:  
        sala = caminhos[sala]()
    except KeyError:
        print("\nHmm... O valor que você selecionou parece ser inválido!")
        print("\nDigite apenas os valores 1 ou 2!\n")    
        continue

    if count == 7: 
        print("\nHmm... O limite de tentativas foi excedido, tente novamente!")
        break
        
    count += 1


