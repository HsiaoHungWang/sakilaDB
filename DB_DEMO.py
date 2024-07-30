import MySQLdb

class Category():
    def __init__():
        pass

    def categories():
       # 其它程式

        # Step1 建立連線
        connection = MySQLdb.connect(
            host='localhost',
            database='sakila',
            user='root',
            password='P@ssw0rd'
        )
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

    