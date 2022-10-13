# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados
def generar_invitados():
    invitado_1 = input('Ingresar el nombre del primer invitado: ')
    invitado_2 = input('Ingresar el nombre del segundo invitado: ')
    invitado_3 = input('Ingresar el nombre del tercer invitado: ')

    lista_invitados = [invitado_1, invitado_2, invitado_3]

    return lista_invitados



# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Crear la función "generar_invitados"

    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar

    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:

    lista_invitados = generar_invitados()

    # Imprimir en pantalla "lista_invitados":

    print('Los invitados son los siguientes: ', lista_invitados)
    print("terminamos")
