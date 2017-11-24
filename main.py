# -*- coding: utf-8 -*-

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import numpy as np
import pyqtgraph as pg

################################ MAIN WINDOW #####################################

class MainWindow(QMainWindow):
	count = 0; # number of open windows
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.mdi = QMdiArea()
		self.setCentralWidget(self.mdi)
		bar = self.menuBar()

		file = bar.addMenu("Datei")
		file.addAction("Speichern")
		file.addAction("Speichern als")
		file.triggered[QAction].connect(self.windowaction)
		self.setWindowTitle("GreenLion Racing 2018c")

		file = bar.addMenu("Telemetrie")
		file.addAction("Verbinden")
		file.addAction("Übersicht")
		file.addAction("Hilfe")
		file.triggered[QAction].connect(self.windowaction)

		file = bar.addMenu("Ansicht")
		file.addAction("Übereinander anordnen")
		file.addAction("Nebeneinander anordnen")
		file.triggered[QAction].connect(self.windowaction)


	def windowaction(self, q):
		
		if q.text() == "Übersicht": # Main Frame with all parameters
			MainWindow.count = MainWindow.count+1
			sub = QMdiSubWindow()
			sub.setWindowTitle("subwindow"+str(MainWindow.count))
			sub.setWidget(sinus_wave())
			self.mdi.addSubWindow(sub)
			sub.show()
		
		if q.text() == "Übereinander anordnen":
 			self.mdi.cascadeSubWindows()
			
		if q.text() == "Nebeneinander anordnen":
			self.mdi.tileSubWindows()

############################ RANDOM NUMBER GENERATOR ####################################

class sinus_wave(QWidget):
    def __init__(self):
        super(sinus_wave, self).__init__()
        self.init_ui()
        self.qt_connections()
        self.plotcurve = pg.PlotCurveItem()
        self.plotwidget.addItem(self.plotcurve)
        self.amplitude = 10
        self.t = 0
        self.updateplot()

        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.moveplot)
        self.timer.start(100)

    def init_ui(self):
        self.setWindowTitle('Sinuswave')
        hbox = QVBoxLayout()
        self.setLayout(hbox)

        self.plotwidget = pg.PlotWidget()
        hbox.addWidget(self.plotwidget)

        self.increasebutton = QPushButton("Increase Amplitude")
        self.decreasebutton = QPushButton("Decrease Amplitude")

        hbox.addWidget(self.increasebutton)
        hbox.addWidget(self.decreasebutton)

        self.setGeometry(10, 10, 1000, 600)


    def qt_connections(self):
        self.increasebutton.clicked.connect(self.on_increasebutton_clicked)
        self.decreasebutton.clicked.connect(self.on_decreasebutton_clicked)

    def moveplot(self):
        self.t+=.1
        self.updateplot()

    def updateplot(self):
        data1 = self.amplitude*np.random.uniform(-1,0,1000)
        self.plotcurve.setData(data1)

    def on_increasebutton_clicked(self):
        self.amplitude += 1
        self.updateplot()

    def on_decreasebutton_clicked(self):
        self.amplitude -= 1
        self.updateplot()

############################ MAIN METHOD #################################

def main():
	app = QApplication(sys.argv)
	ex = MainWindow()
	ex.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
