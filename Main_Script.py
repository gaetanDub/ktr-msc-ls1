# -*- coding: utf-8 -*-
"""
@author:  gaetan Dubuc
"""

import sys
from Main_Window import *
import Style as S

"""Mains script to run"""

if not QApplication.instance():
	app = QApplication(sys.argv)
else:
	app = QApplication.instance() 

app.setStyleSheet(S.Style)
myWindow = MyWindow()
myWindow.show()

sys.exit( app.exec_() )