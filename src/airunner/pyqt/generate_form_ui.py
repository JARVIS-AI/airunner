# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/generate_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 793)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(370, 0))
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setContentsMargins(-1, -1, 14, -1)
        self.formLayout.setObjectName("formLayout")
        self.PromptTabsSection = QtWidgets.QTabWidget(parent=Form)
        self.PromptTabsSection.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PromptTabsSection.sizePolicy().hasHeightForWidth())
        self.PromptTabsSection.setSizePolicy(sizePolicy)
        self.PromptTabsSection.setMinimumSize(QtCore.QSize(0, 180))
        self.PromptTabsSection.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.PromptTabsSection.setAcceptDrops(False)
        self.PromptTabsSection.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.PromptTabsSection.setObjectName("PromptTabsSection")
        self.PromptTab = QtWidgets.QWidget()
        self.PromptTab.setObjectName("PromptTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PromptTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.PromptTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.prompt = QtWidgets.QPlainTextEdit(parent=self.PromptTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prompt.sizePolicy().hasHeightForWidth())
        self.prompt.setSizePolicy(sizePolicy)
        self.prompt.setMinimumSize(QtCore.QSize(0, 40))
        self.prompt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.prompt.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.prompt.setObjectName("prompt")
        self.verticalLayout_2.addWidget(self.prompt)
        self.label_5 = QtWidgets.QLabel(parent=self.PromptTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.negative_prompt = QtWidgets.QPlainTextEdit(parent=self.PromptTab)
        self.negative_prompt.setMinimumSize(QtCore.QSize(0, 40))
        self.negative_prompt.setObjectName("negative_prompt")
        self.verticalLayout_2.addWidget(self.negative_prompt)
        self.PromptTabsSection.addTab(self.PromptTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.embeddings = QtWidgets.QScrollArea(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.embeddings.sizePolicy().hasHeightForWidth())
        self.embeddings.setSizePolicy(sizePolicy)
        self.embeddings.setMinimumSize(QtCore.QSize(0, 50))
        self.embeddings.setWidgetResizable(True)
        self.embeddings.setObjectName("embeddings")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 323, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.embeddings.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.embeddings)
        self.PromptTabsSection.addTab(self.tab, "")
        self.lora_tab = QtWidgets.QWidget()
        self.lora_tab.setObjectName("lora_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.lora_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.lora_scroll_area = QtWidgets.QScrollArea(parent=self.lora_tab)
        self.lora_scroll_area.setWidgetResizable(True)
        self.lora_scroll_area.setObjectName("lora_scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 323, 129))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.lora_scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.lora_scroll_area, 0, 0, 1, 1)
        self.PromptTabsSection.addTab(self.lora_tab, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.PromptTabsSection)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.model_dropdown = QtWidgets.QComboBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_dropdown.sizePolicy().hasHeightForWidth())
        self.model_dropdown.setSizePolicy(sizePolicy)
        self.model_dropdown.setMaximumSize(QtCore.QSize(16777215, 25))
        self.model_dropdown.setObjectName("model_dropdown")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.model_dropdown)
        self.scheduler_label = QtWidgets.QLabel(parent=Form)
        self.scheduler_label.setObjectName("scheduler_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.scheduler_label)
        self.scheduler_dropdown = QtWidgets.QComboBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scheduler_dropdown.sizePolicy().hasHeightForWidth())
        self.scheduler_dropdown.setSizePolicy(sizePolicy)
        self.scheduler_dropdown.setMaximumSize(QtCore.QSize(16777215, 25))
        self.scheduler_dropdown.setObjectName("scheduler_dropdown")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.scheduler_dropdown)
        self.controlnet_label = QtWidgets.QLabel(parent=Form)
        self.controlnet_label.setObjectName("controlnet_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.controlnet_label)
        self.controlnet_dropdown = QtWidgets.QComboBox(parent=Form)
        self.controlnet_dropdown.setObjectName("controlnet_dropdown")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.controlnet_dropdown)
        self.groupBox_21 = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy)
        self.groupBox_21.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_21.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        self.groupBox_21.setFont(font)
        self.groupBox_21.setObjectName("groupBox_21")
        self.layoutWidget = QtWidgets.QWidget(parent=self.groupBox_21)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 30, 333, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_5 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.steps_slider = QtWidgets.QSlider(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steps_slider.sizePolicy().hasHeightForWidth())
        self.steps_slider.setSizePolicy(sizePolicy)
        self.steps_slider.setMinimumSize(QtCore.QSize(250, 0))
        self.steps_slider.setMinimum(1)
        self.steps_slider.setMaximum(100)
        self.steps_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.steps_slider.setObjectName("steps_slider")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.steps_slider)
        self.steps_spinbox = QtWidgets.QSpinBox(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steps_spinbox.sizePolicy().hasHeightForWidth())
        self.steps_spinbox.setSizePolicy(sizePolicy)
        self.steps_spinbox.setMinimumSize(QtCore.QSize(75, 0))
        self.steps_spinbox.setMaximumSize(QtCore.QSize(75, 16777215))
        self.steps_spinbox.setMinimum(1)
        self.steps_spinbox.setMaximum(100)
        self.steps_spinbox.setObjectName("steps_spinbox")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.steps_spinbox)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.groupBox_21)
        self.scale_box = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_box.sizePolicy().hasHeightForWidth())
        self.scale_box.setSizePolicy(sizePolicy)
        self.scale_box.setMinimumSize(QtCore.QSize(0, 60))
        self.scale_box.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        self.scale_box.setFont(font)
        self.scale_box.setObjectName("scale_box")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.scale_box)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 30, 331, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.scale_slider = QtWidgets.QSlider(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_slider.sizePolicy().hasHeightForWidth())
        self.scale_slider.setSizePolicy(sizePolicy)
        self.scale_slider.setMinimumSize(QtCore.QSize(250, 0))
        self.scale_slider.setMaximum(10000)
        self.scale_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.scale_slider.setObjectName("scale_slider")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.scale_slider)
        self.scale_spinbox = QtWidgets.QDoubleSpinBox(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_spinbox.sizePolicy().hasHeightForWidth())
        self.scale_spinbox.setSizePolicy(sizePolicy)
        self.scale_spinbox.setMinimumSize(QtCore.QSize(0, 0))
        self.scale_spinbox.setMaximumSize(QtCore.QSize(75, 16777215))
        self.scale_spinbox.setMaximum(100.0)
        self.scale_spinbox.setSingleStep(0.1)
        self.scale_spinbox.setObjectName("scale_spinbox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.scale_spinbox)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.scale_box)
        self.image_scale_box = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_scale_box.sizePolicy().hasHeightForWidth())
        self.image_scale_box.setSizePolicy(sizePolicy)
        self.image_scale_box.setMinimumSize(QtCore.QSize(0, 60))
        self.image_scale_box.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        self.image_scale_box.setFont(font)
        self.image_scale_box.setObjectName("image_scale_box")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.image_scale_box)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 30, 333, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.image_scale_slider = QtWidgets.QSlider(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_scale_slider.sizePolicy().hasHeightForWidth())
        self.image_scale_slider.setSizePolicy(sizePolicy)
        self.image_scale_slider.setMinimumSize(QtCore.QSize(250, 0))
        self.image_scale_slider.setMaximum(10000)
        self.image_scale_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.image_scale_slider.setObjectName("image_scale_slider")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.image_scale_slider)
        self.image_scale_spinbox = QtWidgets.QDoubleSpinBox(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_scale_spinbox.sizePolicy().hasHeightForWidth())
        self.image_scale_spinbox.setSizePolicy(sizePolicy)
        self.image_scale_spinbox.setMinimumSize(QtCore.QSize(75, 0))
        self.image_scale_spinbox.setMaximum(100.0)
        self.image_scale_spinbox.setSingleStep(0.1)
        self.image_scale_spinbox.setObjectName("image_scale_spinbox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.image_scale_spinbox)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.image_scale_box)
        self.strength = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strength.sizePolicy().hasHeightForWidth())
        self.strength.setSizePolicy(sizePolicy)
        self.strength.setMinimumSize(QtCore.QSize(0, 60))
        self.strength.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        self.strength.setFont(font)
        self.strength.setObjectName("strength")
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.strength)
        self.layoutWidget3.setGeometry(QtCore.QRect(9, 30, 333, 28))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.strength_slider = QtWidgets.QSlider(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strength_slider.sizePolicy().hasHeightForWidth())
        self.strength_slider.setSizePolicy(sizePolicy)
        self.strength_slider.setMinimumSize(QtCore.QSize(250, 0))
        self.strength_slider.setMaximum(100)
        self.strength_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.strength_slider.setObjectName("strength_slider")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.strength_slider)
        self.strength_spinbox = QtWidgets.QDoubleSpinBox(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strength_spinbox.sizePolicy().hasHeightForWidth())
        self.strength_spinbox.setSizePolicy(sizePolicy)
        self.strength_spinbox.setMinimumSize(QtCore.QSize(75, 0))
        self.strength_spinbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.strength_spinbox.setMaximum(100.0)
        self.strength_spinbox.setSingleStep(0.1)
        self.strength_spinbox.setObjectName("strength_spinbox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.strength_spinbox)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.strength)
        self.groupBox_24 = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy)
        self.groupBox_24.setMinimumSize(QtCore.QSize(0, 66))
        self.groupBox_24.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        self.groupBox_24.setFont(font)
        self.groupBox_24.setObjectName("groupBox_24")
        self.random_checkbox = QtWidgets.QCheckBox(parent=self.groupBox_24)
        self.random_checkbox.setGeometry(QtCore.QRect(260, 30, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.random_checkbox.sizePolicy().hasHeightForWidth())
        self.random_checkbox.setSizePolicy(sizePolicy)
        self.random_checkbox.setObjectName("random_checkbox")
        self.seed = QtWidgets.QTextEdit(parent=self.groupBox_24)
        self.seed.setGeometry(QtCore.QRect(10, 30, 241, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seed.sizePolicy().hasHeightForWidth())
        self.seed.setSizePolicy(sizePolicy)
        self.seed.setMinimumSize(QtCore.QSize(0, 24))
        self.seed.setObjectName("seed")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.groupBox_24)
        self.samples_groupbox = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samples_groupbox.sizePolicy().hasHeightForWidth())
        self.samples_groupbox.setSizePolicy(sizePolicy)
        self.samples_groupbox.setMinimumSize(QtCore.QSize(0, 60))
        self.samples_groupbox.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        self.samples_groupbox.setFont(font)
        self.samples_groupbox.setObjectName("samples_groupbox")
        self.samples_slider = QtWidgets.QSlider(parent=self.samples_groupbox)
        self.samples_slider.setGeometry(QtCore.QRect(9, 30, 131, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samples_slider.sizePolicy().hasHeightForWidth())
        self.samples_slider.setSizePolicy(sizePolicy)
        self.samples_slider.setMinimum(1)
        self.samples_slider.setMaximum(200)
        self.samples_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.samples_slider.setObjectName("samples_slider")
        self.samples_spinbox = QtWidgets.QSpinBox(parent=self.samples_groupbox)
        self.samples_spinbox.setGeometry(QtCore.QRect(150, 30, 71, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samples_spinbox.sizePolicy().hasHeightForWidth())
        self.samples_spinbox.setSizePolicy(sizePolicy)
        self.samples_spinbox.setMinimum(1)
        self.samples_spinbox.setMaximum(200)
        self.samples_spinbox.setObjectName("samples_spinbox")
        self.interrupt_button = QtWidgets.QPushButton(parent=self.samples_groupbox)
        self.interrupt_button.setEnabled(False)
        self.interrupt_button.setGeometry(QtCore.QRect(230, 30, 111, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interrupt_button.sizePolicy().hasHeightForWidth())
        self.interrupt_button.setSizePolicy(sizePolicy)
        self.interrupt_button.setObjectName("interrupt_button")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.samples_groupbox)
        self.generate = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate.sizePolicy().hasHeightForWidth())
        self.generate.setSizePolicy(sizePolicy)
        self.generate.setObjectName("generate")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.ItemRole.LabelRole, self.generate)
        self.progressBar = QtWidgets.QProgressBar(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.progressBar)

        self.retranslateUi(Form)
        self.PromptTabsSection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Prompt"))
        self.label_5.setText(_translate("Form", "Negative prompt"))
        self.PromptTabsSection.setTabText(self.PromptTabsSection.indexOf(self.PromptTab), _translate("Form", "Prompt"))
        self.label_3.setText(_translate("Form", "Available embeddings"))
        self.PromptTabsSection.setTabText(self.PromptTabsSection.indexOf(self.tab), _translate("Form", "Embeddings"))
        self.PromptTabsSection.setTabText(self.PromptTabsSection.indexOf(self.lora_tab), _translate("Form", "LoRA"))
        self.label.setText(_translate("Form", "Model"))
        self.scheduler_label.setText(_translate("Form", "Scheduler"))
        self.controlnet_label.setText(_translate("Form", "Controlnet"))
        self.groupBox_21.setTitle(_translate("Form", "Steps"))
        self.scale_box.setTitle(_translate("Form", "Scale"))
        self.image_scale_box.setTitle(_translate("Form", "Image Scale"))
        self.strength.setTitle(_translate("Form", "Strength"))
        self.groupBox_24.setTitle(_translate("Form", "Seed"))
        self.random_checkbox.setText(_translate("Form", "Random"))
        self.samples_groupbox.setTitle(_translate("Form", "Samples"))
        self.interrupt_button.setText(_translate("Form", "Interrupt"))
        self.generate.setText(_translate("Form", "Generate"))