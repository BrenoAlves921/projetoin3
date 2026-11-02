def somatorio(n: int) -> int: 
        soma = 0
        for i in range (1, n + 1):
              soma = soma + i
              print(soma)
              
        




def main() -> None:
    n = int(input("Insira um numero: "))
    print(f"{somatorio(n)}")
    



main()
    