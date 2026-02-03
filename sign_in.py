from PyQt5.QtWidgets import * # type: ignore
from database import Sql
from social_page import social

class SignIN(QWidget):
    def __init__(self,obj:QWidget):
        super().__init__()
        self.setFixedSize(400, 450)
        self.setWindowTitle("SIGN IN")

        self.main_win=obj
        self.sql=Sql()

        self.V_main=QVBoxLayout()

        self.main_lab=QLabel("Tizimga kirish")

        self.user_edit=QLineEdit()
        self.user_edit.setPlaceholderText("USERNAME")

        self.password_edit=QLineEdit()
        self.password_edit.setPlaceholderText("PASSWORD")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.submit_but=QPushButton("Kirish")
        self.submit_but.clicked.connect(self.submit)

        self.back_but=QPushButton("<<<")
        self.back_but.clicked.connect(self.back)

        self.widgets=[self.main_lab, self.user_edit, self.password_edit, self.submit_but, self.back_but]

        for i in self.widgets:
            self.V_main.addWidget(i)

        # CSS WITH AI
        self.setStyleSheet("""
    QWidget {
        background-color: #e8f5e9;
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel {
        font-size: 28px;
        font-weight: bold;
        color: #1b5e20;
        padding: 12px;
        margin-bottom: 20px;
        border-bottom: 2px solid #43a047;
        qproperty-alignment: AlignCenter;
    }

    QLineEdit {
        font-size: 16px;
        padding: 6px;
        border: 2px solid #43a047;
        border-radius: 6px;
        margin: 6px;
        min-height: 32px;
        background-color: #ffffff;
        color: #1b5e20;
    }

    QPushButton {
        font-size: 18px;
        font-weight: bold;
        background-color: #43a047;
        color: #ffffff;
        padding: 8px 20px;
        border-radius: 8px;
        margin: 8px;
        min-height: 38px;
    }

    QPushButton:hover {
        background-color: #2e7d32;
    }

    QPushButton:pressed {
        background-color: #1b5e20;
    }
""")

        self.setLayout(self.V_main)

    def back(self):
        self.hide()
        self.main_win.show()

    def submit(self):
        user=self.user_edit.text()
        pasw=self.password_edit.text()
        if  user and pasw:
            pas=self.sql.Checkuser(user)
            if pas:
                if pas[0]==pasw:
                    self.social_win=social(user)
                    self.hide()
                    self.social_win.show()
                    return
                else:
                    xabar="Parol noto'gri kiritilgan"
                    self.password_edit.clear()
                    icon=QMessageBox.Warning
            else:
                xabar="Bunday user mavjud emas!"
                icon=QMessageBox.Information
                self.user_edit.clear()
                self.password_edit.clear()
        else:
            xabar="To'liq malumot bering"
            icon=QMessageBox.Warning
        self.msg=QMessageBox()
        self.msg.setText(xabar)
        self.msg.setIcon(icon)
        self.msg.setStyleSheet("""
    QMessageBox {
        background-color: #e8f5e9;
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel {
        font-size: 20px; 
        color: #1b5e20;
    }

    QPushButton {
        font-size: 16px;
        font-weight: bold;
        background-color: #43a047;
        color: #ffffff;
        padding: 8px 18px;
        border-radius: 6px;
        min-height: 32px;
    }

    QPushButton:hover {
        background-color: #2e7d32;
    }

    QPushButton:pressed {
        background-color: #1b5e20;
    }
""")
        self.msg.exec_()