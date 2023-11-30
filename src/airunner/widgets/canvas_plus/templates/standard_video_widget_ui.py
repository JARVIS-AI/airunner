# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/canvas_plus/templates/standard_video_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_standard_video_widget(object):
    def setupUi(self, standard_video_widget):
        standard_video_widget.setObjectName("standard_video_widget")
        standard_video_widget.resize(552, 1194)
        standard_video_widget.setMaximumSize(QtCore.QSize(552, 16777215))
        self.gridLayout_2 = QtWidgets.QGridLayout(standard_video_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_frame = QtWidgets.QFrame(parent=standard_video_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_frame.sizePolicy().hasHeightForWidth())
        self.image_frame.setSizePolicy(sizePolicy)
        self.image_frame.setMinimumSize(QtCore.QSize(532, 532))
        self.image_frame.setMaximumSize(QtCore.QSize(532, 532))
        self.image_frame.setAcceptDrops(True)
        self.image_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.image_frame.setObjectName("image_frame")
        self.verticalLayout.addWidget(self.image_frame)
        self.controls_container = QtWidgets.QWidget(parent=standard_video_widget)
        self.controls_container.setObjectName("controls_container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controls_container)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.controls_container)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton = QtWidgets.QPushButton(parent=self.controls_container)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.controls_container)
        self.delete_confirmation = QtWidgets.QWidget(parent=standard_video_widget)
        self.delete_confirmation.setObjectName("delete_confirmation")
        self.gridLayout = QtWidgets.QGridLayout(self.delete_confirmation)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.delete_confirmation)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        self.button_container = QtWidgets.QWidget(parent=self.delete_confirmation)
        self.button_container.setObjectName("button_container")
        self.buttons = QtWidgets.QHBoxLayout(self.button_container)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setObjectName("buttons")
        self.gridLayout.addWidget(self.button_container, 0, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.delete_confirmation)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.delete_confirmation)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.delete_confirmation)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(standard_video_widget)
        self.pushButton_5.clicked.connect(standard_video_widget.confirm_delete) # type: ignore
        self.pushButton_6.clicked.connect(standard_video_widget.cancel_delete) # type: ignore
        self.pushButton.clicked.connect(standard_video_widget.delete_image) # type: ignore
        self.pushButton_7.clicked.connect(standard_video_widget.export_image) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(standard_video_widget)

    def retranslateUi(self, standard_video_widget):
        _translate = QtCore.QCoreApplication.translate
        standard_video_widget.setWindowTitle(_translate("standard_video_widget", "Form"))
        self.pushButton_7.setText(_translate("standard_video_widget", "Export"))
        self.pushButton.setToolTip(_translate("standard_video_widget", "Permanently delete this image"))
        self.pushButton.setText(_translate("standard_video_widget", "Delete"))
        self.label.setText(_translate("standard_video_widget", "Permanently delete?"))
        self.pushButton_5.setText(_translate("standard_video_widget", "Yes"))
        self.pushButton_6.setText(_translate("standard_video_widget", "No"))
