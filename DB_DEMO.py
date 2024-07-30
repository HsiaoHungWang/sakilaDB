import MySQLdb

class Category():
    def __init__():
        pass

    def categories():
        # 建立連線
        connection = MySQLdb.connect(
            host='localhost',
            database='sakila',
            user='root',
            password='P@ssw0rd'
        )
        if not connection:
            return None
        
        return connection
    