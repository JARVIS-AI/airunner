from airunner.windows.setup_wizard.agreement_page import AgreementPage
from airunner.windows.setup_wizard.templates.user_agreement_ui import Ui_user_agreement


class UserAgreement(AgreementPage):
    class_name_ = Ui_user_agreement
    setting_key = "user"

