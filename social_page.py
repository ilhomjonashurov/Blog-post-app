from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
from database import Sql
from new_post import new_post
from my_posts import my_posts

class social(QWidget):
    def __init__(self, user):
        super().__init__()
        self.setFixedSize(400, 500)
        self.setWindowTitle("SOCIAL MEDIA")

        self.user=user

        self.sql=Sql()
        self.new_post_but=QPushButton("Post yaratish")
        self.new_post_but.clicked.connect(self.new_post)
        self.post_but=QPushButton("Postlarim")
        self.post_but.clicked.connect(self.myposts)

        self.posts_wdg=QListWidget()
        self.postupd()

        self.V_main=QVBoxLayout()
        self.H_button=QHBoxLayout()

        self.H_button.addWidget(self.new_post_but)
        self.H_button.addWidget(self.post_but)

        self.V_main.addLayout(self.H_button)
        self.V_main.addWidget(self.posts_wdg)

        # CSS WITH AI
        self.setStyleSheet("""
    QWidget {
        background-color: #1b1b1b;
        font-family: 'Segoe UI', sans-serif;
    }

    QPushButton {
        font-size: 16px;
        font-weight: bold;
        background-color: #2e7d32;
        color: #ffffff;
        padding: 6px 18px;
        border-radius: 6px;
        margin: 6px;
        min-height: 34px;
    }

    QPushButton:hover {
        background-color: #1b5e20;
    }

    QPushButton:pressed {
        background-color: #0d3d14;
    }

    QListWidget {
        font-size: 15px;
        background-color: #2c2c2c;
        border: 2px solid #2e7d32;
        border-radius: 6px;
        padding: 8px;
        margin-top: 10px;
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
""")

        self.setLayout(self.V_main)

    def new_post(self):
        self.hide()
        self.add_post_win=new_post(self, self.user)
        self.add_post_win.show()
    
    def myposts(self):
        self.hide()
        self.post_win=my_posts(self, self.user)
        self.post_win.show()

    def postupd(self):
        self.posts_wdg.clear()
        posts = self.sql.posts()
        for user, post, kun in posts:
            item = QListWidgetItem(f"{user}\n{post}\nSana:{kun.strftime('%Y-%m-%d %H:%M')}")
            self.posts_wdg.addItem(item)