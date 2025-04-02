# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NewMemoryLayerDialog
                                 A QGIS plugin
 Creates a memory layer
                             -------------------
        begin                : 2011-05-14
        copyright            : (C) 2011 by Borys Jurgiel
        email                : info at borysjurgiel dot pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt import QtWidgets
from .ui_newmemorylayer import Ui_NewMemoryLayer


class NewMemoryLayerDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_NewMemoryLayer()
        self.ui.setupUi(self)
        self.geomType = None
        self.ui.butPoint.released.connect(self.runPoint)
        self.ui.butLine.released.connect(self.runLine)
        self.ui.butPoly.released.connect(self.runPoly)

    def runPoint(self):
        self.geomType = "Point"
        self.accept()

    def runLine(self):
        self.geomType = "LineString"
        self.accept()

    def runPoly(self):
        self.geomType = "Polygon"
        self.accept()
