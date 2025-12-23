import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

def set_target():
    return random.randint(1, 100)
class GTNWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(470, 250, 600, 400)
        self.setWindowTitle("Number Guessing Game")

        self.target = set_target()
        self.attempts = 0

        self.input_box = QLineEdit(self)
        self.check_btn = QPushButton("Check", self)
        self.feedback = QLabel("", self)
        self.attempt_label = QLabel("Attempts: 0", self)
        self.reset_btn = QPushButton("Reset", self)

        self.initUI()

    def initUI(self):
        # self.setStyleSheet("background-color: black;")

        self.input_box.setGeometry(200, 120, 200, 40)
        self.input_box.setStyleSheet("font-size: 20px; background-color: #333; color: white;")
        self.input_box.setPlaceholderText("Enter number 1-100")

        self.check_btn.setGeometry(250, 180, 100, 40)
        self.check_btn.setStyleSheet("font-size: 20px; background-color: #555; color: white;")
        self.check_btn.clicked.connect(self.check_guess)

        self.feedback.setGeometry(200, 240, 200, 40)
        self.feedback.setStyleSheet("font-size: 22px; color: yellow;")
        self.feedback.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.attempt_label.setGeometry(240, 280, 160, 40)
        self.attempt_label.setStyleSheet("font-size: 20px; color: cyan;")

        self.reset_btn.resize(self.reset_btn.sizeHint())
        self.reset_btn.move(self.width() - self.reset_btn.width(), self.height() - self.reset_btn.height())
        self.reset_btn.setStyleSheet("background-color: white; color: black; font-weight: bold")
        self.reset_btn.clicked.connect(self.reset_game)

        self.show()

    def check_guess(self):
        guess = self.input_box.text()

        if not guess.isdigit():
            self.feedback.setText("Enter a valid number!")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempt_label.setText(f"Attempts: {self.attempts}")

        if guess < self.target:
            self.feedback.setText("Too Low!")
        
        elif guess > self.target:
            self.feedback.setText("Too High!")

        else:
            self.feedback.setText("🎉 Correct! Reset")
            self.target = set_target()
            self.attempts = 0

    def reset_game(self):
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.attempt_label.setText("Attempts: 0")
        self.feedback.setText("Game Reset")
        self.input_box.clear()

def main():
    app = QApplication(sys.argv)
    w = GTNWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
