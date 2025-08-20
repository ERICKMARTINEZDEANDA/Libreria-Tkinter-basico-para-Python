import tkinter as tk	#Importamos la libreria Tkinter
#Agregar una ventana


#Etiquetas
#Label(objeto contenedor, diccionario con caracteristicas)
#Label(contenedor, text="opcion", fg="color texto", bg="color fondo", font = (FUENTE, TAMAÑO), 

class Interfaz:
	def  __init__(self, contendor):
		self.e1 = tk.Label(contendor, 
							text = "Etiqueta 1", 
							fg = "black",
							bg = "white",
							font = ("Arial",12),
							pady = 10,	# Espacio vertical (arriba/abajo)
							padx = 15,	# Espacio horizontal (izquierda/derecha)
						)
		self.e1.pack() #Se indica que debe agregar este elementi a su contendor

ventana = tk.Tk()
ventana.title("Tkinter Ventana")	#Colocamos Título a la ventana
ventana.geometry("400x400")	#Le damos tamaño a la ventana

#Creamos la instancia de la interfaz
miInterfaz = Interfaz(ventana)


ventana.mainloop()	#Crea un cliclo infinito que minitorea las acciones en la ventana





