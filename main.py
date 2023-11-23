import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QDialog, QApplication
from ui_file import Ui_Dialog


class Example(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        # uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        # Задаем кисть
        for i in range(15):
            r = random.randint(2, 255)
            g = random.randint(2, 255)
            b = random.randint(2, 255)
            qp.setBrush(QColor(r, g, b))

            x = random.randint(0, 320)
            y = random.randint(0, 460)
            r = random.randint(15, 125)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
