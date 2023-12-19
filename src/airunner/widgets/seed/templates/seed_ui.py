# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/seed/templates/seed.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_seed_widget(object):
    def setupUi(self, seed_widget):
        seed_widget.setObjectName("seed_widget")
        seed_widget.resize(558, 43)
        self.gridLayout = QtWidgets.QGridLayout(seed_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.random_button = QtWidgets.QPushButton(parent=seed_widget)
        self.random_button.setMinimumSize(QtCore.QSize(24, 24))
        self.random_button.setMaximumSize(QtCore.QSize(24, 24))
        self.random_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dark/dice-game-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.random_button.setIcon(icon)
        self.random_button.setCheckable(True)
        self.random_button.setFlat(True)
        self.random_button.setObjectName("random_button")
        self.gridLayout.addWidget(self.random_button, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=seed_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=seed_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(seed_widget)
        self.lineEdit.textChanged['QString'].connect(seed_widget.action_value_changed_seed) # type: ignore
        self.random_button.toggled['bool'].connect(seed_widget.action_clicked_button_random_seed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(seed_widget)

    def retranslateUi(self, seed_widget):
        _translate = QtCore.QCoreApplication.translate
        seed_widget.setWindowTitle(_translate("seed_widget", "Form"))
        self.random_button.setToolTip(_translate("seed_widget", "Toggle random seed"))
        self.lineEdit.setPlaceholderText(_translate("seed_widget", "seed"))
        self.label.setText(_translate("seed_widget", "Seed"))