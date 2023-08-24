# -*- coding: latin-1 -*-
import random

number = random.randint(0,100)
tentativa = 10
print("qual é o numero?")
while tentativa != number:
    tentativa = int(input())
    if tentativa > number:
        print("O numero é Menor")
    else:
        print("O numero é maior")

print("Você acertou!")