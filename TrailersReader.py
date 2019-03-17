import glob
import webbrowser
import shutil
import os

from PySide2 import *
from PySide2.QtWidgets import *

from mod.func import *

class TrailersReader(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)		
		#-----------------------------------------------------------------------------------------------------------
		self.setWindowTitle("Trailers Reader")
		self.setFixedSize(873, 370)
		self.setWindowIcon(QtGui.QIcon("./mod/icon.ico"))
		#********************************************************************************************
		self.list_dias = QListWidget(self)
		self.list_pelis = QListWidget(self)
		self.borrar_dia = QPushButton(self, text="Borrar!")
		self.dia_visto = QPushButton(self, text="Vista")
		self.peli_arriba = QPushButton(self, text="▲")
		self.peli_abajo = QPushButton(self, text="▼")		
		self.borrar_peli = QPushButton(self, text="Borrar!")
		self.peli_pendiente = QPushButton(self, text="Pendiente")
		self.calendario = QCalendarWidget(self)
		self.poner_fecha = QPushButton(self, text=">")
		#********************************************************************************************
		self.list_dias.resize(418,290)
		self.list_dias.move(12,42)
		self.list_pelis.resize(418,290)
		self.list_pelis.move(436,42)
		self.borrar_dia.resize(87, 21)
		self.borrar_dia.move(171, 338)
		self.dia_visto.resize(87, 21)
		self.dia_visto.move(343, 338)
		self.peli_arriba.resize(87, 21)
		self.peli_arriba.move(495, 338)
		self.peli_abajo.resize(87, 21)
		self.peli_abajo.move(588, 338)
		self.borrar_peli.resize(87, 21)
		self.borrar_peli.move(681, 338)
		self.peli_pendiente.resize(87, 21)
		self.peli_pendiente.move(774, 338)
		self.calendario.resize(250, 200)
		self.calendario.move(600, 29)
		self.poner_fecha.resize(25, 21)
		self.poner_fecha.move(825, 8)
		#-----------------------------------------------------------------------------------------------------------
		self.list_dias.itemSelectionChanged.connect(self.ev_list_dias_select)
		self.list_pelis.itemDoubleClicked.connect(self.ev_list_pelis_dclick)
		self.borrar_dia.clicked.connect(self.ev_borrar_dia)
		self.dia_visto.clicked.connect(self.ev_dia_visto)
		self.peli_arriba.clicked.connect(self.ev_peli_arriba)
		self.peli_abajo.clicked.connect(self.ev_peli_abajo)
		self.borrar_peli.clicked.connect(self.ev_borrar_peli)
		self.peli_pendiente.clicked.connect(self.ev_peli_pendiente)
		self.calendario.selectionChanged.connect(self.ev_calendario)
		self.poner_fecha.clicked.connect(self.ev_poner_fecha)
		#-----------------------------------------------------------------------------------------------------------
		self.links = []
		self.nombres = []
		self.dia_actual = []
		self.calendario.hide()
		self.iscalendarioshow = False
		for arch in glob.glob("./Trailers/*.txt"):
			self.list_dias.addItem(arch.split("\\")[-1][:-4])
		#-----------------------------------------------------------------------------------------------------------
	def ev_list_dias_select(self):
		self.list_pelis.clear()
		pelis = open(f"./Trailers/{self.list_dias.currentItem().text()}.txt", encoding="utf-8").readlines()
		pelis = [pelis[i].strip() for i in range(len(pelis))]
		self.list_pelis.addItems(pelis[::3])
		self.links = pelis[1::3]
		self.nombres = pelis[::3]
		self.dia_actual = self.list_dias.currentItem().text()
		
	def ev_list_pelis_dclick(self):
		webbrowser.open(self.links[self.list_pelis.currentRow()])

	def ev_borrar_dia(self):
		os.remove(f"./Trailers/{self.list_dias.currentItem().text()}.txt")
		self.list_dias.takeItem(self.list_dias.currentRow())
		
	def ev_dia_visto(self):
		shutil.move(f"./Trailers/{self.list_dias.currentItem().text()}.txt",
					f"./Trailers/vistas/{self.list_dias.currentItem().text()}.txt")
		self.list_dias.takeItem(self.list_dias.currentRow())

	def ev_peli_arriba(self):
		i = self.list_pelis.currentRow()
		self.nombres[i], self.nombres[i-1] = self.nombres[i-1], self.nombres[i]
		self.links[i], self.links[i-1] = self.links[i-1], self.links[i]	
		self.list_pelis.insertItem(i-1, self.list_pelis.item(i).text())
		self.list_pelis.setCurrentRow(i-1)
		self.list_pelis.takeItem(i+1)
		escribir_archivo(self.nombres, self.links, self.dia_actual)

	def ev_peli_abajo(self):
		i = self.list_pelis.currentRow()
		self.nombres[i], self.nombres[i+1] = self.nombres[i+1], self.nombres[i]
		self.links[i], self.links[i+1] = self.links[i+1], self.links[i]	
		self.list_pelis.insertItem(i+2, self.list_pelis.item(i).text())
		self.list_pelis.setCurrentRow(i+2)
		self.list_pelis.takeItem(i)
		escribir_archivo(self.nombres, self.links, self.dia_actual)
		
	def ev_borrar_peli(self):
		self.nombres.pop(self.list_pelis.currentRow())
		self.links.pop(self.list_pelis.currentRow())
		escribir_archivo(self.nombres, self.links, self.dia_actual)
		self.list_pelis.takeItem(self.list_pelis.currentRow())

	def ev_peli_pendiente(self):
		with open("./Trailers/000-00-0.txt", "a", encoding="utf-8") as arch:
			arch.write("\n"+self.list_pelis.currentItem().text()+"\n")
			arch.write("\t"+self.links[self.list_pelis.currentRow()]+"\n")
	
	def ev_calendario(self):
		fecha = self.calendario.selectedDate().toString("dd-MM-yyyy")
		i = self.list_pelis.currentRow()
		self.nombres[i] = self.nombres[i].strip() + "-" + fecha
		escribir_archivo(self.nombres, self.links, self.dia_actual)
		self.list_pelis.insertItem(i+1, self.nombres[i])
		self.list_pelis.takeItem(i)
		self.calendario.hide()
		self.iscalendarioshow = False
	
	def ev_poner_fecha(self):
		if self.iscalendarioshow:
			self.calendario.hide()
		else:
			self.calendario.show()
		self.iscalendarioshow = not self.iscalendarioshow



if __name__ == "__main__":
	app = QtWidgets.QApplication()

	widget = TrailersReader()
	widget.show()

	app.exec_()