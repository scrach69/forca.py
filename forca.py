import random
import os

# Função de Forca 
def jogar_forca():
    print("JOGO DA FORCA")
    print("Escolha o tema:")
    print("1 - Animais")
    print("2 - Culinaria")
    print("3 - Tecnologia")
    
    tema = input("Digite o número do tema (1-3): ")
    
    if tema == '1': 
        arquivo = 'animais.txt'
    elif tema == '2': 
        arquivo = 'culinaria.txt'
    elif tema == '3': 
        arquivo = 'tecnologia.txt'
    else:
        print("Tema inválido! Voltando ao menu.")
        return

    # Lê as palavras do arquivo
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            palavras = [linha.strip().lower() for linha in f]
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado! Verifique se o arquivo está no diretório.")
        return

    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_secreta]
    erros = 0
    letras_tentadas = []

    # Loop do jogo da forca
    while erros < 6 and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print(f"Erros: {erros}/6")
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_tentadas:
            print("Você já tentou essa letra!")
            continue
        
        letras_tentadas.append(tentativa)

        if tentativa in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_descobertas[i] = tentativa
        else:
            erros += 1 # Lógica de erros corrigida
            print(f"Letra errada! Você tem {6 - erros} tentativas restantes.")

    if "_" not in letras_descobertas:
        print(f"\nParabéns! Você acertou: {palavra_secreta}")
    else:
        print(f"\nVocê foi enforcado! A palavra era: {palavra_secreta}")

# Função de Adivinhação
def jogar_adivinhacao():
    print("\n--- JOGO DA ADIVINHAÇÃO ---")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))
            if chute < 1 or chute > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
            tentativas += 1
            if chute == numero_secreto:
                print(f"Acertou em {tentativas} tentativas!")
                break
            elif chute < numero_secreto:
                print("Maior...")
            else:
                print("Menor...")
        except ValueError:
            print("Entrada inválida! Digite um número.")

# Menu Principal
def menu_principal():
    while True: # Laço infinito
        print("\nMENU DE JOGOS")
        print("1 - Jogar Forca")
        print("2 - Jogar Adivinhação")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            jogar_forca()
        elif opcao == '2':
            jogar_adivinhacao()
        elif opcao == '0':
            print("Saindo... Tchau!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
