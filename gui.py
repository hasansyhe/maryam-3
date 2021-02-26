# import pyqt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


# this code by Hasan SyheMuhammet
# you can share this code with ur friends
# ,,, THANKS for LARA and MERYEM and SHAHED ,,,
# you can find more source code just to my facebook page ( programmer-مبرمج )

app = QApplication(sys.argv)
# create my window
root = QWidget()
root.setWindowTitle("Kdin3")


# create main layout
mainlayout = QVBoxLayout()
# set layout inside my window
root.setLayout(mainlayout)

# create three layout
onelayout = QHBoxLayout()
twolayout = QVBoxLayout()
threelayout = QHBoxLayout()
# ADD THIS LAYOUT TO mainlayout
mainlayout.addLayout(onelayout)
mainlayout.addLayout(twolayout)
mainlayout.addLayout(threelayout)

# inside onelayout i will add image

# two layout
# create three layout inside two layout
greenBoxlayout = QHBoxLayout()
greenProgrsslayout = QHBoxLayout()
comPortbox = QHBoxLayout()
# add greenBoxlayout and greenProgrsslayout to two layout
twolayout.addLayout(greenBoxlayout)
twolayout.addLayout(greenProgrsslayout)

groupPort = QGroupBox("ID:COM")
twolayout.addWidget(groupPort)
groupPort.setLayout(comPortbox)

#------------------------------------------#
boxGreen0 = QLineEdit()
boxGreen1 = QLineEdit()
boxGreen2 = QLineEdit()
boxGreen3 = QLineEdit()
boxGreen4 = QLineEdit()
boxGreen5 = QLineEdit()
boxGreen6 = QLineEdit()
boxGreen7 = QLineEdit()
listBoxgreen = [boxGreen0, boxGreen1, boxGreen2, boxGreen3, boxGreen4, boxGreen5, boxGreen6, boxGreen7]
for boxElement in listBoxgreen:
	boxElement.setReadOnly(True)
	boxElement.setStyleSheet("height:70px;")
	greenBoxlayout.addWidget(boxElement)
#------------------------------------------#
progressbar0 = QProgressBar()
progressbar1 = QProgressBar()
progressbar2 = QProgressBar()
progressbar3 = QProgressBar()
progressbar4 = QProgressBar()
progressbar5 = QProgressBar()
progressbar6 = QProgressBar()
progressbar7 = QProgressBar()

listProgress = [progressbar0, progressbar1, progressbar2, progressbar3, progressbar4, progressbar5, progressbar6, progressbar7]
for progressElement in listProgress:
	greenProgrsslayout.addWidget(progressElement)
#------------------------------------------#
idcom0 = QLineEdit()
idcom1 = QLineEdit()
idcom2 = QLineEdit()
idcom3 = QLineEdit()
idcom4 = QLineEdit()
idcom5 = QLineEdit()
idcom6 = QLineEdit()
idcom7 = QLineEdit()
listIdcom = [idcom0, idcom1, idcom2, idcom3, idcom4, idcom5, idcom6, idcom7]
for idcomElement in listIdcom:
	idcomElement.setReadOnly(True)
	comPortbox.addWidget(idcomElement)



#----------------------------------#
leftLayout = QHBoxLayout()
rightLayout = QVBoxLayout()

threelayout.addLayout(leftLayout)
threelayout.addLayout(rightLayout)


# noteboot
notebook = QTabWidget() # create tabwidget to add other widgets

tablog = QWidget() # Log Tab
logArea = QPlainTextEdit()
logArea.setStyleSheet("width:50px;" "height:180px;")
loglayout = QHBoxLayout()
tablog.setLayout(loglayout)
loglayout.addWidget(logArea)

taboption = QWidget() # Option Tab

tabpit = QWidget() # Pit Tab
notebook.addTab(tablog, "Log")
notebook.addTab(taboption, "Options")
notebook.addTab(tabpit, "Pit")
leftLayout.addWidget(notebook)

#------------------------------#

tipsLayout = QGroupBox("Tips How to download HOME binary")
flashlayout = QVBoxLayout()
buttonslayout = QHBoxLayout()

rightLayout.addWidget(tipsLayout)
layoutBoxtip = QVBoxLayout()
tipsLayout.setLayout(layoutBoxtip)

tipsLabel = QLabel("OLD model : Download one binary \" (BUILD_VER)_XXXHOME.tar.md5\" ")
layoutBoxtip.addWidget(tipsLabel)

# create layout inside flashlayout
blLayout = QHBoxLayout() # for one part widgets
apLayout = QHBoxLayout() # for two part widgets
cpLayout = QHBoxLayout() # for three pat widgets
cscLayout = QHBoxLayout() # for four part widgets
umsLayout = QHBoxLayout() # for five part wdgets

# add this layout to flashlayout
flashlayout.addLayout(blLayout) # add to flash layout
flashlayout.addLayout(apLayout) # add to flash layout
flashlayout.addLayout(cpLayout) # add to flash layout
flashlayout.addLayout(cscLayout) # add to flash layout
flashlayout.addLayout(umsLayout) # add to flash layout

# add radio buttons and entry to abov layout
# one part
radio1 = QCheckBox() # create chack button
buttonBL = QPushButton("BL") # button
buttonBL.setStyleSheet("height:30px;")
pathPleace1 = QLineEdit() # for path of files
pathPleace1.setStyleSheet("width:450px;height:30px;")
# add widgets
blLayout.addWidget(radio1) # create chack button
blLayout.addWidget(buttonBL) # button
blLayout.addWidget(pathPleace1)

# two part
radio2 = QCheckBox() # create chack button
buttonAP = QPushButton("AP") # button
buttonAP.setStyleSheet("height:30px;")
pathPleace2 = QLineEdit() # for path of files
pathPleace2.setStyleSheet("width:450px;height:30px;")
# add widgets
apLayout.addWidget(radio2)
apLayout.addWidget(buttonAP)
apLayout.addWidget(pathPleace2)

# three part
radio3 = QCheckBox() # create chack button
buttonCP = QPushButton("CP") # button
buttonCP.setStyleSheet("height:30px;")
pathPleace3 = QLineEdit() # for path of files
pathPleace3.setStyleSheet("width:450px;height:30px;")
# add widgets
cpLayout.addWidget(radio3)
cpLayout.addWidget(buttonCP)
cpLayout.addWidget(pathPleace3)

# four part
radio4 = QCheckBox() # create chack button
buttonCSC = QPushButton("CSC") # button
buttonCSC.setStyleSheet("height:30px;")
pathPleace4 = QLineEdit() # for path of files
pathPleace4.setStyleSheet("width:450px;height:30px;")
# add widgets
cscLayout.addWidget(radio4)
cscLayout.addWidget(buttonCSC)
cscLayout.addWidget(pathPleace4)

# five part
radio5 = QCheckBox() # create chack button
buttonUMS = QPushButton("UMS") # button
buttonUMS.setStyleSheet("height:30px;")
pathPleace5 = QLineEdit() # for path of files
pathPleace5.setStyleSheet("width:450px;height:30px;")
# add widgets
umsLayout.addWidget(radio5)
umsLayout.addWidget(buttonUMS)
umsLayout.addWidget(pathPleace5)

# add flashlayout to rightlayout
rightLayout.addLayout(flashlayout)

# --------------------- buttons ------------------- #
startBut = QPushButton("Start") # button
startBut.setStyleSheet("height:35px;margin:20px;float:left;")
resetBut = QPushButton("Reset") # button
resetBut.setStyleSheet("height:35px;margin:20px;float:left;")
exitBut = QPushButton("Exit") # button
exitBut.setStyleSheet("height:35px;margin:20px;float:left;")
# add buttons to buttonslayout
buttonslayout.addWidget(startBut)
buttonslayout.addWidget(resetBut)
buttonslayout.addWidget(exitBut)
# add buttonslayout to rightlayout
rightLayout.addLayout(buttonslayout)
# show everything
root.show()
sys.exit(app.exec_())
