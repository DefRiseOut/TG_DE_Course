# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


class UiMainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 798)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1021, 791))
        self.tabWidget.setObjectName("tabWidget")

        self.Tab1 = QtWidgets.QWidget()
        self.Tab1.setObjectName("Tab1")

        self.x0Input = QtWidgets.QLineEdit(self.Tab1)
        self.x0Input.setGeometry(QtCore.QRect(890, 110, 113, 22))
        self.x0Input.setObjectName("lineEdit")
        self.x0Input.setText("2")

        self.label = QtWidgets.QLabel(self.Tab1)
        self.label.setGeometry(QtCore.QRect(890, 90, 55, 16))
        self.label.setObjectName("label")

        self.y0Input = QtWidgets.QLineEdit(self.Tab1)
        self.y0Input.setGeometry(QtCore.QRect(890, 170, 113, 22))
        self.y0Input.setObjectName("lineEdit_2")
        self.y0Input.setText("1")

        self.label_2 = QtWidgets.QLabel(self.Tab1)
        self.label_2.setGeometry(QtCore.QRect(890, 150, 55, 16))
        self.label_2.setObjectName("label_2")

        self.Xinput = QtWidgets.QLineEdit(self.Tab1)
        self.Xinput.setGeometry(QtCore.QRect(890, 230, 113, 22))
        self.Xinput.setObjectName("lineEdit_3")
        self.Xinput.setText("10")

        self.label_3 = QtWidgets.QLabel(self.Tab1)
        self.label_3.setGeometry(QtCore.QRect(890, 210, 55, 16))
        self.label_3.setObjectName("label_3")

        self.NInput = QtWidgets.QLineEdit(self.Tab1)
        self.NInput.setGeometry(QtCore.QRect(890, 290, 113, 22))
        self.NInput.setObjectName("lineEdit_4")
        self.NInput.setText("100")

        self.label_4 = QtWidgets.QLabel(self.Tab1)
        self.label_4.setGeometry(QtCore.QRect(890, 270, 55, 16))
        self.label_4.setObjectName("label_4")

        self.graphwidget = pg.PlotWidget(self.Tab1)
        self.graphwidget.setGeometry(QtCore.QRect(20, 40, 851, 301))
        self.graphwidget.setObjectName("widget")
        self.graphwidget.addLegend()
        self.graphwidget.setTitle("Graphs", color="b", size="15pt")
        self.graphwidget.setLabel("left", "Y")
        self.graphwidget.setLabel("bottom", "X")
        self.graphwidget.showGrid(x=True, y=True)

        self.graphwidget_2 = pg.PlotWidget(self.Tab1)
        self.graphwidget_2.setGeometry(QtCore.QRect(20, 370, 851, 361))
        self.graphwidget_2.setObjectName("widget_2")
        self.graphwidget_2.addLegend()
        self.graphwidget_2.setTitle("Local Errors", color="b", size="15pt")
        self.graphwidget_2.setLabel("left", "Y")
        self.graphwidget_2.setLabel("bottom", "X")
        self.graphwidget_2.showGrid(x=True, y=True)

        self.checkBox = QtWidgets.QCheckBox(self.Tab1)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(self.Tab1)
        self.checkBox_2.setGeometry(QtCore.QRect(110, 10, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(self.Tab1)
        self.checkBox_3.setGeometry(QtCore.QRect(210, 10, 131, 20))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self.Tab1)
        self.checkBox_4.setGeometry(QtCore.QRect(350, 10, 101, 20))
        self.checkBox_4.setObjectName("checkBox_4")

        self.tabWidget.addTab(self.Tab1, "")
        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")

        self.graphwidget_3 = pg.PlotWidget(self.Tab2)
        self.graphwidget_3.setGeometry(QtCore.QRect(20, 50, 851, 691))
        self.graphwidget_3.setObjectName("widget_3")
        self.graphwidget_3.addLegend()
        self.graphwidget_3.setTitle("Total errors", color="b", size="15pt")
        self.graphwidget_3.setLabel("left", "Y")
        self.graphwidget_3.setLabel("bottom", "X")
        self.graphwidget_3.showGrid(x=True, y=True)

        self.NstartInput = QtWidgets.QLineEdit(self.Tab2)
        self.NstartInput.setGeometry(QtCore.QRect(890, 100, 113, 22))
        self.NstartInput.setText("10")
        self.NstartInput.setObjectName("lineEdit_5")

        self.NendInput = QtWidgets.QLineEdit(self.Tab2)
        self.NendInput.setGeometry(QtCore.QRect(890, 180, 113, 22))
        self.NendInput.setObjectName("lineEdit_6")
        self.NendInput.setText("15")

        self.label_5 = QtWidgets.QLabel(self.Tab2)
        self.label_5.setGeometry(QtCore.QRect(890, 80, 81, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.Tab2)
        self.label_6.setGeometry(QtCore.QRect(890, 160, 91, 16))
        self.label_6.setObjectName("label_6")

        self.checkBox_5 = QtWidgets.QCheckBox(self.Tab2)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")

        self.checkBox_6 = QtWidgets.QCheckBox(self.Tab2)
        self.checkBox_6.setGeometry(QtCore.QRect(230, 10, 101, 20))
        self.checkBox_6.setObjectName("checkBox_7")

        self.checkBox_7 = QtWidgets.QCheckBox(self.Tab2)
        self.checkBox_7.setGeometry(QtCore.QRect(90, 10, 131, 20))
        self.checkBox_7.setObjectName("checkBox_8")

        self.tabWidget.addTab(self.Tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "x0"))
        self.label_2.setText(_translate("MainWindow", "y0"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "N"))
        self.checkBox.setText(_translate("MainWindow", "Exact"))
        self.checkBox_2.setText(_translate("MainWindow", "Euler"))
        self.checkBox_3.setText(_translate("MainWindow", "Improved Euler"))
        self.checkBox_4.setText(_translate("MainWindow", "Runge-Kutta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("MainWindow", "Tab 1"))
        self.label_5.setText(_translate("MainWindow", "N range start"))
        self.label_6.setText(_translate("MainWindow", "N range finish"))
        self.checkBox_5.setText(_translate("MainWindow", "Euler"))
        self.checkBox_6.setText(_translate("MainWindow", "Runge-Kutta"))
        self.checkBox_7.setText(_translate("MainWindow", "Improved Euler"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("MainWindow", "Tab 2"))