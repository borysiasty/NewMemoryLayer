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

# standard library
import os

# PyQGIS
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsWkbTypes, QgsIconUtils, QgsVectorLayer, QgsProject
from qgis.utils import iface

FORM_CLASS = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "ui_newmemorylayer.ui")
)[0]


class NewMemoryLayerDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        geom_types = [
            QgsWkbTypes.Type.Point,
            QgsWkbTypes.Type.LineString,
            QgsWkbTypes.Type.Polygon,
            QgsWkbTypes.Type.MultiPoint,
            QgsWkbTypes.Type.MultiLineString,
            QgsWkbTypes.Type.MultiPolygon,
            QgsWkbTypes.Type.MultiCurve,
            QgsWkbTypes.Type.CompoundCurve,
            QgsWkbTypes.Type.CurvePolygon,
            QgsWkbTypes.Type.MultiSurface,
        ]

        nb_col = 3
        for i, geom_type in enumerate(geom_types):
            row = i // nb_col
            col = i % nb_col
            button = QtWidgets.QPushButton(
                QgsIconUtils.iconForWkbType(geom_type),
                QgsWkbTypes.translatedDisplayString(geom_type),
                self,
            )
            button.clicked.connect(lambda clicked, t=geom_type: self.add_layer(t))
            self.lyt_geometry_types.addWidget(button, row, col)

    def add_layer(self, geom_type: QgsWkbTypes.Type):
        layer_wkb_str = QgsWkbTypes.displayString(geom_type)
        geomType = f"{layer_wkb_str}?crs={QgsProject.instance().crs().authid()}"
        memLay = QgsVectorLayer(geomType, self.leName.text(), "memory")
        QgsProject().instance().addMapLayer(memLay)

        if self.chk_start_edition.isChecked():
            memLay.startEditing()
            iface.layerTreeView().setCurrentLayer(memLay)
            iface.actionAddFeature().trigger()
