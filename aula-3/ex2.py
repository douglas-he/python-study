import random


palavras = ["teste1", "teste2", "teste3"]
scrambled_word = []
for word in palavras:
    scrambled_word.append("".join(random.sample(word, len(word))))

index = random.choice(range(len(palavras)))
print(scrambled_word[index])

response = ""
tentativas = 0
while response != palavras[index] and tentativas < 3:
    response = input("Digite a palavra:\n")
    tentativas += 1

if response != palavras[index]: 
    print('palavra Errada')
else:
    print('palavra Correta')