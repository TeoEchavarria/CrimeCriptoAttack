# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:20:29 2022

@author: MATEO
"""

aut_cookie = """
POST / HTTP/1.1
Pedro Picapiedra=123124141; expires=8/11/2022; max-age=10; path=/triple-plato; domain=thebankserver.com; secure; httponly
Host: thebankserver.com
Tales de tales
Cookie: secret=cxc89f+94/wa
Mas textico por aqui
"""
import string
abecedario = list(dict.fromkeys(string.ascii_lowercase, 0).keys())
abecedario.extend(list(dict.fromkeys(string.ascii_uppercase, 0).keys()))
abecedario.extend([i for i in "0123456789_áéíóúÁÉÍÓÚüÜ«»,.;-+\?¿!¡()'\"ñ]*$]"])
print(abecedario, len(abecedario))

hack_cookie = "Cookie: secret="

for i in range(12):
  min_len = None
  letter_aux = ""
  print("\n LETTER")
  for letter in abecedario:
    hack_cookie_aux = hack_cookie + letter
    solicitud_http = bytes( aut_cookie + "\n" + hack_cookie_aux, encoding = "utf-8")
    #print(solicitud_http)

    import deflate
    compressed = deflate.gzip_compress(solicitud_http, 6)
    #print(compressed)

    len_compressed = sys.getsizeof(compressed)

    import sys
    if min_len == None:
      min_len = len_compressed
      letter_aux = letter
    elif len_compressed < min_len:
      min_len = len_compressed
      letter_aux = letter
      #Si hay otro que tenga el mismo tamaño se prueba entonces tambein con ese y se toma en el que el proximo es menor
    print(sys.getsizeof(solicitud_http),len_compressed, letter)

  hack_cookie += letter_aux
  print(hack_cookie, letter_aux, min_len)
print(hack_cookie)

#for i in abecedario:
    
