################################################################
# Importing this module sets the Hugging Face environment
# variables for the application.
################################################################
import sys
import signal
import traceback
from functools import partial
from PySide6 import QtCore
from PySide6.QtCore import (
    QObject,
    QTimer
)
from PySide6.QtGui import (
    QGuiApplication,
    QPixmap,
    Qt,
    QWindow
)
from PySide6.QtWidgets import (
    QApplication,
    QSplashScreen
)

from airunner.enums import SignalCode
from airunner.mediator_mixin import MediatorMixin
from airunner.windows.main.settings_mixin import SettingsMixin


class App(
    QObject,
    SettingsMixin,
    MediatorMixin
):
    """
    The main application class for AI Runner.
    This class can be run as a GUI application or as a socket server.
    """
    def __init__(
        self,
        main_window_class: QWindow = None,
        restrict_os_access=None,
        defendatron=None
    ):
        """
        Initialize the application and run as a GUI application or a socket server.
        :param main_window_class: The main window class to use for the application.
        """
        from airunner.windows.main.main_window import MainWindow
        from airunner.aihandler.logger import Logger

        self.main_window_class_ = main_window_class or MainWindow
        self.app = None
        self.logger = Logger(prefix=self.__class__.__name__)
        self.restrict_os_access = restrict_os_access
        self.defendatron = defendatron
        self.splash = None

        """
        Mediator and Settings mixins are initialized here, enabling the application
        to easily access the application settings dictionary.
        """
        MediatorMixin.__init__(self)
        SettingsMixin.__init__(self)
        super(App, self).__init__()

        if (
            "txt2img_model_path" not in self.settings["path_settings"]
        ):
            self.reset_paths()

        self.register(SignalCode.LOG_LOGGED_SIGNAL, self.on_log_logged_signal)

        self.start()
        self.run()

    def on_log_logged_signal(self, data: dict):
        message = data["message"].split(" - ")
        self.update_splash_message(self.splash, message[4])

    def start(self):
        """
        Conditionally initialize and display the setup wizard.
        :return:
        """
        signal.signal(signal.SIGINT, self.signal_handler)
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL)
        self.app = QApplication([])

    def run(self):
        """
        Run as a GUI application.
        A splash screen is displayed while the application is loading
        and a main window is displayed once the application is ready.

        Override this method to run the application in a different mode.
        """

        # Continue with application execution
        self.splash = self.display_splash_screen(self.app)

        # Show the main application window
        QTimer.singleShot(
            50,
            partial(
                self.show_main_application,
                self.app,
                self.splash
            )
        )
        sys.exit(self.app.exec())

    @staticmethod
    def signal_handler(
        _signal,
        _frame
    ):
        """
        Handle the SIGINT signal in a clean way.
        :param _signal:
        :param _frame:
        :return: None
        """
        print("\nExiting...")
        try:
            app = QApplication.instance()
            app.quit()
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(0)

    @staticmethod
    def display_splash_screen(app):
        """
        Display a splash screen while the application is loading.
        :param app:
        :return:
        """
        screens = QGuiApplication.screens()
        try:
            screen = screens.at(0)
        except AttributeError:
            screen = screens[0]
        pixmap = QPixmap("images/splashscreen.png")
        splash = QSplashScreen(
            screen,
            pixmap,
            QtCore.Qt.WindowType.WindowStaysOnTopHint
        )
        splash.show()
        App.update_splash_message(splash, f"Loading AI Runner")
        app.processEvents()
        return splash

    @staticmethod
    def update_splash_message(splash, message: str):
        splash.showMessage(
            message,
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignCenter,
            QtCore.Qt.GlobalColor.white
        )

    def show_main_application(
        self,
        app,
        splash
    ):
        """
        Show the main application window.
        :param app:
        :param splash:
        :return:
        """
        try:
            window = self.main_window_class_(
                restrict_os_access=self.restrict_os_access,
                defendatron=self.defendatron
            )
        except Exception as e:
            traceback.print_exc()
            print(e)
            splash.finish(None)
            sys.exit("""
                An error occurred while initializing the application.
                Please report this issue on GitHub or Discord."
            """)
        app.main_window = window
        splash.finish(window)
        window.raise_()
