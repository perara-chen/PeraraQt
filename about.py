# about.py
# Simple About Me profile application.
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QMessageBox,
                               QPushButton, QWidget)


class MainWindow(QWidget):
    """The main window class of the application."""
    
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.more_info_window = MoreInfo()
    
    def initialize_ui(self):
        """Set up the GUI."""
        self.setWindowTitle("About Me")
        self.setFixedSize(QSize(450, 300))
        self.setup_widgets()
        self.show()
    
    def setup_widgets(self):
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
        
        summary_label = QLabel(
            """<h1>Perara</h1><p>Lorem ipsum dolor sit amet, consectetur
            adipiscing elit.</p><h2>Programming Languages</h2><p>Bash, C,
            Python, Swift</p><h2>Contact Information</h2><p>Phone :
            +959XXXXXXXXX<br>Email : username@example.com</p>""",
            self)
        summary_label.resize(330, 230)
        summary_label.move(100, 10)
        
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close_application)
        close_button.move(235, 260)
        
        more_info_button = QPushButton("More Information", self)
        more_info_button.clicked.connect(self.more_info)
        more_info_button.move(305, 260)
    
    def close_application(self):
        """Close the application."""
        self.close()
    
    def more_info(self):
        """Set up the More Info window."""
        self.more_info_window.show()


class MoreInfo(QDialog):
    """The More Info window class of the application."""
    
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initialize_ui()
    
    def initialize_ui(self):
        """Set up the GUI."""
        self.setFixedSize(500, 310)
        self.setup_widgets()
    
    def setup_widgets(self):
        """Set up the widgets for the window."""
        more_info_label = QLabel(
            """<h1>More About Me</h1><p>Lorem ipsum dolor sit amet,
            consectetur adipiscing elit. Sed euismod<br>scelerisque tortor,
            vitae finibus massa consequat non. Fusce iaculis odio a<br>risus
            consectetur congue.</p><p>In hac habitasse platea dictumst.
            Praesent tincidunt condimentum tortor, sit<br>amet eleifend enim
            venenatis a. Nullam accumsan, odio non tincidunt<br>bibendum,
            nisi mauris vestibulum arcu, a tincidunt massa urna sed
            nunc.</p><p>Donec sagittis ultrices elit, at bibendum dolor. Ut
            vel varius felis. Integer<br>convallis lacinia tellus,
            eget vestibulum massa vulputate eu. Suspendisse<br>auctor tellus
            sit amet lacus tincidunt, vitae semper nisi rhoncus. Nulla
            dapibus<br>ultrices nunc, id venenatis nibh tempus a. Integer
            posuere tellus in feugiat<br>iaculis.</p>""",
            self)
        more_info_label.resize(465, 240)
        more_info_label.move(20, 15)
        
        ok_button = QPushButton("Ok", self)
        ok_button.move(440, 270)
        ok_button.clicked.connect(self.close_window)
    
    def close_window(self):
        """Close the more info window."""
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
