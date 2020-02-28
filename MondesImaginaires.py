# PROGRAMME DE CALCUL MONDES IMAGINAIRE

# PAR THEO SILVAGNO
# LE 3/02/2020
# POUR COLLECTIF CONSCIENCE
#
# NE FONCTIONNE PAS AVEC ECRAN HAUTE DENSITE (OPTIMISE POUR 1920x1080)
# SI LES IMAGES NE SE CHARGENT PAS, VEUILLEZ CHANGER LE CHEMIN D'ACCES DU DOSSIER CONTENANT LES IMAGES ET LE PROGRAMME LIGNE 254 DANS LES " " EN SEPARANT LES DOSSIER PAR DES //

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QColor, QBrush, QMouseEvent, QCursor
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget

import numpy as np
import numpy.random as rdm
import os
import sys

class Ui_MainWindow(object):

    def reinit (self) : 

        self.MasseLab.setValue(0)
        self.RayonLab.setValue(2500)
        self.D=0
        self.DistEP.setText('Non renseigné')
        self.Prev.setText('Non renseigné')
        self.Grav.setText('Non renseigné')
        
    def revolution (self) :
        m=(10**20)*self.MasseLab.value()
        print(str(self.DistEP.text()))
        if m==0 or str(self.DistEP.text())=='Non renseigné': 
           self.Prev.setText("Vous n'avez pas choisi votre planète. Quelle erreur...")

        else : 
            d=float(self.D)*1000
            P=2*np.pi*np.sqrt((d**3)/((6.67e-11)*m))
            P=P/(3600*24)
            self.Prev.setText(str(round(P,1)) + ' jours')

    def randompla(self)   : 
        a=rdm.randint(5)+1
        self.D=Dist[a-1]
        self.planeterandom.setText('Fiona vous a forcé à choisir la planète N°' + str(a))
        self.planeterandom_2.setText( 'Mode Fiona activé')
        self.DistEP.setText(str(self.D)+' km')
        
        
    def choix (self, indic) : 
        
        choice = self.ChoixPlanete_2.value()
        self.D=Dist[choice]
        self.planeterandom_2.setText( 'Vous avez choisi la planète N°' + str(choice+1))
        self.planeterandom.setText('Vous avez mis Fiona en mode Silencieux.')
        self.DistEP.setText(str(self.D)+ " km")
        indic=indic+1
  

    def grav (self) :
        m=(10**20)*self.MasseLab.value()
        r=1000*self.RayonLab.value()

        if r==0 or m==0 : 
           self.Grav.setText('Erreur')
        else : 
            g=(6.67e-11*m)/(r**2)
            gt=g/9.81
            print(g)
            self.Grav.setText(str(round(gt,2)) + 'g')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1020)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.fond = QtWidgets.QLabel(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.fond.setObjectName("FOND")
        self.fond.setPixmap(QtGui.QPixmap("image\fd.png"))
        self.fond.setAlignment(Qt.AlignCenter)
        self.fond.setContentsMargins(0, 0, 0, 0)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1900, 1000))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.RayonLab = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.RayonLab.setFont(font)
        self.RayonLab.setMinimum(250.0)
        self.RayonLab.setMaximum(9999999999.99)
        self.RayonLab.setSingleStep(0.1)
        self.RayonLab.setObjectName("RayonLab")
        self.horizontalLayout_2.addWidget(self.RayonLab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.MasseLab = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.MasseLab.setFont(font)
        self.MasseLab.setMinimum(5.0)
        self.MasseLab.setMaximum(2e+8)
        self.MasseLab.setSingleStep(0.1)
        self.MasseLab.setObjectName("MasseLab")
        self.horizontalLayout_4.addWidget(self.MasseLab)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.CalculG = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.CalculG.setFont(font)
        self.CalculG.setFlat(False)
        self.CalculG.setObjectName("CalculG")
        self.horizontalLayout_5.addWidget(self.CalculG)
        

        self.Grav = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.Grav.setFont(font)
        self.Grav.setObjectName("Grav")
        self.horizontalLayout_5.addWidget(self.Grav)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.CalculP = QtWidgets.QPushButton(self.gridLayoutWidget)
        pixp=QPixmap("image\br.png")
        iconp = QtGui.QIcon()
        iconp.addPixmap(pixp, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CalculP.setIcon(iconp)
        self.CalculP.setIconSize(pixp.rect().size())
        self.CalculP.setFlat(True)
        self.CalculP.setObjectName("CalculP")

        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(10)
        #self.CalculP.setFont(font)

        
        pix=QPixmap("bg.png")
        icon = QtGui.QIcon()
        icon.addPixmap(pix, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CalculG.setIcon(icon)
        self.CalculG.setIconSize(pix.rect().size())
        self.CalculG.setFlat(True)
        self.horizontalLayout_7.addWidget(self.CalculP)
        self.Prev = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.Prev.setFont(font)
        self.Prev.setObjectName("Prev")
        self.horizontalLayout_7.addWidget(self.Prev)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Libel Suit")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.DistEP = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(16)
        self.DistEP.setFont(font)
        self.DistEP.setObjectName("DistEP")
        self.horizontalLayout_9.addWidget(self.DistEP)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.Systeme = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Systeme.setMouseTracking(True)
        self.Systeme.setObjectName("Systeme")

        self.gridLayout.addWidget(self.Systeme, 0, 2, 1, 1)
       
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushrandom = QtWidgets.QPushButton(self.gridLayoutWidget)
        pixf=QPixmap("image\bf.png")
        iconf = QtGui.QIcon()
        iconf.addPixmap(pixf, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushrandom.setIcon(iconf)
        self.pushrandom.setIconSize(pixf.rect().size())
        self.pushrandom.setFlat(True)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(12)
        #self.pushrandom.setFont(font)
        self.pushrandom.setObjectName("pushrandom")
        self.horizontalLayout_3.addWidget(self.pushrandom)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.planeterandom = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(20)
        self.planeterandom.setFont(font)
        self.planeterandom.setObjectName("planeterandom")
        self.planeterandom.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.planeterandom)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ChoixPlanete_2 = QtWidgets.QDial(self.gridLayoutWidget)
        self.ChoixPlanete_2.setMaximum(4)
        self.ChoixPlanete_2.setObjectName("ChoixPlanete_2")
        self.verticalLayout_6.addWidget(self.ChoixPlanete_2)
        self.ChoixPlanete_2.valueChanged.connect(self.choix)
        self.planeterandom_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(20)
        self.planeterandom_2.setFont(font)
        self.planeterandom_2.setObjectName("planeterandom_2")
        self.planeterandom_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6.addWidget(self.planeterandom_2)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(40)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_8.addWidget(self.label_13)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.Reinit = QtWidgets.QPushButton(self.gridLayoutWidget)
        pixre=QPixmap("image\bre.png")
        iconf = QtGui.QIcon()
        iconf.addPixmap(pixre, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Reinit.setIcon(iconf)
        self.Reinit.setIconSize(pixre.rect().size())
        self.Reinit.setFlat(True)
        self.Reinit.setObjectName("Reinit")
        self.verticalLayout.addWidget(self.Reinit)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        #Clique sur les boutons
        self.CalculG.clicked.connect(self.grav)
        self.CalculP.clicked.connect(self.revolution)
        self.Reinit.clicked.connect(self.reinit)
       

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.RayonLab, self.CalculG)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mondes Imagninaires"))
        MainWindow.setWindowIcon(QIcon("image\LOGO.ico"))
        self.label.setText(_translate("MainWindow", "PARAMETRES"))
        self.label_2.setText(_translate("MainWindow", "     "+"RAYON EN Km"))
        self.label_6.setText(_translate("MainWindow", "     "+"MASSE EN kg (x10"+chr(0x00B2)+chr(0x2070)+")"))
        self.Grav.setText(_translate("MainWindow", "Non renseigné"))
        self.Prev.setText(_translate("MainWindow", "Non renseigné"))
        self.label_3.setText(_translate("MainWindow", "DONNÉES: "))
        self.label_4.setText(_translate("MainWindow", "     "+"DISTANCE PLANÈTE/ÉTOILE :"))
        self.DistEP.setText(_translate("MainWindow", "Non renseigné"))

        #Image du système

        self.Systeme.setText(_translate("MainWindow", " "))
        self.pixmapsys=QPixmap("image\Sys.png")
        self.Systeme.setPixmap(self.pixmapsys)

        self.planeterandom.setText(_translate("MainWindow", "Fiona vous a forcé à choisir la planète N°X."))

        #Bouton random

        self.pushrandom.clicked.connect(self.randompla)

        self.planeterandom_2.setText(_translate("MainWindow", "Vous avez choisi la planète N°X."))
        self.label_13.setText(_translate("MainWindow", "BIENVENUE"))
        self.label_5.setText(_translate("MainWindow",
"\nBonjour, je suis Fiona. Suivez mes instruction et la création de votre planète se passera bien.\nINSTRUCTIONS: \n"
"   - Choisissez une planète : Vous pouvez choisir une planète avec la molette ou me laisser décider de\n"
"    votre destin Mouhahaha. Pardon...\n"
"   - Entrez les paramètres des votre 'planète' dans les boites Rayon et Masse prévues à cet effet.\n"
"   - Appuyez sur les boutons 'Calcul de ...' pour récupérer des précieuses informations que je vous\n"
"     fournirai gracieusement.\n"
"   - Rermerciez moi. J'ai quand même fait tout le boulot.  \n"))
        #self.Reinit.setText(_translate("MainWindow", "REINITIALISER"))




if __name__ == "__main__":

    Dist= np.array([4487936.121,10471850.949, 44879361.210, 149597870.700, 254316380.190])
    indic=0


    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    #Le style 
    app.setStyle("Fusion")

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(41, 35, 92))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(54, 169, 225))
    dark_palette.setColor(QPalette.AlternateBase, QColor(54, 169, 225))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(54, 169, 225))
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(54, 169, 225))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
   

    app.setPalette(dark_palette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    #Fin du style

    MainWindow.show()
    sys.exit(app.exec_())

