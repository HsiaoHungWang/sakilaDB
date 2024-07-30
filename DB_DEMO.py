import MySQLdb

class Category():
    def __init__():
        pass
    # Step1 建立連線
    def create_connection():
        
        try:
            connection = MySQLdb.connect(
                host='localhost',
                database='sakila',
                user='root',
                password='P@ssw0rd'
            )
            return connection
        except MySQLdb.MySQLError as e:
            print(f"資料庫連線錯誤：{ e }")
            return None
        

    # 讀取所有資料
    def category_all():
       # 其它程式
        connection = Category.create_connection()
       
        if not connection:
            return None
        
        # Step2 SQL語法
        sql = 'SELECT * FROM category'
        
        # Step3 建立Cursor物件執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    # step 3-1
                    results = cursor.fetchall()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯誤：{e}")
                    return None

    # 讀取單筆資料
    def category_single(id):
       # 其它程式

        # Step1 建立連線
        # connection = MySQLdb.connect(
        #     host='localhost',
        #     database='sakila',
        #     user='root',
        #     password='P@ssw0rd'
        # )
        connection = Category.create_connection()
        if not connection:
            return None
        
        # Step2 SQL語法
        sql = 'SELECT * FROM category WHERE category_id=%s'
        
        # Step3 建立Cursor物件執行SQL語法
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql,(id,))
                    # step 3-1
                    results = cursor.fetchone()
                    return results
                except MySQLdb.MySQLError as e:
                    print(f"資料讀取錯誤：{e}")
                    return None

    # 新增資料
    def category_create(category_name):
        connection = Category.create_connection()
        if not connection:
            return None
        
        # step2 SQL INSERT
        sql = 'INSERT INTO category (name) VALUES (%s)'

        # step3 cursor 執行 SQL
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql,(category_name,))
                    # step 3-2
                    connection.commit()
                    return cursor.rowcount
                except MySQLdb.MySQLError as e:
                    print(f"資料新增失敗：{ e }")
                    return None
