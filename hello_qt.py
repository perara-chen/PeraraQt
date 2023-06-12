import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    """The main window of the application."""
    
    def __init__(self):
        super().__init__()
        self.initialize_ui()
    
    def initialize_ui(self):
        """Set up the GUI."""
        self.setWindowTitle("Perara's Qt App")
        self.setFixedSize(QSize(450, 400))
        
        self.setup_widget()
        self.show()
    
    def setup_widget(self):
        """Set up the widgets of the main window."""
        hello_label = QLabel("Hello, PySide6!", self)
        hello_label.setFont(QFont("Menlo", 28))
        hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(hello_label)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
