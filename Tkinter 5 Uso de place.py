#Uso de Place
import tkinter as tk	#Importamos la libreria Tkinter
#Agregar una ventana


#Etiquetas
#Label(objeto contenedor, diccionario con caracteristicas)
#Label(contenedor, text="opcion", fg="color texto", bg="color fondo", font = (FUENTE, TAMAÑO), 

class Interfaz:
	def  __init__(self, contendor):
		self.e1 = tk.Label(contendor, text = "Etiqueta 1",	fg = "black", bg = "white")

					#Asignamos posiciones
						#(posicion x, posicion y, ancho, alto)
		self.e1.place(x=20, y = 30, width = 120, height = 25)
		

ventana = tk.Tk()
ventana.title("Tkinter Ventana")	
ventana.geometry("400x400")	

#Creamos la instancia de la interfaz
miInterfaz = Interfaz(ventana)


ventana.mainloop()	#Crea un cliclo infinito que minitorea las acciones en la ventana





