import sys
import requests
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QPalette, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtMultimedia import QSound
import os

class BuzzerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.buzzed = False  # Flag to track if a buzzer has buzzed

    def initUI(self):
        self.setWindowTitle('Buzzer Status')
        self.setGeometry(100, 100, 300, 200)

        self.buzzer_label = QLabel('', self)
        self.buzzer_label.setAlignment(Qt.AlignCenter)  # Center the text
        self.buzzer_label.setAutoFillBackground(True)
        palette = self.buzzer_label.palette()
        palette.setColor(QPalette.Window, QColor('white'))
        self.buzzer_label.setPalette(palette)

        # Set font to the largest possible size
        font = QFont()
        font.setPointSize(500)  # Initial large font size, adjust if necessary
        font.setBold(True)
        self.buzzer_label.setFont(font)

        reset_button = QPushButton('Reset Buzzers', self)
        reset_button.clicked.connect(self.reset_buzzers)

        vbox = QVBoxLayout()
        vbox.addWidget(self.buzzer_label)
        vbox.addWidget(reset_button)

        self.setLayout(vbox)
        self.show()

        # Start periodic update timer
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_buzzer_status)
        self.update_timer.start(1000)  # Update every 1 second

    def update_buzzer_status(self):
        if self.buzzed:
            with open('buzzers.txt', 'r') as file:
                line = file.readline().strip()
                if(len(line) == 1):
                    self.buzzed = False
                else:
                    return  # If a buzzer has buzzed, do nothing until reset

        try:
            with open('buzzers.txt', 'r') as file:
                line = file.readline().strip()
                if len(line) == 2:  # Change '1' to the specific value you're checking for
                    buzz = chr(ord('A')-1+int(line[1]))
                    self.buzzer_label.setText(f'{buzz}')
                    palette = self.buzzer_label.palette()
                    palette.setColor(QPalette.Window, QColor('green'))
                    self.buzzer_label.setPalette(palette)
                    QSound.play('buzzer.wav')  # Ensure you have a sound file named 'buzzer.wav'
                    self.buzzed = True  # Set the flag to indicate a buzzer has buzzed
                else:
                    self.buzzer_label.setText('')
                    self.buzzed = False
                    palette = self.buzzer_label.palette()
                    palette.setColor(QPalette.Window, QColor('white'))
                    self.buzzer_label.setPalette(palette)
        except FileNotFoundError:
            print('buzzers.txt file not found')
        except Exception as e:
            print(f'Error reading buzzer status: {e}')

    def reset_buzzers(self):
        self.perform_reset()

    def perform_reset(self):
        try:
            response = requests.get('http://localhost:5000/reset')
            if response.status_code == 200 and response.text.strip() == '2':
                self.buzzer_label.setText('')
                palette = self.buzzer_label.palette()
                palette.setColor(QPalette.Window, QColor('white'))
                self.buzzer_label.setPalette(palette)
                self.buzzed = False  # Reset the flag to allow further updates
        except requests.exceptions.RequestException as e:
            print(f'Error resetting buzzers: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    buzzer_app = BuzzerApp()
    sys.exit(app.exec_())
