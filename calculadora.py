def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def calcular(operacao, a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os argumentos devem ser números (int ou float).")
    if operacao == 'adicionar':
        return adicionar(a, b)
    elif operacao == 'subtrair':
        return subtrair(a, b)
    elif operacao == 'multiplicar':
        return multiplicar(a, b)
    elif operacao == 'dividir':
        return dividir(a, b)
    else:
        raise ValueError("Operação inválida. Use 'adicionar', 'subtrair', 'multiplicar' ou 'dividir'.")
