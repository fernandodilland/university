'''
De una lista con palabras (mínimo 10 palabras), recuperar aquellas que inicien con vocales
mediante comprensión de listas
'''

palabras = ['manzana', 'naranja', 'pera', 'leche', 'pan', 'sandía','uva','elote','helado','miel']

# Método 1
for palabra in palabras:
    if palabra[0] in 'aeiou':
        print(palabra)
        
# Método 2
vocal=[]
for palabra in palabras:
    if palabra[0] in "aeiou":
        vocal.append(palabra)
print (vocal)

# Método 3
vocal=[]
"""for palabra in palabras:
    if palabra[0] in "aeiou":
        vocal.append(palabra)
print (vocal)"""
vocal = [palabra for palabra in palabras if palabra[0] in "aeiou"]
print(vocal)
# vocal = filter(lambda x : x[0] in "aeiou", palabras)