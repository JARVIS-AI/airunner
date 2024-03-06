# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/image_generator_preferences/templates/image_generator_preferences.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_image_generator_preferences(object):
    def setupUi(self, image_generator_preferences):
        image_generator_preferences.setObjectName("image_generator_preferences")
        image_generator_preferences.resize(496, 416)
        self.gridLayout = QtWidgets.QGridLayout(image_generator_preferences)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=image_generator_preferences)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)
        self.action = QtWidgets.QComboBox(parent=self.groupBox)
        self.action.setObjectName("action")
        self.gridLayout_2.addWidget(self.action, 8, 0, 1, 1)
        self.pipeline = QtWidgets.QComboBox(parent=self.groupBox)
        self.pipeline.setObjectName("pipeline")
        self.gridLayout_2.addWidget(self.pipeline, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.category = QtWidgets.QComboBox(parent=self.groupBox)
        self.category.setObjectName("category")
        self.gridLayout_2.addWidget(self.category, 1, 0, 1, 1)
        self.generator_form = StableDiffusionSettingsWidget(parent=self.groupBox)
        self.generator_form.setObjectName("generator_form")
        self.gridLayout_2.addWidget(self.generator_form, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(image_generator_preferences)
        self.category.currentTextChanged['QString'].connect(image_generator_preferences.category_changed) # type: ignore
        self.pipeline.currentTextChanged['QString'].connect(image_generator_preferences.pipeline_changed) # type: ignore
        self.action.currentTextChanged['QString'].connect(image_generator_preferences.action_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(image_generator_preferences)

    def retranslateUi(self, image_generator_preferences):
        _translate = QtCore.QCoreApplication.translate
        image_generator_preferences.setWindowTitle(_translate("image_generator_preferences", "Form"))
        self.label_4.setText(_translate("image_generator_preferences", "Action"))
        self.label.setText(_translate("image_generator_preferences", "Category"))
        self.label_2.setText(_translate("image_generator_preferences", "Pipeline"))
from airunner.widgets.stablediffusion.stable_diffusion_settings_widget import StableDiffusionSettingsWidget
