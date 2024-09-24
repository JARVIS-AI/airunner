from PySide6.QtCore import QPoint
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsItem, QGraphicsPixmapItem

from airunner.enums import CanvasToolName
from airunner.mediator_mixin import MediatorMixin
from airunner.utils.snap_to_grid import snap_to_grid
from airunner.windows.main.settings_mixin import SettingsMixin


class DraggablePixmap(
    QGraphicsPixmapItem,
    MediatorMixin,
    SettingsMixin
):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        MediatorMixin.__init__(self)
        SettingsMixin.__init__(self)
        self.pixmap = pixmap
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.last_pos = QPoint(0, 0)
        self.save = False
        self.setFlag(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable,
            True
        )

    @property
    def current_tool(self):
        return CanvasToolName(self.application_settings.current_tool)

    def mouseMoveEvent(self, event):
        if self.current_tool not in [
            CanvasToolName.ACTIVE_GRID_AREA,
            CanvasToolName.SELECTION
        ]:
            return
        super().mouseMoveEvent(event)
        self.snap_to_grid()

    def mouseReleaseEvent(self, event):
        if self.current_tool in [
            CanvasToolName.ACTIVE_GRID_AREA,
            CanvasToolName.SELECTION
        ]:
            self.snap_to_grid(save=True)
        super().mouseReleaseEvent(event)

    def snap_to_grid(self, save=False):
        x, y = snap_to_grid(
            self.grid_settings,
            int(self.x()),
            int(self.y()),
            False
        )
        x += self.last_pos.x()
        y += self.last_pos.y()
        self.setPos(x, y, save)

    def setPos(self, x, y, save = True):
        super().setPos(x, y)
        if save:
            if self.current_tool is CanvasToolName.ACTIVE_GRID_AREA:
                self.update_active_grid_settings("pos_x", x)
                self.update_active_grid_settings("pos_y", y)

    def paint(self, painter: QPainter, option, widget=None):
        painter.drawPixmap(self.pixmap.rect(), self.pixmap)

    def setPixmap(self, pixmap):
        self.pixmap = pixmap
        super().setPixmap(pixmap)
