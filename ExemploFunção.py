print('Exemplo Função')

def funcao_obter_numeros():
    lista_numeros_func = []  

    while len(lista_numeros_func) < 10:  
        numero = int(input("Digite um número: "))  
        lista_numeros_func.append(numero)  

    return lista_numeros_func

lista_numeros = []  

print("Vamos obter os números.")
lista_numeros = funcao_obter_numeros()  

print("Agora, vamos mostrar os números:")
print(lista_numeros)  
