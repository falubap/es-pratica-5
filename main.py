from calculadora import calcular

def main():
    print("Calculadora Simples")
    print("Escolha uma operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    operacao = input("Digite o número da operação (1/2/3/4): ")
    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida. Tente novamente.")
        return
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira apenas números.")
        return
    operacoes = {
        '1': 'adicionar',
        '2': 'subtrair',
        '3': 'multiplicar',
        '4': 'dividir'
    }
    try:
        resultado = calcular(operacoes[operacao], a, b)
        print(f"O resultado é: {resultado}")
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()