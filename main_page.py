from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
from sign_in import SignIN
from sign_up import SignUP

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAIN PAGE")
        self.setFixedSize(300, 350)

        self.V_main=QVBoxLayout()
        self.V_main.setAlignment(Qt.AlignCenter)

        self.main_lab=QLabel("Bosh sahifa")
        self.V_main.addWidget(self.main_lab)

        self.signIN_but=QPushButton("Tizimga kirish")
        self.signIN_but.clicked.connect(self.signin)
        self.V_main.addWidget(self.signIN_but)

        self.signUP_but=QPushButton("Ro'yhatdan o'tish")
        self.signUP_but.clicked.connect(self.signup)
        self.V_main.addWidget(self.signUP_but)

        # CSS WITH AI
        self.setStyleSheet("""
    QWidget {
        background-color: #e8f5e9;
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel {
        font-size: 32px;
        font-weight: bold;
        color: #1b5e20;
        padding: 16px;
        margin-bottom: 24px;
        border-bottom: 3px solid #43a047;
        qproperty-alignment: AlignCenter;
    }

    QPushButton {
        font-size: 20px;
        font-weight: bold;
        background-color: #43a047;
        color: #ffffff;
        padding: 12px 28px;
        border-radius: 10px;
        margin: 10px;
    }

    QPushButton:hover {
        background-color: #2e7d32;
    }

    QPushButton:pressed {
        background-color: #1b5e20;
    }
""")
        self.resize(200, 300)

        self.setLayout(self.V_main)

    def signin(self):
        self.hide()
        self.sign_in=SignIN(self)
        self.sign_in.show()
    
    def signup(self):
        self.hide()
        self.sign_up=SignUP(self)
        self.sign_up.show()