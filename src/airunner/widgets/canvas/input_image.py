from PIL import Image
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap, QImage, Qt, QPen
from PySide6.QtWidgets import QGraphicsScene

from airunner.settings import VALID_IMAGE_FILES
from airunner.utils.convert_base64_to_image import convert_base64_to_image
from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.canvas.templates.input_image_ui import Ui_input_image


class InputImage(BaseWidget):
    widget_class_ = Ui_input_image

    def __init__(self, *args, **kwargs):
        self.settings_key = kwargs.pop("settings_key")
        self.use_generated_image = kwargs.pop("use_generated_image", False)
        super().__init__(*args, **kwargs)

    @property
    def current_settings(self):
        settings = None
        if self.settings_key == "controlnet_settings":
            settings = self.controlnet_settings
        elif self.settings_key == "image_to_image_settings":
            settings = self.image_to_image_settings
        elif self.settings_key == "outpaint_settings":
            settings = self.outpaint_settings
        elif self.settings_key == "brush":
            settings = self.drawing_pad_settings

        if not settings:
            raise ValueError(f"Settings not found for key: {self.settings_key}")

        return settings

    def on_mask_generator_worker_response_signal(self):
        if self.settings_key == "outpaint_settings":
            self.load_image_from_settings()

    def update_current_settings(self, key, value):
        if self.settings_key == "controlnet_settings":
            self.update_controlnet_settings(key, value)
        elif self.settings_key == "image_to_image_settings":
            self.update_image_to_image_settings(key, value)
        elif self.settings_key == "outpaint_settings":
            self.update_outpaint_settings(key, value)
        elif self.settings_key == "brush":
            self.update_drawing_pad_settings(key, value)

    def showEvent(self, event):
        super().showEvent(event)
        if self.settings_key == "controlnet_settings":
            self.ui.strength_slider_widget.hide()
            self.ui.controlnet_settings.show()
        else:
            self.ui.strength_slider_widget.show()
            self.ui.controlnet_settings.hide()

        if self.settings_key == "outpaint_settings":
            self.ui.strength_slider_widget.setProperty("settings_property", 'outpaint_settings.strength')
            self.ui.mask_blur_slider_widget.show()
        else:
            self.ui.mask_blur_slider_widget.hide()

        self.ui.enable_checkbox.blockSignals(True)
        self.ui.use_grid_image_as_input_checkbox.blockSignals(True)
        self.ui.enable_checkbox.setChecked(self.current_settings.enabled)
        if self.settings_key == "outpaint_settings":
            self.ui.import_button.hide()
            self.ui.use_grid_image_as_input_checkbox.hide()
            self.ui.use_grid_image_as_input_checkbox.hide()
        else:
            self.ui.use_grid_image_as_input_checkbox.setChecked(
                self.current_settings.use_grid_image_as_input
            )
        self.ui.enable_checkbox.blockSignals(False)
        self.ui.use_grid_image_as_input_checkbox.blockSignals(False)
        self.load_image_from_settings()

    @Slot(bool)
    def enabled_toggled(self, val):
        self.update_current_settings("enabled", val)

    @Slot(bool)
    def use_grid_image_as_input_toggled(self, val):
        self.update_current_settings("use_grid_image_as_input", val)

    @Slot()
    def import_clicked(self):
        self.import_image()

    @Slot()
    def delete_clicked(self):
        self.delete_image()

    def import_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.window(),
            "Open Image", "", f"Image Files ({' '.join(VALID_IMAGE_FILES)})"
        )
        if file_path == "":
            return
        self.load_image(file_path)

    def load_image(self, file_path: str):
        image = Image.open(file_path)
        self.load_image_from_object(image)

    def load_image_from_settings(self):
        if self.use_generated_image:
            image = self.current_settings.generated_image
        else:
            image = self.current_settings.image

        if self.settings_key == "outpaint_settings":
            image = self.drawing_pad_settings.mask

        if image is not None:
            image = convert_base64_to_image(image)
            if image is not None:
                self.load_image_from_object(image)
            else:
                print("image is none")

    def load_image_from_object(self, image: Image):
        if image is None:
            self.logger.warning("Image is None, unable to add to scene")
            return

        # Resize the image to maintain aspect ratio, but not exceed 512x512
        max_size = (512, 512)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)

        # Convert PIL image to QImage
        qimage = ImageQt(image)
        qpixmap = QPixmap.fromImage(QImage(qimage))

        # Create a QGraphicsScene and clear it
        scene = QGraphicsScene()
        scene.clear()  # Clear the scene before adding new items
        scene.addPixmap(qpixmap)

        # Set scene width and height
        scene.setSceneRect(0, 0, qpixmap.width(), qpixmap.height())

        # Set the QGraphicsScene to the QGraphicsView
        self.ui.image_container.setScene(scene)

        # Set the alignment to top-left corner
        self.ui.image_container.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Draw a red border around the image
        pen = QPen(Qt.GlobalColor.red)
        pen.setWidth(3)  # Set the width of the border
        scene.addRect(0, 0, qpixmap.width(), qpixmap.height(), pen)

    def delete_image(self):
        if self.settings_key == "outpaint_settings":
            self.update_drawing_pad_settings("mask", None)
        else:
            self.update_current_settings("image", None)
        self.ui.image_container.setScene(None)
