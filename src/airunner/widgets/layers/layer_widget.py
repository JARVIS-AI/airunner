from functools import partial

from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QPoint

from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.layers.layer_image_widget import LayerImageWidget
from airunner.widgets.layers.templates.layer_ui import Ui_LayerWidget
from airunner.utils import image_to_pixmap


class LayerWidget(BaseWidget):
    widget_class_ = Ui_LayerWidget
    layer_data = None
    offset = QPoint(0, 0)
    _previous_pos = None

    def __init__(self, *args, **kwargs):
        self.layer_data = kwargs.pop("layer_data", None)
        self.layer_index = kwargs.pop("layer_index", None)
        self.layer_data.layer_widget = self
        super().__init__(*args, **kwargs)
        self.ui.layer_images.hide()
        self.set_thumbnail()

        # listen for click on entire widget
        self.ui.mousePressEvent = partial(self.action_clicked, self.layer_data, self.layer_index)
        self.ui.layer_name.setText(self.layer_data.name)

    def reset_position(self):
        self._previous_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if not self._previous_pos:
            print("setting previous pos")
            self._previous_pos = self.pos()
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.move(self._previous_pos)

    def action_clicked(self):
        print("select layer")

    def action_clicked_button_toggle_layer_visibility(self, val):
        self.layer_data.hidden = not val
        self.settings_manager.save_and_emit(
            "layer_data.hidden",
            self.layer_data.hidden
        )

    def action_toggled_button_layer_images(self, val):
        self.ui.layer_images.setVisible(val)
        if val:
            # empty the scrollArea
            for i in reversed(range(self.ui.layer_images.layout().count())):
                self.ui.layer_images.layout().itemAt(i).widget().setParent(None)
            # add the layer images
            for layer_image in self.layer_data.layer_images:
                layer_image_widget = LayerImageWidget(layer_image)
                self.ui.layer_images.layout().addWidget(layer_image_widget)

    def set_thumbnail(self):
        if len(self.layer_data.image_data) == 0:
            return
        image = self.layer_data.image_data[0].image
        if image:
            thumbnail = image.copy()
            pixmap = image_to_pixmap(thumbnail, 32)
            self.ui.thumbnail.setPixmap(pixmap)
        else:
            self.ui.thumbnail.width = 32
            self.ui.thumbnail.height = 32
            self.ui.thumbnail.setPixmap(QtGui.QPixmap())
