import pymysql
from pymysql import cursors

class Database:
    def __init__(self, user, password, database, host = 'localhost', charset = 'utf8mb4'):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            cursorclass=cursors.DictCursor
        )
    
    def get_user_by_email(self, email):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
            return cursor.fetchone()
    
    def get_user_by_username(self, username):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            return cursor.fetchone()
    
    
    def create_user(self, username, password, email):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO users (username, password, email) 
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (username, password, email))
            self.conn.commit()
            return cursor.lastrowid

if __name__ == '__main__': # debug
    debug_instance = Database("root", "123456", "debug_database")
    # debug_instance.create_user('aaaa', 'eee', 'a@b.com')
    print(debug_instance.get_user_by_email('a@b.com'))
    print(debug_instance.get_user_by_email('c@d.com'))