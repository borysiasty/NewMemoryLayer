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
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.core import *
from qgis.core import QgsWkbTypes
from .newmemorylayerdialog import NewMemoryLayerDialog
import os
from qgis.PyQt.QtWidgets import QToolBar
from typing import Optional


class NewMemoryLayer:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.dlg = None
        # i18n
        pluginPath = QFileInfo(os.path.realpath(__file__)).path()
        localeName = QLocale.system().name()
        if QFileInfo(pluginPath).exists():
            self.localePath = pluginPath + "/i18n/newmemorylayer_" + localeName + ".qm"
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
            QCoreApplication.installTranslator(self.translator)
        self.toolbar: Optional[QToolBar] = None

    def initGui(self):
        self.action = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), "layer-memory-create.png")),
            QCoreApplication.translate("NewMemoryLayer", "New Memory Layer..."),
            self.iface.mainWindow(),
        )
        self.action.setShortcut("Ctrl+W")
        self.iface.registerMainWindowAction(self.action, "Ctrl+W")
        self.action.triggered.connect(self.run)
        self.iface.newLayerMenu().addAction(self.action)
        self.iface.layerToolBar().addAction(self.action)

        # Toolbar
        if self.toolbar is None:
            self.toolbar = QToolBar("NewMemoryLayerToolbar", self.iface.mainWindow())
            self.toolbar.setObjectName("NewMemoryLayerToolbar")
            self.iface.addToolBar(self.toolbar)

        # Add action Point / Line / Polygon
        self._add_layer_action(
            ":images/themes/default/mIconPointLayer.svg",
            "Add new point layer",
            "Add new point layer...",
            QgsWkbTypes.Type.Point,
            "Point",
        )

        self._add_layer_action(
            ":images/themes/default/mIconLineLayer.svg",
            "Add new line layer",
            "Add new line layer...",
            QgsWkbTypes.Type.LineString,
            "Line",
        )

        self._add_layer_action(
            ":images/themes/default/mIconPolygonLayer.svg",
            "Add new polygon layer",
            "Add new polygon layer...",
            QgsWkbTypes.Type.Polygon,
            "Polygon",
        )

    def _add_layer_action(self, icon_path, context, text, wkb_type, label):
        action = QAction(
            QIcon(icon_path),
            QCoreApplication.translate(context, text),
            self.iface.mainWindow(),
        )
        action.triggered.connect(
            lambda: NewMemoryLayerDialog().generic_add_layer(wkb_type, label, False)
        )
        self.toolbar.addAction(action)

    def unload(self):
        if self.action:
            self.action.triggered.disconnect(self.run)
            self.iface.unregisterMainWindowAction(self.action)
            self.iface.newLayerMenu().removeAction(self.action)
            self.iface.layerToolBar().removeAction(self.action)

        # remove toolbar :
        if self.toolbar:
            self.toolbar.deleteLater()

    def run(self):
        if not self.dlg:
            self.dlg = NewMemoryLayerDialog()
        self.dlg.show()
        self.dlg.activateWindow()
