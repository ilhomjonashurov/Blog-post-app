import pymysql

class Sql:
    def __init__(self):
        self.ConnectDB()
        self.write=self.db.cursor()
        self.db.autocommit(True)

    def ConnectDB(self):
        self.db=pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="foundation_hw"
        )

    def Checkuser(self, user):
        self.write.execute(f'SELECT password from users WHERE user="{user}"')
        return self.write.fetchone()
    
    def createuser(self, name, num, user, password):
        self.write.execute(f'''INSERT INTO users(name, number, user, password) VALUES("{name}", "{num}", "{user}", "{password}")''')

    def addpost(self, user, post):
        self.write.execute(f'''INSERT INTO posts(post, u_user) VALUES("{post}", "{user}")''')

    def posts(self):
        self.write.execute(f"SELECT u_user, post, kun FROM posts ORDER BY kun DESC")
        return self.write.fetchall()
    
    def postbyUser(self, user):
        self.write.execute(f'SELECT u_user, post, kun FROM posts WHERE u_user="{user}"')
        return self.write.fetchall()
