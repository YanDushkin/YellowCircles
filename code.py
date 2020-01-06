from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from Ui import Ui_MainWindow
import sys
from random import randint


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.need_to_draw = False
        self.points_data = []
        self.create_circle_button.clicked.connect(self.draw)

    def draw(self):
        self.need_to_draw = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(255, 255, 0))
        self.draw_circle(painter)
        painter.end()

    def draw_circle(self, painter):
        if self.need_to_draw:
            diameter = randint(10, 200)
            coord_x = randint(diameter // 2, 600 - diameter // 2)
            coord_y = randint(diameter // 2, 400 - diameter // 2)
            circle = {
                "x": coord_x - diameter // 2,
                "y": coord_y - diameter // 2,
                "d": diameter,
            }
            self.points_data.append(circle)
            for circle in self.points_data:
                painter.drawEllipse(circle["x"], circle["y"], circle["d"], circle["d"])
            self.need_to_draw = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    yellow_circles = YellowCircles()
    yellow_circles.show()
    sys.exit(app.exec())
