from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
from database import Sql

class my_posts(QWidget):
    def __init__(self, obj:QWidget, user):
        super().__init__()
        self.setFixedSize(400, 450)
        self.setWindowTitle("MY POSTS")

        self.social_win=obj
        self.user=user
        self.sql=Sql()

        self.V_main=QVBoxLayout()

        self.main_lab=QLabel("Mening postlarim")

        self.posts_wd=QListWidget()

        self.back_but=QPushButton("<<<")
        self.back_but.clicked.connect(self.back)

        posts=self.sql.postbyUser(self.user)
        for user, post, kun in posts:
            item = QListWidgetItem(f"{user}\n{post}\nSana:{kun.strftime('%Y-%m-%d %H:%M')}")
            self.posts_wd.addItem(item)

        self.V_main.addWidget(self.main_lab)
        self.V_main.addWidget(self.posts_wd)
        self.V_main.addWidget(self.back_but)
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

    QListWidget {
        font-size: 15px;
        background-color: #2c2c2c;
        border: 2px solid #2e7d32;
        border-radius: 6px;
        padding: 8px;
        margin: 10px 0;
        color: #e0e0e0;
    }

    QListWidget::item {
        padding: 10px;
        margin: 4px;
        border-bottom: 1px solid #3d3d3d;
    }

    QListWidget::item:selected {
        background-color: #43a047;
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

    def back(self):
        self.hide()
        self.social_win.show()