# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iplot3val.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1182, 800)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1180, 800))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(12, 12, 1160, 719))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ViewPort = GraphicsLayoutWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewPort.sizePolicy().hasHeightForWidth())
        self.ViewPort.setSizePolicy(sizePolicy)
        self.ViewPort.setMinimumSize(QtCore.QSize(1140, 600))
        self.ViewPort.setObjectName(_fromUtf8("ViewPort"))
        self.gridLayout.addWidget(self.ViewPort, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(1158, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 3)
        self.Label1 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Label1.setFont(font)
        self.Label1.setObjectName(_fromUtf8("Label1"))
        self.gridLayout.addWidget(self.Label1, 2, 0, 1, 1)
        self.Slider1 = QtGui.QSlider(self.widget)
        self.Slider1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider1.setObjectName(_fromUtf8("Slider1"))
        self.gridLayout.addWidget(self.Slider1, 2, 1, 1, 1)
        self.LcdNumber1 = QtGui.QLCDNumber(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LcdNumber1.setFont(font)
        self.LcdNumber1.setFrameShape(QtGui.QFrame.Box)
        self.LcdNumber1.setFrameShadow(QtGui.QFrame.Plain)
        self.LcdNumber1.setLineWidth(1)
        self.LcdNumber1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.LcdNumber1.setObjectName(_fromUtf8("LcdNumber1"))
        self.gridLayout.addWidget(self.LcdNumber1, 2, 2, 1, 1)
        self.Label2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Label2.setFont(font)
        self.Label2.setObjectName(_fromUtf8("Label2"))
        self.gridLayout.addWidget(self.Label2, 3, 0, 1, 1)
        self.Slider2 = QtGui.QSlider(self.widget)
        self.Slider2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider2.setObjectName(_fromUtf8("Slider2"))
        self.gridLayout.addWidget(self.Slider2, 3, 1, 1, 1)
        self.LcdNumber2 = QtGui.QLCDNumber(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LcdNumber2.setFont(font)
        self.LcdNumber2.setFrameShape(QtGui.QFrame.Box)
        self.LcdNumber2.setFrameShadow(QtGui.QFrame.Plain)
        self.LcdNumber2.setLineWidth(1)
        self.LcdNumber2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.LcdNumber2.setObjectName(_fromUtf8("LcdNumber2"))
        self.gridLayout.addWidget(self.LcdNumber2, 3, 2, 1, 1)
        self.Label3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Label3.setFont(font)
        self.Label3.setObjectName(_fromUtf8("Label3"))
        self.gridLayout.addWidget(self.Label3, 4, 0, 1, 1)
        self.Slider3 = QtGui.QSlider(self.widget)
        self.Slider3.setOrientation(QtCore.Qt.Horizontal)
        self.Slider3.setObjectName(_fromUtf8("Slider3"))
        self.gridLayout.addWidget(self.Slider3, 4, 1, 1, 1)
        self.LcdNumber3 = QtGui.QLCDNumber(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LcdNumber3.setFont(font)
        self.LcdNumber3.setFrameShape(QtGui.QFrame.Box)
        self.LcdNumber3.setFrameShadow(QtGui.QFrame.Plain)
        self.LcdNumber3.setLineWidth(1)
        self.LcdNumber3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.LcdNumber3.setObjectName(_fromUtf8("LcdNumber3"))
        self.gridLayout.addWidget(self.LcdNumber3, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.StatusBar = QtGui.QStatusBar(MainWindow)
        self.StatusBar.setEnabled(False)
        self.StatusBar.setObjectName(_fromUtf8("StatusBar"))
        MainWindow.setStatusBar(self.StatusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Utrecht Condensed Matter Demonstrator", None))
        self.Label1.setText(_translate("MainWindow", "Variable name", None))
        self.Label2.setText(_translate("MainWindow", "Variable name", None))
        self.Label3.setText(_translate("MainWindow", "Variable name", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

from pyqtgraph import GraphicsLayoutWidget
