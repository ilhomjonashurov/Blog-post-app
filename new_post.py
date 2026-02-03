from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
from database import Sql

class new_post(QWidget):
    def __init__(self, obj:QWidget, user):
        super().__init__()
        self.setFixedSize(300, 220)
        self.setWindowTitle("NEW POST")

        self.social_win=obj
        self.user=user
        self.sql=Sql()

        self.main_lab=QLabel("Post yozish")

        self.main_edit=QLineEdit()
        self.main_edit.setPlaceholderText("Post yozing")

        self.upload_but=QPushButton("Yuklash")
        self.upload_but.clicked.connect(self.upload)

        self.V_main=QVBoxLayout()
        self.V_main.addWidget(self.main_lab)
        self.V_main.addWidget(self.main_edit)
        self.V_main.addWidget(self.upload_but)
        self.setStyleSheet("""
    QWidget {
        background-color: #1b1b1b;
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel {
        font-size: 22px;
        font-weight: bold;
        color: #e0e0e0;
        padding: 8px;
        margin-bottom: 12px;
        qproperty-alignment: AlignCenter;
    }

    QLineEdit {
        font-size: 16px;
        padding: 6px;
        border: 2px solid #2e7d32;
        border-radius: 6px;
        margin: 6px;
        min-height: 30px;
        background-color: #2c2c2c;
        color: #ffffff;
    }

    QPushButton {
        font-size: 16px;
        font-weight: bold;
        background-color: #2e7d32;
        color: #ffffff;
        padding: 6px 18px;
        border-radius: 6px;
        margin: 8px;
        min-height: 34px;
    }

    QPushButton:hover {
        background-color: #1b5e20;
    }

    QPushButton:pressed {
        background-color: #0d3d14;
    }
""")

        self.setLayout(self.V_main)


    def upload(self):
        if self.main_edit.text():
            self.hide()
            self.sql.addpost(self.user, self.main_edit.text())
            self.social_win.show()
            self.social_win.postupd()
        else:
            self.msg=QMessageBox()
            self.msg.setText("Post yozishingiz shart!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.exec_()