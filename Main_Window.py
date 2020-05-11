# -*- coding: utf-8 -*-
"""
	@author: gaetan Dubuc
"""

import sys
from PyQt5.Qt import *
import pandas as pd
import Style as S
import pickle
import hashlib
import Table_Model as TM
import re



class MyWindow( QStackedWidget ):

	"""Our main window."""

	def __init__ ( self ) :

		"""all the widgets of the window are gathered like attributes here."""

	# ======Creation of the main window.=======================================

		QStackedWidget.__init__( self )
		self.setWindowTitle( 'Card application' )
		self.resize(500,300)
	
	# ======Users Data recovery.===============================================
		
		with open("Users","rb") as fichier: # Used to get the user file and their cards companies
			mon_deplicker = pickle.Unpickler(fichier)
			self.Users = mon_deplicker.load()
			self.UsersCompanies = mon_deplicker.load()

	# =========Creation of the different interfaces.===========================
			
		self.Window1 = QWidget()
		self.Window1.setLayout(self.Frame1())
		
		self.Window2 = QWidget()
		self.Window2.setLayout(self.Frame2())
		
		self.addWidget(self.Window1)
		self.addWidget(self.Window2)
		
		
	def Frame1 (self):
		
		"""Display the Profile interface"""
		
		# ======Création of the widgets.===============================
		
		self.TitleInfoF1 = QLabel("Please fill to log in or click on 'Add User' to create an account.")
		self.NameF1 = QLabel("User name :")
		self.LineNameF1 = QLineEdit ()
		self.LineNameF1.setPlaceholderText("Enter your User Name")
		
		self.PassWordF1 = QLabel("Password :")
		self.LinePassF1 = QLineEdit()
		self.LinePassF1.setPlaceholderText("Enter your Password")
		self.LinePassF1.setEchoMode(QLineEdit.Password)
		self.ErrorMessF1 = QLabel()
		
		self.AddUser = QPushButton("Add User")
		self.Connexion = QPushButton("Log in")
		
		self.AddUser.clicked.connect(self.AddUsers)
		self.Connexion.clicked.connect(self.ConnexionUser)
		
	# ======Widgets oganization===============================================
		
		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.NameF1)
		hbox1.addWidget(self.LineNameF1)
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.PassWordF1)
		hbox2.addWidget(self.LinePassF1)
		vbox1 = QVBoxLayout()
		vbox1.addLayout(hbox2)
		vbox1.addWidget(self.ErrorMessF1)
		hbox3 = QHBoxLayout()
		hbox3.addWidget(self.AddUser)
		hbox3.addWidget(self.Connexion)
		vbox2 = QVBoxLayout()
		vbox2.addWidget(self.TitleInfoF1)
		vbox2.addLayout(hbox1)
		vbox2.addLayout(vbox1)
		vbox2.addLayout(hbox3)
		
		return vbox2

	def Frame2 (self):
		
		"""Display the Add user interface"""
		
		# ======Création of the widgets.===============================
		
		self.TitleInfoF2 = QLabel("Please fill the following form to create an account:")
		self.NameF2 = QLabel("Name :")
		self.LineNameF2 = QLineEdit ()
		self.LineNameF2.setPlaceholderText("Enter your User Name")
		
		self.CompNameF2 = QLabel("Company Name*:")
		self.LineCompF2 = QLineEdit ()
		self.LineCompF2.setPlaceholderText("Enter your Company Name")
		
		self.EmailF2 = QLabel("Email*:")
		self.LineEmailF2 = QLineEdit ()
		self.LineEmailF2.setPlaceholderText("Enter your Email, format: XXX@XXX.XX")
		
		self.TelF2 = QLabel("TelephoneNumber*:")
		self.LineTelF2 = QLineEdit ()
		self.LineTelF2.setPlaceholderText("Enter your phone number, format: XX XX XX XX XX")
		reg_ex = QRegExp("([0-9]{2} ){4}[0-9]{2}")
		input_validator = QRegExpValidator(reg_ex)
		self.LineTelF2.setValidator(input_validator)
		
		self.PassCreateF2 = QLabel("Password :")
		self.LinePassCreateF2 = QLineEdit()
		self.LinePassCreateF2.setPlaceholderText("Enter your Password")
		self.LinePassCreateF2.setEchoMode(QLineEdit.Password)
		self.ErrorMessF2 = QLabel()
		
		self.InfoF2 = QLabel("* These fields are optionals")
		
		self.CreateUser = QPushButton("Create User", enabled=False)
		self.BackButton = QPushButton("Back")
		
		self.LineNameF2.textChanged.connect(self.VerifF2)
		self.LinePassCreateF2.textChanged.connect(self.VerifF2)
		self.LineEmailF2.textChanged.connect(self.VerifF2)
		self.LineTelF2.textChanged.connect(self.VerifF2)
		self.CreateUser.clicked.connect(self.Create_User)
		self.BackButton.clicked.connect(self.Back)
		
	# ======Widgets oganization===============================================
		
		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.NameF2)
		hbox1.addWidget(self.LineNameF2)
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.CompNameF2)
		hbox2.addWidget(self.LineCompF2)
		hbox3 = QHBoxLayout()
		hbox3.addWidget(self.EmailF2)
		hbox3.addWidget(self.LineEmailF2)
		hbox4 = QHBoxLayout()
		hbox4.addWidget(self.TelF2)
		hbox4.addWidget(self.LineTelF2)
		hbox5 = QHBoxLayout()
		hbox5.addWidget(self.CreateUser)
		hbox5.addWidget(self.BackButton)
		hbox6 = QHBoxLayout()
		hbox6.addWidget(self.PassCreateF2)
		hbox6.addWidget(self.LinePassCreateF2)
		vbox1 = QVBoxLayout()
		vbox1.addWidget(self.TitleInfoF2)
		vbox1.addLayout(hbox1)
		vbox1.addLayout(hbox2)
		vbox1.addLayout(hbox3)
		vbox1.addLayout(hbox4)
		vbox1.addLayout(hbox6)
		vbox1.addWidget(self.ErrorMessF2)
		vbox1.addWidget(self.InfoF2)
		vbox1.addLayout(hbox5)
		

		return vbox1
	
	def Frame3 (self, UserTag):
		
		"""Display the Add user interface"""
		
		# ======Création of the widgets.===============================
		
		self.TitleInfoF3 = QLabel("Hello "+ self.UserName+".\
 Please fill the following form to add a company to your data.")
		self.NameF3 = QLabel("Name*:")
		self.LineNameF3 = QLineEdit ()
		self.LineNameF3.setPlaceholderText("Enter your User Name")
		
		self.CompNameF3 = QLabel("Company Name*:")
		self.LineCompF3 = QLineEdit ()
		self.LineCompF3.setPlaceholderText("Enter your Company Name")
		
		self.EmailF3 = QLabel("Email:")
		self.LineEmailF3 = QLineEdit ()
		self.LineEmailF3.setPlaceholderText("Enter your Email, format: XXX@XXX.XX")
		
		self.TelF3 = QLabel("TelephoneNumber*:")
		self.LineTelF3 = QLineEdit ()
		self.LineTelF3.setPlaceholderText("Enter your phone number, format: XX XX XX XX XX")
		reg_ex = QRegExp("([0-9]{2} ){4}[0-9]{2}")
		input_validator = QRegExpValidator(reg_ex)
		self.LineTelF3.setValidator(input_validator)
		
		self.InfoF3 = QLabel("* These fields are optionals")
		
		self.Table = TM.NewQTableView(self.UsersCompanies[UserTag])
		
		self.SaveCompany = QPushButton("Save Company", enabled=False)
		self.Deconnexion = QPushButton("Log out")
		self.RemoveCard = QPushButton("Remove card")
		self.RemoveCard.setToolTip("To remove a company card, click\
on its index, then click on this button.")
		
		self.LineTelF3.textChanged.connect(self.VerifF3)
		self.LineEmailF3.textChanged.connect(self.VerifF3)
		self.SaveCompany.clicked.connect(self.Save_Company)
		self.Deconnexion.clicked.connect(self.Deconnexion_User)
		self.RemoveCard.clicked.connect(self.Remove_Card)
		
	# ======Widgets oganization===============================================
		
		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.NameF3)
		hbox1.addWidget(self.LineNameF3)
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.CompNameF3)
		hbox2.addWidget(self.LineCompF3)
		hbox3 = QHBoxLayout()
		hbox3.addWidget(self.EmailF3)
		hbox3.addWidget(self.LineEmailF3)
		hbox4 = QHBoxLayout()
		hbox4.addWidget(self.TelF3)
		hbox4.addWidget(self.LineTelF3)
		hbox5 = QHBoxLayout()
		hbox5.addWidget(self.SaveCompany)
		hbox5.addWidget(self.RemoveCard)
		hbox5.addWidget(self.Deconnexion)
		vbox1 = QVBoxLayout()
		vbox1.addWidget(self.TitleInfoF3)
		vbox1.addLayout(hbox1)
		vbox1.addLayout(hbox2)
		vbox1.addLayout(hbox3)
		vbox1.addLayout(hbox4)
		vbox1.addWidget(self.InfoF3)
		vbox1.addWidget(self.Table)
		vbox1.addLayout(hbox5)
		
		return vbox1

#======= Functions Frame1 =====================================================
		
	def AddUsers (self):
		
		""" There is a click on the Add User File Button."""
		
		self.setCurrentIndex(1)
		self.CleanFrame1()
		
	def ConnexionUser (self):
		
		"""User is trying to connect"""
		
		Entry = self.LinePassF1.text().encode()
		EntryPass = hashlib.sha1(Entry).hexdigest() # Used to get the crypted Pass
		
		self.UserTag = self.LineNameF1.text()+"/"+EntryPass
		
		if self.UserTag in self.Users:
			self.Window3 = QWidget()
			self.addWidget(self.Window3)
			self.setCurrentIndex(2)
			self.UserName = self.Users[self.LineNameF1.text()+"/"+EntryPass][0]
			
			self.Window3.setLayout(self.Frame3(self.UserTag))
			self.resize(800,700)

			self.CleanFrame1()

		else: 
			self.ErrorMessF1.setText("""The user name or the password is wrong.""")
			self.LinePassF1.clear()
			self.LineNameF1.clear()
	
	def CleanFrame1(self):
		
		"""Function used to clean QEditLine in Frame 1"""
		
		self.LinePassF1.clear()
		self.LineNameF1.clear()
		self.ErrorMessF1.clear()
		
#======= Functions Frame2 =====================================================
	
	def Create_User (self):
		
		""" Function used to create user if QLineEdits are correctly filled"""
		
		Entry = self.LinePassCreateF2.text().encode()
		EntryPass = hashlib.sha1(Entry).hexdigest() # Used to protect the Password
		
		UserTag = self.LineNameF2.text()+"/"+EntryPass
		
		if UserTag not in self.Users:
			
			self.Users[UserTag] = [self.LineNameF2.text(),self.LineCompF2.text(),\
					self.LineEmailF2.text(),self.LineTelF2.text(),self.LinePassCreateF2.text()]
				
			self.UsersCompanies[UserTag] = pd.DataFrame(columns=["Name","Company","Email","Telephone"])
				
			with open ("Users","wb") as fichier: # Used to save the data
				mon_pickler = pickle.Pickler(fichier)
				mon_pickler.dump(self.Users)
				mon_pickler.dump(self.UsersCompanies)
				
			self.Back()
			self.ErrorMessF1.setText("Thank you for having created a new account.")
			
		else:
			self.ErrorMessF2.setText("User account already exists")

	def Back (self):
		
		"""Back Button is clicked"""
		
		self.setCurrentIndex(0)
		self.CleanFrame2()
		
	def VerifF2 (self): 
		
		""" Function used to verify if the QLineEdits are correctly filled"""
		
		if self.LineNameF2.text() != '' and self.LinePassCreateF2.text() != '':
			if (re.search("([0-9]{2} ){4}[0-9]{2}",self.LineTelF2.text()) is not None or self.LineTelF2.text() == "")\
			and (re.search("^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,6}$",self.LineEmailF2.text()) is not None or self.LineEmailF2.text() == "") :
				self.CreateUser.setEnabled(True)
			else:
				self.CreateUser.setEnabled(False)
		else:
			self.CreateUser.setEnabled(False)

	def CleanFrame2(self):
		
		"""Function used to clean QEditLine from the Frame2"""
		
		self.LineNameF2.clear()
		self.LineCompF2.clear()
		self.LineEmailF2.clear()
		self.LineTelF2.clear()
		self.LinePassCreateF2.clear()
		self.ErrorMessF2.clear()
		self.CreateUser.setEnabled(False)
	
#======= Functions Frame3 =====================================================
	
	def Save_Company (self):
		
		"""Function used to save the campany card in the table"""
		
		Data = pd.DataFrame([[self.LineNameF3.text(),self.LineCompF3.text(),\
					self.LineEmailF3.text(),self.LineTelF3.text()]]\
					, columns=self.UsersCompanies[self.UserTag].columns)
			
		self.UsersCompanies[self.UserTag] =\
		self.UsersCompanies[self.UserTag].append(Data)
		
		self.UsersCompanies[self.UserTag].reset_index(drop=True,inplace=True)
		
		self.Table.Data = self.UsersCompanies[self.UserTag]
		
		self.CleanFrame3()
	
	def Deconnexion_User (self):
		
		"""Function used to log out"""
		
		self.setCurrentIndex(0)
		self.removeWidget(self.Window3)
		self.resize(500,300)
		self.CleanFrame3() 
		
		with open ("Users","wb") as fichier: # If there is a log out the data are saved
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self.Users)
			mon_pickler.dump(self.UsersCompanies)
		
		
	def Remove_Card (self):
		
		""" Allows to delete a card company. To remove a card, 
		click on its index and click on remove button"""
		
		indexes = self.Table.selectionModel().selectedRows()
		for index in sorted(indexes):
			self.UsersCompanies[self.UserTag].drop(index.row(), inplace=True)
		
		# Used to always have sorted indexes
		self.UsersCompanies[self.UserTag].reset_index(drop=True,inplace=True)
		
		self.Table.Data = self.UsersCompanies[self.UserTag]
		
	def closeEvent (self,event):
		
		""" Function used if the app is quit"""
		
		with open ("Users","wb") as fichier: # Save the data
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self.Users)
			mon_pickler.dump(self.UsersCompanies)
			
		event.accept()
		
	def VerifF3 (self):
		
		"""Function used to verify if Email line is filled"""
		
		if (re.match("^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,6}$",self.LineEmailF3.text()) is not None)\
			and (re.match("([0-9]{2} ){4}[0-9]{2}",self.LineTelF3.text()) is not None or self.LineTelF3.text() == ""):
			self.SaveCompany.setEnabled(True)
			
		else:
			self.SaveCompany.setEnabled(False)
		
	def CleanFrame3 (self):
		
		"""Function used to clean the Library interface"""
		
		self.LineNameF3.clear()
		self.LineCompF3.clear()
		self.LineEmailF3.clear()
		self.LineTelF3.clear()
		
	
