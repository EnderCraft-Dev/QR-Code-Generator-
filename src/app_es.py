from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from uuid import uuid4

import png
import pyqrcode 

from time import sleep

class App:
	def __init__(self):
		self.app = Tk()
		self.app.title("Generador de códigos QR")
		self.app.geometry('430x200')
		self.app.resizable(False,False)
		self.app['bg'] = 'teal'

		# menu
		mainmenu = Menu(self.app)

		toolsmenu = Menu(mainmenu, tearoff=0)
		toolsmenu.add_command(label="Generar Código QR", command=self.generate_code)

		mainmenu.add_cascade(label="Herramientas", menu=toolsmenu)
		mainmenu.add_command(label="Limpiar", command=self.reset_values)
		mainmenu.add_command(label="Salir", command=self.exit_app)

		self.app.config(menu=mainmenu)

		# url entry
		url_lbl = Label(self.app, text="ENLACE DE DESTINO:", font="bold 12", fg="white")
		url_lbl.place(x=10,y=7)
		url_lbl['bg'] = 'teal'

		self.urlVar = StringVar()
		url_entry = Entry(self.app, width=65, textvariable=self.urlVar)
		url_entry.place(x=10,y=30)

		# image config
		name_lbl = Label(self.app, text="NOMBRE DEL ARCHIVO PNG:", font="bold 12", fg='white')
		name_lbl.place(x=10,y=65)
		name_lbl['bg'] = 'teal'

		self.nameVar = StringVar()
		url_entry = Entry(self.app, width=65, textvariable=self.nameVar)
		url_entry.place(x=10,y=90)

		# scale config
		name_lbl = Label(self.app, text="ESCALA DE LA IMAGEN\n(Valores recomendables: Enteros del 1 al 10)", font="bold 12", fg='white')
		name_lbl.place(x=10,y=125)
		name_lbl['bg'] = 'teal'

		self.scaleVar = IntVar()
		url_entry = Entry(self.app, width=30, textvariable=self.scaleVar)
		url_entry.place(x=10,y=170)


	def exit_app(self):
		self.app.quit()

	def reset_values(self):
		self.urlVar.set(" ")
		self.nameVar.set(" ")
		self.scaleVar.set(0)

	def generate_code(self):
		url = self.urlVar.get()
		name = self.nameVar.get()
		
		try:
			scale = self.scaleVar.get()
			scale = int(scale)
			if(len(url) > 0 and len(name) > 0 and scale > 0):
				try:
					code = pyqrcode.create(url)
					filename = f"{name.upper()}_{str(uuid4())}.png"
					with open(filename, 'wb') as qr:
						code.png(qr, scale=scale)
					messagebox.showinfo("Generador de códigos QR", "Archivo guardado como {}".format(filename))
				except:
					messagebox.showerror("Error", "Ha ocurrido un error")
			else:
				messagebox.showerror("Error", "Ingresa una URL de destino y un nombre para el archivo PNG\nLa escala debe ser > 0")
		except:
			messagebox.showerror("Error", "Solo valores numericos")

	def run(self):
		self.app.mainloop()

if __name__=="__main__":
	GUI = App()
	GUI.run()