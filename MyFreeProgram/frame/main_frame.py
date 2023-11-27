from PyQt5.QtWidgets import QMainWindow,QWidget, QMenu, QMenuBar, QAction, QApplication, QPushButton, QLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_main_window_ui()


    def init_main_window_ui(self):
        self.setMinimumSize(1200, 800)
        self.setWindowTitle("My application")

        self.init_menubar()

        self.show()

    
    def init_menubar(self):
        self.main_menubar = self.menuBar()

        file_menu = QMenu('file', self)
        file_menu.addAction('exit', self.exit_this_program)  # 绑定退出程序事件

        self.main_menubar.addMenu(file_menu)

    # 退出程序 exit
    def exit_this_program(self):
        app = QApplication.instance()    # 获取当前应用程序对象
        app.quit()
