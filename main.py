import sys

from PyQt5.QtWidgets import QApplication

from mytest_gui import MyTestApp
from mytest_console import main

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        app = QApplication(sys.argv)
        window = MyTestApp()
        window.show()
        sys.exit(app.exec_())
