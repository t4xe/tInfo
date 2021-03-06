#tInfo v1.4 by t4xe.
from PyQt5 import QtCore, QtGui, QtWidgets
from platform import node, machine, processor, platform, system, version
from datetime import datetime
import qdarkstyle
import psutil
    
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 328)
        Form.setMaximumSize(541, 328)
        Form.setMinimumSize(541, 328)
        
        Form.setWindowIcon(QtGui.QIcon("icon.ico"))
        lightTheme = (open("lightTheme.qss", "r").read())
        darkTheme = qdarkstyle.load_stylesheet_pyqt5()
        
        self.firstPixLabel = 10
        self.secondPixLabel = 290
        
        self.cpuDetailsLabel = QtWidgets.QLabel(Form)
        self.cpuDetailsLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 25, 101, 21))
        self.cpuDetailsLabel.setObjectName("cpuDetailsLabel")
        
        self.cpuBaseFreqLabel = QtWidgets.QLabel(Form)
        self.cpuBaseFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 50, 131, 31))
        self.cpuBaseFreqLabel.setObjectName("cpuBaseFreqLabel")
        
        self.cpuBaseFreqLine = QtWidgets.QLineEdit(Form)
        self.cpuBaseFreqLine.setGeometry(QtCore.QRect(140, 60, 125, 16))
        self.cpuBaseFreqLine.setReadOnly(True)
        self.cpuBaseFreqLine.setObjectName("cpuBaseFreqLine")
        
        self.cpuMaxFreqLabel = QtWidgets.QLabel(Form)
        self.cpuMaxFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 85, 111, 23))
        self.cpuMaxFreqLabel.setObjectName("cpuMaxFreqLabel")
        
        self.cpuMinFreqLabel = QtWidgets.QLabel(Form)
        self.cpuMinFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 110, 111, 31))
        self.cpuMinFreqLabel.setObjectName("cpuMinFreqLabel")
        
        self.cpuNphysLabel = QtWidgets.QLabel(Form)
        self.cpuNphysLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 150, 131, 31))
        self.cpuNphysLabel.setObjectName("cpuNphysLabel")
        
        self.cpuNlogLabel = QtWidgets.QLabel(Form)
        self.cpuNlogLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 185, 131, 21))
        self.cpuNlogLabel.setObjectName("cpuNlogLabel")
        
        self.cpuCurrUtilLabel = QtWidgets.QLabel(Form)
        self.cpuCurrUtilLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 235, 111, 21))
        self.cpuCurrUtilLabel.setObjectName("cpuCurrUtilLabel")
        
        self.cpuCurrPcpuLabel = QtWidgets.QLabel(Form)
        self.cpuCurrPcpuLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 260, 121, 31))
        self.cpuCurrPcpuLabel.setObjectName("cpuCurrPcpuLabel")
        
        self.cpuProcTypeLabel = QtWidgets.QLabel(Form)
        self.cpuProcTypeLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 285, 101, 41))
        self.cpuProcTypeLabel.setObjectName("cpuProcTypeLabel")
        
        self.cpuMaxFreqLine = QtWidgets.QLineEdit(Form)
        self.cpuMaxFreqLine.setGeometry(QtCore.QRect(140, 90, 125, 16))
        self.cpuMaxFreqLine.setReadOnly(True)
        self.cpuMaxFreqLine.setObjectName("cpuMaxFreqLine")
        
        self.cpuMinFreqLine = QtWidgets.QLineEdit(Form)
        self.cpuMinFreqLine.setGeometry(QtCore.QRect(140, 120, 125, 16))
        self.cpuMinFreqLine.setReadOnly(True)
        self.cpuMinFreqLine.setObjectName("cpuMinFreqLine")
        
        self.cpuNphysLine = QtWidgets.QLineEdit(Form)
        self.cpuNphysLine.setGeometry(QtCore.QRect(140, 160, 125, 16))
        self.cpuNphysLine.setReadOnly(True)
        self.cpuNphysLine.setObjectName("cpuNphysLine")
        
        self.cpuNlogLine = QtWidgets.QLineEdit(Form)
        self.cpuNlogLine.setGeometry(QtCore.QRect(140, 190, 125, 16))
        self.cpuNlogLine.setReadOnly(True)
        self.cpuNlogLine.setObjectName("cpuNlogLine")
        
        self.cpuCurrUtilLine = QtWidgets.QLineEdit(Form)
        self.cpuCurrUtilLine.setGeometry(QtCore.QRect(140, 240, 125, 16))
        self.cpuCurrUtilLine.setReadOnly(True)
        self.cpuCurrUtilLine.setObjectName("cpuCurrUtilLine")
        
        self.cpuCurrPcpuLine = QtWidgets.QLineEdit(Form)
        self.cpuCurrPcpuLine.setGeometry(QtCore.QRect(140, 270, 125, 16))
        self.cpuCurrPcpuLine.setReadOnly(True)
        self.cpuCurrPcpuLine.setObjectName("cpuCurrPcpuLine")
        
        self.cpuProcTypeLine = QtWidgets.QLineEdit(Form)
        self.cpuProcTypeLine.setGeometry(QtCore.QRect(140, 300, 125, 16))
        self.cpuProcTypeLine.setReadOnly(True)
        self.cpuProcTypeLine.setObjectName("cpuProcTypeLine")
        
        self.ramDetailsLabel = QtWidgets.QLabel(Form)
        self.ramDetailsLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 25, 101, 21))
        self.ramDetailsLabel.setObjectName("ramDetailsLabel")
        
        self.ramRamUsageLine = QtWidgets.QLineEdit(Form)
        self.ramRamUsageLine.setGeometry(QtCore.QRect(410, 150, 125, 16))
        self.ramRamUsageLine.setReadOnly(True)
        self.ramRamUsageLine.setObjectName("ramRamUsageLine")
        
        self.ramTotalRamLine = QtWidgets.QLineEdit(Form)
        self.ramTotalRamLine.setGeometry(QtCore.QRect(410, 60, 125, 16))
        self.ramTotalRamLine.setReadOnly(True)
        self.ramTotalRamLine.setObjectName("ramTotalRamLine")
        
        self.ramUsedRamLabel = QtWidgets.QLabel(Form)
        self.ramUsedRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 110, 91, 31))
        self.ramUsedRamLabel.setObjectName("ramUsedRamLabel")
        
        self.ramAvaRamLabel = QtWidgets.QLabel(Form)
        self.ramAvaRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 85, 101, 21))
        self.ramAvaRamLabel.setObjectName("ramAvaRamLabel")
        
        self.ramRamUsageLabel = QtWidgets.QLabel(Form)
        self.ramRamUsageLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 145, 81, 22))
        self.ramRamUsageLabel.setObjectName("ramRamUsageLabel")
        
        self.ramAvaRamLine = QtWidgets.QLineEdit(Form)
        self.ramAvaRamLine.setGeometry(QtCore.QRect(410, 90, 125, 16))
        self.ramAvaRamLine.setReadOnly(True)
        self.ramAvaRamLine.setObjectName("ramAvaRamLine")
        
        self.ramUsedRamLine = QtWidgets.QLineEdit(Form)
        self.ramUsedRamLine.setGeometry(QtCore.QRect(410, 120, 125, 16))
        self.ramUsedRamLine.setReadOnly(True)
        self.ramUsedRamLine.setObjectName("ramUsedRamLine")
        
        self.ramTotalRamLabel = QtWidgets.QLabel(Form)
        self.ramTotalRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 50, 81, 31))
        self.ramTotalRamLabel.setObjectName("ramTotalRamLabel")
        
        self.generalInformationLabel = QtWidgets.QLabel(Form)
        self.generalInformationLabel.setGeometry(QtCore.QRect(290, 184, 181, 21))
        self.generalInformationLabel.setObjectName("generalInformationLabel")
        
        self.pcNwNameLabel = QtWidgets.QLabel(Form)
        self.pcNwNameLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 209, 121, 31))
        self.pcNwNameLabel.setObjectName("pcNwNameLabel")
        
        self.machineTypeLabel = QtWidgets.QLabel(Form)
        self.machineTypeLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 234, 111, 41))
        self.machineTypeLabel.setObjectName("machineTypeLabel")
 
        self.osDetailsLabel = QtWidgets.QLabel(Form)
        self.osDetailsLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 275, 81, 21))
        self.osDetailsLabel.setObjectName("osDetailsLabel")
 
        self.platformTypeLabel = QtWidgets.QLabel(Form)
        self.platformTypeLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 292, 101, 41))
        self.platformTypeLabel.setObjectName("platformTypeLabel")
        
        self.pcNwNameLine = QtWidgets.QLineEdit(Form)
        self.pcNwNameLine.setGeometry(QtCore.QRect(410, 220, 125, 16))
        self.pcNwNameLine.setReadOnly(True)
        self.pcNwNameLine.setObjectName("pcNwNameLine")
        
        self.machineTypeLine = QtWidgets.QLineEdit(Form)
        self.machineTypeLine.setGeometry(QtCore.QRect(410, 247, 125, 16))
        self.machineTypeLine.setReadOnly(True)
        self.machineTypeLine.setObjectName("machineTypeLine")
        
        self.platformTypeLine = QtWidgets.QLineEdit(Form)
        self.platformTypeLine.setGeometry(QtCore.QRect(410, 305, 125, 16))
        self.platformTypeLine.setReadOnly(True)
        self.platformTypeLine.setObjectName("platformTypeLine")
        
        self.osDetailsLine = QtWidgets.QLineEdit(Form)
        self.osDetailsLine.setGeometry(QtCore.QRect(410, 276, 125, 16))
        self.osDetailsLine.setReadOnly(True)
        self.osDetailsLine.setObjectName("osDetailsLine")
        
        self.dateLabel = QtWidgets.QLabel(Form)
        self.dateLabel.setGeometry(QtCore.QRect(440, 5, 140, 21))     
        self.dateLabel.setObjectName("dateLabel") 

        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(5, 5, 80, 21))
        self.refreshButton.setObjectName("refreshButton")
        
        self.themeCheckBox = QtWidgets.QCheckBox(Form)
        self.themeCheckBox.setGeometry(QtCore.QRect(90, 5, 80, 21))
        self.themeCheckBox.setObjectName("themeCheckBox")
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.lineEditContent)
        self.timer.start(5000)

        self.lineEditContent()
        self.refreshButton.clicked.connect(self.lineEditContent)
        self.themeCheckBox.stateChanged.connect(self.themeCheckBoxStateChanged)  

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        date = datetime.now()
        currentDate = datetime.strftime(date, "%D")
        
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "tInfo"))
        self.cpuDetailsLabel.setText(_translate("Form", "CPU Details:"))
        self.cpuBaseFreqLabel.setText(_translate("Form", "Base Frequency:"))
        self.cpuMaxFreqLabel.setText(_translate("Form", "Max. Frequency:"))
        self.cpuMinFreqLabel.setText(_translate("Form", "Min. Frequency:"))
        self.cpuNphysLabel.setText(_translate("Form", "Num. of phs. cores:"))
        self.cpuNlogLabel.setText(_translate("Form", "Num. of log. cores:"))
        self.cpuCurrUtilLabel.setText(_translate("Form", "Curr. utilization:"))
        self.cpuCurrPcpuLabel.setText(_translate("Form", "Curr. per-cpu util.:"))
        self.cpuProcTypeLabel.setText(_translate("Form", "Processor type:"))
        self.ramDetailsLabel.setText(_translate("Form", "RAM Details:"))
        self.ramUsedRamLabel.setText(_translate("Form", "Used RAM:"))
        self.ramAvaRamLabel.setText(_translate("Form", "Available RAM:"))
        self.ramRamUsageLabel.setText(_translate("Form", "RAM Usage:"))
        self.ramTotalRamLabel.setText(_translate("Form", "Total RAM:"))
        self.generalInformationLabel.setText(_translate("Form", "General Information:"))
        self.pcNwNameLabel.setText(_translate("Form", "PC Net. Name:"))
        self.machineTypeLabel.setText(_translate("Form", "Machine Type:"))
        self.platformTypeLabel.setText(_translate("Form", "Platform Type:"))
        self.osDetailsLabel.setText(_translate("Form", "OS Details:"))
        self.dateLabel.setText(_translate("Form", "Date: " + currentDate)) 
        self.refreshButton.setText(_translate("Form", "Refresh"))
        self.themeCheckBox.setText(_translate("Form", "Dark Mode"))
        
    def lineEditContent(self):
        cpuCurrFreq = str(psutil.cpu_freq().current)
        cpuMinFreq = str(psutil.cpu_freq().min)
        cpuMaxFreq = str(psutil.cpu_freq().max)
        
        cpuNphys = str(psutil.cpu_count(logical=False))
        cpuNlog = str(psutil.cpu_count(logical=True))
        
        cpuCurrUtil = str(psutil.cpu_percent(interval=1))
        cpuCurrPcpu = str(psutil.cpu_percent(interval=1, percpu=True))
        cpuCurrPcpu = cpuCurrPcpu.replace("[", "")
        cpuCurrPcpu = cpuCurrPcpu.replace("]", "")
        
        ramTotal = round(psutil.virtual_memory().total/1000000000, 2) - 1
        ramTotalRam = ("{0} GB".format(ramTotal))
        
        ramAva = round(psutil.virtual_memory().available/1000000000, 2) - 1
        ramAvaRam = ("{0} GB".format(ramAva))
        
        ramUsed = round(psutil.virtual_memory().used/1000000000, 2) - 1
        ramUsedRam = ("{0} GB".format(ramUsed))
        
        ramRamUsage = str(psutil.virtual_memory().percent) + "%"

        pcNwName = str(node())
        machineType = str(machine())
        processorType = str(processor())
        platformType = str(platform())
        osDetails = str(system() + " " + version())
        
        self.cpuBaseFreqLine.setText(cpuCurrFreq)
        self.cpuMinFreqLine.setText(cpuMinFreq)
        self.cpuMaxFreqLine.setText(cpuMaxFreq)
        self.cpuNphysLine.setText(cpuNphys)
        self.cpuNlogLine.setText(cpuNlog)
        self.cpuCurrUtilLine.setText(cpuCurrUtil)
        self.cpuCurrPcpuLine.setText(cpuCurrPcpu)
        self.ramTotalRamLine.setText(ramTotalRam)
        self.ramAvaRamLine.setText(ramAvaRam)
        self.ramUsedRamLine.setText(ramUsedRam)
        self.ramRamUsageLine.setText(ramRamUsage)
        self.pcNwNameLine.setText(pcNwName)
        self.machineTypeLine.setText(machineType)
        self.cpuProcTypeLine.setText(processorType)
        self.platformTypeLine.setText(platformType)
        self.osDetailsLine.setText(osDetails)  

    def themeCheckBoxStateChanged(self):
        lightTheme = (open("lightTheme.qss", "r").read())
        darkTheme = qdarkstyle.load_stylesheet_pyqt5()
        if self.themeCheckBox.isChecked():
            app.setStyleSheet(lightTheme + darkTheme)
            self.firstPixLabel = self.firstPixLabel - 5
            self.secondPixLabel = self.secondPixLabel - 5
            self.cpuDetailsLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 25, 101, 21))
            self.cpuBaseFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 50, 131, 31))
            self.cpuMaxFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 85, 111, 23))
            self.cpuMinFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 110, 111, 31))
            self.cpuNphysLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 150, 131, 31))
            self.cpuNlogLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 185, 131, 21))
            self.ramDetailsLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 25, 101, 21))
            self.ramUsedRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 110, 91, 31))
            self.ramAvaRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 85, 101, 21))
            self.ramTotalRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 50, 81, 31))
            self.generalInformationLabel.setGeometry(QtCore.QRect(290, 184, 181, 21))
            self.pcNwNameLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 209, 121, 31))
            self.machineTypeLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 234, 111, 41))
            self.platformTypeLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 292, 101, 41))
            self.osDetailsLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 275, 81, 21))
            self.dateLabel.setGeometry(QtCore.QRect(440, 5, 140, 21))   
            
        else:
            app.setStyleSheet(lightTheme)   
            self.firstPixLabel = self.firstPixLabel + 5
            self.secondPixLabel = self.secondPixLabel + 5
            self.cpuDetailsLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 25, 101, 21))
            self.cpuBaseFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 50, 131, 31))
            self.cpuMaxFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 85, 111, 23))
            self.cpuMinFreqLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 110, 111, 31))
            self.cpuNphysLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 150, 131, 31))
            self.cpuNlogLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 185, 131, 21))
            self.ramDetailsLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 25, 101, 21))
            self.ramUsedRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 110, 91, 31))
            self.ramAvaRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 85, 101, 21))
            self.ramTotalRamLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 50, 81, 31))
            self.generalInformationLabel.setGeometry(QtCore.QRect(290, 184, 181, 21))
            self.pcNwNameLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 209, 121, 31))
            self.machineTypeLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 234, 111, 41))
            self.platformTypeLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 292, 101, 41))
            self.osDetailsLabel.setGeometry(QtCore.QRect(self.secondPixLabel, 275, 81, 21))
            self.dateLabel.setGeometry(QtCore.QRect(440, 5, 140, 21))  
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()  
    app.setStyleSheet(open("lightTheme.qss", "r").read())
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
