# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/export_preferences.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(457, 429)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.actionAuto_export_images = QtWidgets.QCheckBox(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.actionAuto_export_images.setFont(font)
        self.actionAuto_export_images.setObjectName("actionAuto_export_images")
        self.gridLayout_2.addWidget(self.actionAuto_export_images, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.image_path = QtWidgets.QLineEdit(parent=Form)
        self.image_path.setObjectName("image_path")
        self.gridLayout_2.addWidget(self.image_path, 4, 0, 1, 1)
        self.image_path_browse_button = QtWidgets.QPushButton(parent=Form)
        self.image_path_browse_button.setObjectName("image_path_browse_button")
        self.gridLayout_2.addWidget(self.image_path_browse_button, 4, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(parent=Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 5, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 8, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.export_metadata = QtWidgets.QCheckBox(parent=Form)
        self.export_metadata.setObjectName("export_metadata")
        self.gridLayout.addWidget(self.export_metadata, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.metadata_prompt = QtWidgets.QCheckBox(parent=Form)
        self.metadata_prompt.setObjectName("metadata_prompt")
        self.gridLayout.addWidget(self.metadata_prompt, 2, 0, 1, 1)
        self.metadata_samples = QtWidgets.QCheckBox(parent=Form)
        self.metadata_samples.setObjectName("metadata_samples")
        self.gridLayout.addWidget(self.metadata_samples, 2, 1, 1, 1)
        self.metadata_negative_prompt = QtWidgets.QCheckBox(parent=Form)
        self.metadata_negative_prompt.setObjectName("metadata_negative_prompt")
        self.gridLayout.addWidget(self.metadata_negative_prompt, 3, 0, 1, 1)
        self.metadata_model = QtWidgets.QCheckBox(parent=Form)
        self.metadata_model.setObjectName("metadata_model")
        self.gridLayout.addWidget(self.metadata_model, 3, 1, 1, 1)
        self.metadata_scale = QtWidgets.QCheckBox(parent=Form)
        self.metadata_scale.setObjectName("metadata_scale")
        self.gridLayout.addWidget(self.metadata_scale, 4, 0, 1, 1)
        self.metadata_model_branch = QtWidgets.QCheckBox(parent=Form)
        self.metadata_model_branch.setObjectName("metadata_model_branch")
        self.gridLayout.addWidget(self.metadata_model_branch, 4, 1, 1, 1)
        self.metadata_seed = QtWidgets.QCheckBox(parent=Form)
        self.metadata_seed.setObjectName("metadata_seed")
        self.gridLayout.addWidget(self.metadata_seed, 5, 0, 1, 1)
        self.metadata_scheduler = QtWidgets.QCheckBox(parent=Form)
        self.metadata_scheduler.setObjectName("metadata_scheduler")
        self.gridLayout.addWidget(self.metadata_scheduler, 5, 1, 1, 1)
        self.metadata_steps = QtWidgets.QCheckBox(parent=Form)
        self.metadata_steps.setObjectName("metadata_steps")
        self.gridLayout.addWidget(self.metadata_steps, 6, 0, 1, 1)
        self.metadata_ddim_eta = QtWidgets.QCheckBox(parent=Form)
        self.metadata_ddim_eta.setObjectName("metadata_ddim_eta")
        self.gridLayout.addWidget(self.metadata_ddim_eta, 6, 1, 1, 1)
        self.metadata_iterations = QtWidgets.QCheckBox(parent=Form)
        self.metadata_iterations.setObjectName("metadata_iterations")
        self.gridLayout.addWidget(self.metadata_iterations, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.import_metadata = QtWidgets.QCheckBox(parent=Form)
        self.import_metadata.setObjectName("import_metadata")
        self.gridLayout.addWidget(self.import_metadata, 7, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 9, 0, 1, 2)
        self.image_type_dropdown = QtWidgets.QComboBox(parent=Form)
        self.image_type_dropdown.setObjectName("image_type_dropdown")
        self.gridLayout_2.addWidget(self.image_type_dropdown, 7, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.actionAuto_export_images.setText(_translate("Form", "Automatically export images"))
        self.label.setText(_translate("Form", "Image export folder"))
        self.label_2.setText(_translate("Form", "Folder to auto export images to"))
        self.image_path_browse_button.setText(_translate("Form", "Browse"))
        self.label_5.setText(_translate("Form", "Image type"))
        self.label_3.setText(_translate("Form", "Metadata"))
        self.export_metadata.setToolTip(_translate("Form", "<html><head/><body><p>Export metadata along with images. </p><p>Only works with PNG files.</p></body></html>"))
        self.export_metadata.setText(_translate("Form", "Export metadata"))
        self.label_4.setText(_translate("Form", "Choose which metadata to include with exported images"))
        self.metadata_prompt.setText(_translate("Form", "Prompt"))
        self.metadata_samples.setText(_translate("Form", "Samples"))
        self.metadata_negative_prompt.setText(_translate("Form", "Negative prompt"))
        self.metadata_model.setText(_translate("Form", "Model"))
        self.metadata_scale.setText(_translate("Form", "Scale"))
        self.metadata_model_branch.setText(_translate("Form", "Model Branch"))
        self.metadata_seed.setText(_translate("Form", "Seed"))
        self.metadata_scheduler.setText(_translate("Form", "Scheduler"))
        self.metadata_steps.setText(_translate("Form", "Steps"))
        self.metadata_ddim_eta.setText(_translate("Form", "DDIM ETA"))
        self.metadata_iterations.setText(_translate("Form", "Iterations"))
        self.import_metadata.setToolTip(_translate("Form", "<html><head/><body><p>Automatically load metadata into generator options. </p><p>Only works with PNG files.</p></body></html>"))
        self.import_metadata.setText(_translate("Form", "Import metadata"))
