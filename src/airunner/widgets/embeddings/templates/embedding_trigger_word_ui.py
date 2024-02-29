# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/embeddings/templates/embedding_trigger_word.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_embedding_trigger_word(object):
    def setupUi(self, embedding_trigger_word):
        embedding_trigger_word.setObjectName("embedding_trigger_word")
        embedding_trigger_word.resize(345, 43)
        self.horizontalLayout = QtWidgets.QHBoxLayout(embedding_trigger_word)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.trigger_word = QtWidgets.QLabel(parent=embedding_trigger_word)
        self.trigger_word.setObjectName("trigger_word")
        self.horizontalLayout.addWidget(self.trigger_word)
        self.button_to_prompt = QtWidgets.QPushButton(parent=embedding_trigger_word)
        self.button_to_prompt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.button_to_prompt.setIcon(icon)
        self.button_to_prompt.setObjectName("button_to_prompt")
        self.horizontalLayout.addWidget(self.button_to_prompt)
        self.button_to_negative_prompt = QtWidgets.QPushButton(parent=embedding_trigger_word)
        self.button_to_negative_prompt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.button_to_negative_prompt.setIcon(icon)
        self.button_to_negative_prompt.setObjectName("button_to_negative_prompt")
        self.horizontalLayout.addWidget(self.button_to_negative_prompt)
        self.button_copy = QtWidgets.QPushButton(parent=embedding_trigger_word)
        self.button_copy.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.button_copy.setText("")
        icon = QtGui.QIcon.fromTheme("edit-copy")
        self.button_copy.setIcon(icon)
        self.button_copy.setObjectName("button_copy")
        self.horizontalLayout.addWidget(self.button_copy)

        self.retranslateUi(embedding_trigger_word)
        self.button_to_prompt.clicked['bool'].connect(embedding_trigger_word.action_click_button_to_prompt) # type: ignore
        self.button_to_negative_prompt.clicked.connect(embedding_trigger_word.action_click_button_to_negative_prompt) # type: ignore
        self.button_copy.clicked.connect(embedding_trigger_word.action_click_button_copy) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(embedding_trigger_word)

    def retranslateUi(self, embedding_trigger_word):
        _translate = QtCore.QCoreApplication.translate
        embedding_trigger_word.setWindowTitle(_translate("embedding_trigger_word", "Form"))
        self.trigger_word.setText(_translate("embedding_trigger_word", "Trigger Word"))
        self.button_to_prompt.setToolTip(_translate("embedding_trigger_word", "Send trigger word to prompt"))
        self.button_to_prompt.setText(_translate("embedding_trigger_word", "Prompt"))
        self.button_to_negative_prompt.setToolTip(_translate("embedding_trigger_word", "Send trigger word to negative prompt"))
        self.button_to_negative_prompt.setText(_translate("embedding_trigger_word", "Negative"))
        self.button_copy.setToolTip(_translate("embedding_trigger_word", "Copy trigger word to clipboard"))
