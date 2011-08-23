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

from PyQt4 import QtCore, QtGui
from ui_newmemorylayer import Ui_NewMemoryLayer

class NewMemoryLayerDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_NewMemoryLayer()
        self.ui.setupUi(self)
        self.geomType = None
        self.connect(self.ui.butPoint, QtCore.SIGNAL("released()"), self.runPoint)
        self.connect(self.ui.butLine, QtCore.SIGNAL("released()"), self.runLine)
        self.connect(self.ui.butPoly, QtCore.SIGNAL("released()"), self.runPoly)
        
    def runPoint(self):
        self.geomType = 'Point'
        self.accept()
        
    def runLine(self):
        self.geomType = 'LineString'
        self.accept()
     
    def runPoly(self):
        self.geomType = 'Polygon'
        self.accept()
