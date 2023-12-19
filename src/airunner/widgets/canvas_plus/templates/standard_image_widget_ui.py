# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/canvas_plus/templates/standard_image_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_standard_image_widget(object):
    def setupUi(self, standard_image_widget):
        standard_image_widget.setObjectName("standard_image_widget")
        standard_image_widget.resize(552, 1194)
        standard_image_widget.setMaximumSize(QtCore.QSize(552, 16777215))
        self.gridLayout_2 = QtWidgets.QGridLayout(standard_image_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_frame = QtWidgets.QFrame(parent=standard_image_widget)
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
        self.controls_container = QtWidgets.QWidget(parent=standard_image_widget)
        self.controls_container.setObjectName("controls_container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controls_container)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.export_button = QtWidgets.QPushButton(parent=self.controls_container)
        self.export_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.export_button.setObjectName("export_button")
        self.horizontalLayout.addWidget(self.export_button)
        self.delete_button = QtWidgets.QPushButton(parent=self.controls_container)
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.to_canvas_button = QtWidgets.QPushButton(parent=self.controls_container)
        self.to_canvas_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.to_canvas_button.setObjectName("to_canvas_button")
        self.horizontalLayout.addWidget(self.to_canvas_button)
        self.verticalLayout.addWidget(self.controls_container)
        self.delete_confirmation = QtWidgets.QWidget(parent=standard_image_widget)
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
        self.confirm_delete_button = QtWidgets.QPushButton(parent=self.delete_confirmation)
        self.confirm_delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.confirm_delete_button.setObjectName("confirm_delete_button")
        self.gridLayout.addWidget(self.confirm_delete_button, 4, 0, 1, 1)
        self.cancel_delete_button = QtWidgets.QPushButton(parent=self.delete_confirmation)
        self.cancel_delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cancel_delete_button.setObjectName("cancel_delete_button")
        self.gridLayout.addWidget(self.cancel_delete_button, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.delete_confirmation)
        self.similar_groupbox = QtWidgets.QGroupBox(parent=standard_image_widget)
        self.similar_groupbox.setObjectName("similar_groupbox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.similar_groupbox)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.samples_widget = SliderWidget(parent=self.similar_groupbox)
        self.samples_widget.setMinimumSize(QtCore.QSize(0, 20))
        self.samples_widget.setProperty("slider_callback", "handle_value_change")
        self.samples_widget.setProperty("current_value", 100)
        self.samples_widget.setProperty("slider_maximum", 100)
        self.samples_widget.setProperty("spinbox_maximum", 1.0)
        self.samples_widget.setProperty("display_as_float", True)
        self.samples_widget.setProperty("spinbox_single_step", 0.01)
        self.samples_widget.setProperty("spinbox_page_step", 0.01)
        self.samples_widget.setProperty("spinbox_minimum", 0.0)
        self.samples_widget.setProperty("slider_minimum", 0)
        self.samples_widget.setObjectName("samples_widget")
        self.horizontalLayout_3.addWidget(self.samples_widget)
        self.generate_single_simillar_button = QtWidgets.QPushButton(parent=self.similar_groupbox)
        self.generate_single_simillar_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_single_simillar_button.setObjectName("generate_single_simillar_button")
        self.horizontalLayout_3.addWidget(self.generate_single_simillar_button)
        self.generate_batch_similar_button = QtWidgets.QPushButton(parent=self.similar_groupbox)
        self.generate_batch_similar_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_batch_similar_button.setObjectName("generate_batch_similar_button")
        self.horizontalLayout_3.addWidget(self.generate_batch_similar_button)
        self.verticalLayout.addWidget(self.similar_groupbox)
        self.groupBox = QtWidgets.QGroupBox(parent=standard_image_widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.upscale_2x = QtWidgets.QPushButton(parent=self.groupBox)
        self.upscale_2x.setObjectName("upscale_2x")
        self.gridLayout_3.addWidget(self.upscale_2x, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=standard_image_widget)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 0, 1, 1)
        self.batch_container = QtWidgets.QWidget(parent=standard_image_widget)
        self.batch_container.setMinimumSize(QtCore.QSize(0, 128))
        self.batch_container.setStyleSheet("")
        self.batch_container.setObjectName("batch_container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.batch_container)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2.addWidget(self.batch_container, 5, 0, 1, 1)

        self.retranslateUi(standard_image_widget)
        self.confirm_delete_button.clicked.connect(standard_image_widget.confirm_delete) # type: ignore
        self.cancel_delete_button.clicked.connect(standard_image_widget.cancel_delete) # type: ignore
        self.to_canvas_button.clicked.connect(standard_image_widget.image_to_canvas) # type: ignore
        self.delete_button.clicked.connect(standard_image_widget.delete_image) # type: ignore
        self.generate_single_simillar_button.clicked.connect(standard_image_widget.similar_image) # type: ignore
        self.generate_batch_similar_button.clicked.connect(standard_image_widget.similar_batch) # type: ignore
        self.export_button.clicked.connect(standard_image_widget.export_image) # type: ignore
        self.upscale_2x.clicked.connect(standard_image_widget.upscale_2x_clicked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(standard_image_widget)

    def retranslateUi(self, standard_image_widget):
        _translate = QtCore.QCoreApplication.translate
        standard_image_widget.setWindowTitle(_translate("standard_image_widget", "Form"))
        self.export_button.setText(_translate("standard_image_widget", "Export"))
        self.delete_button.setToolTip(_translate("standard_image_widget", "Permanently delete this image"))
        self.delete_button.setText(_translate("standard_image_widget", "Delete"))
        self.to_canvas_button.setToolTip(_translate("standard_image_widget", "Send this image to the canvas"))
        self.to_canvas_button.setText(_translate("standard_image_widget", "To Canvas"))
        self.label.setText(_translate("standard_image_widget", "Permanently delete?"))
        self.confirm_delete_button.setText(_translate("standard_image_widget", "Yes"))
        self.cancel_delete_button.setText(_translate("standard_image_widget", "No"))
        self.similar_groupbox.setTitle(_translate("standard_image_widget", "Generate similar images"))
        self.samples_widget.setProperty("label_text", _translate("standard_image_widget", "Similarity"))
        self.samples_widget.setProperty("settings_property", _translate("standard_image_widget", "image_similarity"))
        self.generate_single_simillar_button.setToolTip(_translate("standard_image_widget", "Generate one variation"))
        self.generate_single_simillar_button.setText(_translate("standard_image_widget", "Single"))
        self.generate_batch_similar_button.setToolTip(_translate("standard_image_widget", "Generate a batch of four variations"))
        self.generate_batch_similar_button.setText(_translate("standard_image_widget", "Batch"))
        self.groupBox.setTitle(_translate("standard_image_widget", "Upscale"))
        self.upscale_2x.setText(_translate("standard_image_widget", "2x Upscale"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("standard_image_widget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("standard_image_widget", "New Column"))
from airunner.widgets.slider.slider_widget import SliderWidget