# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/layers/templates/layer_container.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_layer_container(object):
    def setupUi(self, layer_container):
        layer_container.setObjectName("layer_container")
        layer_container.resize(435, 323)
        self.gridLayout = QtWidgets.QGridLayout(layer_container)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(parent=layer_container)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.layer_widget_button_container = QtWidgets.QWidget(parent=layer_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_widget_button_container.sizePolicy().hasHeightForWidth())
        self.layer_widget_button_container.setSizePolicy(sizePolicy)
        self.layer_widget_button_container.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.layer_widget_button_container.setObjectName("layer_widget_button_container")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layer_widget_button_container)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.new_layer_button = QtWidgets.QPushButton(parent=self.layer_widget_button_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_layer_button.sizePolicy().hasHeightForWidth())
        self.new_layer_button.setSizePolicy(sizePolicy)
        self.new_layer_button.setMinimumSize(QtCore.QSize(40, 40))
        self.new_layer_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.new_layer_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.new_layer_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dark/add-plus-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.new_layer_button.setIcon(icon)
        self.new_layer_button.setIconSize(QtCore.QSize(20, 20))
        self.new_layer_button.setFlat(True)
        self.new_layer_button.setObjectName("new_layer_button")
        self.horizontalLayout_8.addWidget(self.new_layer_button)
        self.layer_up_button = QtWidgets.QPushButton(parent=self.layer_widget_button_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_up_button.sizePolicy().hasHeightForWidth())
        self.layer_up_button.setSizePolicy(sizePolicy)
        self.layer_up_button.setMinimumSize(QtCore.QSize(40, 40))
        self.layer_up_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.layer_up_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.layer_up_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/dark/round-black-top-arrow-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.layer_up_button.setIcon(icon1)
        self.layer_up_button.setIconSize(QtCore.QSize(20, 20))
        self.layer_up_button.setFlat(True)
        self.layer_up_button.setObjectName("layer_up_button")
        self.horizontalLayout_8.addWidget(self.layer_up_button)
        self.layer_down_button = QtWidgets.QPushButton(parent=self.layer_widget_button_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_down_button.sizePolicy().hasHeightForWidth())
        self.layer_down_button.setSizePolicy(sizePolicy)
        self.layer_down_button.setMinimumSize(QtCore.QSize(40, 40))
        self.layer_down_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.layer_down_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.layer_down_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/dark/round-black-bottom-arrow-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.layer_down_button.setIcon(icon2)
        self.layer_down_button.setIconSize(QtCore.QSize(20, 20))
        self.layer_down_button.setFlat(True)
        self.layer_down_button.setObjectName("layer_down_button")
        self.horizontalLayout_8.addWidget(self.layer_down_button)
        self.merge_layer_button = QtWidgets.QPushButton(parent=self.layer_widget_button_container)
        self.merge_layer_button.setMinimumSize(QtCore.QSize(40, 40))
        self.merge_layer_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.merge_layer_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/dark/compress-vertical-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.merge_layer_button.setIcon(icon3)
        self.merge_layer_button.setIconSize(QtCore.QSize(20, 20))
        self.merge_layer_button.setFlat(True)
        self.merge_layer_button.setObjectName("merge_layer_button")
        self.horizontalLayout_8.addWidget(self.merge_layer_button)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.delete_layer_button = QtWidgets.QPushButton(parent=self.layer_widget_button_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_layer_button.sizePolicy().hasHeightForWidth())
        self.delete_layer_button.setSizePolicy(sizePolicy)
        self.delete_layer_button.setMinimumSize(QtCore.QSize(40, 40))
        self.delete_layer_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_layer_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.delete_layer_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/dark/red-x-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_layer_button.setIcon(icon4)
        self.delete_layer_button.setIconSize(QtCore.QSize(20, 20))
        self.delete_layer_button.setFlat(True)
        self.delete_layer_button.setObjectName("delete_layer_button")
        self.horizontalLayout_8.addWidget(self.delete_layer_button)
        self.gridLayout.addWidget(self.layer_widget_button_container, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=layer_container)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.layers = QtWidgets.QScrollArea(parent=layer_container)
        self.layers.setAcceptDrops(True)
        self.layers.setStyleSheet("border-radius: 0px")
        self.layers.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.layers.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.layers.setWidgetResizable(True)
        self.layers.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.layers.setObjectName("layers")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 435, 243))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layers.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.layers, 2, 0, 1, 1)
        self.opacity_slider_widget = SliderWidget(parent=layer_container)
        self.opacity_slider_widget.setProperty("slider_maximum", 100)
        self.opacity_slider_widget.setProperty("spinbox_maximum", 1.0)
        self.opacity_slider_widget.setProperty("current_value", 100)
        self.opacity_slider_widget.setProperty("display_as_float", True)
        self.opacity_slider_widget.setProperty("spinbox_single_step", 0.01)
        self.opacity_slider_widget.setProperty("spinbox_page_step", 1.0)
        self.opacity_slider_widget.setProperty("spinbox_minimum", 0.0)
        self.opacity_slider_widget.setProperty("slider_minimum", 0)
        self.opacity_slider_widget.setObjectName("opacity_slider_widget")
        self.gridLayout.addWidget(self.opacity_slider_widget, 0, 0, 1, 1)

        self.retranslateUi(layer_container)
        self.new_layer_button.clicked.connect(layer_container.action_clicked_button_add_new_layer) # type: ignore
        self.layer_up_button.clicked.connect(layer_container.action_clicked_button_move_layer_up) # type: ignore
        self.layer_down_button.clicked.connect(layer_container.action_clicked_button_move_layer_down) # type: ignore
        self.merge_layer_button.clicked.connect(layer_container.action_clicked_button_merge_selected_layers) # type: ignore
        self.delete_layer_button.clicked.connect(layer_container.action_clicked_button_delete_selected_layers) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(layer_container)

    def retranslateUi(self, layer_container):
        _translate = QtCore.QCoreApplication.translate
        layer_container.setWindowTitle(_translate("layer_container", "Form"))
        self.new_layer_button.setToolTip(_translate("layer_container", "Create a new layer"))
        self.layer_up_button.setToolTip(_translate("layer_container", "Move layer up"))
        self.layer_down_button.setToolTip(_translate("layer_container", "Move layer down"))
        self.merge_layer_button.setToolTip(_translate("layer_container", "Merge selected layers"))
        self.delete_layer_button.setToolTip(_translate("layer_container", "Delete layer"))
        self.opacity_slider_widget.setProperty("label_text", _translate("layer_container", "Layer Opacity"))
        self.opacity_slider_widget.setProperty("slider_callback", _translate("layer_container", "layer_opacity_changed"))
from airunner.widgets.slider.slider_widget import SliderWidget
