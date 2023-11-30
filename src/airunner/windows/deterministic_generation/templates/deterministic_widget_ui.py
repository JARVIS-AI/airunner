# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/windows/deterministic_generation/templates/deterministic_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(203, 233)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(203, 233))
        Form.setMaximumSize(QtCore.QSize(203, 233))
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 202, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.new_batch_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_batch_button.setFont(font)
        self.new_batch_button.setObjectName("new_batch_button")
        self.gridLayout.addWidget(self.new_batch_button, 1, 0, 1, 1)
        self.thumbnail = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy)
        self.thumbnail.setMinimumSize(QtCore.QSize(200, 200))
        self.thumbnail.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.thumbnail.setFont(font)
        self.thumbnail.setStyleSheet("border: 1px solid black")
        self.thumbnail.setText("")
        self.thumbnail.setObjectName("thumbnail")
        self.gridLayout.addWidget(self.thumbnail, 0, 0, 1, 2)
        self.to_canvas_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_canvas_button.setFont(font)
        self.to_canvas_button.setObjectName("to_canvas_button")
        self.gridLayout.addWidget(self.to_canvas_button, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.new_batch_button.setToolTip(_translate("Form", "Generate a new batch of four images using this as the  base image."))
        self.new_batch_button.setText(_translate("Form", "New Batch"))
        self.to_canvas_button.setToolTip(_translate("Form", "Send this image to the canvas"))
        self.to_canvas_button.setText(_translate("Form", "To Canvas"))
