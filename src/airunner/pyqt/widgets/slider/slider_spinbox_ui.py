# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/slider/slider_spinbox.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(157, 67)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.slider = QtWidgets.QSlider(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.slider.setFont(font)
        self.slider.setMaximum(100)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout.addWidget(self.slider, 1, 0, 1, 1)
        self.spinbox = QtWidgets.QSpinBox(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinbox.setFont(font)
        self.spinbox.setObjectName("spinbox")
        self.gridLayout.addWidget(self.spinbox, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Label"))
