from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainterPath
from PySide6.QtGui import QPen, QPixmap, QPainter
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFileDialog
from airunner.enums import SignalCode, CanvasToolName
from airunner.settings import VALID_IMAGE_FILES
from airunner.widgets.canvas.custom_scene import CustomScene


class BrushScene(CustomScene):
    settings_key = "drawing_pad_settings"

    def __init__(self, canvas_type: str):
        super().__init__(canvas_type)
        brush_color = self.brush_settings.primary_color
        self._brush_color = QColor(brush_color)
        self.pen = QPen(
            self._brush_color,
            self.brush_settings.size,
            Qt.PenStyle.SolidLine,
            Qt.PenCapStyle.RoundCap
        )
        self.path = None
        self._is_drawing = False
        self._is_erasing = False
        self._do_generate_image = False

        self.register(SignalCode.BRUSH_COLOR_CHANGED_SIGNAL, self.handle_brush_color_changed)

    @property
    def is_brush_or_eraser(self):
        return self.current_tool in (
            CanvasToolName.BRUSH,
            CanvasToolName.ERASER
        )

    def import_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open Image",
            "",
            f"Image Files ({' '.join(VALID_IMAGE_FILES)})"
        )
        if file_path == "":
            return
        self.handle_load_image(file_path)

    def handle_brush_color_changed(self, data):
        self._brush_color = QColor(data["color"])

    def drawBackground(self, painter, rect):
        if self.painter is None:
            self.refresh_image()

        if self.painter is not None and self.painter.isActive():
            self.painter.drawImage(0, 0, self.image)

            if self.last_pos:
                if self.current_tool is CanvasToolName.BRUSH:
                    self.draw_at(self.painter)
                elif self.current_tool is CanvasToolName.ERASER:
                    self.erase_at(self.painter)
        super().drawBackground(painter, rect)

    def create_line(self, drawing=False, erasing=False, painter=None, color: QColor=None):
        if drawing and not self._is_drawing or erasing and not self._is_erasing:
            self._is_drawing = drawing
            self._is_erasing = erasing

            # set the size of the pen
            self.pen.setWidth(self.brush_settings.size)

            if drawing:
                composition_mode = QPainter.CompositionMode.CompositionMode_SourceOver
            else:
                composition_mode = QPainter.CompositionMode.CompositionMode_Source

            # check if painter is active
            if not painter.isActive():
                painter.begin(self.image)

            self.pen.setColor(self._brush_color if color is None else color)

            # Set the pen to the painter
            painter.setPen(self.pen)

            # Set the CompositionMode to SourceOver
            painter.setCompositionMode(composition_mode)

            # Create a QPainterPath object
            self.path = QPainterPath()

        if not self.start_pos:
            return

        self.path.moveTo(self.start_pos)

        # Calculate the midpoint and use it as control point for quadTo
        start_pos = self.start_pos
        last_pos = self.last_pos

        control_point = QPointF(
            (start_pos.x() + last_pos.x()) * 0.5,
            (start_pos.y() + last_pos.y()) * 0.5
        )
        self.path.quadTo(
            control_point,
            self.last_pos
        )

        # Draw the path
        painter.drawPath(self.path)

        self.start_pos = self.last_pos

        # Create a QPixmap from the image and set it to the QGraphicsPixmapItem
        pixmap = QPixmap.fromImage(self.image)

        # save the image
        self.item.setPixmap(pixmap)

    def draw_at(self, painter=None):
        self.create_line(
            drawing=True,
            painter=painter
        )

    def erase_at(self, painter=None):
        self.create_line(
            erasing=True,
            painter=painter,
            color=QColor(Qt.GlobalColor.transparent)
        )
