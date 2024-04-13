from PySide6.QtWidgets import QWizardPage, QVBoxLayout
from airunner.mediator_mixin import MediatorMixin
from airunner.windows.main.settings_mixin import SettingsMixin


class BaseWizard(QWizardPage, MediatorMixin, SettingsMixin):
    class_name_ = None
    widget_class_ = None

    def __init__(self):
        MediatorMixin.__init__(self)
        SettingsMixin.__init__(self)
        super(BaseWizard, self).__init__()
        if self.class_name_:
            self.ui = self.class_name_()
            self.ui.setupUi(self)
        if self.widget_class_:
            widget = self.widget_class_()
            layout = QVBoxLayout()
            layout.addWidget(widget)
            self.setLayout(layout)
        self.initialize_form()

    def initialize_form(self):
        """
        Override this function to initialize form based on specific page in question.
        :return:
        """
        pass

    def save_settings(self):
        """
        Override this function to save settings based on specific page in question.
        :return:
        """
        pass

    def nextId(self):
        self.save_settings()
        return super().nextId()