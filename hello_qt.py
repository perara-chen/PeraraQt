import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    """The main window of the application."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()

        # Window settings
        self.setWindowTitle("Perara's Qt App")
        self.setFixedSize(QSize(450, 400))

        # Label widget
        label = QLabel("Hello, PyQt!")

        # Label widget's settings
        label_font = label.font()
        label_font.setPointSize(40)
        label.setFont(label_font)
        label.setAlignment(Qt.AlignCenter)

        # Central widget of the window
        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
