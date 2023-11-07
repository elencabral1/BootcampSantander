print('Exemplo Lista/Arrays')

lista_numeros = []  
numero_atual = 1 

while len(lista_numeros) < 20: 
    if (numero_atual % 2 == 0) or (numero_atual % 5 == 0):
        lista_numeros.append(numero_atual)  
    numero_atual += 1 


print("Os primeiros 20 números divisíveis por 2 e por 5 são:")
for numero in lista_numeros:
    print(numero)
