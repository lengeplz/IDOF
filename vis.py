import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PIL import Image, ImageFilter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IDOF")
        
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.screen_width = int(screen_geometry.width() / 4)
        self.screen_height = int(screen_geometry.height() / 4)
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setMinimumSize(400, 300)  # Set minimum size to prevent too small window

        self.show_enter_menu()
        
    def resizeEvent(self, event):
        """Handle window resize events"""
        super().resizeEvent(event)
        # Update screen dimensions when window is resized
        self.screen_width = self.width()
        self.screen_height = self.height()
        # Redraw current menu
        if hasattr(self, 'current_menu'):
            if self.current_menu == 'enter':
                self.show_enter_menu()
            elif self.current_menu == 'input':
                self.show_input_menu()

    def show_enter_menu(self):
        self.current_menu = 'enter'
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        blurred_pixmap = self.create_blurred_image("lgc.jpg", self.screen_width, self.screen_height)

        self.background_label = QLabel(central_widget)
        self.background_label.setPixmap(blurred_pixmap)
        self.background_label.setGeometry(0, 0, self.screen_width, self.screen_height)

        self.enter_button = QPushButton("Enter", central_widget)
        self.enter_button.clicked.connect(self.on_enter)
        button_width = int(self.screen_width * 0.20)
        button_height = int(self.screen_height * 0.10)
        button_x = (self.screen_width - button_width) // 2
        button_y = (self.screen_height - button_height) // 2 + int(self.screen_height * 0.1)
        self.enter_button.setGeometry(button_x, button_y, button_width, button_height)
        self.enter_button.setStyleSheet("""
                QPushButton {
                background-color: rgba(255,255,255,0.30);
                border: 2px solid #333;
                border-radius: 10px;
                font-size: 24px;
                font-weight: bold;
                color: #333;
                                        }
                QPushButton:hover {
                background-color: rgba(255,255,255,255);                                
                                        } 
                QPushButton:pressed {
                background-color: rgba(200,200,200,255)
                                        }
                                        """)
    
    def on_enter(self):
        self.show_input_menu()
    
    def create_blurred_image(self, image_path, width, height):
        img = Image.open(image_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((width, height))
        blurred = img.filter(ImageFilter.GaussianBlur(radius=10))
        
        # Convert PIL image to QPixmap
        data = blurred.tobytes("raw", "RGB")
        qimage = QImage(data, width, height, 3 * width, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(qimage)
    
    def show_input_menu(self):
        """Display the input menu with text box"""
        self.current_menu = 'input'
        
        # Create main container
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: transparent;")
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Add blurred background
        blurred_pixmap = self.create_blurred_image("lgc.jpg", self.screen_width, self.screen_height)
        background_label = QLabel()
        background_label.setPixmap(blurred_pixmap)
        
        # Create semi-transparent container
        container = QWidget()
        container.setMaximumWidth(int(self.screen_width * 0.8))
        container.setMaximumHeight(int(self.screen_height * 0.6))
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(20, 20, 20, 20)
        container_layout.setSpacing(15)
        container.setStyleSheet("""
            QWidget {
                background-color: rgba(255,255,255,0.15);
                border-radius: 15px;
            }
        """)
        
        # Input label
        label = QLabel("Enter your input:")
        label.setStyleSheet("color: #333; font-size: 18px; font-weight: bold;")
        container_layout.addWidget(label)
        
        # Input box
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type here...")
        self.input_box.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,0.8);
                border: 2px solid #333;
                border-radius: 8px;
                font-size: 16px;
                padding: 10px;
                color: #333;
            }
        """)
        container_layout.addWidget(self.input_box)
        
        # Submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.on_submit)
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(100,200,100,0.8);
                border: 2px solid #333;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                padding: 8px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: rgba(100,200,100,1);
            }
        """)
        container_layout.addWidget(submit_button)
        
        # Back button
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_enter_menu)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(200,100,100,0.8);
                border: 2px solid #333;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                padding: 8px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: rgba(200,100,100,1);
            }
        """)
        container_layout.addWidget(back_button)
        
        # Add container to main layout (centered)
        layout.addStretch()
        layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        
        self.setCentralWidget(central_widget)

    def on_submit(self):
        """Handle input submission"""
        user_input = self.input_box.text()
        print(f"User entered: {user_input}")
        self.show_enter_menu()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())