# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/slider/templates/slider.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_slider_widget(object):
    def setupUi(self, slider_widget):
        slider_widget.setObjectName("slider_widget")
        slider_widget.resize(242, 93)
        self.gridLayout = QtWidgets.QGridLayout(slider_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.slider = QtWidgets.QSlider(parent=slider_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy)
        self.slider.setAutoFillBackground(False)
        self.slider.setMaximum(100)
        self.slider.setPageStep(1)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout.addWidget(self.slider, 0, 0, 1, 1)
        self.spinbox = QtWidgets.QDoubleSpinBox(parent=slider_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox.sizePolicy().hasHeightForWidth())
        self.spinbox.setSizePolicy(sizePolicy)
        self.spinbox.setStyleSheet("background-color: transparent;")
        self.spinbox.setWrapping(False)
        self.spinbox.setFrame(False)
        self.spinbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinbox.setProperty("showGroupSeparator", False)
        self.spinbox.setMaximum(1.0)
        self.spinbox.setSingleStep(0.01)
        self.spinbox.setObjectName("spinbox")
        self.gridLayout.addWidget(self.spinbox, 0, 1, 1, 1)

        self.retranslateUi(slider_widget)
        QtCore.QMetaObject.connectSlotsByName(slider_widget)

    def retranslateUi(self, slider_widget):
        _translate = QtCore.QCoreApplication.translate
        slider_widget.setWindowTitle(_translate("slider_widget", "Form"))
