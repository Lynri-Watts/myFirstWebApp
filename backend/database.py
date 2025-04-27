import pymysql
from pymysql import cursors

class UserDatabase:
    def __init__(self, user, password, database,  host = 'localhost', charset = 'utf8mb4'):
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
    
    def delete_user(self, id):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM users
                     WHERE id = %s"""
            cursor.execute(sql, (id,))
            self.conn.commit()
            return cursor.rowcount == 1
    
    def create_user(self, username, password_hash, salt, email):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO users (username, password_hash, salt, email) 
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (username, password_hash, salt, email))
            self.conn.commit()
            return cursor.lastrowid
        

if __name__ == '__main__': # debug
    debug_instance = UserDatabase("root", "123456", "debug_database")
    # debug_instance.create_user('aaaa', 'eee', 'a@b.com')
    print(debug_instance.get_user_by_email('a@b.com'))
    print(debug_instance.get_user_by_email('c@d.com'))

# mysql -u root -p
# CREATE USER 'loginsystem'@'localhost' IDENTIFIED BY '123456';
# GRANT ALL ON debug_database.* TO 'loginsystem'@'localhost';