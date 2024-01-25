from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QDoubleSpinBox

from airunner.enums import SignalCode, ServiceCode
from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.slider.templates.slider_ui import Ui_slider_widget


class SliderWidget(BaseWidget):
    widget_class_ = Ui_slider_widget
    display_as_float = False
    divide_by = 1.0

    @property
    def slider_single_step(self):
        return self.ui.slider.singleStep()

    @slider_single_step.setter
    def slider_single_step(self, val):
        self.ui.slider.setSingleStep(int(val))

    @property
    def slider_page_step(self):
        return self.ui.slider.pageStep()

    @slider_page_step.setter
    def slider_page_step(self, val):
        self.ui.slider.setPageStep(int(val))

    @property
    def spinbox_single_step(self):
        return self.ui.slider_spinbox.singleStep

    @spinbox_single_step.setter
    def spinbox_single_step(self, val):
        self.ui.slider_spinbox.setSingleStep(val)

    @property
    def is_double_spin_box(self):
        return type(self.ui.slider_spinbox) == QDoubleSpinBox

    @property
    def spinbox_page_step(self):
        if self.is_double_spin_box:
            return self.spinbox_single_step
        return self.ui.slider_spinbox.pageStep

    @spinbox_page_step.setter
    def spinbox_page_step(self, val):
        if self.is_double_spin_box:
            self.spinbox_single_step = val
        else:
            self.ui.slider_spinbox.pageStep = val

    @property
    def slider_tick_interval(self):
        return self.ui.slider.tickInterval()

    @slider_tick_interval.setter
    def slider_tick_interval(self, val):
        self.ui.slider.tickInterval = val

    @property
    def slider_minimum(self):
        return self.ui.slider.minimum

    @slider_minimum.setter
    def slider_minimum(self, val):
        self.ui.slider.minimum = int(val)

    @property
    def slider_maximum(self):
        return self.ui.slider.maximum()

    @slider_maximum.setter
    def slider_maximum(self, val):
        self.ui.slider.setMaximum(int(val))

    @property
    def spinbox_maximum(self):
        return self.ui.slider_spinbox.maximum()

    @spinbox_maximum.setter
    def spinbox_maximum(self, val):
        self.ui.slider_spinbox.setMaximum(val)

    @property
    def spinbox_minimum(self):
        return self.ui.slider_spinbox.minimum()

    @spinbox_minimum.setter
    def spinbox_minimum(self, val):
        self.ui.slider_spinbox.setMinimum(val)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slider_callback = None
        self.label_text = None
        self.settings_property = None
        self.label = None
        self.register(SignalCode.MAIN_WINDOW_LOADED_SIGNAL, self.on_main_window_loaded_signal)
    
    def on_main_window_loaded_signal(self):
        self.initialize()
    
    def initialize(self, **kwargs):
        slider_callback = kwargs.pop("slider_callback", None)
        slider_minimum = kwargs.pop("slider_minimum", 0)
        slider_maximum = kwargs.pop("slider_maximum", 100)
        spinbox_minimum = kwargs.pop("spinbox_minimum", 0.0)
        spinbox_maximum = kwargs.pop("spinbox_maximum", 100.0)
        current_value = kwargs.pop("current_value", 0)
        settings_property = kwargs.pop("settings_property", None)
        label_text = kwargs.pop("label_text", "")
        display_as_float = kwargs.pop("display_as_float", False)
        
        slider_minimum = self.property("slider_minimum") or slider_minimum
        slider_maximum = self.property("slider_maximum") or slider_maximum
        slider_tick_interval = self.property("slider_tick_interval") or 8
        slider_callback = self.property("slider_callback") or slider_callback
        slider_single_step = self.property("slider_single_step") or 1
        slider_page_step = self.property("slider_page_step") or 1
        spinbox_minimum = self.property("spinbox_minimum") or spinbox_minimum
        spinbox_maximum = self.property("spinbox_maximum") or spinbox_maximum
        spinbox_single_step = self.property("spinbox_single_step") or 0.01
        spinbox_page_step = self.property("spinbox_page_step") or 0.01
        label_text = self.property("label_text") or label_text
        current_value = self.property("current_value") or current_value
        slider_name = self.property("slider_name") or None
        spinbox_name = self.property("spinbox_name") or None
        settings_property = self.property("settings_property") or settings_property
        self.display_as_float = self.property("display_as_float") or display_as_float
        self.divide_by = self.property("divide_by") or 1.0

        if settings_property is not None:
            current_value = self.get_service(ServiceCode.GET_SETTINGS_VALUE)(settings_property)

        # check if slider_callback is str
        if isinstance(slider_callback, str):
            slider_callback = self.get_service(ServiceCode.GET_CALLBACK_FOR_SLIDER)(slider_callback)

        # set slider and spinbox names
        if slider_name:
            self.ui.slider.setObjectName(slider_name)

        if spinbox_name:
            self.ui.slider_spinbox.setObjectName(spinbox_name)

        self.slider_callback = slider_callback
        self.slider_maximum = slider_maximum
        self.slider_minimum = slider_minimum
        self.slider_tick_interval = slider_tick_interval
        self.slider_single_step = slider_single_step
        self.slider_page_step = slider_page_step
        self.spinbox_single_step = spinbox_single_step
        self.spinbox_page_step = spinbox_page_step
        self.spinbox_minimum = spinbox_minimum
        self.spinbox_maximum = spinbox_maximum
        self.label_text = label_text
        self.settings_property = settings_property

        self.label = QLabel(f"{label_text}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.label.setObjectName("slider_label")
        #self.ui.slider.valueChanged.connect(lambda value: self.ui.slider_spinbox.setValue(value / self.slider_maximum))
        # add the label to the ui
        self.layout().addWidget(self.label, 0, 0, 1, 1)
        # self.ui.slider_spinbox.lineEdit().hide()
        self.ui.slider_spinbox.setFixedWidth(50)
        self.ui.slider_spinbox.valueChanged.connect(self.handle_spinbox_change)
        self.ui.slider.valueChanged.connect(self.handle_slider_change)
        self.set_slider_and_spinbox_values(current_value)
        if not self.display_as_float:
            self.ui.slider_spinbox.setDecimals(0)
        else:
            decimals = len(str(spinbox_single_step).split(".")[1])
            self.ui.slider_spinbox.setDecimals(2 if decimals < 2 else decimals)
    
    def set_slider_and_spinbox_values(self, val):
        self.ui.slider.blockSignals(True)
        self.ui.slider_spinbox.blockSignals(True)

        single_step = self.ui.slider.singleStep()
        adjusted_value = val
        if single_step > 0:
            adjusted_value = round(val / single_step) * single_step
        normalized = adjusted_value / self.slider_maximum
        spinbox_val = normalized * self.spinbox_maximum
        spinbox_val = round(spinbox_val, 2)
        self.ui.slider_spinbox.setValue(spinbox_val)

        self.ui.slider.setValue(int(val))
        self.ui.slider_spinbox.setValue(spinbox_val)

        self.ui.slider.blockSignals(False)
        self.ui.slider_spinbox.blockSignals(False)

    @property
    def current_value(self):
        return self.ui.slider.value()

    def handle_spinbox_change(self, val):
        normalized = val / self.spinbox_maximum
        slider_val = normalized * self.slider_maximum
        self.ui.slider.setValue(round(slider_val))
        # self.update_label()

    def handle_slider_change(self, val):
        position = val#self.ui.slider.sliderPosition()
        single_step = self.ui.slider.singleStep()
        adjusted_value = round(position / single_step) * single_step
        if adjusted_value < self.slider_minimum:
            adjusted_value = self.slider_minimum
        self.ui.slider.setValue(int(adjusted_value))

        normalized = adjusted_value / self.slider_maximum
        spinbox_val = normalized * self.spinbox_maximum
        spinbox_val = round(spinbox_val, 2)
        self.ui.slider_spinbox.setValue(spinbox_val)

        # self.update_label()
        if self.slider_callback:
            self.slider_callback(self.settings_property, adjusted_value)

    def update_value(self, val):
        self.ui.slider.setValue(int(val))

        if self.display_as_float:
            val = self.ui.slider_spinbox.value()

        # self.update_label()

    # def update_label(self):
    #     if self.display_as_float:
    #         val = f"{self.ui.slider_spinbox.value():.2f}"
    #     else:
    #         val = f"{int(self.ui.slider_spinbox.value())}"
    #     self.label.setText(f"{self.label_text} {val}")

    def set_tick_value(self, val):
        """
        This will set all intervals in spinbox and slider to the same amount.
        :param val:
        :return:
        """
        self.slider_minimum = val
        self.slider_tick_interval = val
        self.slider_single_step = val
        self.slider_page_step = val
        self.spinbox_single_step = val
        self.spinbox_page_step = val
        self.spinbox_minimum = val

    def setValue(self, val):
        self.ui.slider.setValue(val)