import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QLineEdit, QWidget
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl, QSize
from PIL import Image, ImageFilter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IDOF")
        self.music_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.music_player.setAudioOutput(self.audio_output)
        self.is_fullscreen = False
        self.is_muted = False
        
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.screen_width = int(screen_geometry.width() / 2)
        self.screen_height = int(screen_geometry.height() / 2)
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setMinimumSize(400, 300)
        
        self.music_player.setSource(QUrl.fromLocalFile("meow.mp3"))
        self.music_player.play()
        self.show_enter_menu()
        
    # FULKL SCREEEEEEEEEEEEEEEN 😜😜😜😜
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.screen_width = self.width()
        self.screen_height = self.height()
        if hasattr(self, 'current_menu'):
            if self.current_menu == 'enter':
                self.show_enter_menu()
            elif self.current_menu == 'input':
                self.show_input_menu()

    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.is_fullscreen = False
            screen = QApplication.primaryScreen()
            screen_geometry = screen.geometry()
            self.screen_width = int(screen_geometry.width() / 2)
            self.screen_height = int(screen_geometry.height() / 2)
            self.showNormal()
            self.move(0, 0)
            self.resize(self.screen_width, self.screen_height)
        else:
            self.is_fullscreen = True
            self.showFullScreen()

    def toggle_mute(self):
        """Toggle mute on/off"""
        if self.is_muted:
            self.is_muted = False
            self.audio_output.setVolume(1.0)
        else:
            self.is_muted = True
            self.audio_output.setVolume(0.0)

    def add_control_buttons(self, parent_widget):
        # MUTE TYPE BEA BUTTON
        mute_button = HoverButton(parent_widget)
        mute_button.setIcon(QIcon("speaker.png"))
        mute_button.clicked.connect(lambda: [self.toggle_mute(), mute_button.set_muted(self.is_muted)])
        mute_button.setGeometry(10, 10, 50, 50)
        mute_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(100,100,100,0.0);
                border: 0px solid #333;
                border-radius: 0px;
            }
            QPushButton:hover {
                background-color: rgba(100,100,100,0.2);
            }
        """)

        fullscreen_button = HoverButton(parent_widget)
        fullscreen_button.setIcon(QIcon("not_fs.png"))
        fullscreen_button.clicked.connect(lambda: [self.toggle_fullscreen(), fullscreen_button.set_fullscreen(self.is_fullscreen)])
        fullscreen_button.setGeometry(self.screen_width - 60, 10, 50, 50)
        fullscreen_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(100,100,100,0.0);
                border: 0px solid #333;
                border-radius: 0px;
            }
            QPushButton:hover {
                background-color: rgba(100,100,100,0.2);
            }
        """)

    def show_enter_menu(self):
        self.current_menu = 'enter'
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        blurred_pixmap = self.create_blurred_image("idc.jpg", self.screen_width, self.screen_height)

        self.background_label = QLabel(central_widget)
        self.background_label.setPixmap(blurred_pixmap)
        self.background_label.setGeometry(0, 0, self.screen_width, self.screen_height)

        self.enter_button = QPushButton("> enter expense zone <", central_widget)
        self.enter_button.clicked.connect(self.on_enter)
        button_width = int(self.screen_width * 0.20)
        button_height = int(self.screen_height * 0.10)
        button_x = (self.screen_width - button_width) // 2
        button_y = (self.screen_height - button_height) // 2 + int(self.screen_height * 0.1)
        self.enter_button.setGeometry(button_x, button_y, button_width, button_height)
        self.enter_button.setStyleSheet("""
                QPushButton {
                background-color: rgba(255,255,255,0.00);
                border: 0px solid #333;
                border-radius: 0px;
                font-size: 24px;
                font-weight: bold;
                color: rgba(32,32,32, 0.5);
                                        }
                QPushButton:hover {
                color: rgba(0, 204, 255, 1);                                
                                        } 
                QPushButton:pressed {
                color: rgba(205, 0, 255, 1)
                                        }
                                        """)
        
        self.add_control_buttons(central_widget)
    
    def on_enter(self):
        self.show_input_menu()
    
    def create_blurred_image(self, image_path, width, height):
        img = Image.open(image_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((width, height))
        blurred = img.filter(ImageFilter.GaussianBlur(radius=0))
        
        data = blurred.tobytes("raw", "RGB")
        qimage = QImage(data, width, height, 3 * width, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(qimage)
    
    def show_input_menu(self):
        """Display the input menu with text box"""
        self.current_menu = 'input'
        
        # Create main container
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: transparent;")
        
        # Add blurred background FIRST (before layout)
        blurred_pixmap = self.create_blurred_image("yay.jpeg", self.screen_width, self.screen_height)
        background_label = QLabel(central_widget)
        background_label.setPixmap(blurred_pixmap)
        background_label.setGeometry(0, 0, self.screen_width, self.screen_height)
        background_label.lower()  # Send to back
        
        # Now add layout on top
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
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
        self.add_control_buttons(central_widget)

    def on_submit(self):
        """Handle input submission"""
        user_input = self.input_box.text()
        print(f"User entered: {user_input}")
        self.show_enter_menu()

class HoverButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.original_size = QSize(40, 40)
        self.hover_size = QSize(50, 50)
        self.setIconSize(self.original_size)
    
    def enterEvent(self, event):
        self.setIconSize(self.hover_size)
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.setIconSize(self.original_size)
        super().leaveEvent(event)
    
    def set_muted(self, is_muted):
        if is_muted:
            self.setIcon(QIcon("speaker_muted.png"))
        else:
            self.setIcon(QIcon("speaker.png"))
    
    def set_fullscreen(self, is_fullscreen):
        if is_fullscreen:
            self.setIcon(QIcon("fs.png"))
        else:
            self.setIcon(QIcon("not_fs.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 