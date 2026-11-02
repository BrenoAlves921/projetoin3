
def main():
    notas = [10, 12, 9, 15, 20]
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual é a sua idade? "))

    print("Seu nome é", nome, "e a sua idade é", idade)

    if idade >= 18:
        print("\nVocê é maior de idade")
        maioridade = True
    else:
        print("\nVocê é menor de idade")
        maioridade = False

    if maioridade:
        print("\n\tSuas notas:")
        print("========================")
        i=1
        for nota in notas:
            print(f"Nota{i}: {nota}")
            i= i+1
    else:
        print("\nNão poderá ver suas notas")

main()
