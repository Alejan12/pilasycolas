from collections import deque
historial=deque()
def crear_historial(historial):
    historial.append(input("primera accion: "))
    historial.append(input("segunda accion: "))
    historial.append(input("tercera accion: "))
    historial.append(input("cuarta accion: "))
    print(f"Este es tu historial: {historial}")

crear_historial(historial)
def elimimar_historial(historial):
   
    while len(historial)>0:
        eliminar=historial.pop()
        print(f"Eliminamos tu historial: {eliminar}")
        print(f"Este es tu historial: {historial}")
        print("#####")

elimimar_historial(historial)
