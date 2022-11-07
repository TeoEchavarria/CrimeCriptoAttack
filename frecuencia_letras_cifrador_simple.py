# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:19:50 2022

@author: Mateo
"""

texto_plano = " Una vez mas se encontro en el gran vestibulo muy cerca de la mesita de cristal Esta vez hare las cosas mucho mejor se dijo a si misma Y empezo por coger la llavecita de oro y abrir la puerta que daba al jardin Entonces se puso a mordisquear cuidadosamente la seta se habia guardado un pedazo en el bolsillo hasta que midio poco mas de un palmo Entonces se adentro por el estrecho pasadizo Y entonces entonces estuvo por fin en el maravilloso jardin entre las flores multicolores y las frescas fuentes "
texto_plano = texto_plano.replace(" ","").lower()
texto_cifrado = texto_plano[::]

from collections import Counter
count_text_plano = Counter(texto_plano)
num = len(count_text_plano)

import random 
abecedario = "etaonihsrlducmwyfgpbvkjxqz"
perm_abecedario = list(random.sample(abecedario.upper(), 26))

for p in range(26):
    texto_cifrado = texto_cifrado.replace(abecedario[p], perm_abecedario[p])
    
count_text_cifrado = Counter(texto_cifrado)
    
import matplotlib.pyplot as plt

plt.title("Frecuencia de letras en Texto Plano")
plt.bar([ abecedario[i] for i in range(num)], count_text_plano.values())
plt.show()

plt.title("Frecuencia de letras en Texto Cifrado")
plt.bar([ perm_abecedario[i] for i in range(num)], count_text_cifrado.values(), color = "r")
plt.show()