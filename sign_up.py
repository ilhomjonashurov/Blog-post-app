from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
from database import Sql
from social_page import social


class SignUP(QWidget):
    def __init__(self,obj:QWidget):
        super().__init__()
        self.setFixedSize(400, 500)
        self.setWindowTitle("SIGN Up")

        self.main_win=obj
        self.sql=Sql()

        self.V_main=QVBoxLayout()

        self.main_lab=QLabel("Ro'yhatdan o'tish")

        self.name_edit=QLineEdit()
        self.name_edit.setPlaceholderText("ISM FAMILIYA")

        self.num_edit=QLineEdit()
        self.num_edit.setPlaceholderText("TELEFON")

        self.user_edit=QLineEdit()
        self.user_edit.setPlaceholderText("USERNAME")

        self.password_edit=QLineEdit()
        self.password_edit.setPlaceholderText("PASSWORD")

        self.submit_but=QPushButton("Ro'yhatdan o'tish")
        self.submit_but.clicked.connect(self.submit)

        self.back_but=QPushButton("<<<")
        self.back_but.clicked.connect(self.back)

        self.widgets=[self.main_lab, self.name_edit, self.num_edit, self.user_edit, self.password_edit, self.submit_but, self.back_but]

        for i in self.widgets:
            self.V_main.addWidget(i)

        # CCS WITH AI
        self.setStyleSheet("""
    QWidget {
        background-color: #e8f5e9;
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel {
        font-size: 26px;
        font-weight: bold;
        color: #1b5e20;
        padding: 10px;
        margin-bottom: 16px;
        border-bottom: 2px solid #43a047;
        qproperty-alignment: AlignCenter;
    }

    QLineEdit {
        font-size: 16px;
        padding: 6px;
        border: 2px solid #43a047;
        border-radius: 6px;
        margin: 6px;
        min-height: 30px;
        background-color: #ffffff;
        color: #1b5e20;
    }

    QPushButton {
        font-size: 16px;
        font-weight: bold;
        background-color: #43a047;
        color: #ffffff;
        padding: 6px 18px;
        border-radius: 6px;
        margin: 6px;
        min-height: 34px;
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
        name=self.name_edit.text()
        num=self.num_edit.text()
        user=self.user_edit.text()
        pasw=self.password_edit.text()
        if name and num and user and pasw:
            if self.sql.Checkuser(user):
                xabar="BU user mavjud"
                icon=QMessageBox.Warning
                self.user_edit.clear()
            else:
                if len(pasw)>=8:
                    self.sql.createuser(name, num, user, pasw)
                    self.social_win=social(user)
                    self.hide()
                    self.social_win.show()
                    return
                else:
                    xabar="Parol 8 belgidan iborat bo'lishi kerak!"
                    icon=QMessageBox.Information
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

