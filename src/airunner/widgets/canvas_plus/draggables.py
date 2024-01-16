from PIL.ImageQt import QImage

from PyQt6.QtCore import QRect
from PyQt6.QtGui import QBrush, QColor, QPen, QPixmap, QPainter
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsPixmapItem

from airunner.data.session_scope import session_scope


class DraggablePixmap(QGraphicsPixmapItem):
    def __init__(self, parent, pixmap):
        self.parent = parent
        super().__init__(pixmap)
        self.pixmap = pixmap
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)

    def snap_to_grid(self):
        cell_size = self.parent.app.settings["grid_settings"]["cell_size"]
        x = round(self.x() / cell_size) * cell_size
        y = round(self.y() / cell_size) * cell_size
        x += self.parent.last_pos.x()
        y += self.parent.last_pos.y()
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
    def __init__(self, parent, pixmap, layer_image_data):
        self.layer_image_data = layer_image_data
        super().__init__(parent, pixmap)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        with session_scope() as session:
            pos = self.pos()
            self.layer_image_data.pos_x = pos.x()
            self.layer_image_data.pos_y = pos.y()
            session.add(self.layer_image_data)


class ActiveGridArea(DraggablePixmap):
    active_grid_area_color = None
    image = None

    @property
    def active_grid_area_rect(self):
        return QRect(
            self.app.settings["active_grid_settings"]["pos_x"],
            self.app.settings["active_grid_settings"]["pos_y"],
            self.app.settings["is_maximized"],
            self.app.settings["working_height"]
        )

    def __init__(self, parent, rect):
        self.app = parent.app
        self.update_settings()

        super().__init__(parent, self.pixmap)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)

    def update_settings(self):
        border_color = self.app.settings["generator_settings"]["active_grid_border_color"]
        border_color = QColor(border_color)
        border_opacity = self.app.settings["active_grid_settings"]["border_opacity"]
        border_color.setAlpha(border_opacity)
        fill_color = self.get_fill_color()

        self.active_grid_area_color = border_color

        if not self.image:
            self.image = QImage(
                self.active_grid_area_rect.width(),
                self.active_grid_area_rect.height(),
                QImage.Format.Format_ARGB32
            )
        else:
            self.image = self.image.scaled(
                self.active_grid_area_rect.width(),
                self.active_grid_area_rect.height()
            )

        self.image.fill(fill_color)
        self.pixmap = QPixmap.fromImage(self.image)

    def redraw(self):
        self.update_settings()
        scene = self.scene()
        if scene:
            scene.removeItem(self)
            if self.app.settings["active_grid_settings"]["enabled"]:
                scene.addItem(self)

    def get_fill_color(self):
        fill_color = self.app.settings["generator_settings"]["active_grid_fill_color"]
        fill_color = QColor(fill_color)
        fill_opacity = self.app.settings["active_grid_settings"]["fill_opacity"]
        fill_opacity = max(1, fill_opacity)
        fill_color.setAlpha(fill_opacity)
        return fill_color

    def paint(self, painter: QPainter, option, widget=None):
        if not self.app.settings["active_grid_settings"]["render_fill"]:
            self.pixmap.fill(QColor(0, 0, 0, 1))

        if self.app.settings["active_grid_settings"]["render_border"]:
            painter.setPen(QPen(
                self.active_grid_area_color,
                self.parent.line_width
            ))
            painter.setBrush(QBrush(QColor(0, 0, 0, 0)))
            painter.drawRect(self.active_grid_area_rect)
            painter.setPen(QPen(
                self.active_grid_area_color,
                self.parent.line_width + 1
            ))
            painter.drawRect(QRect(
                self.active_grid_area_rect.x(),
                self.active_grid_area_rect.y(),
                self.active_grid_area_rect.width(),
                self.active_grid_area_rect.height()
            ))
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
