# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/llm/templates/llm_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_llm_widget(object):
    def setupUi(self, llm_widget):
        llm_widget.setObjectName("llm_widget")
        llm_widget.resize(511, 872)
        self.gridLayout = QtWidgets.QGridLayout(llm_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=llm_widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.send_button = QtWidgets.QPushButton(parent=self.tab)
        self.send_button.setObjectName("send_button")
        self.horizontalLayout_2.addWidget(self.send_button)
        self.generate_characters_button = QtWidgets.QPushButton(parent=self.tab)
        self.generate_characters_button.setObjectName("generate_characters_button")
        self.horizontalLayout_2.addWidget(self.generate_characters_button)
        self.clear_conversatiion_button = QtWidgets.QPushButton(parent=self.tab)
        self.clear_conversatiion_button.setObjectName("clear_conversatiion_button")
        self.horizontalLayout_2.addWidget(self.clear_conversatiion_button)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prompt = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.prompt.setObjectName("prompt")
        self.horizontalLayout.addWidget(self.prompt)
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout_8.addWidget(self.groupBox_5, 3, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_8.addWidget(self.progressBar, 5, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.username = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.username.setObjectName("username")
        self.gridLayout_7.addWidget(self.username, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.botname = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.botname.setCursorPosition(6)
        self.botname.setObjectName("botname")
        self.gridLayout_6.addWidget(self.botname, 0, 0, 1, 1)
        self.personality_type = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.personality_type.setObjectName("personality_type")
        self.personality_type.addItem("")
        self.personality_type.addItem("")
        self.personality_type.addItem("")
        self.personality_type.addItem("")
        self.personality_type.addItem("")
        self.gridLayout_6.addWidget(self.personality_type, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.conversation = QtWidgets.QScrollArea(parent=self.tab)
        self.conversation.setStyleSheet("")
        self.conversation.setWidgetResizable(True)
        self.conversation.setObjectName("conversation")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 487, 532))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.conversation.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_8.addWidget(self.conversation, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("user-available")
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(parent=self.tab_2)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(parent=self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.prefix = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.prefix.setObjectName("prefix")
        self.gridLayout_3.addWidget(self.prefix, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.suffix = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.suffix.setObjectName("suffix")
        self.gridLayout_4.addWidget(self.suffix, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("preferences-desktop")
        self.tabWidget.addTab(self.tab_2, icon, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.do_sample = QtWidgets.QCheckBox(parent=self.tab_3)
        self.do_sample.setObjectName("do_sample")
        self.gridLayout_5.addWidget(self.do_sample, 13, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.model = QtWidgets.QComboBox(parent=self.groupBox_7)
        self.model.setObjectName("model")
        self.gridLayout_10.addWidget(self.model, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radio_button_4bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_4bit.setObjectName("radio_button_4bit")
        self.horizontalLayout_3.addWidget(self.radio_button_4bit)
        self.radio_button_8bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_8bit.setObjectName("radio_button_8bit")
        self.horizontalLayout_3.addWidget(self.radio_button_8bit)
        self.radio_button_16bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_16bit.setObjectName("radio_button_16bit")
        self.horizontalLayout_3.addWidget(self.radio_button_16bit)
        self.radio_button_32bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_32bit.setObjectName("radio_button_32bit")
        self.horizontalLayout_3.addWidget(self.radio_button_32bit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.dtype_description = QtWidgets.QLabel(parent=self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dtype_description.setFont(font)
        self.dtype_description.setObjectName("dtype_description")
        self.gridLayout_9.addWidget(self.dtype_description, 2, 0, 1, 1)
        self.use_gpu_checkbox = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.use_gpu_checkbox.setObjectName("use_gpu_checkbox")
        self.gridLayout_9.addWidget(self.use_gpu_checkbox, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_6, 3, 0, 1, 1)
        self.groupBox_19 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.seed_2 = QtWidgets.QLineEdit(parent=self.groupBox_19)
        self.seed_2.setObjectName("seed_2")
        self.gridLayout_23.addWidget(self.seed_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_19, 11, 0, 1, 1)
        self.override_parameters = QtWidgets.QGroupBox(parent=self.tab_3)
        self.override_parameters.setCheckable(True)
        self.override_parameters.setChecked(True)
        self.override_parameters.setObjectName("override_parameters")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.override_parameters)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_24 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_24.setObjectName("groupBox_24")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.groupBox_24)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.length_penalty_2 = SliderWidget(parent=self.groupBox_24)
        self.length_penalty_2.setProperty("slider_minimum", 0)
        self.length_penalty_2.setProperty("slider_maximum", 200)
        self.length_penalty_2.setProperty("spinbox_minimum", 0.0)
        self.length_penalty_2.setProperty("spinbox_maximum", 2.0)
        self.length_penalty_2.setProperty("display_as_float", True)
        self.length_penalty_2.setProperty("slider_single_step", 1)
        self.length_penalty_2.setProperty("slider_page_step", 10)
        self.length_penalty_2.setProperty("spinbox_single_step", 0.01)
        self.length_penalty_2.setProperty("spinbox_page_step", 0.1)
        self.length_penalty_2.setObjectName("length_penalty_2")
        self.gridLayout_28.addWidget(self.length_penalty_2, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.groupBox_24)
        self.groupBox_25 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_25.setObjectName("groupBox_25")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.groupBox_25)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.num_beams_2 = SliderWidget(parent=self.groupBox_25)
        self.num_beams_2.setProperty("slider_minimum", 1)
        self.num_beams_2.setProperty("slider_maximum", 100)
        self.num_beams_2.setProperty("spinbox_minimum", 0.0)
        self.num_beams_2.setProperty("spinbox_maximum", 100.0)
        self.num_beams_2.setProperty("display_as_float", False)
        self.num_beams_2.setProperty("slider_single_step", 1)
        self.num_beams_2.setProperty("slider_page_step", 10)
        self.num_beams_2.setProperty("spinbox_single_step", 0.01)
        self.num_beams_2.setProperty("spinbox_page_step", 0.1)
        self.num_beams_2.setObjectName("num_beams_2")
        self.gridLayout_29.addWidget(self.num_beams_2, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.groupBox_25)
        self.gridLayout_12.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_20 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.top_p_2 = SliderWidget(parent=self.groupBox_20)
        self.top_p_2.setProperty("slider_minimum", 1)
        self.top_p_2.setProperty("slider_maximum", 100)
        self.top_p_2.setProperty("spinbox_minimum", 0.0)
        self.top_p_2.setProperty("spinbox_maximum", 1.0)
        self.top_p_2.setProperty("display_as_float", True)
        self.top_p_2.setProperty("slider_single_step", 1)
        self.top_p_2.setProperty("slider_page_step", 10)
        self.top_p_2.setProperty("spinbox_single_step", 0.01)
        self.top_p_2.setProperty("spinbox_page_step", 0.1)
        self.top_p_2.setObjectName("top_p_2")
        self.gridLayout_24.addWidget(self.top_p_2, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.groupBox_20)
        self.groupBox_21 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.max_length_2 = SliderWidget(parent=self.groupBox_21)
        self.max_length_2.setProperty("slider_minimum", 1)
        self.max_length_2.setProperty("slider_maximum", 2556)
        self.max_length_2.setProperty("spinbox_minimum", 1.0)
        self.max_length_2.setProperty("spinbox_maximum", 2556.0)
        self.max_length_2.setProperty("display_as_float", False)
        self.max_length_2.setProperty("slider_single_step", 1)
        self.max_length_2.setProperty("slider_page_step", 2556)
        self.max_length_2.setProperty("spinbox_single_step", 1)
        self.max_length_2.setProperty("spinbox_page_step", 2556)
        self.max_length_2.setObjectName("max_length_2")
        self.gridLayout_25.addWidget(self.max_length_2, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.groupBox_21)
        self.gridLayout_12.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_17 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.ngram_size_2 = SliderWidget(parent=self.groupBox_17)
        self.ngram_size_2.setProperty("slider_minimum", 1)
        self.ngram_size_2.setProperty("slider_maximum", 100)
        self.ngram_size_2.setProperty("spinbox_minimum", 0.0)
        self.ngram_size_2.setProperty("spinbox_maximum", 1.0)
        self.ngram_size_2.setProperty("display_as_float", True)
        self.ngram_size_2.setProperty("slider_single_step", 1)
        self.ngram_size_2.setProperty("slider_page_step", 10)
        self.ngram_size_2.setProperty("spinbox_single_step", 0.01)
        self.ngram_size_2.setProperty("spinbox_page_step", 0.1)
        self.ngram_size_2.setObjectName("ngram_size_2")
        self.gridLayout_21.addWidget(self.ngram_size_2, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_17)
        self.groupBox_18 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.temperature_2 = SliderWidget(parent=self.groupBox_18)
        self.temperature_2.setProperty("slider_minimum", 1)
        self.temperature_2.setProperty("slider_maximum", 200)
        self.temperature_2.setProperty("spinbox_minimum", 0.0)
        self.temperature_2.setProperty("spinbox_maximum", 2.0)
        self.temperature_2.setProperty("display_as_float", True)
        self.temperature_2.setProperty("slider_single_step", 1)
        self.temperature_2.setProperty("slider_page_step", 10)
        self.temperature_2.setProperty("spinbox_single_step", 0.01)
        self.temperature_2.setProperty("spinbox_page_step", 0.1)
        self.temperature_2.setObjectName("temperature_2")
        self.gridLayout_22.addWidget(self.temperature_2, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_18)
        self.gridLayout_12.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_11 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.repetition_penalty_2 = SliderWidget(parent=self.groupBox_11)
        self.repetition_penalty_2.setProperty("slider_minimum", 0)
        self.repetition_penalty_2.setProperty("slider_maximum", 10000)
        self.repetition_penalty_2.setProperty("spinbox_minimum", 0.0)
        self.repetition_penalty_2.setProperty("spinbox_maximum", 100.0)
        self.repetition_penalty_2.setProperty("display_as_float", True)
        self.repetition_penalty_2.setProperty("slider_single_step", 0)
        self.repetition_penalty_2.setProperty("slider_page_step", 1)
        self.repetition_penalty_2.setProperty("spinbox_single_step", 1.0)
        self.repetition_penalty_2.setProperty("spinbox_page_step", 10.0)
        self.repetition_penalty_2.setObjectName("repetition_penalty_2")
        self.gridLayout_19.addWidget(self.repetition_penalty_2, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_11)
        self.groupBox_16 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.min_length_2 = SliderWidget(parent=self.groupBox_16)
        self.min_length_2.setProperty("slider_minimum", 1)
        self.min_length_2.setProperty("slider_maximum", 2556)
        self.min_length_2.setProperty("spinbox_minimum", 1.0)
        self.min_length_2.setProperty("spinbox_maximum", 2556.0)
        self.min_length_2.setProperty("display_as_float", False)
        self.min_length_2.setProperty("slider_single_step", 1)
        self.min_length_2.setProperty("slider_page_step", 2556)
        self.min_length_2.setProperty("spinbox_single_step", 1)
        self.min_length_2.setProperty("spinbox_page_step", 2556)
        self.min_length_2.setObjectName("min_length_2")
        self.gridLayout_20.addWidget(self.min_length_2, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_16)
        self.gridLayout_12.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBox_22 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.sequences_2 = SliderWidget(parent=self.groupBox_22)
        self.sequences_2.setProperty("slider_minimum", 1)
        self.sequences_2.setProperty("slider_maximum", 100)
        self.sequences_2.setProperty("spinbox_minimum", 0.0)
        self.sequences_2.setProperty("spinbox_maximum", 100.0)
        self.sequences_2.setProperty("display_as_float", False)
        self.sequences_2.setProperty("slider_single_step", 1)
        self.sequences_2.setProperty("slider_page_step", 10)
        self.sequences_2.setProperty("spinbox_single_step", 0.01)
        self.sequences_2.setProperty("spinbox_page_step", 0.1)
        self.sequences_2.setObjectName("sequences_2")
        self.gridLayout_26.addWidget(self.sequences_2, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.groupBox_22)
        self.groupBox_23 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_23.setObjectName("groupBox_23")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.groupBox_23)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.top_k_2 = SliderWidget(parent=self.groupBox_23)
        self.top_k_2.setProperty("slider_minimum", 1)
        self.top_k_2.setProperty("slider_maximum", 256)
        self.top_k_2.setProperty("spinbox_minimum", 0.0)
        self.top_k_2.setProperty("spinbox_maximum", 256.0)
        self.top_k_2.setProperty("display_as_float", False)
        self.top_k_2.setProperty("slider_single_step", 1)
        self.top_k_2.setProperty("slider_page_step", 10)
        self.top_k_2.setProperty("spinbox_single_step", 1)
        self.top_k_2.setProperty("spinbox_page_step", 10)
        self.top_k_2.setObjectName("top_k_2")
        self.gridLayout_27.addWidget(self.top_k_2, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.groupBox_23)
        self.gridLayout_12.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.gridLayout_5.addWidget(self.override_parameters, 4, 0, 1, 1)
        self.early_stopping = QtWidgets.QCheckBox(parent=self.tab_3)
        self.early_stopping.setObjectName("early_stopping")
        self.gridLayout_5.addWidget(self.early_stopping, 14, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.model_version = QtWidgets.QComboBox(parent=self.groupBox_8)
        self.model_version.setObjectName("model_version")
        self.gridLayout_11.addWidget(self.model_version, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_8, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 16, 0, 1, 1)
        self.random_seed = QtWidgets.QCheckBox(parent=self.tab_3)
        self.random_seed.setObjectName("random_seed")
        self.gridLayout_5.addWidget(self.random_seed, 12, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 15, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("preferences-other")
        self.tabWidget.addTab(self.tab_3, icon, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(llm_widget)
        self.tabWidget.setCurrentIndex(0)
        self.model_version.setCurrentIndex(-1)
        self.prefix.textChanged.connect(llm_widget.prefix_text_changed) # type: ignore
        self.suffix.textChanged.connect(llm_widget.suffix_text_changed) # type: ignore
        self.send_button.clicked.connect(llm_widget.action_button_clicked_send) # type: ignore
        self.generate_characters_button.clicked.connect(llm_widget.action_button_clicked_generate_characters) # type: ignore
        self.clear_conversatiion_button.clicked.connect(llm_widget.action_button_clicked_clear_conversation) # type: ignore
        self.comboBox.currentTextChanged['QString'].connect(llm_widget.message_type_text_changed) # type: ignore
        self.botname.textEdited['QString'].connect(llm_widget.botname_text_changed) # type: ignore
        self.username.textEdited['QString'].connect(llm_widget.username_text_changed) # type: ignore
        self.prompt.textEdited['QString'].connect(llm_widget.prompt_text_changed) # type: ignore
        self.personality_type.currentTextChanged['QString'].connect(llm_widget.personality_type_changed) # type: ignore
        self.radio_button_4bit.toggled['bool'].connect(llm_widget.toggled_4bit) # type: ignore
        self.radio_button_8bit.toggled['bool'].connect(llm_widget.toggled_8bit) # type: ignore
        self.radio_button_16bit.toggled['bool'].connect(llm_widget.toggled_16bit) # type: ignore
        self.radio_button_32bit.toggled['bool'].connect(llm_widget.toggled_32bit) # type: ignore
        self.model_version.currentTextChanged['QString'].connect(llm_widget.model_version_changed) # type: ignore
        self.seed_2.textEdited['QString'].connect(llm_widget.seed_changed) # type: ignore
        self.random_seed.toggled['bool'].connect(llm_widget.random_seed_toggled) # type: ignore
        self.do_sample.toggled['bool'].connect(llm_widget.do_sample_toggled) # type: ignore
        self.early_stopping.toggled['bool'].connect(llm_widget.early_stopping_toggled) # type: ignore
        self.model.currentTextChanged['QString'].connect(llm_widget.model_text_changed) # type: ignore
        self.pushButton.clicked.connect(llm_widget.reset_settings_to_default_clicked) # type: ignore
        self.use_gpu_checkbox.toggled['bool'].connect(llm_widget.use_gpu_toggled) # type: ignore
        self.override_parameters.toggled['bool'].connect(llm_widget.override_parameters_toggled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(llm_widget)
        llm_widget.setTabOrder(self.botname, self.personality_type)
        llm_widget.setTabOrder(self.personality_type, self.username)
        llm_widget.setTabOrder(self.username, self.prompt)
        llm_widget.setTabOrder(self.prompt, self.comboBox)
        llm_widget.setTabOrder(self.comboBox, self.send_button)
        llm_widget.setTabOrder(self.send_button, self.generate_characters_button)
        llm_widget.setTabOrder(self.generate_characters_button, self.clear_conversatiion_button)
        llm_widget.setTabOrder(self.clear_conversatiion_button, self.conversation)
        llm_widget.setTabOrder(self.conversation, self.prefix)
        llm_widget.setTabOrder(self.prefix, self.suffix)
        llm_widget.setTabOrder(self.suffix, self.radio_button_4bit)
        llm_widget.setTabOrder(self.radio_button_4bit, self.radio_button_8bit)
        llm_widget.setTabOrder(self.radio_button_8bit, self.radio_button_16bit)
        llm_widget.setTabOrder(self.radio_button_16bit, self.radio_button_32bit)
        llm_widget.setTabOrder(self.radio_button_32bit, self.seed_2)
        llm_widget.setTabOrder(self.seed_2, self.random_seed)
        llm_widget.setTabOrder(self.random_seed, self.tabWidget)

    def retranslateUi(self, llm_widget):
        _translate = QtCore.QCoreApplication.translate
        llm_widget.setWindowTitle(_translate("llm_widget", "Form"))
        self.send_button.setText(_translate("llm_widget", "Send"))
        self.generate_characters_button.setText(_translate("llm_widget", "Generate Characters"))
        self.clear_conversatiion_button.setText(_translate("llm_widget", "Clear Conversation"))
        self.groupBox_5.setTitle(_translate("llm_widget", "Message"))
        self.comboBox.setItemText(0, _translate("llm_widget", "Chat"))
        self.comboBox.setItemText(1, _translate("llm_widget", "Action"))
        self.groupBox_4.setTitle(_translate("llm_widget", "User name"))
        self.username.setText(_translate("llm_widget", "User"))
        self.groupBox_3.setTitle(_translate("llm_widget", "Bot name"))
        self.botname.setText(_translate("llm_widget", "ChatAI"))
        self.personality_type.setItemText(0, _translate("llm_widget", "Nice"))
        self.personality_type.setItemText(1, _translate("llm_widget", "Mean"))
        self.personality_type.setItemText(2, _translate("llm_widget", "Weird"))
        self.personality_type.setItemText(3, _translate("llm_widget", "Insane"))
        self.personality_type.setItemText(4, _translate("llm_widget", "Random"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("llm_widget", "Chat"))
        self.groupBox.setTitle(_translate("llm_widget", "Prefix"))
        self.groupBox_2.setTitle(_translate("llm_widget", "Suffix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("llm_widget", "Preferences"))
        self.do_sample.setText(_translate("llm_widget", "Do sample"))
        self.groupBox_7.setTitle(_translate("llm_widget", "Model"))
        self.groupBox_6.setTitle(_translate("llm_widget", "DType"))
        self.radio_button_4bit.setText(_translate("llm_widget", "4-bit"))
        self.radio_button_8bit.setText(_translate("llm_widget", "8-bit"))
        self.radio_button_16bit.setText(_translate("llm_widget", "16-bit"))
        self.radio_button_32bit.setText(_translate("llm_widget", "32-bit"))
        self.dtype_description.setText(_translate("llm_widget", "Description"))
        self.use_gpu_checkbox.setText(_translate("llm_widget", "Use GPU"))
        self.groupBox_19.setTitle(_translate("llm_widget", "Seed"))
        self.override_parameters.setTitle(_translate("llm_widget", "Override Prameters"))
        self.groupBox_24.setTitle(_translate("llm_widget", "Length penalty"))
        self.length_penalty_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.length_penalty"))
        self.length_penalty_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_25.setTitle(_translate("llm_widget", "Num beams"))
        self.num_beams_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.num_beams"))
        self.num_beams_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_20.setTitle(_translate("llm_widget", "Top P"))
        self.top_p_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.top_p"))
        self.top_p_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_21.setTitle(_translate("llm_widget", "Max length"))
        self.max_length_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.max_length"))
        self.max_length_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_17.setTitle(_translate("llm_widget", "No repeat ngram size"))
        self.ngram_size_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.ngram_size"))
        self.ngram_size_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_18.setTitle(_translate("llm_widget", "Temperature"))
        self.temperature_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.temperature"))
        self.temperature_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_11.setTitle(_translate("llm_widget", "Repetition penalty"))
        self.repetition_penalty_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.repetition_penalty"))
        self.repetition_penalty_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_16.setTitle(_translate("llm_widget", "Min length"))
        self.min_length_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.min_length"))
        self.min_length_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_22.setTitle(_translate("llm_widget", "Sequences to generate"))
        self.sequences_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.sequences"))
        self.sequences_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.groupBox_23.setTitle(_translate("llm_widget", "Top k"))
        self.top_k_2.setProperty("settings_property", _translate("llm_widget", "llm_generator_setting.top_k"))
        self.top_k_2.setProperty("slider_callback", _translate("llm_widget", "handle_value_change"))
        self.early_stopping.setText(_translate("llm_widget", "Early stopping"))
        self.groupBox_8.setTitle(_translate("llm_widget", "Model Version"))
        self.random_seed.setText(_translate("llm_widget", "Random seed"))
        self.pushButton.setText(_translate("llm_widget", "Reset Settings to Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("llm_widget", "Settings"))
from airunner.widgets.slider.slider_widget import SliderWidget
