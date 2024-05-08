# Vulnerabilidades y deficiencias en la concurrencia de sistemas de compresión y encripción

El ataque CRIME 🚨, descubierto en 2012 por Juliano Rizzo y Thai Duong, explota vulnerabilidades en la compresión previa a la encriptación 🛡️ en protocolos como TLS, permitiendo a los atacantes deducir información confidencial observando las variaciones en el tamaño de los paquetes cifrados 📦. Este descubrimiento llevó a cambios significativos en la seguridad de los protocolos de comunicación, recomendando desactivar la compresión en TLS. 

### Analogia

Imagina que estás jugando un juego de cartas 🃏 donde el objetivo es adivinar una carta oculta en el mazo de un oponente. Para ayudarte a adivinar, cada vez que haces una suposición, tu oponente añade la carta que tú adivinaste a una caja que ya contiene algunas cartas predeterminadas y luego pesa toda la caja en una balanza ⚖️. El truco es que todas las cartas idénticas pesan menos juntas debido a un "mecanismo de compresión" especial en la caja: cuantas más cartas iguales hay en la caja, menos aumenta el peso total cuando añades una más de la misma.

En este juego, tu objetivo es usar las variaciones en el peso total para deducir cuál es la carta oculta. Si el peso no cambia mucho después de añadir una carta específica, puedes inferir que la carta oculta podría ser la misma que adivinaste, ya que la "compresión" ha sido efectiva 🤔.

### Codigo Auxiliar

Encontraras aquí el codigo usado para generar las graficas utilizadas en el documento, junto con la idea detras del ataque CRIME.

Puede acceder a estos notebooks con el fin de correr el codigo:

- [Grafica de Frecuencia de letras | Sustitución Simple](https://colab.research.google.com/drive/103xlsw4cZCAfpyGIsX-vaAHD1nluFBbn?usp=sharing)

- [Implementación AES-256](https://colab.research.google.com/drive/1LtJqE1dqNz7OISun4VWWQeJ2-kfj5K9k?usp=sharing)

- [SPDY Ataque CRIME - idea principal](https://colab.research.google.com/drive/1LtJqE1dqNz7OISun4VWWQeJ2-kfj5K9k?usp=sharing)

- [TLS Ataque CRIME - idea principal](https://colab.research.google.com/drive/1prWkRECXYI7fWilbzqC9X07c4SYnxAH1?usp=sharing)
