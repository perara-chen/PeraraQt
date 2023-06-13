# about.py
# Simple About Me profile application.
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QMessageBox)


class MainWindow(QMainWindow):
    """The main window class of the application."""
    
    def __init__(self):
        super().__init__()
        self.initialize_ui()
    
    def initialize_ui(self):
        """Set up the GUI."""
        self.setWindowTitle("About Me")
        self.setFixedSize(QSize(450, 300))
        
        self.setup_widget()
        self.show()
    
    def setup_widget(self):
        """Set up the widgets of the window."""
        profile_image = 'images/profile.svg'
        
        try:
            with open(profile_image):
                profile_image_label = QLabel(self)
                pixmap = QPixmap(profile_image)
                profile_image_label.setPixmap(pixmap)
                profile_image_label.resize(64, 64)
                profile_image_label.move(20, 20)
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error Message", f"""
                                <h1>File not found</h1><p>Error: {error}</p>
                                """, QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
            
        name_label = QLabel("Perara", self)
        name_label.setFont(QFont("Arial", 20))
        name_label.resize(110, 23)
        name_label.move(100, 20)
        
        summary_label = QLabel("A junior Linux System Administrator and a "
                               "person who would\nlike to be a system "
                               "programmer.", self)
        summary_label.setFont(QFont("Arial", 12))
        summary_label.resize(325, 30)
        summary_label.move(100, 50)
        
        language_label = QLabel("Programming Languages", self)
        language_label.setFont(QFont("Arial", 14))
        language_label.resize(180, 17)
        language_label.move(100, 95)
        
        language_list_label = QLabel("Bash, C, Python, Swift", self)
        language_list_label.setFont(QFont("Arial", 12))
        language_list_label.resize(250, 15)
        language_list_label.move(100, 120)
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
