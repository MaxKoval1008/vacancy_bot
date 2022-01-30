import sqlite3


class UsersBase:

    def __init__(self, database) -> object:
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()

    def create_table_users(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
                         user_id INTEGER PRIMARY KEY, 
                         user_name TEXT)''')

    def exists_user(self, user_id):
        return bool(self.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone())

    def profile_user(self, user_id):
        return self.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()

    def add_to_db_users(self, user_id, user_name):
        self.cur.execute("INSERT INTO users(user_id, user_name) VALUES(?,?)", (user_id, user_name))
        self.conn.commit()

    def get_all_users(self):
        all_users = self.cur.execute("SELECT * FROM users")
        return all_users.fetchall()

    def create_table_announcement(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS announcement(
                         work_type TEXT, 
                         name_vacancy TEXT, 
                         description TEXT, 
                         salary TEXT, 
                         tel_number TEXT,
                         user INTEGER, 
                         FOREIGN KEY (user) REFERENCES users (user_id))''')

    def add_to_db_announcement(self, list):
        self.cur.execute('''INSERT INTO announcement(work_type, name_vacancy, description, salary, tel_number, user) 
                         VALUES(?,?,?,?,?,?)''', list)
        self.conn.commit()

    def all_announcements(self):
        self.cur.execute("SELECT * FROM announcement")
        return self.cur.fetchall()

    def create_table_summary(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS summary(
                         user_name TEXT, 
                         skills TEXT, 
                         district TEXT, 
                         tel_number TEXT, 
                         user INTEGER, 
                         FOREIGN KEY (user) REFERENCES users (user_id))''')

    def add_to_db_summary(self, list):
        print(list)
        self.cur.execute('''INSERT INTO summary(user_name, skills, district, tel_number, user)
                         VALUES(?,?,?,?,?)''', list)
        self.conn.commit()

    def all_summary(self):
        print(self.cur.execute("SELECT * FROM summary"))
        return self.cur.fetchall()


    # def profile_user(self, user_id):
    #     return self.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    #
    # def create_table_summary(self):
    #     self.cur.execute('CREATE TABLE IF NOT EXISTS summary('
    #                      'user_id INTEGER, '
    #                      'user_name TEXT)')
    #
    # def exists_user(self, user_id):
    #     return bool(self.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone())
    #
    # def profile_user(self, user_id):
    #     return self.cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    #
    # def add_to_db(self, user_id, user_name):
    #     self.cur.execute("INSERT INTO users(user_id, user_name) VALUES(?,?)", (user_id, user_name))
    #     self.conn.commit()
