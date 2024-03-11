# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/canvas/templates/canvas.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_canvas(object):
    def setupUi(self, canvas):
        canvas.setObjectName("canvas")
        canvas.resize(709, 787)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(canvas.sizePolicy().hasHeightForWidth())
        canvas.setSizePolicy(sizePolicy)
        canvas.setMinimumSize(QtCore.QSize(66, 66))
        canvas.setStyleSheet("b")
        self.gridLayout = QtWidgets.QGridLayout(canvas)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.central_widget = QtWidgets.QWidget(parent=canvas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setMinimumSize(QtCore.QSize(200, 200))
        self.central_widget.setStyleSheet("")
        self.central_widget.setObjectName("central_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.canvas_splitter = QtWidgets.QSplitter(parent=self.central_widget)
        self.canvas_splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.canvas_splitter.setObjectName("canvas_splitter")
        self.canvas_side_splitter = QtWidgets.QSplitter(parent=self.canvas_splitter)
        self.canvas_side_splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.canvas_side_splitter.setObjectName("canvas_side_splitter")
        self.drawing_pad_groupbox = QtWidgets.QGroupBox(parent=self.canvas_side_splitter)
        self.drawing_pad_groupbox.setCheckable(True)
        self.drawing_pad_groupbox.setObjectName("drawing_pad_groupbox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.drawing_pad_groupbox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.drawing_pad = CustomGraphicsView(parent=self.drawing_pad_groupbox)
        self.drawing_pad.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.drawing_pad.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.drawing_pad.setObjectName("drawing_pad")
        self.gridLayout_3.addWidget(self.drawing_pad, 0, 0, 1, 1)
        self.controlnet_groupbox = QtWidgets.QGroupBox(parent=self.canvas_side_splitter)
        self.controlnet_groupbox.setCheckable(True)
        self.controlnet_groupbox.setObjectName("controlnet_groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controlnet_groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.controlnet = CustomGraphicsView(parent=self.controlnet_groupbox)
        self.controlnet.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.controlnet.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.controlnet.setObjectName("controlnet")
        self.gridLayout_2.addWidget(self.controlnet, 0, 0, 1, 1)
        self.canvas_container = CustomGraphicsView(parent=self.canvas_splitter)
        self.canvas_container.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.canvas_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.canvas_container.setObjectName("canvas_container")
        self.gridLayout_4.addWidget(self.canvas_splitter, 0, 0, 1, 1)
        self.canvas_position = QtWidgets.QLabel(parent=self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_position.sizePolicy().hasHeightForWidth())
        self.canvas_position.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.canvas_position.setFont(font)
        self.canvas_position.setStyleSheet("")
        self.canvas_position.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.canvas_position.setObjectName("canvas_position")
        self.gridLayout_4.addWidget(self.canvas_position, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.central_widget, 0, 0, 1, 1)

        self.retranslateUi(canvas)
        self.controlnet_groupbox.toggled['bool'].connect(canvas.toggle_controlnet) # type: ignore
        self.drawing_pad_groupbox.clicked['bool'].connect(canvas.toggle_drawing_pad) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(canvas)

    def retranslateUi(self, canvas):
        _translate = QtCore.QCoreApplication.translate
        canvas.setWindowTitle(_translate("canvas", "Form"))
        self.drawing_pad_groupbox.setTitle(_translate("canvas", "Drawing pad"))
        self.drawing_pad.setProperty("canvas_type", _translate("canvas", "brush"))
        self.controlnet_groupbox.setTitle(_translate("canvas", "Controlnet"))
        self.controlnet.setProperty("canvas_type", _translate("canvas", "controlnet"))
        self.canvas_container.setProperty("canvas_type", _translate("canvas", "image"))
        self.canvas_position.setText(_translate("canvas", "TextLabel"))
from airunner.widgets.canvas.custom_view import CustomGraphicsView
