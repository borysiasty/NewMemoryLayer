# -*- coding: utf-8 -*-
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
import os

class NewMemoryLayer:

    def __init__(self, iface):
        self.iface = iface
        #i18n
        pluginPath = QFileInfo(os.path.realpath(__file__)).path()
        localeName = QLocale.system().name()
        if QFileInfo(pluginPath).exists():
            self.localePath = pluginPath+"/i18n/newmemorylayer_" + localeName + ".qm"
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


    def initGui(self):
        self.action = QAction(QIcon(":/plugins/newmemorylayer/layer-memory-create.png"), QCoreApplication.translate("NewMemoryLayer","New Memory Layer..."), self.iface.mainWindow())
        self.action2 = QAction(QIcon(":/plugins/newmemorylayer/layer-memory-create.png"), QCoreApplication.translate("NewMemoryLayer","New Memory Layer"), self.iface.mainWindow())
        self.iface.registerMainWindowAction(self.action, "Ctrl+M")
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        QObject.connect(self.action2, SIGNAL("triggered()"), self.run)
        try:
            self.iface.newLayerMenu().addAction(self.action)  # API >= 1.9
        except:
            self.iface.addPluginToMenu("New Memory Layer", self.action)
        try:
            self.iface.layerToolBar().addAction(self.action2)  # API >= 1.8
        except:
            self.iface.addToolBarIcon(self.action2)


    def unload(self):
        QObject.disconnect(self.action, SIGNAL("triggered()"), self.run)
        QObject.disconnect(self.action2, SIGNAL("triggered()"), self.run)
        self.iface.unregisterMainWindowAction(self.action)
        try:
            self.iface.newLayerMenu().removeAction(self.action)  # API >= 1.9
        except:
            self.iface.removePluginMenu("New Memory Layer",self.action)
        try:
            self.iface.layerToolBar().removeAction(self.action2)  # API >= 1.8
        except:
            self.iface.removeToolBarIcon(self.action2)


    def run(self):
        dlg = NewMemoryLayerDialog()
        dlg.show()
        result = dlg.exec_()
        if result == 1:
            geomType = dlg.geomType + '?crs=proj4:' + QgsProject.instance().readEntry("SpatialRefSys","/ProjectCRSProj4String")[0] #dodana linia
            memLay = QgsVectorLayer(geomType, dlg.ui.leName.text(), 'memory') #zmieniona linia
            if hasattr( QgsMapLayerRegistry.instance(), "addMapLayers" ):
                QgsMapLayerRegistry.instance().addMapLayers([memLay])  # API >= 1.9
            else:
                QgsMapLayerRegistry.instance().addMapLayer(memLay)
