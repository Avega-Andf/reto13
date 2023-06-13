def crear_diccionario():
    """
    Crea un diccionario a partir de las entradas del usuario.

    Args:
        None

    Returns:
        dict: Un diccionario creado a partir de las entradas del usuario.
    """
    diccionario = {} # Se crea un diccionario vacio
    tamaño = int(input("Ingrese el tamaño del diccionario: ")) # Se digita el tamaño del diccionario que se quiere crear
    for i in range(tamaño): # Se itera hasta el tamaño ingresado por el usuario
        clave = input("Ingrese la clave: ") # Se digita la clave 
        valor = input("Ingrese el valor: ") # Y se respectivo valor
        diccionario[clave] = valor # Se añade la clave con su valor al diccionario
    return diccionario # Regresa un diccionario

def mezclardiccionarios(dic1, dic2): 
    """
    Combina dos diccionarios en uno nuevo, manteniendo las claves del diccionario uno (dic1)
    en caso de existir claves duplicadas.

    Args:
        dic1 (dict): El primer diccionario.
        dic2 (dict): El segundo diccionario.

    Returns:
        dict: Un nuevo diccionario que combina los valores de ambos diccionarios.
    """
    nuevodiccionario = dic1.copy() # Crea una copia del diccionario uno, (Se trabajara sobre esta copia)
    for clave, valor in dic2.items(): # Por cada clave y valor en el diccionario 2
        if clave in nuevodiccionario: # Si la clave ya estaba en el diccionario 1, no se añade esta y continua analizando los siguientes elementos
            continue
        else:
            nuevodiccionario[clave] = valor # Si la clave del diccionario 2 no estaba en el diccionario uno, se añade la clave y valor al nuevo diccionario
    return nuevodiccionario

if __name__ == "__main__":
# Crear el primer diccionario
    print("Primer diccionario:")
    diccionario1 = crear_diccionario()
    print(diccionario1)

# Crear el segundo diccionario
    print("Segundo diccionario:")
    diccionario2 = crear_diccionario()
    print(diccionario2)
    
# Mezclar los diccionarios
    diccionariomezclado = mezclardiccionarios(diccionario1, diccionario2)

# Imprimir el resultado
    print("Diccionario mezclado:")
    print(diccionariomezclado)