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
                         id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         work_type TEXT, 
                         name_vacancy TEXT, 
                         description TEXT, 
                         salary TEXT, 
                         tel_number TEXT, 
                         user INTEGER,
                         is_active TEXT,  
                         FOREIGN KEY (user) REFERENCES users (user_id))''')

    def add_to_db_announcement(self, list):
        self.cur.execute('''INSERT INTO announcement(work_type, name_vacancy, description, salary, tel_number, user, 
        is_active) VALUES(?,?,?,?,?,?,?)''', list)
        self.conn.commit()

    def check_users_announcement(self, user_id):
        return bool(self.cur.execute("SELECT * FROM announcement WHERE user=?", (user_id,)).fetchone())

    def all_user_announcement(self, user_id):
        self.cur.execute("SELECT * FROM announcement WHERE user=?", (user_id,))
        return self.cur.fetchall()

    def all_announcements(self):
        self.cur.execute("SELECT * FROM announcement")
        return self.cur.fetchall()

    def change_user_announcement(self, data_list):
        self.cur.execute('''UPDATE announcement SET work_type=?, 
                                                    name_vacancy=?, 
                                                    description=?, 
                                                    salary=?, 
                                                    tel_number=?, 
                                                    user=?, 
                                                    is_active=? WHERE id=?''', data_list)
        self.conn.commit()

    def change_status_announcements(self, id):
        self.cur.execute('SELECT is_active FROM announcement WHERE id=?', (id,))
        if self.cur.fetchone()[0] == 'Active':
            self.cur.execute('''UPDATE announcement SET is_active='Inactive' WHERE id=?;''', (id,))
            self.conn.commit()
        else:
            self.cur.execute('''UPDATE announcement SET is_active='Active' WHERE id=?;''', (id,))
            self.conn.commit()

    def create_table_summary(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS summary(
                         id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         user_name TEXT, 
                         skills TEXT, 
                         district TEXT, 
                         tel_number TEXT, 
                         user INTEGER, 
                         is_active TEXT, 
                         FOREIGN KEY (user) REFERENCES users (user_id))''')

    def check_users_summary(self, user_id):
        return bool(self.cur.execute("SELECT * FROM summary WHERE user=?", (user_id,)).fetchone())

    def change_user_summary(self, data_list):
        self.cur.execute('''UPDATE summary SET user_name=?, 
                                                    skills=?, 
                                                    district=?, 
                                                    tel_number=?, 
                                                    user=?, 
                                                    is_active=? WHERE id=?''', data_list)
        self.conn.commit()

    def all_user_summary(self, user_id):
        self.cur.execute("SELECT * FROM summary WHERE user=?", (user_id,))
        return self.cur.fetchall()

    def add_to_db_summary(self, list):
        self.cur.execute('''INSERT INTO summary(user_name, skills, district, tel_number, user, is_active)
                         VALUES(?,?,?,?,?,?)''', list)
        self.conn.commit()

    def change_status_summary(self, id):
        self.cur.execute('SELECT is_active FROM summary WHERE id=?', (id,))
        if self.cur.fetchone()[0] == 'Active':
            self.cur.execute('''UPDATE summary SET is_active='Inactive' WHERE id=?;''', (id,))
            self.conn.commit()
        else:
            self.cur.execute('''UPDATE summary SET is_active='Active' WHERE id=?;''', (id,))
            self.conn.commit()

    def all_summary(self):
        self.cur.execute("SELECT * FROM summary")
        return self.cur.fetchall()
