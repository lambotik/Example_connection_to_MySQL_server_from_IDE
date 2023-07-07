from Example_connection_to_MySQL_server_from_IDE.mysql.main import MySQL

start = MySQL()
connection = start.connect_to_my_sql()
with connection.cursor() as cursor:
    try:
        #  query for example
        cursor.execute('''
        SELECT name, number_plate, violation    
        from fine
        GROUP BY name, number_plate, violation
        having count(violation) > 1
        order by name;''')
        result = cursor.fetchall()
        print(*result)
    except Exception as ex:
        print(ex)

