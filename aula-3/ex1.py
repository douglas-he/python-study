name = input("Digite seu Nome")
lenght = len(name)
while lenght > 0:
    name = name[:-1]
    print(name)
    lenght -= 1
