from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5 import uic,QtWidgets
import sys

class calculatorClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calculator.ui',self)
        self.show()
        self.memLabel = self.findChild(QLabel,'memLabel')
        self.mainLabel = self.findChild(QLabel,'mainLabel')
        self.memLabel.setText('')
        self.mainLabel.setText('0')
        self.btnOn = self.findChild(QPushButton,'btnon')
        self.btnClear = self.findChild(QPushButton, 'btnclear')
        self.btnOn.clicked.connect(self.clearFunction)
        self.btnclear.clicked.connect(self.clearFunction)

        self.numArray = []
        collection = self.findChildren(QPushButton)
        for x in collection:
            if x.text().isnumeric():
                self.numArray.append(x)
        for x in self.numArray:
            x.clicked.connect(self.readKey)
        #QMessageBox.information(self,'info',str(len(self.numArray)))

        self.actionArray = []
        self.actionArray.append(self.findChild(QPushButton, 'add'))
        self.actionArray.append(self.findChild(QPushButton, 'sub'))
        self.actionArray.append(self.findChild(QPushButton, 'mul'))
        self.actionArray.append(self.findChild(QPushButton, 'div'))
        for x in self.actionArray:
            x.clicked.connect(self.actionFunction)

        self.btndot = self.findChild(QPushButton,'btndot')
        self.btnsign = self.findChild(QPushButton, 'btnsign')
        self.btndot.clicked.connect(self.dotFunction)
        self.btnsign.clicked.connect(self.signFunction)

        self.solveBtn = self.findChild(QPushButton, 'btnSolve')
        self.solveBtn.clicked.connect(self.solveFunction)

        self.op1 = ''
        self.op2 = ''
        self.operation = ''
        self.ans = ''

    def clearFunction(self):
        self.memLabel.setText('')
        self.mainLabel.setText('0')
        self.op1 = ''
        self.op2 = ''
        self.operation = ''
        self.actionStr = ''
        self.ans = ''

    def dotFunction(self):
        if not self.operation:
            self.op1 = self.op1 + '.'
            self.mainLabel.setText(self.op1)
        else:
            self.op2 = self.op2 + '.'
            self.mainLabel.setText(self.op2)
        #QMessageBox.information(self,'info','Button Pressed'+str(a.text()))

    def signFunction(self):
        if not self.operation:
            if self.op1[0]=='-':
                self.op1 = self.op1[1:]
            else:
                self.op1 = '-' + self.op1
            self.mainLabel.setText(self.op1)
        else:
            if self.op2[0]=='-':
                self.op2= self.op2[1:]
            else:
                self.op2 = '-' + self.op2
            self.mainLabel.setText(self.op2)
        #QMessageBox.information(self,'info','Button Pressed'+str(a.text()))

    def actionFunction(self):
        if len(self.ans)>0:
            self.op1 = self.ans
        if len(self.op1)>0:
            self.operation = self.sender().text()
            if len(self.op2)>0:
                self.solveFunction()
                self.operation = self.sender().text()
                self.op1 = self.ans

    def solveFunction(self):
        #print('op1:',self.op1)
        #print('op2:',self.op2)
        #print('ans:',self.ans)
        if len(self.op1)>0 and len(self.op2)>0 and len(self.operation)>0:
            op1 = float(self.op1)
            op2 = float(self.op2)
            if self.operation=='+':
                ans = op1+op2
            elif self.operation=='-':
                ans = op1-op2
            elif self.operation=='X':
                ans = op1*op2
            elif self.operation=='/':
                try:
                    ans = op1/op2
                except ZeroDivisionError:
                    ans = 0
            else:
                QMessageBox.information(self,'info','Error while solving!!!',QMessageBox.Yes)
            self.op1 = ''
            self.op2 = ''
            self.operation = ''
            self.ans = '{:g}'.format(ans)
        #print('{:g}'.format(ans))
        self.mainLabel.setText(self.ans)

    def readKey(self):
        a = self.sender()
        if not self.operation:
            self.ans = ''
            self.op1 = self.op1 + a.text()
            self.mainLabel.setText(self.op1)
        else:
            self.op2 = self.op2 + a.text()
            self.mainLabel.setText(self.op2)
        #QMessageBox.information(self,'info','Button Pressed'+str(a.text()))



app = QApplication(sys.argv)
window = calculatorClass()
sys.exit(app.exec())
