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
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
        self.setGeometry(0, 0, self.screen_width, self.screen_height)

        # Show the enter menu initially
        self.show_enter_menu()
        

    def show_enter_menu(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        blurred_pixmap = self.create_blurred_image("lgc.jpg", self.screen_width, self.screen_height)

        self.background_label = QLabel(central_widget)
        self.background_label.setPixmap(blurred_pixmap)
        self.background_label.setGeometry(0,0,self.screen_width,self.screen_height)

        self.enter_button = QPushButton("Enter", central_widget)
        self.enter_button.clicked.connect(self.on_enter)
        button_width = int(self.screen_width * 0.05)  # 10% of screen width
        button_height = int(self.screen_height * 0.025)  # 10% of screen height
        button_x = (self.screen_width - button_width) // 2  # Center horizontally
        button_y = (self.screen_height - button_height) // 2 + int(self.screen_height * 0.1)  # Center vertically
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
                QPushButtonm:pressed {
                background-color: rgba(200,200,200,255)
                                        }
                                        """)
    
    def on_enter(self):
        """Navigate to the input menu"""
        self.show_input_menu()
    
    def create_blurred_image(self, image_path, width, height):
        """Load your image and blur it"""
        img = Image.open(image_path)  # Load your image
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((width, height))  # Resize to window size
        blurred = img.filter(ImageFilter.GaussianBlur(radius=10))  # Adjust radius for more/less blur
        
        # Convert PIL image to QPixmap
        data = blurred.tobytes("raw", "RGB")
        qimage = QImage(data, width, height, 3 * width, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(qimage)
    
    def show_input_menu(self):
        """Display the input menu with text box"""
        # Clear previous widgets
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add blurred background
        blurred_pixmap = self.create_blurred_image("lgc.jpg", self.screen_width, self.screen_height)
        background_label = QLabel(central_widget)
        background_label.setPixmap(blurred_pixmap)
        background_label.setGeometry(0, 0, self.screen_width, self.screen_height)
        background_label.lower()  # Send to back
        
        # Create a semi-transparent container for the input box
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container.setStyleSheet("background-color: rgba(255,255,255,0.15); border-radius: 15px;")
        
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
        self.input_box.setMinimumWidth(400)
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
            }
            QPushButton:hover {
                background-color: rgba(200,100,100,1);
            }
        """)
        container_layout.addWidget(back_button)
        
        layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(central_widget)

    def on_submit(self):
        """Handle input submission"""
        user_input = self.input_box.text()
        print(f"User entered: {user_input}")
        # Do whatever you want with the input here
        self.show_enter_menu()  # Go back to enter menu after submission

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())