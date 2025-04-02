# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newmemorylayer.ui'
#
# Created: Sat May 14 22:30:53 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtWidgets, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_NewMemoryLayer(object):
    def setupUi(self, NewMemoryLayer):
        NewMemoryLayer.setObjectName(_fromUtf8("NewMemoryLayer"))
        NewMemoryLayer.resize(494, 134)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewMemoryLayer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtWidgets.QLabel(NewMemoryLayer)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leName = QtWidgets.QLineEdit(NewMemoryLayer)
        self.leName.setObjectName(_fromUtf8("leName"))
        self.horizontalLayout_2.addWidget(self.leName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.butPoint = QtWidgets.QPushButton(NewMemoryLayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butPoint.sizePolicy().hasHeightForWidth())
        self.butPoint.setSizePolicy(sizePolicy)
        self.butPoint.setObjectName(_fromUtf8("butPoint"))
        self.horizontalLayout.addWidget(self.butPoint)
        self.butLine = QtWidgets.QPushButton(NewMemoryLayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLine.sizePolicy().hasHeightForWidth())
        self.butLine.setSizePolicy(sizePolicy)
        self.butLine.setObjectName(_fromUtf8("butLine"))
        self.horizontalLayout.addWidget(self.butLine)
        self.butPoly = QtWidgets.QPushButton(NewMemoryLayer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butPoly.sizePolicy().hasHeightForWidth())
        self.butPoly.setSizePolicy(sizePolicy)
        self.butPoly.setObjectName(_fromUtf8("butPoly"))
        self.horizontalLayout.addWidget(self.butPoly)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewMemoryLayer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.leName)

        self.retranslateUi(NewMemoryLayer)
        self.buttonBox.accepted.connect(NewMemoryLayer.accept)
        self.buttonBox.rejected.connect(NewMemoryLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(NewMemoryLayer)
        NewMemoryLayer.setTabOrder(self.leName, self.butPoint)
        NewMemoryLayer.setTabOrder(self.butPoint, self.butLine)
        NewMemoryLayer.setTabOrder(self.butLine, self.butPoly)
        NewMemoryLayer.setTabOrder(self.butPoly, self.buttonBox)

    def retranslateUi(self, NewMemoryLayer):
        NewMemoryLayer.setWindowTitle(
            QtWidgets.QApplication.translate(
                "NewMemoryLayer",
                "NewMemoryLayer",
                None,
            )
        )
        self.label.setText(
            QtWidgets.QApplication.translate("NewMemoryLayer", "Name", None)
        )
        self.leName.setText(
            QtWidgets.QApplication.translate(
                "NewMemoryLayer",
                "Memory layer",
                None,
            )
        )
        self.butPoint.setText(
            QtWidgets.QApplication.translate("NewMemoryLayer", "Point", None)
        )
        self.butLine.setText(
            QtWidgets.QApplication.translate("NewMemoryLayer", "Line", None)
        )
        self.butPoly.setText(
            QtWidgets.QApplication.translate("NewMemoryLayer", "Polygon", None)
        )
