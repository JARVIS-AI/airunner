from PIL.ImageQt import QImage

from PyQt6.QtCore import QRect, QPoint
from PyQt6.QtGui import QBrush, QColor, QPen, QPixmap, QPainter
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsPixmapItem
from airunner.mediator_mixin import MediatorMixin
from airunner.service_locator import ServiceLocator


class DraggablePixmap(
    QGraphicsPixmapItem,
    MediatorMixin
):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        MediatorMixin.__init__(self)
        self.pixmap = pixmap
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.last_pos = QPoint(0, 0)

    def snap_to_grid(self):
        settings = ServiceLocator.get("get_settings")()
        cell_size = settings["grid_settings"]["cell_size"]
        x = round(self.x() / cell_size) * cell_size
        y = round(self.y() / cell_size) * cell_size
        x += self.last_pos.x()
        y += self.last_pos.y()
        self.setPos(x, y)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.snap_to_grid()

    def mouseReleaseEvent(self, event):
        self.snap_to_grid()
        super().mouseReleaseEvent(event)

    def paint(self, painter: QPainter, option, widget=None):
        painter.drawPixmap(self.pixmap.rect(), self.pixmap)


class LayerImageItem(DraggablePixmap):
    def __init__(self, pixmap, layer_image_data):
        self.layer_image_data = layer_image_data
        super().__init__(pixmap)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        pos = self.pos()
        self.layer_image_data["pos_x"] = pos.x()
        self.layer_image_data["pos_y"] = pos.y()


class ActiveGridArea(DraggablePixmap):
    active_grid_area_color = None
    image = None

    def __init__(self, rect):
        self.rect = rect
        self.update_draggable_settings()
        super().__init__(self.pixmap)
        self.update_position()
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)

    def update_draggable_settings(self):
        settings = ServiceLocator.get("get_settings")()
        border_color = settings["generator_settings"]["active_grid_border_color"]
        border_color = QColor(border_color)
        border_opacity = settings["active_grid_settings"]["border_opacity"]
        border_color.setAlpha(border_opacity)
        fill_color = self.get_fill_color()

        self.active_grid_area_color = border_color

        width = abs(self.rect.width())
        height = abs(self.rect.height())

        if not self.image:
            self.image = QImage(
                width,
                height,
                QImage.Format.Format_ARGB32
            )
        else:
            self.image = self.image.scaled(
                width,
                height
            )

        self.image.fill(fill_color)
        self.pixmap = QPixmap.fromImage(self.image)

    def update_position(self):
        self.setPos(
            min(self.rect.x(), self.rect.x() + self.rect.width()),
            min(self.rect.y(), self.rect.y() + self.rect.height())
        )

    def get_fill_color(self):
        settings = ServiceLocator.get("get_settings")()
        fill_color = settings["generator_settings"]["active_grid_fill_color"]
        fill_color = QColor(fill_color)
        fill_opacity = settings["active_grid_settings"]["fill_opacity"]
        fill_opacity = max(1, fill_opacity)
        fill_color.setAlpha(fill_opacity)
        return fill_color

    def paint(self, painter: QPainter, option, widget=None):
        self.update_position()
        settings = ServiceLocator.get("get_settings")()
        self.update_draggable_settings()

        if settings["active_grid_settings"]["render_border"]:
            rect = QRect(
                0,
                0,
                abs(self.rect.width()),
                abs(self.rect.height())
            )
            painter.setPen(QPen(
                self.active_grid_area_color,
                self.settings["grid_settings"]["line_width"]
            ))
            painter.setBrush(QBrush(QColor(0, 0, 0, 0)))
            painter.drawRect(rect)
            painter.setPen(QPen(
                self.active_grid_area_color,
                self.settings["grid_settings"]["line_width"] + 1
            ))
            painter.drawRect(rect)
            self.update_position()
        super().paint(painter, option, widget)

    def toggle_render_fill(self, render_fill):
        if not render_fill:
            self.pixmap.fill(QColor(0, 0, 0, 1))
        else:
            self.pixmap.fill(self.get_fill_color())

    def toggle_render_border(self, value):
        pass

    def change_border_opacity(self, value):
        pass

    def change_fill_opacity(self, value):
        self.pixmap.fill(self.get_fill_color())

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        pos = self.pos()

    @property
    def settings(self):
        return ServiceLocator.get("get_settings")()

    @settings.setter
    def settings(self, value):
        ServiceLocator.get("set_settings")(value)