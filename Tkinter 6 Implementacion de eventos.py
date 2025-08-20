#Implementacion de eventos
import tkinter as tk	#Importamos la libreria Tkinter
#Agregar una ventana


#Etiquetas
#Label(objeto contenedor, diccionario con caracteristicas)
#Label(contenedor, text="opcion", fg="color texto", bg="color fondo", font = (FUENTE, TAMAÑO), 

class Interfaz:
	def  __init__(self, contendor):
		self.textoE3 = tk.StringVar()

		self.e1 = tk.Label(contendor, text = "Convertir Celsius a Fahrenheit",	fg = "black")
		self.e2 = tk.Label(contendor, text = "Celsius",	fg = "black")
		self.e3 = tk.Label(contendor, text = "Fahrenheit",	fg = "black")
		self.e4 = tk.Button(contendor, text = "Convertir",	fg = "black", bg = "cyan", command = self.hacerConverion)
		self.e5 = tk.Entry(contendor,	fg = "black", bg = "white")
		self.e6 = tk.Label(contendor, text = "",	fg = "black", bg = "red", textvariable=self.textoE3) #Se modifica dinamicamente el texto de la etiqueta

					#Asignamos posiciones
		self.e1.grid(column = 0, row = 0, columnspan = 2)
		self.e2.grid(column = 0, row = 1)
		self.e3.grid(column = 0, row = 2)
		self.e4.grid(column = 0, row = 3, columnspan = 2)
		self.e5.grid(column = 1, row = 1)
		self.e6.grid(column = 1, row = 2)

	def hacerConverion(self):
		#Obtenemos el valor del texto y se convierte a decimal
		cel=float(self.e5.get())
		far = (cel*1.8) + 32
		self.textoE3.set(far)
		#get() = leer
		#set() =  escribir
		

ventana = tk.Tk()
ventana.title("Celsius a Fahrenheit")	
ventana.geometry("300x100")	

#Creamos la instancia de la interfaz
miInterfaz = Interfaz(ventana)


ventana.mainloop()	#Crea un cliclo infinito que minitorea las acciones en la ventana





