# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/lora/templates/lora_trigger_word.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_lora_trigger_word(object):
    def setupUi(self, lora_trigger_word):
        lora_trigger_word.setObjectName("lora_trigger_word")
        lora_trigger_word.resize(345, 43)
        self.horizontalLayout = QtWidgets.QHBoxLayout(lora_trigger_word)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.trigger_word = QtWidgets.QLabel(parent=lora_trigger_word)
        self.trigger_word.setObjectName("trigger_word")
        self.horizontalLayout.addWidget(self.trigger_word)
        self.button_to_prompt = QtWidgets.QPushButton(parent=lora_trigger_word)
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.button_to_prompt.setIcon(icon)
        self.button_to_prompt.setObjectName("button_to_prompt")
        self.horizontalLayout.addWidget(self.button_to_prompt)
        self.button_to_negative_prompt = QtWidgets.QPushButton(parent=lora_trigger_word)
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.button_to_negative_prompt.setIcon(icon)
        self.button_to_negative_prompt.setObjectName("button_to_negative_prompt")
        self.horizontalLayout.addWidget(self.button_to_negative_prompt)

        self.retranslateUi(lora_trigger_word)
        self.button_to_prompt.clicked['bool'].connect(lora_trigger_word.action_click_button_to_prompt) # type: ignore
        self.button_to_negative_prompt.clicked.connect(lora_trigger_word.action_click_button_to_negative_prompt) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(lora_trigger_word)

    def retranslateUi(self, lora_trigger_word):
        _translate = QtCore.QCoreApplication.translate
        lora_trigger_word.setWindowTitle(_translate("lora_trigger_word", "Form"))
        self.trigger_word.setText(_translate("lora_trigger_word", "Trigger Word"))
        self.button_to_prompt.setText(_translate("lora_trigger_word", "Prompt"))
        self.button_to_negative_prompt.setText(_translate("lora_trigger_word", "Negative Prompt"))
