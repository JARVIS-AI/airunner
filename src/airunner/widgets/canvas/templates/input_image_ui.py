# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_image.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_input_image(object):
    def setupUi(self, input_image):
        if not input_image.objectName():
            input_image.setObjectName(u"input_image")
        input_image.resize(564, 539)
        self.gridLayout = QGridLayout(input_image)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.image_container = QGraphicsView(input_image)
        self.image_container.setObjectName(u"image_container")

        self.gridLayout.addWidget(self.image_container, 2, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.use_grid_image_as_input_checkbox = QCheckBox(input_image)
        self.use_grid_image_as_input_checkbox.setObjectName(u"use_grid_image_as_input_checkbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_grid_image_as_input_checkbox.sizePolicy().hasHeightForWidth())
        self.use_grid_image_as_input_checkbox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.use_grid_image_as_input_checkbox)

        self.enable_checkbox = QCheckBox(input_image)
        self.enable_checkbox.setObjectName(u"enable_checkbox")
        sizePolicy.setHeightForWidth(self.enable_checkbox.sizePolicy().hasHeightForWidth())
        self.enable_checkbox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.enable_checkbox)

        self.import_button = QPushButton(input_image)
        self.import_button.setObjectName(u"import_button")
        icon = QIcon(QIcon.fromTheme(u"folder"))
        self.import_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.import_button)

        self.delete_button = QPushButton(input_image)
        self.delete_button.setObjectName(u"delete_button")
        icon1 = QIcon(QIcon.fromTheme(u"user-trash"))
        self.delete_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_button)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)

        self.line = QFrame(input_image)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.label = QLabel(input_image)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(input_image)
        self.import_button.clicked.connect(input_image.import_clicked)
        self.delete_button.clicked.connect(input_image.delete_clicked)
        self.enable_checkbox.toggled.connect(input_image.enabled_toggled)
        self.use_grid_image_as_input_checkbox.toggled.connect(input_image.use_grid_image_as_input_toggled)

        QMetaObject.connectSlotsByName(input_image)
    # setupUi

    def retranslateUi(self, input_image):
        input_image.setWindowTitle(QCoreApplication.translate("input_image", u"Form", None))
        self.use_grid_image_as_input_checkbox.setText(QCoreApplication.translate("input_image", u"Use grid image as input", None))
        self.enable_checkbox.setText(QCoreApplication.translate("input_image", u"Enable ", None))
        self.import_button.setText(QCoreApplication.translate("input_image", u"Import", None))
        self.delete_button.setText(QCoreApplication.translate("input_image", u"Delete", None))
        self.label.setText(QCoreApplication.translate("input_image", u"TextLabel", None))
    # retranslateUi

