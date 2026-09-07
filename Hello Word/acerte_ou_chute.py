import random

print("tente adivinha um numero de 0 a 100")

tentativas = 0
numero_secreto = random.randint(0, 100)

while True:
    chute = int(input("digite um numero de 0 a 100: "))
    tentativas += 1
    if chute == numero_secreto:
        print("vocẽ acertou")
        break
    elif chute < numero_secreto:
        print("muito baixo, tente um numero maior")
    else:
        print("muito alto, tente um numero baixo")
