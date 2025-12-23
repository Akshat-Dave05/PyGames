import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from random import choice

HEADS_IMG = r"Assets\heads.png"
TAILS_IMG = r"Assets\tails.png"

class CTWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(470, 250, 600, 400)
        self.setWindowTitle("Heads or Tails")

        self.player_score = 0
        self.computer_score = 0

        self.heads = QPushButton("Heads", self)
        self.tails = QPushButton("Tails", self)

        self.comp = QLabel(self)
        self.comp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comp.setGeometry(400, 120, 150, 150)
        pixmap = QPixmap(HEADS_IMG).scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        self.comp.setPixmap(pixmap)

        self.display_winner = QLabel("", self)
        self.display_player_score = QLabel(self)
        self.display_computer_score = QLabel(self)

        self.reset_btn = QPushButton('Reset', self)

        self.initUI()

    def initUI(self):
        # self.setStyleSheet("background-color: #F0F0F0;")
        self.setStyleSheet("background-color: black;")

        self.heads.setGeometry(100, 120, 120, 60)
        self.heads.setStyleSheet("font-size: 27px; background-color: #bababa; font-weight: bold;")
        self.heads.clicked.connect(lambda: self.play_round("Heads"))

        self.tails.setGeometry(100, 200, 120, 60)
        self.tails.setStyleSheet("font-size: 27px; background-color: #bababa; font-weight: bold;")
        self.tails.clicked.connect(lambda: self.play_round("Tails"))

        self.display_winner.setGeometry(215, 60, 200, 50)
        self.display_winner.setStyleSheet("font-size: 25px; font-weight: bold; color: #029c14; text-decoration: underline")
        self.display_winner.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.display_player_score.setGeometry(240, 150, 160, 60)
        self.display_player_score.setStyleSheet("font-size: 22px; color: blue;")

        self.display_computer_score.setGeometry(240, 200, 160, 60)
        self.display_computer_score.setStyleSheet("font-size: 22px; color: red;")

        self.reset_btn.resize(self.reset_btn.sizeHint())
        self.reset_btn.move(self.width() - self.reset_btn.width(), self.height() - self.reset_btn.height())
        self.reset_btn.setStyleSheet("background-color: white; color: black; font-weight: bold")
        self.reset_btn.clicked.connect(self.reset_game)

        self.show()

    def play_round(self, player_choice):
        comp_choice = choice(["Heads", "Tails"])
        img_path = HEADS_IMG if comp_choice == "Heads" else TAILS_IMG

        pixmap = QPixmap(img_path).scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        self.comp.setPixmap(pixmap)

        if player_choice == comp_choice:
            self.player_score += 1
            self.display_player_score.setText(f"You: {self.player_score}")
            self.display_winner.setText("You Won!!")
        else:
            self.computer_score += 1
            self.display_computer_score.setText(f"Computer: {self.computer_score}")
            self.display_winner.setText("Computer Won!!")

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.display_player_score.setText(f"You: {self.player_score}")
        self.display_computer_score.setText(f"Computer: {self.computer_score}")
        self.display_winner.setText("Game Reset")
        self.comp.clear()

def main():
    app = QApplication(sys.argv)
    w = CTWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
