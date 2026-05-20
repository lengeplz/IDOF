import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PIL import Image, ImageFilter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IDOF")
        self.setGeometry(100, 100, 1920, 1080)

        screen = QApplication

        blurred_pixmap = self.create_blurred_image("ato.jpg", 1920, 1080)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(blurred_pixmap)
        self.background_label.setGeometry(0,0,1920,1080)

        self.enter_button = QPushButton("Enter", self)
        self.enter_button.clicked.connect(self.on_enter)
        self.enter_button.setGeometry(860,720, 150, 50)
        self.enter_button.setStyleSheet("""
                QPushButton {
                background-color: rgba(255,255,255,200);
                border: 2px solid #333;
                border-radius: 10px;
                font-size: 24px;
                font-weight: bold;
                color: #333;
                                        }
                QPushButton:hover {
                background-color: rgba(255,255,255,255);                                
                                        } 
                QPushButtonm:pressed {
                background-color: rgba(200,200,200,255)
                                        }
                                        """)
    def create_blurred_image(self, image_path, width, height):
        """Load your image and blur it"""
        img = Image.open(image_path)  # Load your image
        img = img.resize((width, height))  # Resize to window size
        blurred = img.filter(ImageFilter.GaussianBlur(radius=10))  # Adjust radius for more/less blur
        
        # Convert PIL image to QPixmap
        data = blurred.tobytes("raw", "RGB")
        qimage = QImage(data, width, height, 3 * width, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(qimage)

    def on_click(self):
        print("Button clicked!")
    
    def on_enter(self):
        print("Whoah")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())