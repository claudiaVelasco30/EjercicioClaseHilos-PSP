import threading
import time

#Clase que hereda de la clase Thread
class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombreArchivo, numLineas):
        super().__init__()

        #Guardamos el nombre del archivo y el número de líneas a procesar
        self.nombreArchivo = nombreArchivo
        self.numLineas = numLineas

    #Metodo que se ejecuta al iniciar el hilo
    def run(self):
        lineaActual = 1 #Inicializamos el contador de la línea actual en 1

        #Iteramos por el número total de líneas que de van a procesar
        for _ in range (self.numLineas):
            #Imprimimos los datos
            print(f"Procesando {self.nombreArchivo} - Línea {lineaActual}")
            lineaActual += 1 #Pasamos a la siguiente línea
            time.sleep(0.5) #Pausa de 0.5 segundos

#Lista para almacenar los "archivos" con las líneas
listaArchivos = ["Hola\nHola\nHola", "Hola\nHola", "Hola\nHola\nHola"]

#Lista para almacenar los hilos
hilos = []

#Iteramos sobre la lista de archivos y creamos un hilo para cada uno
for i in range(len(listaArchivos)):
    nombre = f"Archivo {i + 1}" #Asignamos un nombre al archivo
    lineasAProcesar = 1

    #Contamos el número de líneas
    for letra in listaArchivos[i]:
        if letra == "\n":
            lineasAProcesar += 1

    #Creamos el hilo pasándole los prámetros
    hilo = ProcesadorArchivo(nombreArchivo=nombre, numLineas=lineasAProcesar)

    #Añadimos el hilo a la lista de hilos y lo iniciamos
    hilos.append(hilo)
    hilo.start()

#Esperamos a que todos los hijos terminen
for hilo in hilos:
    hilo.join()

print("Los hilos han finalizado")