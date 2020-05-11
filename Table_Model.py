# -*- coding: utf-8 -*-
"""
@author:  gaetan Dubuc
"""

import sys
import pandas as pd
from PyQt5 import *
from PyQt5.QtWidgets import QApplication, QTableView,QAbstractItemView
from PyQt5.QtCore import QAbstractTableModel, QItemSelectionModel, Qt


class pandasModel(QAbstractTableModel):
	
	""" Class which inherit of QAbstractTableModel and define the tableview From the DataFrame associated to the user""" 
	
	
	def __init__( self, Data ): 
		
		"""Used to define our _Data"""
		
		QAbstractTableModel.__init__(self)
		self._Data = Data
		
	def rowCount( self, parent=None ):
		
		"""Used to return the shape of the dataframe to construct the QTableView"""
		
		return self._Data.shape[0]

	def columnCount( self, parnet=None ):
		
		"""Used to return the shape of the dataframe to construct the QTableView"""
		
		return self._Data.shape[1]

	def data( self, index, role=Qt.DisplayRole ):
		
		"""Used construct data in cells"""
		
		if index.isValid():
			if role == Qt.DisplayRole:
				return str(self._Data.iloc[index.row(), index.column()])
		return None

	def headerData( self, col, orientation, role ):
		
		"""Used to construct the header"""
		
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			return str(self._Data.columns[col])
		if orientation == Qt.Vertical and role == Qt.DisplayRole:
			return str(self._Data.index[col])
		return None
	
class NewQTableView( QTableView ):
		
	def __init__(self, DataFrame):
		
		"""Used to construct our QTableView"""
		
		QTableView.__init__(self)
		
		self._Data = DataFrame
		
		self.Model = pandasModel(self.Data) 
		self.setModel(self.Model)
		
	@property
	def Data( self ):
		
		"""Return the attribute _Data"""
		
		return self._Data
		
	@Data.setter
	def Data( self, NewData ):
		
		"""When the Data is modified, we modify the QtableView"""
		
		self._Data = NewData
		self.Model._Data = NewData
		self.Model.layoutChanged.emit()
		

