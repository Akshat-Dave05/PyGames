import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt

from random import choice

def R_P_S(pch):
    options = ["🪨","📃","✂️"]
    cch = choice(options)

    if((pch == "🪨" and cch == "✂️") or (pch == "📃" and cch == "🪨") or (pch == "✂️" and cch == "📃")):
        return cch, 'p'
    elif(pch == cch):
        return cch, 't'
    else:
        return cch, 'c'

class RPSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(470, 250, 600, 400)
        self.setWindowTitle("Rock Paper Scissor")

        self.computer_score = 0
        self.player_score = 0
        self.comp_choice = ''

        self.rock = QPushButton("🪨", self)

        self.paper = QPushButton("📃", self)

        self.scissor = QPushButton("✂️", self)

        self.comp = QLabel(self.comp_choice,self)
        self.display_winner = QLabel("", self)

        self.display_player_score = QLabel(self)
        self.display_computer_score = QLabel(self)

        self.reset_btn = QPushButton('Reset', self)

        self.initUI()

    def initUI(self):
        # self.setStyleSheet("background-color: white;")

        self.rock.setGeometry(100, 80, 70, 70)
        self.rock.setStyleSheet("font-size: 40px;"
                                "background-color: #454545;")
        self.rock.clicked.connect(self.r_btn)

        self.paper.setGeometry(100, 165, 70, 70)
        self.paper.setStyleSheet("font-size: 40px;"
                                 "background-color: #454545;")
        self.paper.clicked.connect(self.p_btn)

        
        self.scissor.setGeometry(100, 250, 70, 70)
        self.scissor.setStyleSheet("font-size: 40px;"
                                   "background-color: #454545;")
        self.scissor.clicked.connect(self.s_btn)


        self.comp.setGeometry(430,165,70,70)
        self.comp.setStyleSheet("background-color: #454545;"
                                "font-size: 40px")
        self.comp.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        self.display_winner.setGeometry(215, 60, 200, 50)
        self.display_winner.setStyleSheet("font-size: 25px; font-weight: bold; color: #029c14; text-decoration: underline")
        self.display_winner.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)


        self.display_player_score.setGeometry(240, 150, 160, 60)
        self.display_player_score.setStyleSheet("font-size: 22px;" 
                                "color: blue;")
        
        self.display_computer_score.setGeometry(240, 200, 160, 60)
        self.display_computer_score.setStyleSheet("font-size: 22px;"
                                "color: red;")
        
        self.reset_btn.resize(self.reset_btn.sizeHint())
        self.reset_btn.move(self.width() - self.reset_btn.width(), self.height() - self.reset_btn.height())
        self.reset_btn.setStyleSheet("background-color: white; color: Black; font-weight: bold")
        self.reset_btn.clicked.connect(self.click_reset)

        self.show()

    def update_result(self, pch):
        cch, winner = R_P_S(pch)
        self.comp.setText(cch)  

        if winner == 'p':
            self.player_score += 1
            self.display_player_score.setText(f"You: {self.player_score}")
            self.display_winner.setText("You Won!!")

        elif winner == 'c':
            self.computer_score += 1
            self.display_computer_score.setText(f"Computer: {self.computer_score}")
            self.display_winner.setText("Computer Won!!")

        else:
            self.display_winner.setText("It's a Tie!!")

    def r_btn(self):
        self.update_result("🪨")

    def p_btn(self):
        self.update_result("📃")

    def s_btn(self):
        self.update_result("✂️")

    def click_reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.display_computer_score.setText(f"Computer: {self.computer_score}")
        self.display_player_score.setText(f"You: {self.player_score}")
        self.display_winner.setText("Game Reset")

def main():
    app = QApplication(sys.argv)
    w = RPSWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()