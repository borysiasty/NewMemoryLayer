# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newmemorylayer.ui'
#
# Created: Sat May 14 22:30:53 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewMemoryLayer(object):
    def setupUi(self, NewMemoryLayer):
        NewMemoryLayer.setObjectName(_fromUtf8("NewMemoryLayer"))
        NewMemoryLayer.resize(494, 134)
        self.verticalLayout = QtGui.QVBoxLayout(NewMemoryLayer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(NewMemoryLayer)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leName = QtGui.QLineEdit(NewMemoryLayer)
        self.leName.setObjectName(_fromUtf8("leName"))
        self.horizontalLayout_2.addWidget(self.leName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.butPoint = QtGui.QPushButton(NewMemoryLayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butPoint.sizePolicy().hasHeightForWidth())
        self.butPoint.setSizePolicy(sizePolicy)
        self.butPoint.setObjectName(_fromUtf8("butPoint"))
        self.horizontalLayout.addWidget(self.butPoint)
        self.butLine = QtGui.QPushButton(NewMemoryLayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLine.sizePolicy().hasHeightForWidth())
        self.butLine.setSizePolicy(sizePolicy)
        self.butLine.setObjectName(_fromUtf8("butLine"))
        self.horizontalLayout.addWidget(self.butLine)
        self.butPoly = QtGui.QPushButton(NewMemoryLayer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butPoly.sizePolicy().hasHeightForWidth())
        self.butPoly.setSizePolicy(sizePolicy)
        self.butPoly.setObjectName(_fromUtf8("butPoly"))
        self.horizontalLayout.addWidget(self.butPoly)
        self.buttonBox = QtGui.QDialogButtonBox(NewMemoryLayer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.leName)

        self.retranslateUi(NewMemoryLayer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewMemoryLayer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewMemoryLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(NewMemoryLayer)
        NewMemoryLayer.setTabOrder(self.leName, self.butPoint)
        NewMemoryLayer.setTabOrder(self.butPoint, self.butLine)
        NewMemoryLayer.setTabOrder(self.butLine, self.butPoly)
        NewMemoryLayer.setTabOrder(self.butPoly, self.buttonBox)

    def retranslateUi(self, NewMemoryLayer):
        NewMemoryLayer.setWindowTitle(QtGui.QApplication.translate("NewMemoryLayer", "NewMemoryLayer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewMemoryLayer", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.leName.setText(QtGui.QApplication.translate("NewMemoryLayer", "Memory layer", None, QtGui.QApplication.UnicodeUTF8))
        self.butPoint.setText(QtGui.QApplication.translate("NewMemoryLayer", "Point", None, QtGui.QApplication.UnicodeUTF8))
        self.butLine.setText(QtGui.QApplication.translate("NewMemoryLayer", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.butPoly.setText(QtGui.QApplication.translate("NewMemoryLayer", "Polygon", None, QtGui.QApplication.UnicodeUTF8))

