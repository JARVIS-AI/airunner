# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/upscale/templates/upscale_widget.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_upscale_widget(object):
    def setupUi(self, upscale_widget):
        upscale_widget.setObjectName("upscale_widget")
        upscale_widget.resize(408, 300)
        self.gridLayout = QtWidgets.QGridLayout(upscale_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(upscale_widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.upscale_model_2 = QtWidgets.QComboBox(self.groupBox)
        self.upscale_model_2.setObjectName("upscale_model_2")
        self.upscale_model_2.addItem("")
        self.upscale_model_2.addItem("")
        self.upscale_model_2.addItem("")
        self.upscale_model_2.addItem("")
        self.upscale_model_2.addItem("")
        self.upscale_model_2.addItem("")
        self.horizontalLayout_8.addWidget(self.upscale_model_2)
        self.face_enhance_2 = QtWidgets.QCheckBox(self.groupBox)
        self.face_enhance_2.setObjectName("face_enhance_2")
        self.horizontalLayout_8.addWidget(self.face_enhance_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_2)
        self.upscale_2x_2 = QtWidgets.QPushButton(self.groupBox)
        self.upscale_2x_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.upscale_2x_2.setObjectName("upscale_2x_2")
        self.horizontalLayout_9.addWidget(self.upscale_2x_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(upscale_widget)
        self.comboBox_2.currentTextChanged['QString'].connect(upscale_widget.upscale_amount_changed) # type: ignore
        self.upscale_2x_2.clicked.connect(upscale_widget.upscale_clicked) # type: ignore
        self.upscale_model_2.currentTextChanged['QString'].connect(upscale_widget.model_changed) # type: ignore
        self.face_enhance_2.toggled['bool'].connect(upscale_widget.face_enhance_toggled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(upscale_widget)

    def retranslateUi(self, upscale_widget):
        _translate = QtCore.QCoreApplication.translate
        upscale_widget.setWindowTitle(_translate("upscale_widget", "Form"))
        self.groupBox.setTitle(_translate("upscale_widget", "Upscale"))
        self.upscale_model_2.setItemText(0, _translate("upscale_widget", "RealESRGAN_x4plus"))
        self.upscale_model_2.setItemText(1, _translate("upscale_widget", "RealESRNet_x4plus"))
        self.upscale_model_2.setItemText(2, _translate("upscale_widget", "RealESRGAN_x4plus_anime_6B"))
        self.upscale_model_2.setItemText(3, _translate("upscale_widget", "RealESRGAN_x2plus"))
        self.upscale_model_2.setItemText(4, _translate("upscale_widget", "realesr-animevideov3"))
        self.upscale_model_2.setItemText(5, _translate("upscale_widget", "realesr-general-x4v3"))
        self.face_enhance_2.setText(_translate("upscale_widget", "Face enhance"))
        self.comboBox_2.setItemText(0, _translate("upscale_widget", "2x"))
        self.comboBox_2.setItemText(1, _translate("upscale_widget", "4x"))
        self.upscale_2x_2.setText(_translate("upscale_widget", "Upscale"))
