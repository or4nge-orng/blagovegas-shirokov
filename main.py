import sys

from PyQt6.QtCore import Qt, QPoint, QPointF
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor

from random import randint
from math import sin, cos, pi


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.figure = None
        self.coor = None
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.resize(1000, 1000)
        self.qp = QPainter()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.figure = 'circle'
            self.drawf()
        elif event.button() == Qt.MouseButton.RightButton:
            self.figure = 'square'
            self.drawf()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.figure = 'triangle'
            self.drawf()

    def mouseMoveEvent(self, event):
        self.coor = (event.pos().x(), event.pos().y())

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_figure()
            self.qp.end()

    def draw_figure(self):
        if self.figure == 'circle':
            R = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(QPointF(self.coor[0],
                                        self.coor[1]), R, R)
        elif self.figure == 'square':
            A = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawRect(int(self.coor[0] - A / 2), int(self.coor[1] - A / 2), A, A)
        elif self.figure == 'triangle':
            A = randint(20, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y = self.coor[0], self.coor[1]
            points = [QPoint(x, y - A),
                      QPoint(int(x + cos(7 * pi / 6) * A),
                             int(y - sin(7 * pi / 6) * A)),
                      QPoint(int(x + cos(11 * pi / 6) * A),
                             int(y - sin(11 * pi / 6) * A))]
            self.qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
