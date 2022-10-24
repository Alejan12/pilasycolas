from collections import deque
cola=deque()
cola.append("hoja1")
cola.append("hoja2")
cola.append("hoja3")
print(f"esta es la cola: {cola}")
while len(cola)>0:
    siguente=cola.popleft()
    print(f"Siguiente elemento: {siguente}")
    print(f"Cola de impresion: {cola}")
    print("#####")