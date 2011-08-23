"""
/***************************************************************************
 NewMemoryLayer
                                 A QGIS plugin
 Creates a memory layer
                              -------------------
        begin                : 2011-05-14
        copyright            : by Borys Jurgiel
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources
from newmemorylayerdialog import NewMemoryLayerDialog

class NewMemoryLayer:

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(QIcon(":/plugins/newmemorylayer/mActionNewVectorLayer.png"), "New Memory Layer", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        self.iface.registerMainWindowAction(self.action, "Ctrl+M")
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("New Memory Layer", self.action)
        #self.iface.layerMenu().findChild(QMenu, 'menuNew').addAction(self.action)
        
    def unload(self):
        self.iface.unregisterMainWindowAction(self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("New Memory Layer",self.action)
        #self.iface.layerMenu().findChild(QMenu, 'menuNew').removeAction(self.action)

    def run(self):
        dlg = NewMemoryLayerDialog()
        dlg.show()
        result = dlg.exec_()
        if result == 1:
            geomType = dlg.geomType + '?crs=proj4:' + QgsProject.instance().readEntry("SpatialRefSys","/ProjectCRSProj4String")[0] #dodana linia
            memLay = QgsVectorLayer(geomType, dlg.ui.leName.text(), 'memory') #zmieniona linia
            QgsMapLayerRegistry.instance().addMapLayer(memLay)            
