
# coding: utf-8

## Programación para *Data Science*

### Unidad 2: Breve introducción a la programación en Python

# Ejercicios y preguntas teóricas
# -------------------------------
# 
# A continuación, encontraréis la parte que tenéis que completar en este módulo y las preguntas teóricas que debéis contestar.
# 
# Podéis encontrar en la documentación oficial de *string* funciones que os puedan ser de ayuda para completar los ejercicios: https://docs.python.org/2/library/string.html

# ### Pregunta 1
# ¿Cuál es la diferencia entre definir un string con comillas simples (' '), comillas dobles(" ") y tres comillas dobles (""" """)?
# 
# #### Respuesta:
# 

# Las comillas simples (' ') y las comillas dobles (" ") puedes utilizarse de forma intercambiable, si bien existe un caso en que deberíamos elegir una u otra: si la cadena de texto o string que queremos definir mediante comillas incluye comillas dentro del mismo, utilizaremos el tipo de comillas opuesto para definir el string. De esta forma, evitaremos que el intérprete Python detecte el fin de la cadena de texto a mitad de frase. Por ejemplo:

# In[1]:

texto_1 = 'Mi libro favorito se titula "El retrato de Dorian Gray".'
print texto_1


# Si, por el contrario, definiéramos dicho string mediante comillas dobles, obtendríamos un error:

# In[2]:

texto_2 = "Mi libro favorito se titula "El retrato de Dorian Gray"."
print texto_2


# Hemos obtenido un error de "sintaxis inválida" debido a que el intérprete ha utilizado la primera comilla doble (correspondiente a la cita del libro) como el final de la cadena de texto. En consecuencia, el nombre del libro no se encuentra dentro de la definición del string, generado el error de sintaxis.
# Finalmente, las comillas triples (""" """ o ''' ''') cumplen la misma funcionalidad que las dobles y las simples, con una salvedad: respetan los saltos de línea especificados en el string definido, sin necesidad de codificarlos como "\n". Veamos un ejemplo:

# In[4]:

texto_3 = """Gama colores fríos:
- Azul
- Gris
- Violeta"""
print texto_3


# Sin embargo, utilizando comillas dobles se rompe la cadena de texto y se nos notifica un error de sintaxis:

# In[5]:

texto_4 = "Gama colores fríos:
- Azul
- Gris
- Violeta"
print texto_4


# Si deseamos mantener el formato sin utilizar comillas triples, debemos utilizar "\n" para definir los saltos de línea: 

# In[6]:

texto_5 = "Gama colores fríos: \n - Azul \n - Gris \n - Violeta"
print texto_5


# ### Pregunta 2
# ¿Qué expresión en Python necesitamos para conseguir el string "DATADATADATADATA" utilizando solo la palabra "DATA"?
# 
# #### Respuesta:

# In[8]:

# Definimos un string con el texto que queremos multiplicar y realizamos la operación sobre él
texto = "DATA"
texto_multiple = texto*4
# Comprobamos el resultado mostrándolo por pantalla 
print texto_multiple


# ### Pregunta 3
# 
# **¿Cuál es el valor final de a, b y c (atención a los tipos de número decimal y entero)?**
# 
# a = 3*2
# 
# b = 9/2.
# 
# c, a = a+1, b*2
# 
# #### Respuesta:

# Las operaciones se realizan secuencialmente. Notamos que la variable "a" está definida como entero (int), mientras que el punto (.) al final de la operación de "b" define dicha variable como como decimal (float). Por tanto, obtenemos "a=6" (int) y "b=4.5" (float).
# 
# La última expresión define una nueva variable "c", la cual también será entera, ya que opera únicamente con valores enteros ("a" y "1"). Además, se asigna un nuevo valor a la variable "a". En este caso, "a=b\*2=4.5\*2=7.0", transformando "a" en decimal (float). Dicho cambio se debe a que las operaciones implicaban tanto valores valores decimales ("b") como enteros ("2"), imponiéndose el formato decimal en el resultado, ya que proporciona una mayor precisión y es por ende priorizado por el intérprete Python en caso de conflicto.
# 
# Así pues, los resultados finales son: a=9.0 b=4.5 y c=7. Lo comprobamos mediante la ejecución de código:

# In[20]:

a=3*2
b=9/2.
c, a = a+1, b*2
print a, b, c


# ### Pregunta 4
# 
# **Marcad las expresiones incorrectas y explicad el porqué.**
# * planetas = ('Saturno', 'Jupiter' 'Tierra')
# * t = '123','abc'
# * dias = ['Lunes', 'Martes', "Miercoles", ''.join(['J','u','e','v','e','s'])]
# * matriz = [[],[],[]]
# 
# **Respuesta:**

# - Incorrecto: El último elemento de la tupla "planetas", 'Tierra' no está separado del anterior, 'Júpiter'. De este modo, se está definiendo un vector de tan sólo dos elementos, 'Saturno' y 'JupiterTierra', ya que el intérprete Python ignora los espacios que no se encuentren entre comillas. Sería necesario añadir una coma (,) en su lugar.
# - Correcto
# - Correcto
# - 

# In[31]:

planetas = ('Saturno', 'Jupiter' 'Tierra')
t = '123','abc'
dias = ['Lunes', 'Martes', "Miercoles", ''.join(['J','u','e','v','e','s'])]
matriz = [[],[],[]]

print planetas
print t
print dias
print matriz


# ### Pregunta 5
# 
# Explicad a qué se refieren con el término "batteries included" en la comunidad Python. Poned algunos ejemplos de paquetes de la librería estándar y una breve explicación de cada uno de ellos.
# 
# **Respuesta:**

# El término "batteries included" hace referencia a la librería estándar de Python, la cual incluye multitud de paquetes...

# ### Pregunta 6
# 
# Python dispone de un idiom muy útil conocido como list comprehensions. ¿Podéis explicar en qué consiste? Indicad tres ejemplos de código que utilicen este idiom y documentad cada parte de código relevante.
# 
# **Respuesta:**

# Respuesta

# ### Ejercicio 1
# 
# Escribid un programa que asigne dos valores enteros cualesquiera (escoged un número entero aleatorio) a dos variables con nombre a y b, calcule el producto de a por b y finalmente muestre el valor del cuadrado del producto de a por b.
# 
# #### Respuesta:

# In[8]:

# Respuesta


# ### Ejercicio 2
# 
# Escribid un programa que defina una lista cuyos valores sean los nombres de los días de la semana. Haced que muestre el primer y el último día de la semana.
# 
# #### Respuesta:

# In[1]:

# Respuesta


# ### Ejercicio 3
# 
# Escribid un programa que calcule el área de un círculo de radio 3.
# 
# #### Respuesta:

# In[2]:

# Respuesta


# ### Ejercicio 4
# 
# Escribid un programa donde se defina un diccionario con algunos de los prefijos telefónicos de España. Por ejemplo: 93 para Barcelona, 91 para Madrid, etc.
# 
# #### Respuesta:

# In[3]:

# Respuesta

