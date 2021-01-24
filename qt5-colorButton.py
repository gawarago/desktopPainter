from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout,
    QWidget,
    QFrame,
    QLabel
)

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()


    window.show()
    app.exec_()