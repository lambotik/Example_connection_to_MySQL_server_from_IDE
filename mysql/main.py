import pymysql

from config import host, database, port, user, password


class MySQL:
    def connect_to_my_sql(self):
        """
        Create connection to MyQSL database
        :return: connection
        """
        try:
            connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                database=database,
                password=password,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('Successfully connected...')
            try:
                with connection.cursor() as cursor:
                    cursor.execute('''
                    select * from fine''')
                    result = cursor.fetchall()
                    print(result)
            finally:
                connection.close()

            return connection
        except Exception as ex:
            print('Connection refused...')
            print(ex)


