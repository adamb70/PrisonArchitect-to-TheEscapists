from PySide import QtCore, QtGui
import os
import PrisonArchData
import webbrowser

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(440, 175)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(440, 175))
        MainWindow.setMaximumSize(QtCore.QSize(440, 175))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(application_path, "Source\\Files\\icon.pbm")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 411, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OKbutton = QtGui.QDialogButtonBox(self.horizontalLayoutWidget)
        self.OKbutton.setToolTip("")
        self.OKbutton.setOrientation(QtCore.Qt.Horizontal)
        self.OKbutton.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.OKbutton.setCenterButtons(True)
        self.OKbutton.setObjectName("OKbutton")
        self.horizontalLayout.addWidget(self.OKbutton)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Filepathselector_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Filepathselector_2.setStatusTip("")
        self.Filepathselector_2.setWhatsThis("")
        self.Filepathselector_2.setObjectName("Filepathselector_2")
        self.horizontalLayout_2.addWidget(self.Filepathselector_2)
        self.toolButton_2 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setSeparatorsCollapsible(False)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHow_to_use = QtGui.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(self.actionHow_to_use, QtCore.SIGNAL("activated()"), self.webhelp)
        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL("clicked()"), self.showDialog)
        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL("pressed()"), self.Filepathselector_2.clear)
        QtCore.QObject.connect(self.OKbutton, QtCore.SIGNAL("rejected()"), MainWindow.close)
        QtCore.QObject.connect(self.OKbutton, QtCore.SIGNAL("accepted()"), self.runscript)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PrisonArchitect to TheEscapist converter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Tileset", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "perks", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "stalagflucht", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "shanktonstatepen", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "jungle", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "sanpancho", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "irongate", None, QtGui.QApplication.UnicodeUTF8))

        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Prison Architect prison file", None, QtGui.QApplication.UnicodeUTF8))
        self.Filepathselector_2.setToolTip(QtGui.QApplication.translate("MainWindow", "Select .prison file", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setToolTip(QtGui.QApplication.translate("MainWindow", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHow_to_use.setText(QtGui.QApplication.translate("MainWindow", "How to use", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

    def showDialog(self):

        fname, _ = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open file',
                    os.environ['USERPROFILE'] + '\AppData\Local\Introversion\Prison Architect\saves\Prison Save Files', 'Prison Files (*.prison)')
        self.Filepathselector_2.insert(fname)

    def webhelp(self):
        webbrowser.open('https://github.com/adamb70/PrisonArchitect-to-TheEscapists')

    def runscript(self):
        heldtext = self.Filepathselector_2.displayText()
        tileset = self.comboBox.currentText()

        if heldtext == '':
            QtGui.QMessageBox.warning(MainWindow, 'Error',
            ("No file selected!"), QtGui.QMessageBox.Close)
        elif os.path.isfile(heldtext) == False:
            QtGui.QMessageBox.warning(MainWindow, 'Error',
            ("File does not exists!"), QtGui.QMessageBox.Close)
            self.Filepathselector_2.clear()
        elif tileset == '':
            QtGui.QMessageBox.warning(MainWindow, 'Error',
            ("No tileset selected!"), QtGui.QMessageBox.Close)
        else:
            PrisonArchData.writeFile(heldtext, tileset)
            QtGui.QMessageBox.information(MainWindow, 'Success!',
            ("File saved in output folder as " + str(heldtext.split('/')[-1].replace('.prison', '.proj'))), QtGui.QMessageBox.Close)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

