# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NewMemoryLayer
                                 A QGIS plugin
 Creates a memory layer
                             -------------------
        begin                : 2011-05-13
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

 This plugin was written during Qgis Programming Workshop in Wrocław 
 2011-05-13 and in a train from Wrocław to Warsaw 2011-05-14
 
 Patch for using project crs by Piotr Pociask 2011-08-22

"""

def name():
    return "New Memory Layer"
def description():
    return "Creates an empty memory layer"
def version():
    return "Version 0.2.1"
def icon():
    return "mActionNewVectorLayer.png"
def qgisMinimumVersion():
    return "1.6"
def classFactory(iface):
    from newmemorylayer import NewMemoryLayer
    return NewMemoryLayer(iface)
