# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/slider/templates/slider.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_slider_widget(object):
    def setupUi(self, slider_widget):
        slider_widget.setObjectName("slider_widget")
        slider_widget.resize(242, 93)
        slider_widget.setStyleSheet("")
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
        self.slider.setStyleSheet("")
        self.slider.setMaximum(100)
        self.slider.setPageStep(1)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout.addWidget(self.slider, 0, 0, 1, 1)
        self.slider_spinbox = QtWidgets.QDoubleSpinBox(parent=slider_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_spinbox.sizePolicy().hasHeightForWidth())
        self.slider_spinbox.setSizePolicy(sizePolicy)
        self.slider_spinbox.setStyleSheet("")
        self.slider_spinbox.setWrapping(False)
        self.slider_spinbox.setFrame(False)
        self.slider_spinbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.slider_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.slider_spinbox.setProperty("showGroupSeparator", False)
        self.slider_spinbox.setMaximum(1.0)
        self.slider_spinbox.setSingleStep(0.01)
        self.slider_spinbox.setObjectName("slider_spinbox")
        self.gridLayout.addWidget(self.slider_spinbox, 0, 1, 1, 1)

        self.retranslateUi(slider_widget)
        QtCore.QMetaObject.connectSlotsByName(slider_widget)

    def retranslateUi(self, slider_widget):
        _translate = QtCore.QCoreApplication.translate
        slider_widget.setWindowTitle(_translate("slider_widget", "Form"))
