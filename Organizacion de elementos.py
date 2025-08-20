#Uso de PACK
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

					#Asignamos posiciones
		self.e1.pack(side = tk.TOP) 
		self.e2.pack(side = tk.RIGHT)
		self.e3.pack(side = tk.BOTTOM, fill = tk.X) #fill ajusta el ancho a la ventana

ventana = tk.Tk()
ventana.title("Tkinter Ventana")	
ventana.geometry("400x400")	

#Creamos la instancia de la interfaz
miInterfaz = Interfaz(ventana)


ventana.mainloop()	#Crea un cliclo infinito que minitorea las acciones en la ventana





