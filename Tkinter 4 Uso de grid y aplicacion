#Uso de Grid y aplicacion
import tkinter as tk	#Importamos la libreria Tkinter
#Agregar una ventana


#Etiquetas
#Label(objeto contenedor, diccionario con caracteristicas)
#Label(contenedor, text="opcion", fg="color texto", bg="color fondo", font = (FUENTE, TAMAÑO), 

class Interfaz:
	def  __init__(self, contendor):
		self.e1 = tk.Label(contendor, text = "Etiqueta 1",	fg = "black", bg = "white")
		self.e2 = tk.Label(contendor, text = "Etiqueta 2",	fg = "black", bg = "gray")
		self.e3 = tk.Label(contendor, text = "Etiqueta 3",	fg = "black", bg = "green")
		self.e4 = tk.Label(contendor, text = "Etiqueta 4",	fg = "black", bg = "blue")
		self.e5 = tk.Label(contendor, text = "Etiqueta 5",	fg = "black", bg = "yellow")
		self.e6 = tk.Label(contendor, text = "Etiqueta 6",	fg = "black", bg = "red")

					#Asignamos posiciones
		self.e1.grid(column = 0, row = 0)
		self.e2.grid(column = 0, row = 1)
		self.e3.grid(column = 0, row = 2)
		self.e4.grid(column = 1, row = 0)
		self.e5.grid(column = 1, row = 1)
		self.e6.grid(column = 1, row = 2)

ventana = tk.Tk()
ventana.title("Tkinter Ventana")	
ventana.geometry("400x400")	

#Creamos la instancia de la interfaz
miInterfaz = Interfaz(ventana)


ventana.mainloop()	#Crea un cliclo infinito que minitorea las acciones en la ventana





