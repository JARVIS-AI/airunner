# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/image/templates/image_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_image_widget(object):
    def setupUi(self, image_widget):
        image_widget.setObjectName("image_widget")
        image_widget.resize(128, 128)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(image_widget.sizePolicy().hasHeightForWidth())
        image_widget.setSizePolicy(sizePolicy)
        image_widget.setMinimumSize(QtCore.QSize(0, 0))
        image_widget.setMaximumSize(QtCore.QSize(128, 128))
        self.gridLayout = QtWidgets.QGridLayout(image_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.image_frame = QtWidgets.QFrame(parent=image_widget)
        self.image_frame.setMinimumSize(QtCore.QSize(128, 128))
        self.image_frame.setMaximumSize(QtCore.QSize(128, 128))
        self.image_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.image_frame.setObjectName("image_frame")
        self.gridLayout.addWidget(self.image_frame, 0, 0, 1, 1)

        self.retranslateUi(image_widget)
        QtCore.QMetaObject.connectSlotsByName(image_widget)

    def retranslateUi(self, image_widget):
        _translate = QtCore.QCoreApplication.translate
        image_widget.setWindowTitle(_translate("image_widget", "Form"))