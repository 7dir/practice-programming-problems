from PyQt4 import QtCore, QtGui
import sys, re, math

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Calculator(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.show()
    def setupUi(self, Calculator):
        Calculator.setObjectName(_fromUtf8("Calculator"))
        Calculator.setEnabled(True)
        Calculator.setFixedSize(350, 250)
        self.gridLayout_2 = QtGui.QGridLayout(Calculator)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textInput = QtGui.QPlainTextEdit(Calculator)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textInput.setFont(font)
        self.textInput.setObjectName(_fromUtf8("textInput"))
        self.gridLayout_2.addWidget(self.textInput, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnClear = QtGui.QPushButton(Calculator)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.btnClear.setToolTip("Clear Display")
        self.gridLayout.addWidget(self.btnClear, 0, 4, 1, 1)
        self.btnOne = QtGui.QPushButton(Calculator)
        self.btnOne.setObjectName(_fromUtf8("btnOne"))
        self.gridLayout.addWidget(self.btnOne, 2, 0, 1, 1)
        self.btnTwo = QtGui.QPushButton(Calculator)
        self.btnTwo.setObjectName(_fromUtf8("btnTwo"))
        self.gridLayout.addWidget(self.btnTwo, 2, 1, 1, 1)
        self.btnEight = QtGui.QPushButton(Calculator)
        self.btnEight.setObjectName(_fromUtf8("btnEight"))
        self.gridLayout.addWidget(self.btnEight, 0, 1, 1, 1)
        self.btnSeven = QtGui.QPushButton(Calculator)
        self.btnSeven.setObjectName(_fromUtf8("btnSeven"))
        self.gridLayout.addWidget(self.btnSeven, 0, 0, 1, 1)
        self.btnMultiply = QtGui.QPushButton(Calculator)
        self.btnMultiply.setObjectName(_fromUtf8("btnMultiply"))
        self.btnMultiply.setToolTip("Multiply[*]")
        self.gridLayout.addWidget(self.btnMultiply, 1, 3, 1, 1)
        self.btnDecimalPoint = QtGui.QPushButton(Calculator)
        self.btnDecimalPoint.setObjectName(_fromUtf8("btnDecimalPoint"))
        self.gridLayout.addWidget(self.btnDecimalPoint, 3, 1, 1, 1)
        self.btnCloseParen = QtGui.QPushButton(Calculator)
        self.btnCloseParen.setObjectName(_fromUtf8("btnCloseParen"))
        self.btnCloseParen.setToolTip("End Group[)]")
        self.gridLayout.addWidget(self.btnCloseParen, 1, 5, 1, 1)
        self.btnSquare = QtGui.QPushButton(Calculator)
        self.btnSquare.setObjectName(_fromUtf8("btnSquare"))
        self.btnSquare.setToolTip("Square[x^2]")
        self.gridLayout.addWidget(self.btnSquare, 2, 4, 1, 1)
        self.btnSqrt = QtGui.QPushButton(Calculator)
        self.btnSqrt.setObjectName(_fromUtf8("btnSqrt"))
        self.btnSqrt.setToolTip("Square root[" + unichr(0x221A) + "x]")
        self.gridLayout.addWidget(self.btnSqrt, 2, 5, 1, 1)
        self.btnSix = QtGui.QPushButton(Calculator)
        self.btnSix.setObjectName(_fromUtf8("btnSix"))
        self.gridLayout.addWidget(self.btnSix, 1, 2, 1, 1)
        self.btnBackspace = QtGui.QPushButton(Calculator)
        self.btnBackspace.setObjectName(_fromUtf8("btnBackspace"))
        self.gridLayout.addWidget(self.btnBackspace, 0, 5, 1, 1)
        self.btnNine = QtGui.QPushButton(Calculator)
        self.btnNine.setObjectName(_fromUtf8("btnNine"))
        self.gridLayout.addWidget(self.btnNine, 0, 2, 1, 1)
        self.btnFive = QtGui.QPushButton(Calculator)
        self.btnFive.setObjectName(_fromUtf8("btnFive"))
        self.gridLayout.addWidget(self.btnFive, 1, 1, 1, 1)
        self.btnSubtract = QtGui.QPushButton(Calculator)
        self.btnSubtract.setObjectName(_fromUtf8("btnSubtract"))
        self.btnSubtract.setToolTip("Subtract[-]")
        self.gridLayout.addWidget(self.btnSubtract, 2, 3, 1, 1)
        self.btnZero = QtGui.QPushButton(Calculator)
        self.btnZero.setObjectName(_fromUtf8("btnZero"))
        self.gridLayout.addWidget(self.btnZero, 3, 0, 1, 1)
        self.btnOpenParen = QtGui.QPushButton(Calculator)
        self.btnOpenParen.setObjectName(_fromUtf8("btnOpenParen"))
        self.btnOpenParen.setToolTip("Start Group[(]")
        self.gridLayout.addWidget(self.btnOpenParen, 1, 4, 1, 1)
        self.btnDivide = QtGui.QPushButton(Calculator)
        self.btnDivide.setObjectName(_fromUtf8("btnDivide"))
        self.btnDivide.setToolTip("Divide[/]")
        self.gridLayout.addWidget(self.btnDivide, 0, 3, 1, 1)
        self.btnAdd = QtGui.QPushButton(Calculator)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.btnAdd.setToolTip("Add[+]")
        self.gridLayout.addWidget(self.btnAdd, 3, 3, 1, 1)
        self.btnFour = QtGui.QPushButton(Calculator)
        self.btnFour.setObjectName(_fromUtf8("btnFour"))
        self.gridLayout.addWidget(self.btnFour, 1, 0, 1, 1)
        self.btnPercent = QtGui.QPushButton(Calculator)
        self.btnPercent.setObjectName(_fromUtf8("btnPercent"))
        self.btnPercent.setToolTip("Percentage[%]")
        self.gridLayout.addWidget(self.btnPercent, 3, 2, 1, 1)
        self.btnSolve = QtGui.QPushButton(Calculator)
        self.btnSolve.setObjectName(_fromUtf8("btnSolve"))
        self.btnSolve.setToolTip("Calculate Result")
        self.gridLayout.addWidget(self.btnSolve, 3, 4, 1, 2)
        self.btnThree = QtGui.QPushButton(Calculator)
        self.btnThree.setObjectName(_fromUtf8("btnThree"))
        self.gridLayout.addWidget(self.btnThree, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(_translate("Calculator", "Calculator", None))
        self.btnClear.setText(_translate("Calculator", "clear", None))
        self.btnOne.setText(_translate("Calculator", "1", None))
        self.btnTwo.setText(_translate("Calculator", "2", None))
        self.btnEight.setText(_translate("Calculator", "8", None))
        self.btnSeven.setText(_translate("Calculator", "7", None))
        self.btnMultiply.setText(_translate("Calculator", "*", None))
        self.btnDecimalPoint.setText(_translate("Calculator", ".", None))
        self.btnCloseParen.setText(_translate("Calculator", ")", None))
        self.btnSquare.setText(_translate("Calculator", "^2", None))
        self.btnSqrt.setText(_translate("Calculator", unichr(0x221A), None))
        self.btnSix.setText(_translate("Calculator", "6", None))
        self.btnBackspace.setText(_translate("Calculator", "bksp", None))
        self.btnNine.setText(_translate("Calculator", "9", None))
        self.btnFive.setText(_translate("Calculator", "5", None))
        self.btnSubtract.setText(_translate("Calculator", "-", None))
        self.btnZero.setText(_translate("Calculator", "0", None))
        self.btnOpenParen.setText(_translate("Calculator", "(", None))
        self.btnDivide.setText(_translate("Calculator", "/", None))
        self.btnAdd.setText(_translate("Calculator", "+", None))
        self.btnFour.setText(_translate("Calculator", "4", None))
        self.btnPercent.setText(_translate("Calculator", "%", None))
        self.btnSolve.setText(_translate("Calculator", "=", None))
        self.btnThree.setText(_translate("Calculator", "3", None))
        
        # Connections for pressing numbers 0-9
        self.btnZero.clicked.connect(self.pressBtn)
        self.btnOne.clicked.connect(self.pressBtn)
        self.btnTwo.clicked.connect(self.pressBtn)
        self.btnThree.clicked.connect(self.pressBtn)
        self.btnFour.clicked.connect(self.pressBtn)
        self.btnFive.clicked.connect(self.pressBtn)
        self.btnSix.clicked.connect(self.pressBtn)
        self.btnSeven.clicked.connect(self.pressBtn)
        self.btnEight.clicked.connect(self.pressBtn)
        self.btnNine.clicked.connect(self.pressBtn)
        
        self.btnDecimalPoint.clicked.connect(self.pressBtn)
        self.btnPercent.clicked.connect(self.pressBtn)
        self.btnAdd.clicked.connect(self.pressBtn)
        self.btnSubtract.clicked.connect(self.pressBtn)
        self.btnMultiply.clicked.connect(self.pressBtn)
        self.btnOpenParen.clicked.connect(self.pressBtn)
        self.btnCloseParen.clicked.connect(self.pressBtn)
        self.btnDivide.clicked.connect(self.pressBtn)
        
        self.btnSquare.clicked.connect(self.pressBtn)
        self.btnSqrt.clicked.connect(self.pressBtn)
        self.btnClear.clicked.connect(self.pressClear)

        self.btnSolve.clicked.connect(lambda: self.compute(self.textInput.toPlainText()))

    def pressClear(self):
        self.textInput.clear()
        self.textInput.setFocus()

    def pressBtn(self):
        if self.sender().text() == unichr(0x221A):
            self.textInput.insertPlainText("math.sqrt(")
        elif self.sender().text() == "^2":
            self.textInput.insertPlainText("**2")
        elif self.sender().text() == "%":
            self.textInput.insertPlainText("/100.0")
        else:
            self.textInput.insertPlainText(self.sender().text())
        self.textInput.setFocus()

    def compute(self, given_expr):
        self.textInput.clear()
        self.textInput.insertPlainText(str(eval(str(given_expr))))
        self.textInput.setFocus()

def main():
    app = QtGui.QApplication([])
    calculator = Ui_Calculator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    # app = QtGui.QApplication(sys.argv)
    # ex = Ui_Calculator()
    # ex.show()
    # sys.exit(app.exec_())