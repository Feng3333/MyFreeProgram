import sys
import time

from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.Qt import QPixmap, QPoint, Qt, QPainter, QIcon
from PyQt5.QtCore import QSize


class ImageBox(QWidget):
    def __init__(self):
        super(ImageBox, self).__init__()  # 执行父类的构造函数，可用于解决多重继承的问题

    def init_ui(self):
        self.setWindowTitle("ImageBox")

    