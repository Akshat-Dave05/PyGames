import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLabel
from PyQt6.QtCore import Qt
from Games.RPS import RPSWindow
from Games.CT import CTWindow
from Games.GTN import GTNWindow

class GameCenter(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Game Center!")
        self.setGeometry(470, 250, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        central_widget.setLayout(main_layout)

        button_grid = QGridLayout()
        main_layout.addLayout(button_grid)

        self.rps_btn = QPushButton("🪨")
        self.rps_btn.setToolTip("'Rock Paper Scissor'")
        self.ht_btn = QPushButton("🪙")
        self.ht_btn.setToolTip("'Flip Coin'")
        self.ng_btn = QPushButton("❓")
        self.ng_btn.setToolTip("'Guess The Number'")

        self.buttons = [self.rps_btn, self.ht_btn, self.ng_btn]


        positions = [(0,0), (0,1), (1,0)]
        for btn, pos in zip(self.buttons, positions):
            btn.setFixedSize(80, 80)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 40px;
                    background-color: #444;
                    color: white;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            button_grid.addWidget(btn, pos[0], pos[1])

        self.rps_btn.clicked.connect(self.open_rps)
        self.ht_btn.clicked.connect(self.open_heads_tails)
        self.ng_btn.clicked.connect(self.open_number_guess)

    def open_rps(self):
        self.rps_window = RPSWindow()
        self.rps_window.show()

    def open_heads_tails(self):
        self.ht_window = CTWindow()
        self.ht_window.show()

    def open_number_guess(self):
        self.ng_window = GTNWindow()
        self.ng_window.show()

def main():
    app = QApplication(sys.argv)
    window = GameCenter()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()