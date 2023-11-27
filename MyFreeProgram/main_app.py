#!/usr/bin/python3
# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication
from frame.main_frame import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())