def calcular_equacao_primeiro_grau(a, b):
    # Calcula o valor de x para a função do 1º grau (ax + b = 0)
    if a != 0:
        x = -b / a
        return x
    else:
        return "O valor de 'a' não pode ser zero."

def main():
    # Recebe os valores de 'a' e 'b' do usuário
    a = float(input("Digite o valor de 'a': "))
    b = float(input("Digite o valor de 'b': "))
    
    # Chama a função para calcular o valor de x
    resultado = calcular_equacao_primeiro_grau(a, b)
    
    # Mostra o resultado
    print(f"O valor de 'x' é: {resultado}")

# Executa a função principal
if __name__ == "__main__":
    main()
