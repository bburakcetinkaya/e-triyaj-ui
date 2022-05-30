# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:14:55 2022

@author: ASUS
"""
from PyQt5 import QtCore

class PrintTable(QtCore.QAbstractTableModel):
    
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
            
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QVariant(str(self._data.iloc[index.row()][index.column()]))
        return QtCore.QVariant()
    
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
   
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._data.columns[section])
    
            if orientation == QtCore.Qt.Vertical:
                return str(self._data.index[section])

        return None