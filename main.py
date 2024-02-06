# Calcula o fatorial de numero (numero!)
def somatoria(numero):
    if numero == 0 or numero == 1:
        return 1
    return somatoria(numero - 1) + numero

# Calcula a somatória de 1 a numero
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return fatorial(numero - 1) * numero


# __main__
if __name__ == '__main__':
    print(fatorial(10))
    print(somatoria(10))
