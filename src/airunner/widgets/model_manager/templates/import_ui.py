# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/model_manager/templates/import.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_import_model_widget(object):
    def setupUi(self, import_model_widget):
        import_model_widget.setObjectName("import_model_widget")
        import_model_widget.resize(521, 275)
        self.gridLayout_4 = QtWidgets.QGridLayout(import_model_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.import_form = QtWidgets.QFrame(parent=import_model_widget)
        self.import_form.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.import_form.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.import_form.setObjectName("import_form")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.import_form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.url_label = QtWidgets.QLabel(parent=self.import_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.gridLayout_2.addWidget(self.url_label, 0, 0, 1, 1)
        self.import_url = QtWidgets.QLineEdit(parent=self.import_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.import_url.setFont(font)
        self.import_url.setObjectName("import_url")
        self.gridLayout_2.addWidget(self.import_url, 1, 0, 1, 1)
        self.import_button = QtWidgets.QPushButton(parent=self.import_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.import_button.setFont(font)
        self.import_button.setObjectName("import_button")
        self.gridLayout_2.addWidget(self.import_button, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.import_form, 0, 0, 1, 1)
        self.model_select_form = QtWidgets.QFrame(parent=import_model_widget)
        self.model_select_form.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.model_select_form.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.model_select_form.setObjectName("model_select_form")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.model_select_form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.download_button = QtWidgets.QPushButton(parent=self.model_select_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.download_button.setFont(font)
        self.download_button.setObjectName("download_button")
        self.gridLayout_3.addWidget(self.download_button, 2, 0, 1, 1)
        self.cancel_download_save_button = QtWidgets.QPushButton(parent=self.model_select_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cancel_download_save_button.setFont(font)
        self.cancel_download_save_button.setObjectName("cancel_download_save_button")
        self.gridLayout_3.addWidget(self.cancel_download_save_button, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.model_version_label = QtWidgets.QLabel(parent=self.model_select_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.model_version_label.setFont(font)
        self.model_version_label.setObjectName("model_version_label")
        self.verticalLayout.addWidget(self.model_version_label)
        self.model_choices = QtWidgets.QComboBox(parent=self.model_select_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.model_choices.setFont(font)
        self.model_choices.setObjectName("model_choices")
        self.verticalLayout.addWidget(self.model_choices)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.model_form_frame = QtWidgets.QVBoxLayout()
        self.model_form_frame.setObjectName("model_form_frame")
        self.gridLayout_3.addLayout(self.model_form_frame, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.model_select_form, 1, 0, 1, 1)
        self.download_form = QtWidgets.QFrame(parent=import_model_widget)
        self.download_form.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.download_form.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.download_form.setObjectName("download_form")
        self.gridLayout = QtWidgets.QGridLayout(self.download_form)
        self.gridLayout.setObjectName("gridLayout")
        self.downloading_label = QtWidgets.QLabel(parent=self.download_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.downloading_label.setFont(font)
        self.downloading_label.setObjectName("downloading_label")
        self.gridLayout.addWidget(self.downloading_label, 0, 0, 1, 1)
        self.cancel_download_button = QtWidgets.QPushButton(parent=self.download_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cancel_download_button.setFont(font)
        self.cancel_download_button.setObjectName("cancel_download_button")
        self.gridLayout.addWidget(self.cancel_download_button, 1, 0, 1, 1)
        self.download_progress_bar = QtWidgets.QProgressBar(parent=self.download_form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.download_progress_bar.setFont(font)
        self.download_progress_bar.setProperty("value", 0)
        self.download_progress_bar.setObjectName("download_progress_bar")
        self.gridLayout.addWidget(self.download_progress_bar, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.download_form, 2, 0, 1, 1)

        self.retranslateUi(import_model_widget)
        self.download_button.clicked.connect(import_model_widget.action_clicked_button_download) # type: ignore
        self.cancel_download_save_button.clicked.connect(import_model_widget.action_clicked_button_cancel) # type: ignore
        self.cancel_download_button.clicked.connect(import_model_widget.action_clicked_button_cancel) # type: ignore
        self.import_button.clicked.connect(import_model_widget.action_clicked_button_import) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(import_model_widget)

    def retranslateUi(self, import_model_widget):
        _translate = QtCore.QCoreApplication.translate
        import_model_widget.setWindowTitle(_translate("import_model_widget", "Form"))
        self.url_label.setText(_translate("import_model_widget", "CivitAI.com URL"))
        self.import_url.setPlaceholderText(_translate("import_model_widget", "URL"))
        self.import_button.setText(_translate("import_model_widget", "Import"))
        self.download_button.setText(_translate("import_model_widget", "Download and Save"))
        self.cancel_download_save_button.setText(_translate("import_model_widget", "Cancel"))
        self.model_version_label.setText(_translate("import_model_widget", "Model Version"))
        self.downloading_label.setText(_translate("import_model_widget", "Downloading model name here"))
        self.cancel_download_button.setText(_translate("import_model_widget", "Cancel"))
