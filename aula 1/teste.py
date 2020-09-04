import math


list_numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]
list_names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def maior_num(num1, num2):
    if num1 < num2:
        return num2
    return num1


def menor_num(lista):
    valor = lista[0]
    for number in lista:
        if valor > number:
            valor = number
    return valor


def media(lista):
    media_lista = 0
    soma = 0
    for number in lista:
        media_lista = media_lista + number
        soma += 1
    return media_lista / soma


def imprime_asterisco(inteiro):
    aux = 0
    while aux < inteiro:
        print("*" * inteiro)
        aux += 1
    return ""


def imprime_semi_piramide(inteiro):
    aux = 1
    while aux <= inteiro:
        print("*" * aux)
        aux += 1
    return ""


def maior_nome(lista):
    nome_final = ""
    for nome in lista:
        if len(nome) > len(nome_final):
            nome_final = nome
    return nome_final


def soma_inteiros(inteiro):
    return sum(range(1, inteiro + 1))


def tinta_total(parede):
    quantidade = math.ceil(parede / (18 * 3))
    return (quantidade, quantidade * 80)


def triagulo_valido(lado1, lado2, lado3):
    conjunto = set([lado1, lado2, lado3])
    if len(conjunto) == 1:
        return 'Triângulo Equilátero: três lados iguais;'
    elif len(conjunto) == 2:
        return 'Triângulo Isósceles: quaisquer dois lados iguais;'
    return 'Triângulo Escaleno: três lados diferentes.'


print(maior_num(1, 2))
print(menor_num(list_numbers))
print(media(list_numbers))
print(imprime_asterisco(2))
print(imprime_semi_piramide(4))
print(maior_nome(list_names))
print(soma_inteiros(5))
print(tinta_total(100))
print(triagulo_valido(1, 1, 1))
