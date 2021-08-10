from PyQt5 import QtCore, QtGui, QtWidgets
from platform import node, machine, processor, platform, system, version
from datetime import datetime
import psutil
    
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 328)
        Form.setMaximumSize(541, 328)
        Form.setMinimumSize(541, 328)
        
        self.cpuDetailsLabel = QtWidgets.QLabel(Form)
        self.cpuDetailsLabel.setGeometry(QtCore.QRect(10, 25, 101, 21))
        self.cpuDetailsLabel.setObjectName("cpuDetailsLabel")
        
        self.cpuBaseFreqLabel = QtWidgets.QLabel(Form)
        self.cpuBaseFreqLabel.setGeometry(QtCore.QRect(10, 50, 131, 31))
        self.cpuBaseFreqLabel.setObjectName("cpuBaseFreqLabel")
        
        self.cpuBaseFreqLine = QtWidgets.QLineEdit(Form)
        self.cpuBaseFreqLine.setGeometry(QtCore.QRect(140, 60, 125, 16))
        self.cpuBaseFreqLine.setReadOnly(True)
        self.cpuBaseFreqLine.setObjectName("cpuBaseFreqLine")
        
        self.cpuMaxFreqLabel = QtWidgets.QLabel(Form)
        self.cpuMaxFreqLabel.setGeometry(QtCore.QRect(10, 85, 103, 23))
        self.cpuMaxFreqLabel.setObjectName("cpuMaxFreqLabel")
        
        self.cpuMinFreqLabel = QtWidgets.QLabel(Form)
        self.cpuMinFreqLabel.setGeometry(QtCore.QRect(10, 110, 111, 31))
        self.cpuMinFreqLabel.setObjectName("cpuMinFreqLabel")
        
        self.cpuNphysLabel = QtWidgets.QLabel(Form)
        self.cpuNphysLabel.setGeometry(QtCore.QRect(10, 150, 131, 31))
        self.cpuNphysLabel.setObjectName("cpuNphysLabel")
        
        self.cpuNlogLabel = QtWidgets.QLabel(Form)
        self.cpuNlogLabel.setGeometry(QtCore.QRect(10, 185, 121, 21))
        self.cpuNlogLabel.setObjectName("cpuNlogLabel")
        
        self.cpuCurrUtilLabel = QtWidgets.QLabel(Form)
        self.cpuCurrUtilLabel.setGeometry(QtCore.QRect(10, 235, 111, 21))
        self.cpuCurrUtilLabel.setObjectName("cpuCurrUtilLabel")
        
        self.cpuCurrPcpuLabel = QtWidgets.QLabel(Form)
        self.cpuCurrPcpuLabel.setGeometry(QtCore.QRect(10, 260, 121, 31))
        self.cpuCurrPcpuLabel.setObjectName("cpuCurrPcpuLabel")
        
        self.cpuProcTypeLabel = QtWidgets.QLabel(Form)
        self.cpuProcTypeLabel.setGeometry(QtCore.QRect(10, 285, 101, 41))
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
        self.ramDetailsLabel.setGeometry(QtCore.QRect(290, 25, 101, 21))
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
        self.ramUsedRamLabel.setGeometry(QtCore.QRect(290, 110, 91, 31))
        self.ramUsedRamLabel.setObjectName("ramUsedRamLabel")
        
        self.ramAvaRamLabel = QtWidgets.QLabel(Form)
        self.ramAvaRamLabel.setGeometry(QtCore.QRect(290, 85, 101, 21))
        self.ramAvaRamLabel.setObjectName("ramAvaRamLabel")
        
        self.ramRamUsageLabel = QtWidgets.QLabel(Form)
        self.ramRamUsageLabel.setGeometry(QtCore.QRect(290, 145, 81, 22))
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
        self.ramTotalRamLabel.setGeometry(QtCore.QRect(290, 50, 81, 31))
        self.ramTotalRamLabel.setObjectName("ramTotalRamLabel")
        
        self.generalInformationLabel = QtWidgets.QLabel(Form)
        self.generalInformationLabel.setGeometry(QtCore.QRect(290, 184, 181, 21))
        self.generalInformationLabel.setObjectName("generalInformationLabel")
        
        self.pcNwNameLabel = QtWidgets.QLabel(Form)
        self.pcNwNameLabel.setGeometry(QtCore.QRect(290, 209, 121, 31))
        self.pcNwNameLabel.setObjectName("pcNwNameLabel")
        
        self.machineTypeLabel = QtWidgets.QLabel(Form)
        self.machineTypeLabel.setGeometry(QtCore.QRect(290, 234, 111, 41))
        self.machineTypeLabel.setObjectName("machineTypeLabel")
        
        self.platformTypeLabel = QtWidgets.QLabel(Form)
        self.platformTypeLabel.setGeometry(QtCore.QRect(290, 259, 101, 51))
        self.platformTypeLabel.setObjectName("platformTypeLabel")
        
        self.osDetailsLabel = QtWidgets.QLabel(Form)
        self.osDetailsLabel.setGeometry(QtCore.QRect(290, 300, 81, 21))
        self.osDetailsLabel.setObjectName("osDetailsLabel")
        
        self.pcNwNameLine = QtWidgets.QLineEdit(Form)
        self.pcNwNameLine.setGeometry(QtCore.QRect(410, 220, 125, 16))
        self.pcNwNameLine.setReadOnly(True)
        self.pcNwNameLine.setObjectName("pcNwNameLine")
        
        self.machineTypeLine = QtWidgets.QLineEdit(Form)
        self.machineTypeLine.setGeometry(QtCore.QRect(410, 247, 125, 16))
        self.machineTypeLine.setReadOnly(True)
        self.machineTypeLine.setObjectName("machineTypeLine")
        
        self.platformTypeLine = QtWidgets.QLineEdit(Form)
        self.platformTypeLine.setGeometry(QtCore.QRect(410, 276, 125, 16))
        self.platformTypeLine.setReadOnly(True)
        self.platformTypeLine.setObjectName("platformTypeLine")
        
        self.osDetailsLine = QtWidgets.QLineEdit(Form)
        self.osDetailsLine.setGeometry(QtCore.QRect(410, 305, 125, 16))
        self.osDetailsLine.setReadOnly(True)
        self.osDetailsLine.setObjectName("osDetailsLine")
        
        self.dateLabel = QtWidgets.QLabel(Form)
        self.dateLabel.setGeometry(QtCore.QRect(440, 5, 140, 21))     
        self.dateLabel.setObjectName("dateLabel") 

        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(5, 5, 80, 21))
        self.refreshButton.setObjectName("refreshButton")

        self.lineEditContent()
        self.refreshButton.clicked.connect(self.lineEditContent)

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
        self.cpuNphysLabel.setText(_translate("Form", "Num. of phys. cores:"))
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
        
        ramAva = round(psutil.virtual_memory().available/1000000000, 2)
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
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("styleSheet.qss", "r").read())
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

